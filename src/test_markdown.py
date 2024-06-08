from markdown import *

# text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
# print(extract_markdown_images(text))
# # [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]

# text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# print(extract_markdown_links(text))
# # [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]

# node = TextNode(
#     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     text_type_text,
# )
# print(split_nodes_image([node]))

# node = TextNode(
#     "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     text_type_text,
# )
# print(split_nodes_link([node]))

text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
print(text_to_textnodes(text))