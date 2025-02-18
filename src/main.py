from textnode import TextNode, TextType
from htmlnode import HTMLNode
from markdown_to_html_node import markdown_to_html_node, text_to_children
import os, shutil

def main(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_static(source, destination)
    generate_pages_recursive("content", "template.html", "public")

def copy_static(source, destination):
    print(f"\nEntering directory: {source}")
    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)
        
        if os.path.isfile(src_path):
            print(f"  Copying file: {item}")
            shutil.copy(src_path, dst_path)
        else:
            print(f"  Creating directory: {item}")

            os.mkdir(dst_path)
            copy_static(src_path, dst_path)
        print(f"Finished with directory: {source}")

# Extracts and returns markdown title, removing "# "
def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        stripped_line = line.lstrip()
        if stripped_line.startswith("# "):
            return stripped_line[2: ].strip()
        elif stripped_line and not stripped_line.startswith("# "):
            raise Exception("First content line not a header")
    raise Exception("No header found")

    # Generates the page!
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Reads the given markdown and stores it
    with open(from_path) as opened: 
        read_md = opened.read()
    # Reads the given template and stores it 
    with open(template_path) as opened:
        read_template = opened.read()
    # Creates html from markdown (our conversion)
    html_string = markdown_to_html_node(read_md).to_html()
    # Extracts the title of the markdown
    title = extract_title(read_md)
    # Replaces the Title and Contents of the template with the title and html_string
    replaced_template = read_template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    # Checks for the destination path and if necessary creates it
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    # Writes the file to the end of the destination path
    with open(dest_path, 'w') as file:
        file.write(replaced_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    for item in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, item)
        
        if os.path.isfile(source_path) and source_path.endswith('.md'):
            # Get the relative path from content directory
            rel_path = os.path.relpath(source_path, dir_path_content)
            # Create the destination path maintaining directory structure
            dest_path = os.path.join(dest_dir_path, rel_path.replace('.md', '.html'))
            
            # Ensure destination directory exists
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            
            generate_page(source_path, template_path, dest_path)
        elif os.path.isdir(source_path):
            # Recurse into subdirectory
            new_dest_dir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(source_path, template_path, new_dest_dir)

    

if __name__ == "__main__":
    main("static", "public")