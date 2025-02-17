import re

def markdown_to_blocks(markdown):
    blocks = []
    block_string = ""

    list_pattern = re.compile(r"^(\d+\.\s|\*\s|- )")  # ✅ Matches both ordered and unordered lists

    for string in markdown.splitlines():
        stripped_string = string.strip()

        if stripped_string:
            # ✅ Ensure a new block if a paragraph follows a heading
            if block_string and (block_string.startswith("#") or stripped_string.startswith("#")):
                blocks.append(block_string)
                block_string = stripped_string

            # ✅ Handle lists properly - keep them together
            elif block_string and list_pattern.match(stripped_string) and list_pattern.match(block_string):
                block_string += "\n" + stripped_string  # ✅ Append to the same block

            # ✅ Default case - group paragraphs normally
            elif block_string:
                block_string += "\n" + stripped_string
            else:
                block_string = stripped_string

        else:  # ✅ Empty line = end of block
            if block_string:
                blocks.append(block_string)
                block_string = ""

    if block_string:
        blocks.append(block_string)

    return blocks




def block_to_block_type(block):

    heading_pattern = r'^#{1,6}\s'
    code_pattern = r'^`{3}.*?`{3}$'
    quote_pattern = r'^>{1}'
    unordered_pattern_asterisk = r'^(\*){1}\s'
    unordered_pattern_minus = r'^(\-){1}\s'
    ordered_pattern = r'^\d\.\s'
    lines = block.split('\n')
    

    if re.match(heading_pattern, block):
        return "heading"
    elif re.match(code_pattern, block, flags=re.DOTALL):
        return "code"
    elif all(re.match(quote_pattern, line) for line in lines):
        return "quote"
    elif all(re.match(unordered_pattern_asterisk, line) for line in lines):   
        return "unordered_list"
    elif all(re.match(unordered_pattern_minus, line) for line in lines):   
        return "unordered_list"
    elif all(re.match(ordered_pattern, line) for line in lines):
        for i in range(len(lines)):
            expected_num = i + 1
            if not lines[i].startswith(str(expected_num) + '. '):
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"