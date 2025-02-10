
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




