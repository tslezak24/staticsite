import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text", "bold", "https://www.google.com")
        node2 = TextNode("This is a text node", "bold", "https://www.google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
