import unittest

from src.html.leafnode import LeafNode
from src.html.parentnode import ParentNode


class MyTestCase(unittest.TestCase):
    def test_initialization(self):
        node = ParentNode("div", [LeafNode("Hello, World!")])
        expected_html = "<div>Hello, World!</div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_initialization_with_multiple_children(self):
        node = ParentNode("p", [LeafNode("Hello, World!"), LeafNode(tag="b", value="bold"), LeafNode(tag="i", value="italic"),
                                LeafNode("End")])
        expected_html = "<p>Hello, World!<b>bold</b><i>italic</i>End</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_initialization_with_props(self):
        node = ParentNode("div", [LeafNode("Hello, World!")], props={"class": "container"})
        expected_html = "<div class=\"container\">Hello, World!</div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_initialization_with_tag_set_to_none(self):
        """Test ParentNode initialization with tag set to None, raising a TypeError"""
        with self.assertRaises(TypeError):
            ParentNode(children=[LeafNode("Hello, World!")])

    def test_to_html_with_children(self):
        """Test to_html with valid children nodes"""
        child1 = LeafNode(value="Child 1", tag="span", props={"class": "child1"})
        child2 = LeafNode(value="Child 2", tag="span", props={"class": "child2"})
        parent = ParentNode(tag="div", children=[child1, child2], props={"class": "parent"})
        expected_html = (
            '<div class="parent">'
            '<span class="child1">Child 1</span>'
            '<span class="child2">Child 2</span>'
            '</div>'
        )
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_no_children(self):
        """Test to_html with no children"""
        parent = ParentNode(tag="div", children=[], props={"id": "empty-parent"})
        expected_html = '<div id="empty-parent"></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_nested_children(self):
        """Test to_html with nested children nodes"""
        child1 = LeafNode(value="Nested Child 1", tag="b")
        child2 = ParentNode(
            tag="span", children=[LeafNode(value="Nested Child 2", tag="i")]
        )
        parent = ParentNode(tag="div", children=[child1, child2])
        expected_html = (
            '<div>'
            '<b>Nested Child 1</b>'
            '<span><i>Nested Child 2</i></span>'
            '</div>'
        )
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_empty_props(self):
        """Test to_html with empty props"""
        child = LeafNode(value="Child", tag="p")
        parent = ParentNode(tag="section", children=[child], props={})
        expected_html = '<section><p>Child</p></section>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_to_html_with_special_character_props(self):
        """Test to_html with special characters in props"""
        child = LeafNode(value="Child with special props", tag="p")
        parent = ParentNode(
            tag="section",
            children=[child],
            props={"data-info": 'Special "data" & value'}
        )
        expected_html = '<section data-info="Special \\"data\\" & value"><p>Child with special props</p></section>'
        self.assertEqual(parent.to_html(), expected_html)


if __name__ == '__main__':
    unittest.main()
