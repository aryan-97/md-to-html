import unittest

from src.markdown.markdown_parser import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_single_heading(self):
        text = "# This is the title"
        expected = "This is the title"
        self.assertEqual(extract_title(text), expected)

    def test_heading_with_extra_spaces(self):
        text = "  # Extra spaces around the title"
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

    def test_multiple_lines_with_title_at_top(self):
        text = "# Main Title\nThis is some content"
        expected = "Main Title"
        self.assertEqual(extract_title(text), expected)

    def test_multiple_lines_with_empty_line_before_title(self):
        text = "\n# Title with empty line above"
        expected = "Title with empty line above"
        self.assertEqual(extract_title(text), expected)

    def test_title_in_middle_of_text(self):
        text = "Some introduction\n# Title in the middle\nMore content"
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

    def test_no_title(self):
        text = "This is just content without any title."
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

    def test_empty_string(self):
        text = ""
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

    def test_only_empty_lines(self):
        text = "\n\n\n"
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

    def test_title_with_non_heading_content_before(self):
        text = "Non-heading content\n# Title after non-heading"
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

    def test_title_with_empty_lines_between(self):
        text = "Some content\n\n# Title with empty lines in between\nMore content"
        with self.assertRaises(ValueError) as context:
            extract_title(text)
        self.assertEqual(str(context.exception), "Title not present.")

if __name__ == "__main__":
    unittest.main()