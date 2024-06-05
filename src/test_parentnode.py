# import unittest

# from parentnode import ParentNode
# from leafnode import LeafNode

# class TestParentNode(unittest.TestCase):
#     def test_nodes(self):
#         node = ParentNode(
#             "p",
#             [
#                 LeafNode("b", "Bold text"),
#                 LeafNode(None, "Normal text"),
#                 LeafNode("i", "italic text"),
#                 LeafNode(None, "Normal text")
#             ],
#         )
#         node2 = ParentNode("p", [node], {"href": "https://www.google.com"})
#         node3 = ParentNode("h1",[node, node2],None)
#         print(node.to_html())
#         print(node2.to_html())
#         print(node3.to_html())

# if __name__ == "__main__":
#     unittest.main()