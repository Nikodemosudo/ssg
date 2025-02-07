import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()

