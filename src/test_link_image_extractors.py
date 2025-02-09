import unittest
from link_image_extractors import extract_markdown_images, extract_markdown_links

class TestHTMLNode(unittest.TestCase):

    # Tests for extract_markdown_images

    def test_image(self):
        text = "This is an image ![alt text](https://example.com/image.png)"
        result = [("alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), result)

    def test_mult_images(self):
        text = "Image1 ![first](https://img1.png) and Image2 ![second](https://img2.png)"
        result = [("first", "https://img1.png"), ("second", "https://img2.png")]
        self.assertEqual(extract_markdown_images(text), result)
    
    def test_no_images(self):
        text = "Here are no images"
        result = []
        self.assertEqual(extract_markdown_images(text), result)

    def test_empty_alt(self):
        text = "![](https://img1.png)"
        result = [("", "https://img1.png")]
        self.assertEqual(extract_markdown_images(text), result)
    
    #Tests for extract_markdown_links

    def test_line(self):
        text = "Here is a [link](https://linkylink.com)"
        result = [("link", "https://linkylink.com")]
        self.assertEqual(extract_markdown_links(text), result)

    def test_mult_lines(self):
        text = "Links: [Google](https://google.com), [GitHub](https://github.com)"
        result = [("Google", "https://google.com"), ("GitHub", "https://github.com")]
        self.assertEqual(extract_markdown_links(text), result)
    
    def test_with_image(self):
        text = "A [link](https://link.com) and an image ![img](https://img.com)"
        result = [("link", "https://link.com")]
        self.assertEqual(extract_markdown_links(text), result)

    def test_empty_link(self):
        text = "No links here!"
        result = []
        self.assertEqual(extract_markdown_links(text), result)