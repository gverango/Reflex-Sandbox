
import reflex as rx
from rxconfig import config

@rx.page(route="/jobs")
def jobsCard_function() -> rx.Component:
    # Use rx.text to create a proper Reflex component
    #return rx.text("It works")
    
    container = rx.container(
        
        rx.text("Role", font_size="25px", color="black"),
        rx.text("Description",font_size="16px", color="black" ),
        rx.button("Apply"),
        style={
            "display": "flex",  # Arrange items in a row
            "flex-direction": "column",  # Stack items vertically
            "justify-content": "space-between",  # Space out items evenly
            "padding": "20px",  # Add some padding inside the container
            "border": "1px solid #ccc",  # Add a border to create the box effect
            "border-radius": "20px",  # Round the corners of the box
            "background-color": "#f9f9f9",  # Light background color for the box
            "box-shadow": "0 2px 10px rgba(0, 0, 0, 0.1)",  # Subtle shadow for a 3D effect
            "width": "500px",  # Set the box to  wide
            "length": "500px"  # Set the box to 500px wide

        }
    )
    return container
