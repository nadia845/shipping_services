from nicegui import ui
from components.navbar import show_navbar as navbar
from components.footer import footer


PRIMARY = "#0A2463"
ACCENT = "#FF6700"


@ui.page("/services/domestic-shipping")
def domestic_shipping_page():
    """UI for the Domestic Shipping service page."""
    navbar()
    ui.query("body").classes("bg-[#f6f6f8] dark:bg-[#101622] font-[Manrope]")

    # --- Hero Section ---
    with ui.column().classes(
        "w-full p-8 lg:p-16 flex flex-col justify-center items-center text-center min-h-[400px] bg-cover bg-center text-white"
    ).style(
        f'background-image: linear-gradient(rgba(10,36,99,0.7), rgba(10,36,99,0.8)), url("https://lh3.googleusercontent.com/aida-public/AB6AXuDwaQv2FiP7W2BjrAaMw60_VOlbRGOxTzwDjwqpPBiQy6IUQDuujzLS2WJ7jInkX7x23AXUjiucRUDUPlAxf6HtaGgZUGHQgIAotyIEFw5aw_VVBhsQg6g-XrJJKyMOYJhjRnYV2WlrR0LBh5MRXsKj--Eb6XwSe94Rlwmywbp_10g7lmSOIHHaKvtRgTOggUz4edR5zWIKcHlVgRKnsjWmcfOUoRj11RhN-7L1BpfP0zLmTIipNqP0xkEp3FpAnonFYzxdI79nQHh1T");'
    ):
        ui.label("Domestic Shipping").classes("text-5xl font-black")
        ui.label(
            "Reliable and timely delivery across the country for businesses and individuals."
        ).classes("text-lg text-white/90 max-w-2xl mt-4")

    # --- Main Content ---
    with ui.column().classes("w-full max-w-4xl mx-auto py-16 px-4"):
        ui.label("Service Overview").classes(
            "text-3xl font-bold text-primary dark:text-white"
        )
        ui.label(
            "Our domestic shipping services are designed for speed, reliability, and cost-effectiveness. Whether you're sending a small parcel or a large shipment, we provide a range of options to meet your needs within the country. We handle every package with care, ensuring it reaches its destination safely and on time."
        ).classes("text-gray-600 dark:text-gray-400 mt-4 text-base")

        # --- Key Features ---
        ui.label("Key Features").classes(
            "text-3xl font-bold text-primary dark:text-white mt-12"
        )
        features = [
            (
                "rocket_launch",
                "Express Delivery",
                "Next-day and same-day delivery options for urgent shipments.",
            ),
            (
                "inventory_2",
                "Standard Parcel",
                "Cost-effective shipping for less urgent packages, typically within 3-5 business days.",
            ),
            (
                "local_shipping",
                "LTL & FTL Freight",
                "Solutions for larger shipments that don't require a full truck.",
            ),
            (
                "track_changes",
                "Real-Time Tracking",
                "Monitor your shipment's journey from pickup to delivery with our live tracking portal.",
            ),
        ]
        with ui.row().classes("grid grid-cols-1 md:grid-cols-2 gap-8 mt-6"):
            for icon, title, desc in features:
                with ui.card().classes("p-6 shadow-md"):
                    ui.icon(icon).classes(f"text-4xl text-accent mb-4")
                    ui.label(title).classes("text-lg font-bold")
                    ui.label(desc).classes("text-sm text-gray-600 dark:text-gray-400")

        # --- CTA ---
        with ui.column().classes(
            "w-full items-center text-center bg-white dark:bg-black/20 p-12 rounded-lg mt-16"
        ):
            ui.label("Ready to Ship?").classes(
                "text-3xl font-bold text-primary dark:text-white"
            )
            ui.label("Get an instant quote and start shipping with us today.").classes(
                "text-gray-600 dark:text-gray-400 mt-2 mb-6"
            )
            ui.button(
                "Get a Quick Quote", on_click=lambda: ui.navigate.to("/contact")
            ).props(f"color='{ACCENT}'").classes("px-8 py-3 text-base font-bold")

    footer()
