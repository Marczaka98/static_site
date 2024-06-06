from leafnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, compare):
        if (
                self.text == compare.text
                and self.text_type == compare.text_type
                and self.url == compare.url
            ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_note_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    raise ValueError(f"Invalid text type: {text_node.text}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Missing matching delimiter in {node.text}")
        node_text = node.text
        if text_type == text_type_bold:
            new_nodes.extend(splitting_nodes(node_text, delimiter, text_type_bold))
        elif text_type == text_type_italic:
            new_nodes.extend(splitting_nodes(node_text, delimiter, text_type_italic))
        elif text_type == text_type_code:
            new_nodes.extend(splitting_nodes(node_text, delimiter, text_type_code))
    return new_nodes

def splitting_nodes(text, delimiter, text_type):
    if delimiter in text:
        text_split = text.split(delimiter)
        return [
            TextNode(text_split[0], text_type_text), 
            TextNode(text_split[1], text_type), 
            TextNode(text_split[2], text_type_text)
        ]
    return [TextNode(text, text_type_text)]
