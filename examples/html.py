from src.treact.renderers.html import html_node, text_node, HtmlRenderer


def component(name):
    with html_node("pre"):
        text_node('#' * (len(name) + 6))
        text_node(f"# {name} #")
        text_node('#' * (len(name) + 6))


def container():
    return html_node("div", {"style": "border: 1px solid black"})


styles = """
button {
    background-color: red;
}
"""


def ui():
    with html_node("html"):
        with html_node("head"):
            with html_node("title"):
                text_node("Hello world")

            with html_node("style"):
                text_node(styles)

        with html_node("body"):
            with html_node("button", {"onclick": "alert('hello')"}):
                text_node("Click me")

            with html_node('ol'):
                for i in range(3):
                    with html_node('li'):
                        text_node(f"list item {i}")

            component("hello components 👋")

            with container():
                component("look ma, i m trapped in a container")


with HtmlRenderer():
    ui()
