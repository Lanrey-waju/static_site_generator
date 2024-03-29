import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italics,
    text_type_link,
    text_type_code,
    text_type_image,
)


class TestTextNode(unittest.TestCase):
    def test_equals(self):
        node = TextNode("Hello, World!", text_type_text)
        node2 = TextNode("Hello, World!", text_type_text)
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("Hello, World!", text_type_text)
        self.assertEqual(node.url, None)

    def test_text_type_is_correct(self):
        node = TextNode("Hello, World", text_type_bold)
        self.assertEqual(node.text_type, text_type_bold)

    def test_text_is_correct(self):
        node = TextNode("Hello, World", text_type_italics)
        self.assertNotEqual(node.text, "Hello, World!")
        self.assertEqual(node.text, "Hello, World")


if __name__ == "__main__":
    unittest.main()
