from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italics = "italics"
text_type_link = "link"
text_type_code = "code"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"{TextNode}({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(text_node.text, tag=None")
    elif text_node.text_type == text_type_bold:
        return LeafNode(text_node.text, tag="b")
    elif text_node.text_type == text_type_italics:
        return LeafNode(text_node.text, tag="i")
    elif text_node.text_type == text_type_link:
        return LeafNode(text_node.text, tag="a", props={"href": text_node.url})
    elif text_node.text_type == text_type_code:
        return LeafNode(text_node.text, tag="code")
    elif text_node.text_type == text_type_image:
        return LeafNode("", tag="img", props={"src": text_node.url, "alt": text_node.text}))
    else:
        raise ValueError("Invalid text type: {textnode.text_type}")
