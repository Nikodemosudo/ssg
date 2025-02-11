import re

def markdown_to_blocks(markdown):
    list_of_strings = []
    block_string = ""
    
    for string in markdown.splitlines():
        stripped_string = string.strip()

        if stripped_string:
            if block_string:
                block_string += "\n"
            block_string += stripped_string
        else:
            if block_string:
                list_of_strings.append(block_string)
                block_string = ""
                
    # This is the last block, which is not accounted for in the loop, in case there is no last-empty line.
    if block_string:
        list_of_strings.append(block_string)
     
    return list_of_strings


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