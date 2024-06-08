from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

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