import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_nodes(self):
        node = LeafNode("This is a header", "h1", {"href": "https://www.google.com"})
        node2 = LeafNode("This is a paragraph","p", None)
        print(node.to_html())
        print(node2.to_html())

if __name__ == "__main__":
    unittest.main()