from nicegui import ui


PRIMARY = "#1152d4"
BG_LIGHT = "#f6f6f8"
BG_DARK = "#101622"


@ui.page("/quote")
def contact():
    ui.colors(primary=PRIMARY)
    ui.query("body").style(
        f"background-color: {BG_LIGHT}; color: #0d121b; font-family: Manrope, sans-serif;"
    )

    # PAGE CONTAINER
    with ui.column().classes("w-full max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8"):
        with ui.row().classes("grid grid-cols-1 lg:grid-cols-5 gap-12 w-full"):

            # LEFT COLUMN: Quote Form
            with ui.column().classes("lg:col-span-3 bg-white p-8 rounded-xl shadow-sm"):
                ui.label("Get an Instant Shipping Quote").classes(
                    "text-3xl font-bold pb-2 text-[#0d121b]"
                )
                ui.label(
                    "Fill in the details below to calculate your shipping costs."
                ).classes("text-gray-500 mb-8")

                with ui.column().classes("space-y-6"):

                    # Origin / Destination
                    with ui.row().classes(
                        "grid grid-cols-1 sm:grid-cols-2 gap-x-4 gap-y-6"
                    ):
                        ui.input("Origin Country/Zip").props(
                            f"outlined dense color={PRIMARY}"
                        ).classes("h-14")
                        ui.input("Destination Country/Zip").props(
                            f"outlined dense color={PRIMARY}"
                        ).classes("h-14")

                    # Weight & Dimensions
                    with ui.column():
                        with ui.row().classes("items-center justify-between pb-2"):
                            ui.label("Package Weight & Dimensions").classes(
                                "text-base font-medium"
                            )
                            ui.label("Units: Lbs / Kg, In / Cm").classes(
                                "text-sm text-gray-500"
                            )

                        with ui.row().classes(
                            "grid grid-cols-1 sm:grid-cols-4 gap-x-4 gap-y-6"
                        ):
                            ui.number(
                                label="Weight (Lbs)", placeholder="Enter weight"
                            ).classes("sm:col-span-2 h-14")
                            ui.number(label="Width", placeholder="Width").classes(
                                "h-14"
                            )
                            ui.number(label="Height", placeholder="Height").classes(
                                "h-14"
                            )

                    # Service Type
                    with ui.column():
                        ui.label("Service Type").classes("text-base font-medium pb-2")
                        ui.select(
                            [
                                "Standard Shipping",
                                "Express Shipping",
                                "International Priority",
                                "Freight & Cargo",
                            ],
                            label="Select a service",  # Use label for the placeholder text
                            value=None,  # Or just omit value, but this is explicit
                        ).classes("w-full rounded-lg h-14")

                    # Submit Button
                    ui.button(
                        "Calculate Estimate",
                        color=PRIMARY,
                        on_click=lambda: ui.notify("Quote calculated!"),
                    ).classes("w-full text-white text-lg font-semibold py-4 rounded-lg")

            # RIGHT COLUMN: Contact + Form
            with ui.column().classes("lg:col-span-2 space-y-8"):

                # Contact Info
                with ui.card().classes("p-8 rounded-xl shadow-sm"):
                    ui.label("Contact Us").classes("text-xl font-bold mb-6")
                    contact_items = [
                        (
                            "location_on",
                            "Our Office",
                            "123 Logistics Lane, Suite 100\nTransport City, TS 54321",
                        ),
                        ("mail", "Customer Support", "support@shipfast.com"),
                        ("call", "Phone", "+1 (800) 555-0123"),
                        (
                            "schedule",
                            "Operating Hours",
                            "Mon–Fri: 8:00 AM - 6:00 PM\nSat: 9:00 AM - 1:00 PM",
                        ),
                    ]

                    for icon, title, info in contact_items:
                        with ui.row().classes("items-start space-x-4 mb-4"):
                            ui.icon(icon).classes(f"text-[{PRIMARY}] text-xl mt-1")
                            with ui.column():
                                ui.label(title).classes("font-semibold text-[#0d121b]")
                                ui.label(info).classes(
                                    "text-gray-600 whitespace-pre-line"
                                )

                    # Map Placeholder
                    ui.image(
                        "https://lh3.googleusercontent.com/aida-public/AB6AXuCtQpW9zOgffW_SXZiOE-otE-bG30e-yEuS7GEiV-qnf-EoHCC7qn1xw5kblOkDKlrZ4vClxKt3zd8UuJnQTZz8EN8LDvLG9O3OFyiIqF7a7LSy2B75-puceQxWCEKEoLRQ0We85EVlNpbKgfSYYL4H6_RbA0jIuIKfSuh-VjZJ1nURYOyw5qHFvKzP32f_LliBpetBUsio5j080ia0bw9ULhQYyaXcKsEXQcXyg8ky0vyrpLTQsvl6ya_qHY7GmUKkE6gK2K6YnSTd"
                    ).classes("rounded-lg h-48 w-full object-cover mt-4")

                # Contact Form
                with ui.card().classes("p-8 rounded-xl shadow-sm"):
                    ui.label("Have a Question?").classes("text-xl font-bold mb-6")
                    name = (
                        ui.input("Name")
                        .props(f"outlined color={PRIMARY}")
                        .classes("h-12 mb-4")
                    )
                    email = (
                        ui.input("Email")
                        .props(f"outlined color={PRIMARY}")
                        .classes("h-12 mb-4")
                    )
                    message = (
                        ui.textarea("Message")
                        .props(f"outlined color={PRIMARY} auto-grow")
                        .classes("min-h-[100px] mb-4")
                    )

                    def send_message():
                        ui.notify(f"Message sent from {name.value or 'Unknown'}!")

                    ui.button(
                        "Send Message", color=PRIMARY, on_click=send_message
                    ).classes("w-full text-white font-semibold py-3 rounded-lg")
