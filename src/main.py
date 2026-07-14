from textnode import TextNode, TextType

def main():
    text = TextNode("this is my text", TextType.CODE_TEXT, "https://google.com")
    print(text)

main()

