from nicegui import ui
from components.navbar import show_navbar as navbar
from components.footer import footer

PRIMARY = "#0A2463"
ACCENT = "#FF6700"


@ui.page("/tracking/{tracking_id}")
def tracking_page(tracking_id: str):
    """UI for the shipment tracking page."""
    navbar()
    ui.query("body").classes("bg-[#f6f6f8] dark:bg-[#101622] font-[Manrope]")

    # --- Main Content ---
    with ui.column().classes("w-full max-w-4xl mx-auto py-16 px-4"):
        # --- Header ---
        with ui.row().classes("w-full justify-between items-center"):
            with ui.column():
                ui.label("Tracking Details").classes(
                    "text-3xl font-bold text-primary dark:text-white"
                )
                ui.label(f"Shipment ID: {tracking_id}").classes(
                    "text-gray-500 dark:text-gray-400 text-lg"
                )

            with ui.row().classes("items-center gap-2"):
                ui.icon("local_shipping", color=ACCENT).classes("text-3xl")
                ui.label("In Transit").classes("text-2xl font-bold")

        # --- Tracking Status Timeline (Placeholder) ---
        ui.label("Shipment History").classes(
            "text-2xl font-bold text-primary dark:text-white mt-12 mb-4"
        )

        # This is a placeholder for a real tracking timeline.
        # In a real application, this data would be fetched from a database or API.
        tracking_history = [
            {
                "status": "Delivered",
                "location": "San Francisco, CA",
                "date": "November 5, 2025",
                "time": "10:30 AM",
                "current": True,
            },
            {
                "status": "Out for Delivery",
                "location": "San Francisco, CA",
                "date": "November 5, 2025",
                "time": "8:00 AM",
            },
            {
                "status": "Arrived at Hub",
                "location": "San Francisco, CA",
                "date": "November 4, 2025",
                "time": "11:45 PM",
            },
            {
                "status": "In Transit to Destination",
                "location": "Los Angeles, CA",
                "date": "November 3, 2025",
                "time": "5:00 PM",
            },
            {
                "status": "Shipment Created",
                "location": "New York, NY",
                "date": "November 1, 2025",
                "time": "2:15 PM",
            },
        ]

        with ui.stepper().props("vertical flat").classes("w-full"):
            for item in tracking_history:
                with ui.step(item["status"]):
                    ui.label(f"{item['location']}").classes("text-base")
                    ui.label(f"{item['date']} at {item['time']}").classes(
                        "text-sm text-gray-500"
                    )

    footer()
