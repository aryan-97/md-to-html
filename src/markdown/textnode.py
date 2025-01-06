from enum import Enum

from src.html.htmlnode import HtmlNode
from src.html.leafnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self, text, texttype, url=None):
        self.text = text
        self.type = texttype
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.type == other.type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"

    def to_htmlnode(self) -> HtmlNode:
        if self.type == TextType.NORMAL:
            return LeafNode(self.text)
        elif self.type == TextType.BOLD:
            return LeafNode(self.text, tag="b")
        elif self.type == TextType.ITALIC:
            return LeafNode(self.text, tag="i")
        elif self.type == TextType.CODE:
            return LeafNode(self.text, tag="code")
        elif self.type == TextType.LINK:
            return LeafNode(self.text, tag="a", props={"href": self.url})
        elif self.type == TextType.IMAGE:
            return LeafNode("", tag="img", props={"src": self.url, "alt": self.text})
        else:
            raise ValueError(f"Invalid TextType: {self.type}")
