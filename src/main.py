from textnode import TextNode
import os
import shutil
from block_markdown import *

def main():
    markdown_path = "/home/austin/Workspace/github.com/Marczaka98/static_site/content/index.md"
    template_path = "/home/austin/Workspace/github.com/Marczaka98/static_site/template.html"
    source = "/home/austin/Workspace/github.com/Marczaka98/static_site/static"
    destination = "/home/austin/Workspace/github.com/Marczaka98/static_site/public"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_directory(source, destination)
    generate_page(markdown_path, template_path, destination)

def copy_directory(source, destination):
    if not os.path.exists(source):
        print(f"Source directory '{source}' does not exist.")
        return
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        destination_item = os.path.join(destination, item)
        if os.path.isdir(source_item):
            copy_directory(source_item, destination_item)
        else:
            shutil.copy(source_item, destination_item)
            # print(f"Copied '{source_item}' to '{destination_item}'")

def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith("# "):
            return line[2:]    
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown_doc = file.read()
    with open(template_path) as file:
        template_doc = file.read()
    html_file = markdown_to_html_node(markdown_doc).to_html()
    title = extract_title(markdown_doc)
    updated_template = template_doc.replace("{{ Title }}", title).replace("{{ Content }}", html_file)
    with open(f"{dest_path}/index.html", 'w') as file:
        file.write(updated_template)

main()