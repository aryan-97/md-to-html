import unittest

from src.markdown.textnode_parser import extract_markdown_image, split_nodes_image
from src.markdown.textnode import TextNode, TextType


class TestExtractMarkdownImage(unittest.TestCase):
    def test_single_image(self):
        text = "Here is an image: ![Alt text](https://example.com/image.png)"
        result = extract_markdown_image(text)
        expected = [("Alt text", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        text = (
            "First image: ![Image1](https://example.com/image1.png) "
            "Second image: ![Image2](https://example.com/image2.png)"
        )
        result = extract_markdown_image(text)
        expected = [
            ("Image1", "https://example.com/image1.png"),
            ("Image2", "https://example.com/image2.png"),
        ]
        self.assertEqual(result, expected)

    def test_no_images(self):
        text = "This text has no images."
        result = extract_markdown_image(text)
        expected = []
        self.assertEqual(result, expected)

    def test_image_with_empty_alt_text(self):
        text = "An image with no alt text: ![](https://example.com/image.png)"
        result = extract_markdown_image(text)
        expected = [("", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_image_with_spaces_in_url(self):
        text = "An image with spaces: ![Alt text](https://example.com/my%20image.png)"
        result = extract_markdown_image(text)
        expected = [("Alt text", "https://example.com/my%20image.png")]
        self.assertEqual(result, expected)

    def test_image_including_special_characters_in_alt_text(self):
        text = "An image with special characters: ![Alt&*^%$#@!](https://example.com/image.png)"
        result = extract_markdown_image(text)
        expected = [("Alt&*^%$#@!", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_mixed_text_and_images(self):
        text = (
            "Some text before. ![First image](https://example.com/image1.png) "
            "More text. ![Second image](https://example.com/image2.png)."
        )
        result = extract_markdown_image(text)
        expected = [
            ("First image", "https://example.com/image1.png"),
            ("Second image", "https://example.com/image2.png"),
        ]
        self.assertEqual(result, expected)

    def test_image_with_invalid_format(self):
        text = "Invalid image format: ![Alt text][https://example.com/image.png]"
        result = extract_markdown_image(text)
        expected = []
        self.assertEqual(result, expected)

    def test_image_with_whitespace_inside_markdown(self):
        text = "Image with extra spaces: ![ Alt text ]( https://example.com/image.png )"
        result = extract_markdown_image(text)
        expected = [(" Alt text ", " https://example.com/image.png ")]
        self.assertEqual(result, expected)


class TestSplitNodesImage(unittest.TestCase):
    def test_no_images(self):
        old_node = TextNode("This is a normal text.", TextType.NORMAL)
        result = split_nodes_image(old_node)
        expected = [TextNode("This is a normal text.", TextType.NORMAL)]
        self.assertEqual(result, expected)

    def test_single_image(self):
        old_node = TextNode("Here is an image: ![alt text](https://example.com/image.png)", TextType.NORMAL)
        result = split_nodes_image(old_node)
        expected = [
            TextNode("Here is an image: ", TextType.NORMAL),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        old_node = TextNode(
            "Text with multiple images ![first](https://example.com/1.png) and ![second](https://example.com/2.png).",
            TextType.NORMAL,
        )
        result = split_nodes_image(old_node)
        expected = [
            TextNode("Text with multiple images ", TextType.NORMAL),
            TextNode("first", TextType.IMAGE, "https://example.com/1.png"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("second", TextType.IMAGE, "https://example.com/2.png"),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_text_between_images(self):
        old_node = TextNode(
            "Image1: ![one](https://example.com/one.png) then text, then Image2: ![two](https://example.com/two.png)",
            TextType.NORMAL,
        )
        result = split_nodes_image(old_node)
        expected = [
            TextNode("Image1: ", TextType.NORMAL),
            TextNode("one", TextType.IMAGE, "https://example.com/one.png"),
            TextNode(" then text, then Image2: ", TextType.NORMAL),
            TextNode("two", TextType.IMAGE, "https://example.com/two.png"),
        ]
        self.assertEqual(result, expected)

    def test_only_image(self):
        old_node = TextNode("![alt text](https://example.com/image.png)", TextType.NORMAL)
        result = split_nodes_image(old_node)
        expected = [TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_empty_text(self):
        old_node = TextNode("", TextType.NORMAL)
        result = split_nodes_image(old_node)
        expected = []
        self.assertEqual(result, expected)

    def test_non_normal_text_type(self):
        old_node = TextNode("This text is bold.", TextType.BOLD)
        result = split_nodes_image(old_node)
        expected = [old_node]  # Should return the same node since the type isn't NORMAL
        self.assertEqual(result, expected)

    def test_malformed_image_syntax(self):
        old_node = TextNode("This is malformed ![alt text](https://example.com/image.png", TextType.NORMAL)
        result = split_nodes_image(old_node)
        expected = [TextNode("This is malformed ![alt text](https://example.com/image.png", TextType.NORMAL)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
