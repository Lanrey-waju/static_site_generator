import unittest

from textnode import TextNdoe


class TestTextNode(unittest.TestCase):
    def test_equals(self):
        node = TextNdoe("Hello, World!", "text")
        node2 = TextNdoe("Hello, World!", "text")
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNdoe("Hello, World!", "text")
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()
