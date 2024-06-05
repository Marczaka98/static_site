import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_all_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        print(f"Testing All Equal For:\n{node}\n{node2}")
        self.assertEqual(node, node2)
    
    def test_url_neq(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "!https://www.boot.dev")
        print(f"Testing URL Not Equal For:\n{node}\n{node2}")
        self.assertEqual(node, node2)

    def test_text_neq(self):
        node = TextNode("This is not a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "!https://www.boot.dev")
        print(f"Testing Text Not Equal For:\n{node}\n{node2}")
        self.assertEqual(node, node2)

    def test_type_neq(self):
        node = TextNode("This is a text node", "italicized", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "!https://www.boot.dev")
        print(f"Testing Text Not Equal For:\n{node}\n{node2}")
        self.assertEqual(node, node2)

    


if __name__ == "__main__":
    unittest.main()
