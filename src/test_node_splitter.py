import unittest

from textnode import TextType, TextNode
from node_splitter import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

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

    # Tests for the image node splitter

    def test_image_split(self):
        input_node = [TextNode("Here is an image ![alt](https://example.com/img.png)", TextType.TEXT)]
        result = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "https://example.com/img.png")
        ]
        self.assertEqual(split_nodes_image(input_node), result)

    def test_multi_images(self):
        input_node = [TextNode("First ![img1](https://img1.png) and second ![img2](https://img2.png)", TextType.TEXT)]
        result = [
            TextNode("First ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "https://img1.png"),
            TextNode(" and second ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "https://img2.png")
        ]
        self.assertEqual(split_nodes_image(input_node), result)

    def test_no_image(self):
        input_node = [TextNode("This text has no images.", TextType.TEXT)]
        result = [TextNode("This text has no images.", TextType.TEXT)]
        self.assertEqual(split_nodes_image(input_node), result)
    
    def test_image_start(self):
        input_node = [TextNode("![start](https://startimage.com) and text", TextType.TEXT)]
        result = [
            TextNode("", TextType.TEXT),
            TextNode("start", TextType.IMAGE, "https://startimage.com"),
            TextNode(" and text", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_image(input_node), result)

    def test_image_end(self):
        input_node = [TextNode("Text first and then ![end](https://endimage.com)", TextType.TEXT)]
        result = [
            TextNode("Text first and then ", TextType.TEXT),
            TextNode("end", TextType.IMAGE, "https://endimage.com"),    
        ]
        self.assertEqual(split_nodes_image(input_node), result)

    # Test for link node splitter

    def test_link_split(self):
        input_node = [TextNode("Check out [Google](https://google.com)", TextType.TEXT)]
        result = [
            TextNode("Check out ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com")
        ]
        self.assertEqual(split_nodes_link(input_node), result)

    def test_multi_link(self):
        input_node = [TextNode("Hey [Link1](https://link1.com) and [Link2](https://link2.com)", TextType.TEXT)]
        result = [
            TextNode("Hey ", TextType.TEXT),
            TextNode("Link1", TextType.LINK, "https://link1.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("Link2", TextType.LINK, "https://link2.com")
        ]
        self.assertEqual(split_nodes_link(input_node), result)

    def test_nolink(self):
        input_node = [TextNode("There are no links here!", TextType.TEXT)]
        result = [TextNode("There are no links here!", TextType.TEXT)]
        self.assertEqual(split_nodes_link(input_node), result)

    def test_end_link(self):
        input_node = [TextNode("This link is right at the [End](https://linkend.com)", TextType.TEXT)]
        result = [
            TextNode("This link is right at the ", TextType.TEXT),
            TextNode("End", TextType.LINK, "https://linkend.com")
        ]
        self.assertEqual(split_nodes_link(input_node), result)

    # Tests for the final text_to_textnodes function

    def test_bold(self):
        input_node = "This is **bold** text"
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_italic(self):
        input_node = "This is *italic* text"
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_code(self):
        input_node = "This is `code` text"
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_multip_image(self):
        input_node = "First ![img1](https://img1.png) and second ![img2](https://img2.png)"
        result = [
            TextNode("First ", TextType.TEXT),
            TextNode("img1", TextType.IMAGE, "https://img1.png"),
            TextNode(" and second ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "https://img2.png")
        ]
        self.assertEqual(text_to_textnodes(input_node), result)
    
    def test_multip_link(self):
        input_node = "First [link1](https://link1.com) and second [link2](https://link2.com)"
        result = [
            TextNode("First ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "https://link1.com"),
            TextNode(" and second ", TextType.TEXT),
            TextNode("link2", TextType.LINK, "https://link2.com")
        ]
        self.assertEqual(text_to_textnodes(input_node), result)
    
    def test_bold_italic(self):
        input_node = "This is **bold** and *italic*"
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC)
        ]
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_link_code(self):
        input_node = "Check [this link](https://thislink.com) with `code`."
        result = [
            TextNode("Check ", TextType.TEXT),
            TextNode("this link", TextType.LINK, "https://thislink.com"),
            TextNode(" with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_empty_string(self):
        input_node = ""
        result = []
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_double_delimiter(self):
        input_node = "We got double **bold****words**!"
        result = [
            TextNode("We got double ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("words", TextType.BOLD),
            TextNode("!", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(input_node), result)

    def test_unbalanced_delimiter(self):
        input_node = "This is **bold and not closed"
        with self.assertRaises(Exception) as context:
            text_to_textnodes(input_node)
        self.assertEqual(str(context.exception), "This is invalid Markdown syntax")
        

    