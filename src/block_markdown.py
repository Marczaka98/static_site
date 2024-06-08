import re
from htmlnode import *

block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered list"
block_type_olist = "ordered list"
block_type_paragraph = "paragraph"

def markdown_to_blocks(markdown):
    block_list = markdown.split('\n\n')
    filtered_list = []
    for block in block_list:
        if block == '':
            continue
        block = block.strip()
        filtered_list.append(block)
    return filtered_list

def block_to_block_type(block):
    block_lines = block.split("\n")
    if re.findall(r"^\#{1,6} .+?", block_lines[0]) != []:
        return block_type_heading
    if len(block_lines) > 1 and block_lines[0].startswith("```") and block_lines[-1].startswith("```"):
        return block_type_code
    if re.findall(r"^>.+?", block_lines[0]) != []:
        return block_type_quote
    if re.findall(r"^\* .+?", block_lines[0]) != [] or re.findall(r"^\- .+?", block_lines[0]) != []:
        return block_type_ulist
    if re.findall(r"^1\. .+?", block_lines[0]) != []:    
        for i in range(1,len(block_lines)):
            if re.findall(r"^"+str(i+1)+"\. .+?", block_lines[i]) == []:
                return block_type_paragraph
        return block_type_olist
    return block_type_paragraph

def heading_block_to_htmlnode(block, block_type):
    heading_tag = f"h{block.count('#')}"
    block_text = re.sub(r"^\#{1,6} ", '', block)
    return [HTMLNode(heading_tag, block_text)]

def code_block_to_htmlnode(block, block_type):
    block_text = block.replace("```\n",'').replace("\n```",'')
    return [HTMLNode("pre", None, HTMLNode("code", block_text))]

def quote_block_to_htmlnode(block, block_type):
    block_text = block.replace(">",'')
    return [HTMLNode("blockquote", block_text)]

def ulist_block_to_htmlnode(block, block_type):
    block_text = block.replace("* ", '')
    block_list = block_text.split("\n")
    line_list = []
    for line in block_list:
        line_list.append(HTMLNode("li", line))
    return [HTMLNode("ul", None, line_list)]

def olist_block_to_htmlnode(block, block_type):
    block_list = block.split("\n")
    line_list = []
    for i in range(len(block_list)):
        block_list[i] = block_list[i].replace(f"{i+1}. ", '')
        line_list.append(HTMLNode("li", block_list[i]))
    return [HTMLNode("ol", None, line_list)]

def paragraph_block_to_htmlnode(block, block_type):
    return [HTMLNode("p", block)]

def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    node_list = []
    for block in block_list:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            node_list.append(heading_block_to_htmlnode(block, block_type))
        if block_type == block_type_code:
            node_list.append(code_block_to_htmlnode(block, block_type))
        if block_type == block_type_quote:
            node_list.append(quote_block_to_htmlnode(block, block_type))
        if block_type == block_type_ulist:
            node_list.append(ulist_block_to_htmlnode(block, block_type))
        if block_type == block_type_olist:
            node_list.append(olist_block_to_htmlnode(block, block_type))
        if block_type == block_type_paragraph:
            node_list.append(paragraph_block_to_htmlnode(block, block_type))
    return HTMLNode("div", None, node_list)