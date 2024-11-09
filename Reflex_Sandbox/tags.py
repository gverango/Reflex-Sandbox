import reflex as rx
from rxconfig import config

def complete_component() -> rx.Component:
    """
    check_icon_svg = (
        '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<path d="M20 6 L9 17 L5 13" stroke="green" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" />'
        '</svg>'
    )
    """
    
    return rx.badge(
        rx.hstack(
            #rx.html(check_icon_svg),  # Embeds the SVG as raw HTML
            rx.text("STARTUP", color="green"),
            spacing="8px"
        ),
        border_color="green",
        border_radius="12px",
        padding="4px 8px",
        background_color="#000000",
        border_width="1px",
        border_style="solid",
        display="inline-flex",
        align_items="center"
    )

@rx.page(route="/tags")
def tags_function() -> rx.Component:
    return rx.vstack(
        completed_component()
    )
