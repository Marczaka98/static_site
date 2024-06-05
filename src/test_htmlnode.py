import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_nodes(self):
        node = HTMLNode("h1", "This is a header", None, {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "This is a paragraph", node, None)
        print(node)
        print(node2)

if __name__ == "__main__":
    unittest.main()