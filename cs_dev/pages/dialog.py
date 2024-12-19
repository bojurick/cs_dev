from .. import styles
from ..templates import template

import reflex as rx


@template(route="/dialog", title="Dialog")
def dialog() -> rx.Component:
    return rx.grid(
    rx.grid(    
    rx.card("Card 1 L"),
    rx.card("Card 2 L"),
    rx.card("Card 3 L"),
    spacing="2",
    ),
    rx.card("Flur", align="center"),
    rx.grid(    
    rx.card("Card 1 R"),
    rx.card("Card 2 R"),
    rx.card("Card 3 R"),
    spacing="2",
    ),
    spacing="2",
    width="100%",
    columns="3",
)
