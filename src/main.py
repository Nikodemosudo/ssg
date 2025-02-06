from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    
    example = TextNode("gekke text", TextType.ITALIC_TEXT,"http://gekkedino.nl" )
    print(example)
    example2 = HTMLNode("a", "I'm a Link", ["a", "b", "c"], {"href": "https://www.google.com"})
    print(example2)
main()
