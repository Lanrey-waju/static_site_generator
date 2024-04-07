from unittest import TestCase

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italics,
    text_type_code,
    text_type_image,
    text_type_link,
)


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

    def test_bold_delimiter_multiple(self):
        old_nodes = [
            TextNode(
                "This is one **bolded** word and another **bold** word",
                text_type_text,
            )
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", text_type_bold)
        self.assertEqual(len(new_nodes), 5)
        self.assertListEqual(
            [
                TextNode("This is one ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and another ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_italics_delimiter(self):
        old_nodes = [TextNode("This is an *italicized* sentence", text_type_text)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", text_type_italics)
        self.assertEqual(len(new_nodes), 3)
        self.assertListEqual(
            [
                TextNode("This is an ", text_type_text),
                TextNode("italicized", text_type_italics),
                TextNode(" sentence", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        text = "This is a text with an ![image](https://imagesource.com)"
        matches = [("image", "https://imagesource.com")]
        self.assertListEqual(extract_markdown_images(text), matches)

    def test_extract_markdown_links(self):
        text = "This is a text with a [link](https://testfunction.com)"
        matches = [("link", "https://testfunction.com")]
        self.assertListEqual(extract_markdown_links(text), matches)

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is a text with a [link](https://www.example.com) and another [second link](https://www.google.com)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is a text with a ", text_type_text),
                TextNode("link", text_type_link, "https://www.example.com"),
                TextNode(" and another ", text_type_text),
                TextNode("second link", text_type_link, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italics),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode(
                    "image",
                    text_type_image,
                    "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png",
                ),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ],
            textnodes,
        )
