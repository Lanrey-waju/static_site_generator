from unittest import TestCase

from htmlnode import HTMLNode


class TestHtmlNode(TestCase):

    def test_props_to_html_works(self):
        node = HTMLNode(
            "div", "Hello, World!", children=None, props={"class": "test", "id": "test"}
        )
        self.assertEqual(node.props_to_html(), ' class="test" id="test"')

    def test_props_to_html_works_when_no_props(self):
        node = HTMLNode("div", "Hello, World!", children=None, props=None)
        self.assertEqual(node.props_to_html(), "")
