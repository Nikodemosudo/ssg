from markdown_to_blocks import markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node
from node_splitter import text_to_textnodes
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    block_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)
        
        children = text_to_children(block)

        if block_type == "paragraph":
            node = ParentNode("p", children)

        elif block_type == "heading":
            def count_heading_level(block):
                block = block.lstrip()
                i = 0
                while i < len(block) and block[i] == '#':
                    i += 1
                return i                                  
            level = count_heading_level(block)
            heading_text = block[level:].strip()

            children = text_to_children(heading_text)
            node = ParentNode(f"h{level}", children)

        elif block_type == "code":
            code_content = block.strip("`").strip()
            code_node = LeafNode("code", code_content)
            node = ParentNode("pre", [code_node])
        
        elif block_type == "quote":
            quote_text = "\n".join(line.lstrip("> ").strip() for line in block.split("\n"))

        # ✅ If the blockquote is just a simple line of text, treat it as raw text
            if "\n" not in quote_text and not quote_text.startswith(("-", "*", "1.")):
                children = [LeafNode(None, quote_text)]  # Just a LeafNode, no paragraph
            else:
                children = markdown_to_html_node(quote_text).children  # Recursively parse if complex

            node = ParentNode("blockquote", children)

        
        elif block_type == "unordered_list":
            items = []
            for line in block.split('\n'):
                item_text = line[1:].strip()
                item_children = text_to_children(item_text)
                li_node = ParentNode("li", item_children)
                items.append(li_node)
            node = ParentNode("ul", items)
        
        elif block_type == "ordered_list":
            items = []
            for line in block.split('\n'):
                period_index = line.find('.')
                if period_index != -1:

                    item_text = line[period_index + 1:].strip()
                    item_children = text_to_children(item_text)
                    li_node = ParentNode("li", item_children)
                    items.append(li_node)
            node = ParentNode("ol", items)
    
        block_nodes.append(node)
    return ParentNode("div", block_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []

    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes



    






