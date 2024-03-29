import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_equals(self):
        node = TextNode("Hello, World!", "text")
        node2 = TextNode("Hello, World!", "text")
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("Hello, World!", "text")
        self.assertEqual(node.url, None)

    def test_text_type_is_correct(self):
        node = TextNode("Hello, World", "bold")
        self.assertEqual(node.text_type, "bold")

    def test_text_is_correct(self):
        node = TextNode("Hello, World", "italics")
        self.assertNotEqual(node.text, "Hello, World!")
        self.assertEqual(node.text, "Hello, World")


if __name__ == "__main__":
    unittest.main()
