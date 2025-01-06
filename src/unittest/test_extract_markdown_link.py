import unittest
from src.markdown.textnode_parser import extract_markdown_link, split_nodes_link
from src.markdown.textnode import TextNode, TextType


class TestExtractMarkdownLink(unittest.TestCase):
    def test_single_link(self):
        text = "Here is a link: [OpenAI](https://openai.com)"
        result = extract_markdown_link(text)
        expected = [("OpenAI", "https://openai.com")]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = (
            "First link: [Google](https://google.com) "
            "Second link: [GitHub](https://github.com)"
        )
        result = extract_markdown_link(text)
        expected = [
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com"),
        ]
        self.assertEqual(result, expected)

    def test_no_links(self):
        text = "This text has no links."
        result = extract_markdown_link(text)
        expected = []
        self.assertEqual(result, expected)

    def test_empty_text_in_link(self):
        text = "A link with no text: [](https://example.com)"
        result = extract_markdown_link(text)
        expected = [("", "https://example.com")]
        self.assertEqual(result, expected)

    def test_empty_url_in_link(self):
        text = "A link with no URL: [Empty]()"
        result = extract_markdown_link(text)
        expected = [("Empty", "")]
        self.assertEqual(result, expected)

    def test_link_with_spaces_in_url(self):
        text = "Link with spaces in URL: [Example](https://example.com/my%20page)"
        result = extract_markdown_link(text)
        expected = [("Example", "https://example.com/my%20page")]
        self.assertEqual(result, expected)

    def test_special_characters_in_text(self):
        text = "Link with special characters: [!@#$%^&*()](https://example.com)"
        result = extract_markdown_link(text)
        expected = [("!@#$%^&*()", "https://example.com")]
        self.assertEqual(result, expected)

    def test_text_and_links_mixed(self):
        text = (
            "Some text before. [First](https://first.com) "
            "More text. [Second](https://second.com)."
        )
        result = extract_markdown_link(text)
        expected = [
            ("First", "https://first.com"),
            ("Second", "https://second.com"),
        ]
        self.assertEqual(result, expected)

    def test_invalid_link_format(self):
        text = "Invalid link format: [OpenAI][https://openai.com]"
        result = extract_markdown_link(text)
        expected = []
        self.assertEqual(result, expected)

    def test_whitespace_inside_markdown(self):
        text = "Link with extra spaces: [ Example ]( https://example.com )"
        result = extract_markdown_link(text)
        expected = [(" Example ", " https://example.com ")]
        self.assertEqual(result, expected)

class TestSplitNodesLink(unittest.TestCase):
    def test_no_links(self):
        old_node = TextNode("This is a normal text.", TextType.NORMAL)
        result = split_nodes_link(old_node)
        expected = [TextNode("This is a normal text.", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_single_link(self):
        old_node = TextNode("Here is a [link](https://example.com).", TextType.NORMAL)
        result = split_nodes_link(old_node)
        expected = [
            TextNode("Here is a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        old_node = TextNode(
            "Check this [first link](https://example.com/1) and this [second link](https://example.com/2).",
            TextType.NORMAL,
        )
        result = split_nodes_link(old_node)
        expected = [
            TextNode("Check this ", TextType.NORMAL),
            TextNode("first link", TextType.LINK, "https://example.com/1"),
            TextNode(" and this ", TextType.NORMAL),
            TextNode("second link", TextType.LINK, "https://example.com/2"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_between_links(self):
        old_node = TextNode(
            "Before [link1](https://example.com/1) and after [link2](https://example.com/2)",
            TextType.NORMAL,
        )
        result = split_nodes_link(old_node)
        expected = [
            TextNode("Before ", TextType.NORMAL),
            TextNode("link1", TextType.LINK, "https://example.com/1"),
            TextNode(" and after ", TextType.NORMAL),
            TextNode("link2", TextType.LINK, "https://example.com/2"),
        ]
        self.assertEqual(result, expected)

    def test_only_link(self):
        old_node = TextNode("[only link](https://example.com)", TextType.NORMAL)
        result = split_nodes_link(old_node)
        expected = [TextNode("only link", TextType.LINK, "https://example.com")]
        self.assertEqual(result, expected)

    def test_empty_text(self):
        old_node = TextNode("", TextType.NORMAL)
        result = split_nodes_link(old_node)
        expected = []
        self.assertEqual(result, expected)

    def test_non_normal_text_type(self):
        old_node = TextNode("This text is bold.", TextType.BOLD)
        result = split_nodes_link(old_node)
        expected = [old_node]  # Should return the same node since the type isn't NORMAL
        self.assertEqual(result, expected)

    def test_malformed_link_syntax(self):
        old_node = TextNode("This is malformed [link](https://example.com", TextType.NORMAL)
        result = split_nodes_link(old_node)
        expected = [TextNode("This is malformed [link](https://example.com", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_ignore_image_links(self):
        old_node = TextNode("Here is an image ![alt](https://example.com/img.png) and a [link](https://example.com).", TextType.NORMAL)
        result = split_nodes_link(old_node)
        expected = [
            TextNode("Here is an image ![alt](https://example.com/img.png) and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()