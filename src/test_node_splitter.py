import unittest

from textnode import TextType, TextNode
from node_splitter import split_nodes_delimiter

class TestHTMLNode(unittest.TestCase):

    def test_basic_bold_split(self):
        input_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)

        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)        
        ]
        self.assertEqual(result, expected_output)

    def test_basic_italic_split(self):
        input_nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        result = split_nodes_delimiter(input_nodes, "*", TextType.ITALIC)

        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected_output)

    def test_invalid_syntax(self):
        input_nodes = [TextNode("This is **invalid bold", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "This is invalid Markdown syntax")

    

        
