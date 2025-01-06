import unittest

from src.markdown.blocknode_parser import text_to_blocks


class TestTextToBlocks(unittest.TestCase):
    def test_single_paragraph(self):
        # Single paragraph with no double line breaks
        text = "This is a single paragraph with no breaks."
        expected = ["This is a single paragraph with no breaks."]
        self.assertEqual(text_to_blocks(text), expected)

    def test_multiple_paragraphs(self):
        # Multiple paragraphs separated by double line breaks
        text = "This is the first paragraph.\n\nThis is the second paragraph."
        expected = ["This is the first paragraph.", "This is the second paragraph."]
        self.assertEqual(text_to_blocks(text), expected)

    def test_trailing_and_leading_whitespace(self):
        # Leading and trailing whitespace around paragraphs
        text = "\n\n  This is the first paragraph.  \n\n  This is the second paragraph.  \n\n"
        expected = ["This is the first paragraph.", "This is the second paragraph."]
        self.assertEqual(text_to_blocks(text), expected)

    def test_empty_text(self):
        # Empty text input
        text = ""
        expected = []
        self.assertEqual(text_to_blocks(text), expected)

    def test_only_whitespace(self):
        # Input contains only whitespace
        text = "   \n\n   \n   "
        expected = []
        self.assertEqual(text_to_blocks(text), expected)

    def test_mixed_spacing(self):
        # Multiple paragraphs with mixed spacing
        text = "First paragraph.\n  \n   \nSecond paragraph.\n\nThird paragraph."
        expected = ["First paragraph.", "Second paragraph.", "Third paragraph."]
        self.assertEqual(text_to_blocks(text), expected)

    def test_inline_newlines(self):
        # Single paragraph with inline newlines
        text = "This is a paragraph\nwith inline newlines."
        expected = ["This is a paragraph", "with inline newlines."]
        self.assertEqual(text_to_blocks(text), expected)

    def test_special_characters(self):
        # Paragraphs with special characters
        text = "First paragraph! 😊\n\nSecond paragraph with #special @chars."
        expected = ["First paragraph! 😊", "Second paragraph with #special @chars."]
        self.assertEqual(text_to_blocks(text), expected)

    def test_single_line_breaks(self):
        # Input with only single line breaks (no double line breaks)
        text = "Line 1\nLine 2\nLine 3"
        expected = ["Line 1","Line 2","Line 3"]
        self.assertEqual(text_to_blocks(text), expected)

    def test_double_newlines_with_tabs(self):
        # Input with double line breaks that include tabs or spaces
        text = "First paragraph.\n\n\tSecond paragraph.\n\n Third paragraph."
        expected = ["First paragraph.", "Second paragraph.", "Third paragraph."]
        self.assertEqual(text_to_blocks(text), expected)

if __name__ == "__main__":
    unittest.main()