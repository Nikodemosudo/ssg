import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_notag_leaf(self):
        node = LeafNode(None, "Zonder Tag")
        self.assertEqual(node.to_html(), "Zonder Tag")

    def test_attr(self):
        node = LeafNode("a", "Klik hier voor meer info", {
                            "href": "https://www.google.com",
                            "target": "_blank",
                        })
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Klik hier voor meer info</a>')

    def test_noval_leaf(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("p", None, None)
            node.to_html()
        self.assertEqual(str(context.exception), "LeafNode must have a value")
    
    def test_leafnode_repr(self):
        node = LeafNode(tag="h1", value="Title", props={"class": "header"})
        expected_repr = 'LeafNode(tag= "h1", value= "Title", props= "{\'class\': \'header\'}")'
        self.assertEqual(repr(node), expected_repr)

    # tests for ParentNode (child of HTMLNode)
        
    def test_singlechild(self):
        child = LeafNode(tag="p", value="Hello, World!")
        parent = ParentNode(tag="div", children=[child])
        self.assertEqual(parent.to_html(), '<div><p>Hello, World!</p></div>')

    def test_multichild(self):
        child1 = LeafNode(tag="p", value="Hello, World!")
        child2 = LeafNode(tag="h1", value="A nice title")
        child3 = LeafNode(tag="p", value="Hello, Moon!")
        parent = ParentNode(tag="div", children=[child1, child2, child3])
        self.assertEqual(parent.to_html(), '<div><p>Hello, World!</p><h1>A nice title</h1><p>Hello, Moon!</p></div>')

    def test_props(self):
        child = LeafNode(tag="p", value="Hello, Google!")
        parent = ParentNode("a", [child], {"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(parent.to_html(), '<a href="https://www.google.com" target="_blank"><p>Hello, Google!</p></a>')

    def test_notag_parent(self):
        with self.assertRaises(ValueError) as context:
            child = LeafNode(tag="p", value="Hello, Google!")
            parent = ParentNode(None, [child], {"href": "https://www.google.com", "target": "_blank",})
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have a tag")

    def test_nochild_parent(self):
        with self.assertRaises(ValueError) as context:
            parent = ParentNode("a", None, {"href": "https://www.google.com", "target": "_blank",})
            parent.to_html()
        self.assertEqual(str(context.exception), "ParentNode must have children")

    def test_moreparents(self):
        grandchild = LeafNode(tag="p", value="Hello, Google!")
        child = ParentNode("a", [grandchild], {"href": "https://www.google.com", "target": "_blank",})
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), '<div><a href="https://www.google.com" target="_blank"><p>Hello, Google!</p></a></div>')

    def test_parentnode_repr(self):
        mf = LeafNode("h1", "ALL")       
        doom = LeafNode("h1", "CAPS")    
        node = ParentNode(tag="h1", children=[mf, doom], props={"class": "header"}) 
        expected_repr = 'ParentNode(tag= "h1", children= "[LeafNode(tag= \"h1\", value= \"ALL\", props= \"None\"), LeafNode(tag= \"h1\", value= \"CAPS\", props= \"None\")]", props= "{\'class\': \'header\'}")'
        self.assertEqual(repr(node), expected_repr)

            
    

    
        


    


