from unittest import TestCase

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(TestCase):

    def test_props_to_html_works(self):
        node = HTMLNode(
            "div", "Hello, World!", children=None, props={"class": "test", "id": "test"}
        )
        self.assertEqual(node.props_to_html(), ' class="test" id="test"')

    def test_props_to_html_works_when_no_props(self):
        node = HTMLNode("div", "Hello, World!", children=None, props=None)
        self.assertEqual(node.props_to_html(), "")


class TestLeafNode(TestCase):

    def test_leaf_node_raises_error_when_value_is_none(self):
        with self.assertRaises(ValueError):
            LeafNode(None).to_html()

    def test_to_html_works(self):
        div_node = LeafNode(
            "div", "Hello, World!", props={"class": "test", "id": "test"}
        )
        link_node = LeafNode(
            "a", "Click me!", props={"href": "https://www.example.com"}
        )
        self.assertNotEqual(div_node.to_html(), "Hello, World!")
        self.assertEqual(
            div_node.to_html(), '<div class="test" id="test">Hello, World!</div>'
        )
        self.assertNotEqual(
            div_node.to_html(), "<p class='test' id='test'>Hello, World!</p>"
        )
        self.assertEqual(
            link_node.to_html(), '<a href="https://www.example.com">Click me!</a>'
        )
        self.assertNotEqual(div_node.to_html(), link_node.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
