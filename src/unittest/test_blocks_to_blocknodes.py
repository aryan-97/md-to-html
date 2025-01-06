import unittest

from src.markdown.blocknode import BlockNode, BlockType
from src.markdown.blocknode_parser import blocks_to_blocknodes


class TestBlocksToBlocknodes(unittest.TestCase):
    def test_headings(self):
        blocks = ["# Heading 1", "## Heading 2", "### Heading 3", "#### Heading 4", "##### Heading 5", "###### Heading 6"]
        expected = [
            BlockNode(["Heading 1"], BlockType.HEADING1),
            BlockNode(["Heading 2"], BlockType.HEADING2),
            BlockNode(["Heading 3"], BlockType.HEADING3),
            BlockNode(["Heading 4"], BlockType.HEADING4),
            BlockNode(["Heading 5"], BlockType.HEADING5),
            BlockNode(["Heading 6"], BlockType.HEADING6),
        ]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_quote(self):
        blocks = ["> This is a quote"]
        expected = [BlockNode(["This is a quote"], BlockType.QUOTE)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_lists(self):
        blocks = ["* Item 1", "1. Item 2"]
        expected = [
            BlockNode(["Item 1"], BlockType.UNORDERED_LIST),
            BlockNode(["Item 2"], BlockType.ORDERED_LIST),
        ]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_code_block(self):
        blocks = ["```code```"]
        expected = [BlockNode(["code"], BlockType.CODE)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_code_block_empty(self):
        blocks = ["``````"]
        expected = [BlockNode([""], BlockType.CODE)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_code_block_7_ticks(self):
        blocks = ["```````"]
        expected = [BlockNode(["`"], BlockType.CODE)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_code_block_5_ticks(self):
        blocks = ["`````"]
        expected = [BlockNode(["``"], BlockType.CODE)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_multiline_code_block(self):
        blocks = ["```", "line1", "line2", "```"]
        expected = [BlockNode(["\nline1\nline2\n"], BlockType.CODE)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))

    def test_paragraph(self):
        blocks = ["This is a paragraph."]
        expected = [BlockNode(["This is a paragraph."], BlockType.PARAGRAPH)]
        self.assertEqual(expected, blocks_to_blocknodes(blocks))