import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = HTMLNode("a", "I'm a Link", ["a", "b", "c"], {"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "I'm a Link")
        self.assertEqual(node.children, ["a", "b", "c"])
        self.assertEqual(node.props, {"href": "https://www.google.com"})

    def test_none(self):
        node = HTMLNode("div")
        self.assertEqual(node.children, None)

    def test_propstohtml(self):
        node = HTMLNode("div", "MFDOOM is cool", ["MF", "DOOM"],
                        {
                            "href": "https://www.google.com",
                            "target": "_blank",
                        })              
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_noneprops(self):
        node = HTMLNode("div", "MFDOOM is cool", ["MF", "DOOM"])
        self.assertEqual(node.props_to_html(), "")

    def test_emptyprops(self):
        node = HTMLNode("div", "MFDOOM is cool", ["MF", "DOOM"], {})
        self.assertEqual(node.props_to_html(), "")

    
        


    


