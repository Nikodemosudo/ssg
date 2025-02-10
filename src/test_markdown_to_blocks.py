import unittest
from markdown_to_blocks import markdown_to_blocks

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
    
    

