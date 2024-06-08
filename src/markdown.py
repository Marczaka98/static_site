from textnode import TextNode
import re

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
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Missing matching delimiter in {node.text}")
        splits = []
        sections = node.text.split(delimiter)
        for i in range(len(sections)):
            if sections[i] == '':
                continue
            if i % 2 == 0:
                splits.append(TextNode(sections[i], text_type_text))
            else:
                splits.append(TextNode(sections[i], text_type))
        new_nodes.extend(splits)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        image = extract_markdown_images(node.text)
        word_list = re.split(r"!\[(.*?)\]\((.*?)\)", node.text)
        return word_list