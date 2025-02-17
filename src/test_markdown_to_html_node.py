import unittest
from markdown_to_html_node import markdown_to_html_node
from htmlnode import ParentNode, LeafNode

class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraph_conversion(self):
        markdown = "This is a paragraph."
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("p", [LeafNode(None, "This is a paragraph.")])
        ])

        self.assertEqual(result, expected_output)

    def test_heading_conversion(self):
        markdown = "# Heading 1"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "Heading 1")])
        ])
        self.assertEqual(result, expected_output)

    def test_heading_conversion2(self):
        markdown = "### Heading 3"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("h3", [LeafNode(None, "Heading 3")])
        ])
        self.assertEqual(result, expected_output)

    def test_code_conversion(self):
        markdown = "```print('Hello, World!')```"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
        ParentNode("pre", [LeafNode("code", "print('Hello, World!')")])
    ])
        self.assertEqual(result, expected_output)

    def test_blockquote_conversion(self):
        markdown = "> This is a quote"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("blockquote", [LeafNode(None, "This is a quote")])
        ])
        self.assertEqual(result, expected_output)

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
        ParentNode("ul", [
            ParentNode("li", [LeafNode(None, "Item 1")]),
            ParentNode("li", [LeafNode(None, "Item 2")])
        ])
    ])
        self.assertEqual(result, expected_output)

    def test_ordered_list(self):
        markdown = "1. First item\n2. Second item"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
        ParentNode("ol", [
            ParentNode("li", [LeafNode(None, "First item")]),
            ParentNode("li", [LeafNode(None, "Second item")])
        ])
    ])
        self.assertEqual(result, expected_output)
    
    def test_empty_markdown(self):
        markdown = ""
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [])
        self.assertEqual(result, expected_output)

    def test_nested_blockquote_with_list(self):
        markdown = "> - Quote item 1\n> - Quote item 2"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
         ParentNode("blockquote", [
             ParentNode("ul", [
                    ParentNode("li", [LeafNode(None, "Quote item 1")]),
                    ParentNode("li", [LeafNode(None, "Quote item 2")])
             ])
         ])
     ])
        self.assertEqual(result, expected_output)

    def test_inline_in_p(self):
        markdown = "This is *italic* and **bold** text."
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("p", [
                LeafNode(None, "This is "),
                LeafNode("i", "italic"),
                LeafNode(None, " and "),
                LeafNode("b", "bold"),
                LeafNode(None, " text.")
            ])                             
        ])
        self.assertEqual(result, expected_output)

    def test_list_inline(self):
        markdown = "- *Italic item*\n- **Bold item**"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [LeafNode("i", "Italic item")]),
                ParentNode("li", [LeafNode("b", "Bold item")])
            ])
        ])
        self.assertEqual(result, expected_output)

    def test_incorrect_markdown(self):
        markdown = "This is **bold without closing"
        with self.assertRaises(Exception) as context:
            markdown_to_html_node(markdown)
        self.assertEqual(str(context.exception), "This is invalid Markdown syntax")
    
    def test_ordered_and_inline(self):
        markdown = "1. Item with *italic* text\n2. Item with **bold** text"
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("ol", [
                ParentNode("li", [
                    LeafNode(None, "Item with "),
                    LeafNode("i", "italic"),
                    LeafNode(None, " text")
                    ]),
                ParentNode("li", [
                    LeafNode(None, "Item with "),
                    LeafNode("b", "bold"),
                    LeafNode(None, " text")
                ])
            ])
        ])
        self.assertEqual(result, expected_output) 
    
    def test_heading_before_p(self):
        markdown = "# Heading\nThis is a paragraph under the heading."
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("h1", [LeafNode(None, "Heading")]),
            ParentNode("p", [LeafNode(None, "This is a paragraph under the heading.")])
        ])
        self.assertEqual(result, expected_output)

    def test_paragraph_link_image(self):
        markdown = "This is a [link](https://example.com) and an image ![alt](https://img.com/img.png)."
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("p", [LeafNode(None, "This is a "),
                             LeafNode("a", "link", {"href": "https://example.com"}),
                             LeafNode(None, " and an image "),
                             LeafNode("img", "", {"src": "https://img.com/img.png", "alt": "alt"}),
                             LeafNode(None, ".")])
        ])
        self.assertEqual(result, expected_output)

    def test_code_backticks(self):
        markdown = '```print("Hello, world!")```'
        result = markdown_to_html_node(markdown)
        expected_output = ParentNode("div", [
            ParentNode("pre", [LeafNode('code', 'print("Hello, world!")')])
                       ])
        self.assertEqual(result, expected_output)

    

if __name__ == "__main__":
    unittest.main()