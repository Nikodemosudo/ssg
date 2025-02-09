from textnode import TextType, TextNode
from link_image_extractors import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    # List of splitted Textnodes
    splitted = []

    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            index = 0
            splits = node.text.split(delimiter)

            # Correctly splitted TextType.TEXT nodes are always splitted odd
            if len(splits) % 2 == 0:
                raise Exception("This is invalid Markdown syntax")
            
            # Pattern is always "TextType.TEXT - TextType.BOLD/ITALIC/CODE" - "TextType.TEXT"
            for split in splits:
                if index % 2 == 0:
                    if split:
                        cleasplitted.append(TextNode(split, TextType.TEXT))
                else:
                    splitted.append(TextNode(split, text_type))
                index += 1
            
        # Else = if texttype is not text, can directly be listed    
        else:
            splitted.append(node)
    
    
    return splitted


# The following functions are commented almost fully
# I found this the way for myself to understand what and why it works.

def split_nodes_image(old_nodes):

    # List of splitted image holding TextNodes
    result = []

    for node in old_nodes:

        # If it's just IMAGE, we can append.
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        # Using this function to store the alt_text + url tuples.
        images = extract_markdown_images(node.text)

        # Are there even images?
        if not images:
            result.append(node)
            continue
        
        # We use current_text to move over different sections of the text in the case there are more images.
        current_text = node.text
        
        # Remember how we got alt_text and url from the extract_markdown_images function?
        for alt_text, url in images:

            # Setting up our split/delimiter.
            image_markdown = f"![{alt_text}]({url})"

            # Only splitting once, making a new section for the next loop (remember current_text)
            sections = current_text.split(image_markdown, 1)

            # There's always a section[0] that will be a TextType.TEXT
            result.append(TextNode(sections[0], TextType.TEXT))

            #This is also our delimiter, and the part we were looking for. Section[1] is all that comes after.
            result.append(TextNode(alt_text, TextType.IMAGE, url))    
            
            # Checking for the number of sections and assigning sections[1] as the new sections[0] for next loop.
            if len(sections) > 1 and sections[1]: 
                current_text = sections[1]
            else:
                current_text = ""

        # If the looping is done, whe check for what's left and append that.        
        if current_text:  
            result.append(TextNode(current_text, TextType.TEXT))
    
    return result

def split_nodes_link(old_nodes):

    result = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue

        current_text = node.text
        for clickable, url in links:
            link_markdown = f"[{clickable}]({url})"
        
            sections = current_text.split(link_markdown, 1)

            result.append(TextNode(sections[0], TextType.TEXT))
            result.append(TextNode(clickable, TextType.LINK, url))

            if len(sections) > 1 and sections[1]:
                current_text = sections[1]
            else:
                current_text = ""
        if current_text:
                result.append(TextNode(current_text, TextType.TEXT))
    
    return result



def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes



     
                



    