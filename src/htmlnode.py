

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        propstr = []
        for key, value in self.props.items():
            propstr.append(f'{key}="{value}"')
        return " " + " ".join(propstr)
    
    def __repr__(self):
        return f'HTMLNode(tag= "{self.tag}", value= "{self.value}", children= "{self.children}", props= "{self.props}")'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        attributes = super().props_to_html()

        if not self.value:
             raise ValueError("LeafNode must have a value")
        if not self.tag:
            return str(self.value)
        else:
            return f'<{self.tag}{attributes}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode(tag= "{self.tag}", value= "{self.value}", props= "{self.props}")'

