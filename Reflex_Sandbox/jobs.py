
import reflex as rx
from rxconfig import config

@rx.page(route="/jobs")
def jobsCard_function() -> rx.Component:
    # Use rx.text to create a proper Reflex component
    return rx.text("It works")