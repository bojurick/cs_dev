from .. import styles
from ..templates import template

import reflex as rx


@template(route="/login", title="Login")
def login() -> rx.Component:
    return rx.container(
        rx.center(
            rx.card(
                rx.vstack(
                    rx.center(
                        rx.color_mode_cond(
                            rx.image(src="/reflex_black.svg", height="1.5em"),
                            rx.image(src="/reflex_white.svg", height="1.5em"),
                        ),
                        rx.heading(
                            "Sign in to your account",
                            size="6",
                            as_="h2",
                            text_align="center",
                            width="100%",
                        ),
                        direction="column",
                        spacing="5",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text(
                            "Email address",
                            size="3",
                            weight="medium",
                            text_align="left",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="user@reflex.dev",
                            type="email",
                            size="3",
                            width="100%",
                        ),
                        justify="start",
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.hstack(
                            rx.text(
                                "Password",
                                size="3",
                                weight="medium",
                            ),
                            rx.link(
                                "Forgot password?",
                                href="#",
                                size="3",
                            ),
                            justify="between",
                            width="100%",
                        ),
                        rx.input(
                            placeholder="Enter your password",
                            type="password",
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button("Sign in", size="3", width="100%"),
                    rx.center(
                        rx.text("New here?", size="3"),
                        rx.link("Sign up", href="#", size="3"),
                        opacity="0.8",
                        spacing="2",
                        direction="row",
                    ),
                    spacing="6",
                    width="100%",
                ),
                size="4",
                max_width="28em",
                width="100%",
            ),
        ),
        width="100%",

    )
