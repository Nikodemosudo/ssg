import unittest
from main import extract_title

class TestHTMLNode(unittest.TestCase):

    # Testing heading extraction, returns heading without "# "
    def test_heading_extraction(self):
        markdown = "# Heading 1\n a whole bunch of text"
        result = extract_title(markdown)
        expected_output = "Heading 1"
        self.assertEqual(result, expected_output)

    # Testing no heading with extraction, returns Exception
    def test_no_heading_extraction(self):
        markdown = "I just start yapping\nAnd yapping\nAnd yapping"
        with self.assertRaises(Exception):
            extract_title(markdown)

    # Testing if header comes after other content, returns Exception
    def test_header_after_content(self):
        markdown = "Starting off with content\n # And now a header"
        with self.assertRaises(Exception):
            extract_title(markdown)

    # Testing multiple blank lines before header
    def test_header_preceded_blanks(self):
        markdown = "\n\n\n# And a header!"
        result = extract_title(markdown)
        expected_output = "And a header!"
        self.assertEqual(result, expected_output)
        







   