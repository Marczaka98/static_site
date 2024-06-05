import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    # def test_all_eq(self):
    #     node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #     node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #     print(f"Testing All Equal For:\n{node}\n{node2}")
    #     self.assertEqual(node, node2)
    
    # def test_url_neq(self):
    #     node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    #     node2 = TextNode("This is a text node", "bold", "!https://www.boot.dev")
    #     print(f"Testing URL Not Equal For:\n{node}\n{node2}")
    #     self.assertEqual(node, node2)

    # def test_text_neq(self):
    #     node = TextNode("This is not a text node", "bold", "https://www.boot.dev")
    #     node2 = TextNode("This is a text node", "bold", "!https://www.boot.dev")
    #     print(f"Testing Text Not Equal For:\n{node}\n{node2}")
    #     self.assertEqual(node, node2)

    # def test_type_neq(self):
    #     node = TextNode("This is a text node", "italicized", "https://www.boot.dev")
    #     node2 = TextNode("This is a text node", "bold", "!https://www.boot.dev")
    #     print(f"Testing Text Not Equal For:\n{node}\n{node2}")
    #     self.assertEqual(node, node2)
    def test_types(self):
        node = TextNode("This is a text node", "text", "https://www.boot.dev")
        node2 = TextNode("This is a bold text node", "bold", "https://www.boot.dev")
        node3 = TextNode("This is an italic text node", "italic", "https://www.boot.dev")
        node4 = TextNode("This is a code node", "code", "https://www.boot.dev")
        node5 = TextNode("This is a link node", "link", "https://www.boot.dev")
        node6 = TextNode("This is an image node", "image", "https://www.boot.dev")
        print(node.text_note_to_html_node().to_html())
        print(node2.text_note_to_html_node().to_html())
        print(node3.text_note_to_html_node().to_html())
        print(node4.text_note_to_html_node().to_html())
        print(node5.text_note_to_html_node().to_html())
        print(node6.text_note_to_html_node().to_html())

if __name__ == "__main__":
    unittest.main()
