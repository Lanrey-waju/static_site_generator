from unittest import TestCase

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHtmlNode(TestCase):

    def test_props_to_html_works(self):
        node = HTMLNode(
            "div", "Hello, World!", children=None, props={"class": "test", "id": "test"}
        )
        self.assertEqual(node.props_to_html(), ' class="test" id="test"')

    def test_props_to_html_works_when_no_props(self):
        node = HTMLNode("div", "Hello, World!", children=None, props=None)
        self.assertEqual(node.props_to_html(), "")

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

    def test_parent_node_to_html_works(self):
        node1 = ParentNode(
            "div",
            [
                LeafNode("b", "bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        node2 = ParentNode(
            "p",
            [
                LeafNode("b", "bold text", props={"class": "test", "id": "test"}),
                LeafNode(None, "Normal text", props={"class": "test", "id": "test"}),
                LeafNode("i", "italic text", props={"class": "test", "id": "test"}),
                LeafNode("a", "link", props={"href": "https://www.example.com"}),
            ],
        )
        self.assertEqual(
            node1.to_html(),
            "<div><b>bold text</b>Normal text<i>italic text</i>Normal text</div>",
        )
        self.assertEqual(
            node2.to_html(),
            '<p><b class="test" id="test">bold text</b>Normal text<i class="test" id="test">italic text</i><a href="https://www.example.com">link</a></p>',
        )
