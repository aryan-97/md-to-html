from enum import Enum
from unittest import TestCase

from src.html.leafnode import LeafNode
from src.markdown.textnode import TextNode, TextType


class TestTextNode(TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_italic(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node1, node2)

    def test_eq_code(self):
        node1 = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node1, node2)

    def test_eq_link(self):
        node1 = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.example.com")
        self.assertEqual(node1, node2)

    def test_eq_image(self):
        node1 = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/image.png")
        self.assertEqual(node1, node2)

    def test_not_eq_link(self):
        node1 = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.example.com/different")
        self.assertNotEqual(node1, node2)

    def test_not_eq_image(self):
        node1 = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/image.png")
        node2 = TextNode("This is a text node", TextType.IMAGE, "https://www.example.com/different.png")
        self.assertNotEqual(node1, node2)

    def test_not_eq_code(self):
        node1 = TextNode("This is a python code", TextType.CODE)
        node2 = TextNode("This is a javascript code", TextType.CODE)
        self.assertNotEqual(node1, node2)

    def test_to_htmlnode_normal(self):
        """Test conversion of normal text"""
        text_node = TextNode("Normal text", TextType.NORMAL)
        expected_node = LeafNode("Normal text")
        self.assertEqual(text_node.to_htmlnode(), expected_node)

    def test_to_htmlnode_bold(self):
        """Test conversion of bold text"""
        text_node = TextNode("Bold text", TextType.BOLD)
        expected_node = LeafNode("Bold text", tag="b")
        self.assertEqual(text_node.to_htmlnode(), expected_node)

    def test_to_htmlnode_italic(self):
        """Test conversion of italic text"""
        text_node = TextNode("Italic text", TextType.ITALIC)
        expected_node = LeafNode("Italic text", tag="i")
        self.assertEqual(text_node.to_htmlnode(), expected_node)

    def test_to_htmlnode_code(self):
        """Test conversion of code text"""
        text_node = TextNode("Code snippet", TextType.CODE)
        expected_node = LeafNode("Code snippet", tag="code")
        self.assertEqual(text_node.to_htmlnode(), expected_node)

    def test_to_htmlnode_link(self):
        """Test conversion of link text"""
        text_node = TextNode("Click here", TextType.LINK, url="https://example.com")
        expected_node = LeafNode("Click here", tag="a", props={"href": "https://example.com"})
        self.assertEqual(text_node.to_htmlnode(), expected_node)

    def test_to_htmlnode_image(self):
        """Test conversion of image"""
        text_node = TextNode("Image alt text", TextType.IMAGE, url="https://example.com/image.png")
        expected_node = LeafNode("", tag="img", props={"src": "https://example.com/image.png", "alt": "Image alt text"})
        self.assertEqual(text_node.to_htmlnode(), expected_node)

    def test_to_htmlnode_invalid_type(self):
        """Test invalid TextType raises ValueError"""
        class InvalidTextType(Enum):
            INVALID = "invalid"

        text_node = TextNode("Invalid text", InvalidTextType.INVALID)
        with self.assertRaises(ValueError):
            text_node.to_htmlnode()

    def test_to_htmlnode_normal_html(self):
        """Test conversion of normal text"""
        text_node = TextNode("Normal text", TextType.NORMAL)
        expected_html = "Normal text"  # Normal text has no HTML tags
        self.assertEqual(text_node.to_htmlnode().to_html(), expected_html)

    def test_to_htmlnode_bold_html(self):
        """Test conversion of bold text"""
        text_node = TextNode("Bold text", TextType.BOLD)
        expected_html = "<b>Bold text</b>"
        self.assertEqual(text_node.to_htmlnode().to_html(), expected_html)

    def test_to_htmlnode_italic_html(self):
        """Test conversion of italic text"""
        text_node = TextNode("Italic text", TextType.ITALIC)
        expected_html = "<i>Italic text</i>"
        self.assertEqual(text_node.to_htmlnode().to_html(), expected_html)

    def test_to_htmlnode_code_html(self):
        """Test conversion of code text"""
        text_node = TextNode("Code snippet", TextType.CODE)
        expected_html = "<code>Code snippet</code>"
        self.assertEqual(text_node.to_htmlnode().to_html(), expected_html)

    def test_to_htmlnode_link_html(self):
        """Test conversion of link text"""
        text_node = TextNode("Click here", TextType.LINK, url="https://example.com")
        expected_html = '<a href="https://example.com">Click here</a>'
        self.assertEqual(text_node.to_htmlnode().to_html(), expected_html)

    def test_to_htmlnode_image_html(self):
        """Test conversion of image"""
        text_node = TextNode("Image alt text", TextType.IMAGE, url="https://example.com/image.png")
        expected_html = '<img src="https://example.com/image.png" alt="Image alt text">'
        self.assertEqual(text_node.to_htmlnode().to_html(), expected_html)