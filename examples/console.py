from src.treact.core import Node
from src.treact.renderers.console import ConsoleRenderer


def component(name):
    with Node(f"My comp {name}"):
        Node("Text")


def container_wrapper(name):
    n = Node(f"My wrapper comp {name}")
    with n:
        component(name)
    return n


def tree():
    with Node("Root"):
        with Node("A"):
            component("123")
            Node("B")
            with Node("C"):
                Node("D")
        Node("E")
        component("456")
        for i in range(3):
            Node(f"iter {i}")
        with Node("F"):
            Node("G")
        with container_wrapper("test"):
            Node("under test")


with ConsoleRenderer():
    tree()
