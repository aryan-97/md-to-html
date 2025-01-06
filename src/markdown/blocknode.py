from enum import Enum

from src.html.htmlnode import HtmlNode
from src.html.leafnode import LeafNode
from src.html.parentnode import ParentNode
from src.markdown.textnode_parser import text_to_textnodes


class BlockType(Enum):
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"
    PARAGRAPH = "paragraph"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


class BlockNode:

    def __init__(self, text: list[str], blocktype: BlockType):
        self.text = text
        self.type = blocktype

    def __eq__(self, other):
        return self.text == other.text and self.type == other.type

    def __repr__(self):
        return f"BlockNode({self.text}, {self.type.value})"

    def to_htmlnode(self) -> HtmlNode:
        if self.type == BlockType.HEADING1:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="h1", children=html_nodes)
        elif self.type == BlockType.HEADING2:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="h2", children=html_nodes)
        elif self.type == BlockType.HEADING3:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="h3", children=html_nodes)
        elif self.type == BlockType.HEADING4:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="h4", children=html_nodes)
        elif self.type == BlockType.HEADING5:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="h5", children=html_nodes)
        elif self.type == BlockType.HEADING6:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="h6", children=html_nodes)
        elif self.type == BlockType.QUOTE:
            return LeafNode(self.text[0], tag="blockquote")
        elif self.type == BlockType.CODE:
            return ParentNode(tag="pre", children=[LeafNode(self.text[0], tag="code")])
        elif self.type == BlockType.UNORDERED_LIST:
            li_children = []
            for item in self.text:
                text_nodes = text_to_textnodes(item)
                html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
                li_children.append(ParentNode(tag="li", children=html_nodes))
            return ParentNode(tag="ul", children=li_children)
        elif self.type == BlockType.ORDERED_LIST:
            li_children = []
            for item in self.text:
                text_nodes = text_to_textnodes(item)
                html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
                li_children.append(ParentNode(tag="li", children=html_nodes))
            return ParentNode(tag="ol", children=li_children)
        elif self.type == BlockType.PARAGRAPH:
            text_nodes = text_to_textnodes(self.text[0])
            html_nodes = [textnode.to_htmlnode() for textnode in text_nodes]
            return ParentNode(tag="p", children=html_nodes)


