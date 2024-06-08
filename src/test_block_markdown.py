from block_markdown import *


# markdown = """This is a **bolded** paragraph

# This is another paragraph with *italic* text and `code` here
# This is the same paragraph on a new line

# * This is a list
# * with items"""
# print(markdown_to_blocks(markdown))

# block = "####### This is a heading"
block = """```
This is a code block
```"""
# block = ">This is a quote"
# block = """* This is an unordered list
# * This is another line of the list"""
# block = """1. This is an ordered list
# 2. This is line 2
# 3. This is line 3
# 4. This is line 4"""
print(block_to_block_type(block))