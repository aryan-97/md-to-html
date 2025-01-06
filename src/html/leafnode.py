from src.html.htmlnode import HtmlNode


class LeafNode(HtmlNode):
    def __init__(self, value: str, tag=None, props=None):
        if value is None:
            raise ValueError("value cannot be None")

        if tag is None and props is not None:
            raise ValueError("tag cannot be None if props is not None")

        super().__init__(tag, value, props, [])

    def to_html(self):
        attributes = f" {self.props_to_html()}" if self.props else ""
        start_tag = f"<{self.tag}{attributes}>" if self.tag else ""
        end_tag = f"</{self.tag}>" if self.tag and self.tag != "img" else ""
        return f"{start_tag}{self.value}{end_tag}"
