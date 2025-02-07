
class HTMLNode:
    """Base class for HTML nodes in the DOM tree"""
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        """Convert node properties to HTML attribute string. Format: key="value" """
        if not self.props:
            return ""
        propstr = []
        for key, value in self.props.items():
            propstr.append(f'{key}="{value}"')
        return " " + " ".join(propstr)
    
    def __repr__(self):
        return f'HTMLNode(tag= "{self.tag}", value= "{self.value}", children= "{self.children}", props= "{self.props}")'
    

class LeafNode(HTMLNode):
    """A leaf node in the DOM tree that can't have children"""
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        """Convert the leaf node to HTML string"""
        attributes = super().props_to_html()

        if not self.value:
             raise ValueError("LeafNode must have a value")
        if not self.tag:
            return str(self.value)
        else:
            return f'<{self.tag}{attributes}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode(tag= "{self.tag}", value= "{self.value}", props= "{self.props}")'
    

class ParentNode(HTMLNode):
    """A parent node in the DOM tree that must have children"""
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        """Convert the parent node and all its children to HTML string, using recursion"""
        attributes = super().props_to_html()
        
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        else:
            string = f"<{self.tag}{attributes}>"
            for child in self.children:
                string += child.to_html()
            string += f"</{self.tag}>"
        return string
    
    def __repr__(self):
        return f'ParentNode(tag= "{self.tag}", children= "{self.children}", props= "{self.props}")'
            
            


