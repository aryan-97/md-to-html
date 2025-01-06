import unittest

from src.markdown.markdown_parser import markdown_to_html


class TestMarkdownToHtml(unittest.TestCase):
    def test_single_heading(self):
        text = "# Heading 1"
        expected = '<div><h1>Heading 1</h1></div>'
        self.assertEqual(markdown_to_html(text), expected)

    def test_multiple_headings(self):
        text = "# Heading 1\n## Heading 2\n### Heading 3"
        expected = (
            '<div>'
            '<h1>Heading 1</h1>'
            '<h2>Heading 2</h2>'
            '<h3>Heading 3</h3>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

    def test_ordered_list(self):
        text = "1. First item\n2. Second item"
        expected = (
            '<div>'
            '<ol>'
            '<li>First item</li>'
            '<li>Second item</li>'
            '</ol>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

    def test_unordered_list(self):
        text = "* Item 1\n* Item 2"
        expected = (
            '<div>'
            '<ul>'
            '<li>Item 1</li>'
            '<li>Item 2</li>'
            '</ul>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

    def test_paragraph(self):
        text = "This is a simple paragraph."
        expected = (
            '<div>'
            '<p>This is a simple paragraph.</p>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

    def test_combined_content(self):
        text = "# Heading\nThis is a paragraph.\n* List item"
        expected = (
            '<div>'
            '<h1>Heading</h1>'
            '<p>This is a paragraph.</p>'
            '<ul>'
            '<li>List item</li>'
            '</ul>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

    def test_empty_string(self):
        text = ""
        expected = '<div></div>'
        self.assertEqual(markdown_to_html(text), expected)

    def test_quote_block(self):
        text = "> This is a blockquote"
        expected = (
            '<div>'
            '<blockquote>This is a blockquote</blockquote>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

    def test_mixed_content(self):
        text = "# Heading\nThis is a paragraph.\n> A blockquote\n* Unordered list"
        expected = (
            '<div>'
            '<h1>Heading</h1>'
            '<p>This is a paragraph.</p>'
            '<blockquote>A blockquote</blockquote>'
            '<ul>'
            '<li>Unordered list</li>'
            '</ul>'
            '</div>'
        )
        self.assertEqual(markdown_to_html(text), expected)

if __name__ == "__main__":
    unittest.main()