from textnode import *
import re

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
        splits = []
        if node.url is not None:
            new_nodes.append(node)
            continue
        sections = re.split(r"(!\[.*?\]\(.*?\))", node.text)
        for i in range(len(sections)):
            if sections[i] == '':
                continue
            if re.findall(r"!\[(.*?)\]\((.*?)\)", sections[i]) != []:
                image_tup = extract_markdown_images(sections[i])
                splits.append(TextNode(image_tup[0][0], text_type_image, image_tup[0][1]))
            else:
                splits.append(TextNode(sections[i], node.text_type))
        new_nodes.extend(splits)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        splits = []
        if node.url is not None:
            new_nodes.append(node)
            continue
        sections = re.split(r"(\[.*?\]\(.*?\))", node.text)
        for i in range(len(sections)):
            if sections[i] == '':
                continue
            if re.findall(r"\[(.*?)\]\((.*?)\)", sections[i]) != []:
                image_tup = extract_markdown_links(sections[i])
                splits.append(TextNode(image_tup[0][0], text_type_link, image_tup[0][1]))
            else:
                splits.append(TextNode(sections[i], node.text_type))
        new_nodes.extend(splits)
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, "text")
    new_nodes = split_nodes_delimiter([node], '**', text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, '*', text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, '`', text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes