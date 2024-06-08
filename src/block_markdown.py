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
    return(HTMLNode(heading_tag, block_text))

def code_block_to_htmlnode(block, block_type):
    block_text = block.replace("```\n",'').replace("\n```",'')
    return HTMLNode("pre", None, [HTMLNode("code", block_text)])
    