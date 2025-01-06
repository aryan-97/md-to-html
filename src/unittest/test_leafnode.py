from unittest import TestCase

from src.html.leafnode import LeafNode


class TestLeafNode(TestCase):
    def test_initialization(self):
        """Test LeafNode initialization with proper values"""
        node = LeafNode(value="Hello, World!", tag="span", props={"class": "highlight"})
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, {"class": "highlight"})
        self.assertEqual(node.children, [])

    def test_initialization_without_tag_and_with_props(self):
        """Test LeafNode initialization with tag set to None and props set to a dictionary, expecting an ValueError"""
        with self.assertRaises(ValueError):
            LeafNode(value="Hello, World!", props={"class": "highlight"})

    def test_initialization_without_value(self):
        """Test LeafNode initialization with value set to None, expecting a ValueError"""
        with self.assertRaises(ValueError):
            LeafNode(value=None, tag="span")

    def test_to_html_with_props(self):
        """Test HTML generation with properties"""
        node = LeafNode(value="Click here", tag="a", props={"href": "https://example.com", "class": "link"})
        expected_html = '<a href="https://example.com" class="link">Click here</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_without_props(self):
        """Test HTML generation without properties"""
        node = LeafNode(value="Bold Text", tag="b")
        expected_html = '<b>Bold Text</b>'
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_props(self):
        """Test HTML generation with an empty props dictionary"""
        node = LeafNode(value="Text", tag="p", props={})
        expected_html = '<p>Text</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_without_tag(self):
        """Test LeafNode initialization with tag set to None"""
        node = LeafNode(value="Hello, World!")
        expected_html = 'Hello, World!'
        self.assertEqual(node.to_html(), expected_html)
