import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type


class TestHTMLNode(unittest.TestCase):

    def test_basic_md(self):
        text = "This is a simple paragraph without breaks"
        result = ["This is a simple paragraph without breaks"]
        self.assertEqual(markdown_to_blocks(text), result)

    def test_multi_lines(self):
        text = """First block.
        
        Second block.
        
        Third block."""  
        result = ["First block.", "Second block.", "Third block."]
        self.assertEqual(markdown_to_blocks(text), result)

    def test_lead_trail_empty(self):
        text = """

        First block.

        Second block.
        
        """  
        result = ["First block.", "Second block."]
        self.assertEqual(markdown_to_blocks(text), result)

    def test_multi_empty(self):
        text = """
        Block one.



        Block two.
        
        """
        result = ["Block one.", "Block two."]
        self.assertEqual(markdown_to_blocks(text), result)

    def test_full_empty(self):
        text = ""
        result = []
        self.assertEqual(markdown_to_blocks(text), result)
    
    def test_only_spaces(self):
        text = "             "
        result = []
        self.assertEqual(markdown_to_blocks(text), result)
    
    def test_md_list(self):
        text = """
        * Item one
        * Item two
        * Item three
        """
        result = ["* Item one\n* Item two\n* Item three"]
        self.assertEqual(markdown_to_blocks(text), result)

    def test_md_inline(self):
        text = "This has **bold** and *italic* text."
        result = ["This has **bold** and *italic* text."]
        self.assertEqual(markdown_to_blocks(text), result)


    # tests for block to blocktype function

    def test_heading(self):
        text = "###### This is a heading, you know"
        result = "heading"
        self.assertEqual(block_to_block_type(text), result)

    def test_faulty_heading(self):
        text = "#I want to be a heading"
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)

    def test_code(self):
        text = """```
        print('Hello World')
        ```"""
        result = "code"
        self.assertEqual(block_to_block_type(text), result)

    def test_unclosed_code(self):
        text = """```
        print('HelloWorld)"""
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)
    
    def test_inline_code(self):
        text = "This is ```print('inline code')```"
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)

    def test_single_quote(self):
        text = "> This is a quote."
        result = "quote"
        self.assertEqual(block_to_block_type(text), result)

    def test_multi_quote(self):
        text = """> Quote 1
> Quote 2
> Quote 3"""     
        result = "quote"
        self.assertEqual(block_to_block_type(text), result)

    def test_faulty_multi(self):
        text = """> Quote 1
Quote 2"""
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)

    def test_unordered_star(self):
        text = """* Item 1
* Item 2
* Item 3"""
        result = "unordered_list"
        self.assertEqual(block_to_block_type(text), result)

    def test_unordered_minus(self):
        text = """- Item 1
- Item 2
- Item 3"""
        result = "unordered_list"
        self.assertEqual(block_to_block_type(text), result)
    
    def test_unordered_mixed(self):
        text = """* Item 1
- Item 2"""
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)

    def test_ordered(self):
        text = """1. First item
2. Second item
3. Third item"""
        result = "ordered_list"
        self.assertEqual(block_to_block_type(text), result)

    def test_faulty_ordered(self):
        text = """1. First item
3. Third item
7. Seventh item"""
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)

    def test_pargraph(self):
        text = "This is just a bunch of text, nothing to see here but paragraph"
        result = "paragraph"
        self.assertEqual(block_to_block_type(text), result)

    
    

