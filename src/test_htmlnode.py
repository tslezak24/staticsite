import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode 

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode('a', "text in a paragraph", None, props)
        propsTranslated = HTMLNode.props_to_html(node)
        self.assertEqual(propsTranslated, f"href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_to_html_no_child(self):
        node = LeafNode(None, "Hello")
        self.assertEqual(node.to_html(), "Hello")

    

if __name__ == "__main__":
    unittest.main()