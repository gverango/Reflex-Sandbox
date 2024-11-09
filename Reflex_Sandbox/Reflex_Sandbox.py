"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .jobs import jobsCard_function

class State(rx.State):
    """The app state."""
    active_tab: str = "Company"  # Default tab

    # Method to set the active tab
    def set_tab(self, tab_name: str):
        self.active_tab = tab_name

def index() -> rx.Component:

    def tabs_function():
        return rx.cond(
            State.active_tab == "Company",
            #content will be swapped with ai generated response 
            rx.text("Broke startup founded in 2024.", margin_top="10px", font_size="14px", color="gray"), 
            rx.cond(
                State.active_tab == "Jobs",
                #rx.text("Frontend Developer, Backend Developer, Sales Intern", margin_top="10px", font_size="14px", color="gray"),
                jobsCard_function(),
                rx.text("Pass the vibe check? \n yes!", margin_top="10px", font_size="14px", color="gray")
            )
        )

    return rx.box(  # Use a full-page box with flex properties
        rx.color_mode.button(position="absolute", top="10px", right="10px"),  # Top-right color mode button
        rx.center(  # Center the main content
            rx.vstack(
                rx.heading("Companies & Internships", size="3", spacing="50"),
                rx.box(  # CARD
                    rx.vstack(
                        # Logo, Company Title, Motto
                        rx.hstack(
                            rx.image(src="path/to/logo.png", height="50px", width="50px", border_radius="10px"),
                            rx.text("Airbnb", font_size="24px", font_weight="bold"),
                            rx.spacer(),
                        ),
                        rx.text("Book accommodations around the world.", font_size="16px", color="gray"),
                        rx.divider(margin_y="10px"),
                        
                        # Tabs
                        rx.hstack(
                            rx.text(
                                "Company",
                                font_size="18px",
                                padding="10px",
                                cursor="pointer",
                                color=rx.cond(State.active_tab == "Company", "black", "gray"),
                                font_weight=rx.cond(State.active_tab == "Company", "bold", "normal"),
                                on_click=State.set_tab("Company")
                            ),
                            rx.text(
                                "Jobs",
                                font_size="18px",
                                padding="10px",
                                cursor="pointer",
                                color=rx.cond(State.active_tab == "Jobs", "black", "gray"),
                                font_weight=rx.cond(State.active_tab == "Jobs", "bold", "normal"),
                                on_click=State.set_tab("Jobs")
                            ),
                            rx.text(
                                "Red Flags",
                                font_size="18px",
                                padding="10px",
                                cursor="pointer",
                                color=rx.cond(State.active_tab == "Red Flags", "black", "gray"),
                                font_weight=rx.cond(State.active_tab == "Red Flags", "bold", "normal"),
                                on_click=State.set_tab("Red Flags")
                            ),
                            spacing="20px"
                        ),
                        tabs_function(),  # Display tab content conditionally
                        padding="20px",
                        border_radius="15px",
                        border="1px solid #e0e0e0",
                        background_color="white",
                        width="600px",  # Fixed width for better centering
                        box_shadow="0 2px 5px rgba(0, 0, 0, 0.1)",
                    )
                ),
                spacing="50px",  # Adjusted spacing between heading and card
            )
        ),
        rx.box(  # Bottom logo box
            rx.logo(),
            position="absolute",
            bottom="10px",
            left="50%",
            transform="translateX(-50%)"  # Center horizontally
        ),
        position="relative",
        min_height="100vh"  # Full page height
    )

# App starting up
app = rx.App()
app.add_page(index)
