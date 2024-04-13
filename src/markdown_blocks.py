block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def block_to_block_type(markdown):
    if markdown.startswith("# "):
        return block_type_heading
    if markdown.startswith("> "):
        return block_type_quote
    if markdown.startswith("```") and markdown.endswith("```"):
        return block_type_code
    if markdown.startswith("* "):
        return block_type_unordered_list
    if markdown.startswith(r"(\d\.) "):
        return block_type_ordered_list
    return block_type_paragraph


def markdown_to_blocks(markdown_text):
    blocks = markdown_text.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks
