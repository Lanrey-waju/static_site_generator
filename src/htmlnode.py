class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        if self.props is not None:
            return "".join([f' {key}="{value}"' for key, value in self.props.items()])
        else:
            return ""

    def __repr__(self):
        return (
            f"HTMLNode{self.tag}, {self.value}, children: {self.children}, {self.props}"
        )


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be empty")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
