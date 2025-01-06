import re

from src.markdown.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: TextNode, delimiter: str, text_type: TextType) -> list[TextNode]:
    if old_nodes.type != TextType.NORMAL:
        return [old_nodes]

    splits = old_nodes.text.split(delimiter)
    if len(splits) % 2 == 0:
        raise ValueError("Invalid markdown syntax. Please check the delimiter.")

    nodes = []
    for i in range(0, len(splits)):
        if i % 2 == 0:
            if splits[i] != "":
                nodes.append(TextNode(splits[i], TextType.NORMAL))
        else:
            nodes.append(TextNode(splits[i], text_type))
    return nodes


def extract_markdown_image(text_with_images: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)]\((.*?)\)", text_with_images)


def split_nodes_image(old_nodes: TextNode) -> list[TextNode]:
    if old_nodes.type != TextType.NORMAL:
        return [old_nodes]

    result = []
    splits = re.split(r"(!\[.*?]\(.*?\))", old_nodes.text)
    for split in splits:
        if split == "":
            continue
        if re.match(r"!\[(.*?)]\((.*?)\)", split):
            img = extract_markdown_image(split)
            result.append(TextNode(img[0][0], TextType.IMAGE, img[0][1]))
        else:
            result.append(TextNode(split, TextType.NORMAL))
    return result


def extract_markdown_link(text_with_links: str) -> list[tuple[str, str]]:
    return re.findall(r"\[(.*?)]\((.*?)\)", text_with_links)


def split_nodes_link(old_nodes: TextNode) -> list[TextNode]:
    if old_nodes.type != TextType.NORMAL:
        return [old_nodes]

    result = []
    splits = re.split(r"(?<!!)(\[.*?]\(.*?\))", old_nodes.text)
    for split in splits:
        if split == "":
            continue
        if re.match(r"(?<!!)\[(.*?)]\((.*?)\)", split):
            link = extract_markdown_link(split)
            result.append(TextNode(link[0][0], TextType.LINK, link[0][1]))
        else:
            result.append(TextNode(split, TextType.NORMAL))
    return result


def iter_for_split(texttype: TextType, nodes: [TextNode]) -> list[TextNode]:
    new_result = []
    for node in nodes:
        match texttype:
            case TextType.BOLD:
                new_result.extend(split_nodes_delimiter(node, "**", TextType.BOLD))
            case TextType.ITALIC:
                new_result.extend(split_nodes_delimiter(node, "*", TextType.ITALIC))
            case TextType.CODE:
                new_result.extend(split_nodes_delimiter(node, "`", TextType.CODE))
            case TextType.LINK:
                new_result.extend(split_nodes_link(node))
            case TextType.IMAGE:
                new_result.extend(split_nodes_image(node))
            case _:
                new_result.append(node)
    return new_result


def text_to_textnodes(text: str) -> list[TextNode]:
    text = TextNode(text, TextType.NORMAL)
    if text.text == "":
        return [text]

    result = [text]
    result = iter_for_split(TextType.CODE, result)
    result = iter_for_split(TextType.IMAGE, result)
    result = iter_for_split(TextType.LINK, result)
    result = iter_for_split(TextType.BOLD, result)
    result = iter_for_split(TextType.ITALIC, result)
    return result
