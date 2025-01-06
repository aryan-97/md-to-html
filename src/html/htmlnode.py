from typing import Optional


class HtmlNode:
    def __init__(self, tag: Optional[str] = None, value: Optional[str] = None, props: Optional[dict[str, str]] = None,
                 children: Optional[list['HtmlNode']] = None):
        self.tag = tag
        self.value = value

        self.props = {}
        self.set_props(props)

        self.children = []
        self.set_children(children)

    def set_children(self, children: Optional[list['HtmlNode']]):
        if children is None:
            self.children = []
        elif not isinstance(children, list):
            raise TypeError(f"children must be a list, but got {type(children).__name__}")
        elif not all(isinstance(child, HtmlNode) for child in children):
            raise TypeError("All elements in children must be instances of HtmlNode")
        else:
            self.children = children

    def set_props(self, props: Optional[dict[str, str]]):
        if props is None:
            self.props = {}
        elif not isinstance(props, dict):
            raise TypeError(f"props must be a dictionary, but got {type(props).__name__}")
        else:
            self.props = props

    def __eq__(self, value: 'HtmlNode'):
        return (self.tag == value.tag and self.value == value.value and self.props == value.props
                and self.children == value.children)

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, {self.props}, {self.children})"

    def to_html(self) -> str:
        raise NotImplementedError("to_html() not implemented")

    def props_to_html(self) -> str:
        return " ".join(f'{key}="{value.replace("\\", "\\\\").replace("\"", "\\\"")}"' for key, value in self.props.items())
