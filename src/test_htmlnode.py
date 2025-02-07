import unittest

from htmlnode import HTMLNode, LeafNode

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

    # tests for LeafNode (child of HTMLNode)
    
    def test_tagval(self):
        node = LeafNode("h1", "Dit is een Titel")
        self.assertEqual(node.to_html(), "<h1>Dit is een Titel</h1>")

    def test_notag(self):
        node = LeafNode(None, "Zonder Tag")
        self.assertEqual(node.to_html(), "Zonder Tag")

    def test_attr(self):
        node = LeafNode("a", "Klik hier voor meer info", {
                            "href": "https://www.google.com",
                            "target": "_blank",
                        })
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Klik hier voor meer info</a>')

    def test_noval(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("p", None, None)
            node.to_html()
        self.assertEqual(str(context.exception), "LeafNode must have a value")
    
    def test_leafnode_repr(self):
        node = LeafNode(tag="h1", value="Title", props={"class": "header"})
        expected_repr = 'LeafNode(tag= "h1", value= "Title", props= "{\'class\': \'header\'}")'
        self.assertEqual(repr(node), expected_repr)
        
    

    

    
        


    


