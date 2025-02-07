import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_init(self):
        node = TextNode("Tokyo, Japan", TextType.ITALIC, "https://kobusdepoes.nl")
        self.assertEqual(node.text, "Tokyo, Japan")
        self.assertEqual(node.text_type, TextType.ITALIC)
        self.assertEqual(node.url, "https://kobusdepoes.nl")

    def test_urlnone(self):
        node = TextNode("Tokyo, Japan", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_diftype(self):
        node = TextNode("Tokyo, Japan", TextType.BOLD)
        self.assertNotEqual(node.text_type, TextType.IMAGE)

    def test_repr(self):
        node = TextNode("Tokyo, Japan", TextType.ITALIC, "https://kobusdepoes.nl")
        expected = "TextNode(Tokyo, Japan, italic, https://kobusdepoes.nl)"
        self.assertEqual(expected, repr(node))

    # Testing Text node to HTML node

    def test_bold(self):
        node = TextNode("I am bold", TextType.BOLD, None)
        self.assertEqual(text_node_to_html_node(node), LeafNode("b", "I am bold", None))

    def test_italic(self):
        node = TextNode("I am italic", TextType.ITALIC, None)
        self.assertEqual(text_node_to_html_node(node), LeafNode("i", "I am italic", None))

    def test_code(self):
        node = TextNode("I am code", TextType.CODE, None)
        self.assertEqual(text_node_to_html_node(node), LeafNode("code", "I am code", None))

    def test_link_with_url(self):
        node = TextNode("I am link", TextType.LINK, "https://example.com")
        self.assertEqual(
        text_node_to_html_node(node),
        LeafNode("a", "I am link", {"href": "https://example.com"})
    )
        
    def test_link_without_url(self):
        node = TextNode("Broken link", TextType.LINK, None)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "No URL detected")

    def test_image_with_url(self):
        node = TextNode("An image", TextType.IMAGE, "https://example.com/image.jpg")
        self.assertEqual(
            text_node_to_html_node(node),
            LeafNode("img", "", {"src": "https://example.com/image.jpg", "alt": "An image"})
        )

    def test_image_without_url(self):
        node = TextNode("Missing URL", TextType.IMAGE, None)
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "No img/URL detected")

    def test_unknown(self):
        node = TextNode("I am text", TextType.NORMAL, None)
        node.text_type = "not_a_valid_type"
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "TextType is not known")




      