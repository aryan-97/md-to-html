import unittest
from src.markdown.textnode import TextNode, TextType
from src.markdown.textnode_parser import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_normal_text_without_delimiter(self):
        node = TextNode("This is normal text", TextType.NORMAL)
        result = split_nodes_delimiter(node, "*", TextType.BOLD)
        expected = [TextNode("This is normal text", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_text_with_single_delimited_section(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_with_multiple_delimited_sections(self):
        node = TextNode("This is **bold** and **italic** text", TextType.NORMAL)
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.NORMAL),
            TextNode("italic", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_with_empty_delimiter_sections(self):
        node = TextNode("**bold**", TextType.NORMAL)
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        expected = [
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_text_with_leading_and_trailing_delimiters(self):
        node = TextNode("*bold* and *italic*", TextType.NORMAL)
        result = split_nodes_delimiter(node, "*", TextType.ITALIC)
        expected = [
            TextNode("bold", TextType.ITALIC),
            TextNode(" and ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

    def test_unsupported_text_type(self):
        node = TextNode("This is bold text", TextType.BOLD)
        result = split_nodes_delimiter(node, "*", TextType.BOLD)
        expected = [node]
        self.assertEqual(result, expected)

    def test_invalid_markdown_syntax(self):
        node = TextNode("This is *bold and italic text", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter(node, "*", TextType.BOLD)
        self.assertEqual(str(context.exception), "Invalid markdown syntax. Please check the delimiter.")

    def test_text_with_adjacent_delimiters(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        result = split_nodes_delimiter(node, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()