from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    #list of splitted Textnodes
    splitted = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            index = 0
            splits = node.text.split(delimiter)

            #correctly splitted TextType.TEXT nodes are always splitted odd
            if len(splits) % 2 == 0:
                raise Exception("This is invalid Markdown syntax")
            
            # pattern is always "TextType.TEXT - TextType.BOLD/ITALIC/CODE" - "TextType.TEXT"
            for split in splits:
                if index % 2 == 0:
                    splitted.append(TextNode(split, TextType.TEXT))
                else:
                    splitted.append(TextNode(split, text_type))
                index += 1
            
        #else = if texttype is not text, can directly be listed    
        else:
            splitted.append(node)
    
    
    return splitted

        


    