from src.html.parentnode import ParentNode
from src.markdown.blocknode_parser import text_to_blocks, blocks_to_blocknodes

def extract_title(text: str) -> str:
    lines = text.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line[2:]
        elif line.strip() == "":
            continue
        else:
            raise ValueError("Title not present.")
    raise ValueError("Title not present.")

def markdown_to_html(text: str) -> str:
    blocks = text_to_blocks(text)
    blocknodes = blocks_to_blocknodes(blocks)
    children = [blocknode.to_htmlnode() for blocknode in blocknodes]
    return ParentNode(tag="div", children=children).to_html()
