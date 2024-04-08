from unittest import TestCase

from markdown_blocks import markdown_to_blocks


class TestMarkdownBlocks(TestCase):

    def test_markdown_to_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italics* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

"""

        blocks = markdown_to_blocks(text)
        self.assertListEqual(
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italics* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
            blocks,
        )
