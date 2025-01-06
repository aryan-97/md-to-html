import re

from src.markdown.blocknode import BlockNode, BlockType


def text_to_blocks(text: str) -> list[str]:
    sections = text.splitlines()
    return [section.strip() for section in sections if section.strip()]


def blocks_to_blocknodes(blocks: list[str]) -> list[BlockNode]:
    result = []
    code_start = False
    code_blocks: list[str] = []
    ordered_list_running = False
    ordered_list = []
    unordered_list_running = False
    unordered_list = []
    for block in blocks:

        if ordered_list_running:
            if not re.match(r"\d+\. ", block) and len(ordered_list) > 0:
                result.append(BlockNode(ordered_list, BlockType.ORDERED_LIST))
                ordered_list_running = False
                ordered_list = []

        if unordered_list_running:
            if not block.startswith("* ") and len(unordered_list) > 0:
                result.append(BlockNode(unordered_list, BlockType.UNORDERED_LIST))
                unordered_list_running = False
                unordered_list = []

        if block.startswith("```") and block.endswith("```") and len(block) >= 6:
            block = block[3:-3]
            result.append(BlockNode([block], BlockType.CODE))
        elif block.startswith("```") and not code_start:
            code_start = True
            block = block[3:]
            code_blocks.append(block)
        elif code_start:
            finished = False
            if block.endswith("```"):
                block = block[:-3]
                code_blocks.append(block)
                finished = True
            elif block.startswith("```"):
                code_blocks.append('')
                finished = True
            else:
                code_blocks.append(block)

            if finished:
                result.append(BlockNode(["\n".join(code_blocks)], BlockType.CODE))
                code_start = False
                code_blocks = []
        elif block.startswith("# "):
            block = block[2:]
            result.append(BlockNode([block], BlockType.HEADING1))
        elif block.startswith("## "):
            block = block[3:]
            result.append(BlockNode([block], BlockType.HEADING2))
        elif block.startswith("### "):
            block = block[4:]
            result.append(BlockNode([block], BlockType.HEADING3))
        elif block.startswith("#### "):
            block = block[5:]
            result.append(BlockNode([block], BlockType.HEADING4))
        elif block.startswith("##### "):
            block = block[6:]
            result.append(BlockNode([block], BlockType.HEADING5))
        elif block.startswith("###### "):
            block = block[7:]
            result.append(BlockNode([block], BlockType.HEADING6))
        elif block.startswith("> "):
            block = block[2:]
            result.append(BlockNode([block], BlockType.QUOTE))
        elif block.startswith("* "):
            unordered_list_running = True
            block = block[2:]
            unordered_list.append(block)
        elif re.match(r"\d+\. ", block):
            ordered_list_running = True
            block = re.split(r"\d+\. ", block)[1]
            ordered_list.append(block)
        else:
            result.append(BlockNode([block], BlockType.PARAGRAPH))

    if len(code_blocks) > 0:
        result.append(BlockNode(["\n".join(code_blocks)], BlockType.CODE))
        code_start = False
        code_blocks = []

    if unordered_list_running:
        result.append(BlockNode(unordered_list, BlockType.UNORDERED_LIST))
        unordered_list_running = False
        unordered_list = []

    if ordered_list_running:
        result.append(BlockNode(ordered_list, BlockType.ORDERED_LIST))
        ordered_list_running = False
        ordered_list = []

    return result
