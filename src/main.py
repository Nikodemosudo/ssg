from textnode import TextNode, TextType
from htmlnode import HTMLNode
import os, shutil

def main(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_static(source, destination)

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




if __name__ == "__main__":
    main("static", "public")

    


