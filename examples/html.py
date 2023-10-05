from src.treact.renderers.html import HtmlRenderer


def component(name, context):
    with context.html_node("pre"):
        context.text_node('#' * (len(name) + 6))
        context.text_node(f"# {name} #")
        context.text_node('#' * (len(name) + 6))


def container(context):
    return context.html_node("div", {"style": "border: 1px solid black"})


styles = """
button {
    background-color: red;
}
"""


def ui(context):
    with context.html_node("html"):
        with context.html_node("head"):
            with context.html_node("title"):
                context.text_node("Hello world")

            with context.html_node("style"):
                context.text_node(styles)

        with context.html_node("body"):
            with context.html_node("button", {"onclick": "alert('hello')"}):
                context.text_node("Click me")

            with context.html_node('ol'):
                for i in range(3):
                    with context.html_node('li'):
                        context.text_node(f"list item {i}")

            component("hello components 👋", context)

            with container(context):
                component("look ma, i m trapped in a container", context)


with HtmlRenderer() as context:
    ui(context)
