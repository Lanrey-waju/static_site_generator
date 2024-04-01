from unittest import TestCase

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
)
from textnode import TextNode, text_type_text, text_type_bold


class TestInlineMarkdown(TestCase):
    def test_bold_delimiter(self):
        old_nodes = [
            TextNode("This is a **bold** text", text_type_text),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", text_type_bold)
        self.assertEqual(len(new_nodes), 3)
        self.assertListEqual(
            [
                TextNode("This is a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" text", text_type_text),
            ],
            new_nodes,
        )
