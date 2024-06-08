from textnode import TextNode
import os
import shutil

def main():
    source = "/home/austin/Workspace/github.com/Marczaka98/static_site/static"
    destination = "/home/austin/Workspace/github.com/Marczaka98/static_site/public"
    if os.path.exists(destination):
        shutil.rmtree(destination)
    copy_directory(source, destination)

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

main()