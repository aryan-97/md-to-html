import unittest

from src.html.htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):

    def test_eq(self):
        node1 = HtmlNode(tag="p", value="This is a paragraph")
        node2 = HtmlNode(tag="p", value="This is a paragraph")
        self.assertEqual(node1, node2)

    def test_eq_with_children(self):
        node1 = HtmlNode(tag="p", value="This is a paragraph", children=[HtmlNode(tag="b", value="Bold text")])
        node2 = HtmlNode(tag="p", value="This is a paragraph", children=[HtmlNode(tag="b", value="Bold text")])
        self.assertEqual(node1, node2)

    def test_eq_with_props(self):
        node1 = HtmlNode(tag="p", value="This is a paragraph", props={"class": "paragraph"})
        node2 = HtmlNode(tag="p", value="This is a paragraph", props={"class": "paragraph"})
        self.assertEqual(node1, node2)

    def test_eq_with_children_and_props(self):
        node1 = HtmlNode(tag="p", value="This is a paragraph", children=[HtmlNode(tag="b", value="Bold text")],
                         props={"class": "paragraph"})
        node2 = HtmlNode(tag="p", value="This is a paragraph", children=[HtmlNode(tag="b", value="Bold text")],
                         props={"class": "paragraph"})
        self.assertEqual(node1, node2)

    def test_not_eq(self):
        node1 = HtmlNode(tag="p", value="This is a paragraph")
        node2 = HtmlNode(tag="p", value="This is a paragraph", props={"class": "paragraph"})
        self.assertNotEqual(node1, node2)

    def test_not_eq_with_children(self):
        node1 = HtmlNode(tag="p", value="This is a paragraph", children=[HtmlNode(tag="b", value="Bold text")])
        node2 = HtmlNode(tag="p", value="This is a paragraph",
                         children=[HtmlNode(tag="b", value="Bold text"), HtmlNode(tag="i", value="Italic text")])
        self.assertNotEqual(node1, node2)

    def test_repr(self):
        node = HtmlNode(tag="p", value="This is a paragraph")
        self.assertEqual(repr(node), "HtmlNode(p, This is a paragraph, {}, [])")

    def test_props_to_html_with_multiple_props(self):
        """Test props_to_html with multiple properties"""
        node = HtmlNode(tag="div", value=None, props={"class": "container", "id": "main"})
        expected_output = 'class="container" id="main"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_single_prop(self):
        """Test props_to_html with a single property"""
        node = HtmlNode(tag="div", value=None, props={"class": "container"})
        expected_output = 'class="container"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_empty_props(self):
        """Test props_to_html with no properties"""
        node = HtmlNode(tag="div", value=None, props={})
        expected_output = ""
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_special_characters(self):
        """Test props_to_html with special characters in values"""
        node = HtmlNode(tag="input", value=None, props={"type": "text", "value": 'a "quote" & symbol'})
        expected_output = 'type="text" value="a \\"quote\\" & symbol"'
        self.assertEqual(node.props_to_html(), expected_output)

    def test_props_to_html_with_none_props(self):
        """Test props_to_html when props is None"""
        node = HtmlNode(tag="div", value=None, props=None)
        expected_output = ""
        self.assertEqual(node.props_to_html(), expected_output)

if __name__ == '__main__':
    unittest.main()
