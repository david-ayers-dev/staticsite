from textnode import TextNode, TextType


def main() -> None:
    node = TextNode("this is my text", TextType.CODE_TEXT, "https://www.boot.dev")
    print(node)


main()
