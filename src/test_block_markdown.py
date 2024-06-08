# from block_markdown import *


# # markdown = """This is a **bolded** paragraph

# # This is another paragraph with *italic* text and `code` here
# # This is the same paragraph on a new line

# # * This is a list
# # * with items"""
# # print(markdown_to_blocks(markdown))

# # block = "# This is a heading"
# # block = """```
# # This is a code block
# # This is the second line
# # This is the third line
# # ```"""
# # block = """>This is a quote
# # >This is the second line
# # >This is the third line"""
# # block = """* This is an unordered list
# # * This is the second line
# # * This is the third line"""
# # block = """1. This is an ordered list
# # 2. This is line 2
# # 3. This is line 3"""

# markdown = """# This is a heading

# ```
# This is a code block
# This is the second line
# This is the third line
# ```

# >This is a quote
# >This is the second line
# >This is the third line

# * This is an unordered list
# * This is the second line
# * This is the third line

# 1. This is an ordered list
# 2. This is line 2
# 3. This is line 3

# This is a paragraph
# with a second line
# and a third line"""

# # block_type = block_to_block_type(block)
# # print(paragraph_block_to_htmlnode(block, block_type))

# print(markdown_to_html_node(markdown))