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
