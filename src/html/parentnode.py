from src.html.htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag: str, children: list[HtmlNode], props=None):
        if tag is None:
            raise TypeError("tag cannot be None")

        if not isinstance(children, list):
            raise TypeError(f"children must be a list, but got {type(children).__name__}")

        if not all(isinstance(child, HtmlNode) for child in children):
            raise TypeError("All elements in children must be instances of HtmlNode")

        if children is None:
            raise ValueError("children cannot be None")

        super().__init__(tag, None, props, children)

    def to_html(self) -> str:
        attributes = f" {self.props_to_html()}" if self.props else ""
        start_tag = f"<{self.tag}{attributes}>"
        end_tag = f"</{self.tag}>"
        return f"{start_tag}{self.children_to_html()}{end_tag}"

    def children_to_html(self) -> str:
        return "".join(child.to_html() for child in self.children)