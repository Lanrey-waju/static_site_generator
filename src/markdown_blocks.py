block_type_paragraph = "paragraph"


def block_to_blocktype():
    pass


def markdown_to_blocks(markdown_text):
    blocks = markdown_text.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks
