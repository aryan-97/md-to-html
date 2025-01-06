import unittest

from src.markdown.textnode_parser import text_to_textnodes
from src.markdown.textnode import TextType


class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_textnodes_normal(self):
        text = "This is a simple text."
        result = text_to_textnodes(text)

        # Check if only a single normal TextNode is returned
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is a simple text.")
        self.assertEqual(result[0].type, TextType.NORMAL)

    def test_text_to_textnodes_bold(self):
        text = "This is a **bold** text."
        result = text_to_textnodes(text)

        # Check if the bold text is properly split into TextNodes
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[0].type, TextType.NORMAL)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].type, TextType.BOLD)
        self.assertEqual(result[2].text, " text.")
        self.assertEqual(result[2].type, TextType.NORMAL)

    def test_text_to_textnodes_italic(self):
        text = "This is an *italic* text."
        result = text_to_textnodes(text)

        # Check if the italic text is properly split into TextNodes
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is an ")
        self.assertEqual(result[0].type, TextType.NORMAL)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].type, TextType.ITALIC)
        self.assertEqual(result[2].text, " text.")
        self.assertEqual(result[2].type, TextType.NORMAL)

    def test_text_to_textnodes_code(self):
        text = "This is a `code` snippet."
        result = text_to_textnodes(text)

        # Check if the code text is properly split into TextNodes
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[0].type, TextType.NORMAL)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].type, TextType.CODE)
        self.assertEqual(result[2].text, " snippet.")
        self.assertEqual(result[2].type, TextType.NORMAL)

    def test_text_to_textnodes_link(self):
        text = "Click [here](https://example.com) for more info."
        result = text_to_textnodes(text)

        # Check if the link text is properly split into TextNodes
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Click ")
        self.assertEqual(result[0].type, TextType.NORMAL)
        self.assertEqual(result[1].text, "here")
        self.assertEqual(result[1].type, TextType.LINK)
        self.assertEqual(result[1].url, "https://example.com")
        self.assertEqual(result[2].text, " for more info.")
        self.assertEqual(result[2].type, TextType.NORMAL)

    def test_text_to_textnodes_image(self):
        text = "This is an ![image](https://example.com/image.png) example."
        result = text_to_textnodes(text)

        # Check if the image text is properly split into TextNodes
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is an ")
        self.assertEqual(result[0].type, TextType.NORMAL)
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].type, TextType.IMAGE)
        self.assertEqual(result[1].url, "https://example.com/image.png")
        self.assertEqual(result[2].text, " example.")
        self.assertEqual(result[2].type, TextType.NORMAL)

    def test_empty_text(self):
        text = ""
        result = text_to_textnodes(text)

        # Check if it returns an empty normal TextNode
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].type, TextType.NORMAL)

    def test_combined_text(self):
        text = "This is **bold** and *italic* and `code`."
        result = text_to_textnodes(text)

        # Check if all markdown types are handled correctly
        self.assertEqual(len(result), 7)
        self.assertEqual(result[0].text, "This is ")
        self.assertEqual(result[0].type, TextType.NORMAL)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].type, TextType.BOLD)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[2].type, TextType.NORMAL)
        self.assertEqual(result[3].text, "italic")
        self.assertEqual(result[3].type, TextType.ITALIC)
        self.assertEqual(result[4].text, " and ")
        self.assertEqual(result[4].type, TextType.NORMAL)
        self.assertEqual(result[5].text, "code")
        self.assertEqual(result[5].type, TextType.CODE)
        self.assertEqual(result[6].text, ".")
        self.assertEqual(result[6].type, TextType.NORMAL)

if __name__ == "__main__":
    unittest.main()