from nicegui import ui
from components.navbar import show_navbar as navbar
from components.footer import footer


PRIMARY = "#0A2463"
ACCENT = "#FF6700"


@ui.page("/services/freight-cargo")
def freight_cargo_page():
    """UI for the Freight & Cargo service page."""
    navbar()
    ui.query("body").classes("bg-[#f6f6f8] dark:bg-[#101622] font-[Manrope]")

    # --- Hero Section ---
    with ui.column().classes(
        "w-full p-8 lg:p-16 flex flex-col justify-center items-center text-center min-h-[400px] bg-cover bg-center text-white"
    ).style(
        f'background-image: linear-gradient(rgba(10,36,99,0.7), rgba(10,36,99,0.8)), url("https://lh3.googleusercontent.com/aida-public/AB6AXuDwnQHkB80bjYfrnRSZUmJkHVsgeBaMZLyVzdQvujS-cUNz5BxcCZxMeoQe0Mv7Ss_uWHcKe4RzT2xGa256ErwaldpHHuRKdBmoDOSDzTaB6kMh1RMSnqyer1H8tMyDkqgqts7DsA0cV6QPSlIbD97fJb6KJuvZO_eqYvRXbfdUoIi0b7Q1Q4jnylRdzARQO3cYUAnwtpOUryHD7VomPQoa05hTNckWb-tmawNogWouTB1TnJEPmayPvDpACFpPmOS5o-1uIiodkZ_g");'
    ):
        ui.label("Freight & Cargo").classes("text-5xl font-black")
        ui.label(
            "Specialized shipping for heavy, bulk, or large items via air, sea, and land."
        ).classes("text-lg text-white/90 max-w-2xl mt-4")

    # --- Main Content ---
    with ui.column().classes("w-full max-w-4xl mx-auto py-16 px-4"):
        ui.label("Service Overview").classes(
            "text-3xl font-bold text-primary dark:text-white"
        )
        ui.label(
            "Our Freight & Cargo services provide robust and reliable transport for your most demanding shipments. We handle everything from Less-Than-Truckload (LTL) to Full-Truckload (FTL), as well as oversized and heavy-haul items. With options for air, ocean, and ground freight, we can build a custom logistics plan to move your goods efficiently and safely, whether domestically or internationally."
        ).classes("text-gray-600 dark:text-gray-400 mt-4 text-base")

        # --- Key Features ---
        ui.label("Key Features").classes(
            "text-3xl font-bold text-primary dark:text-white mt-12"
        )
        features = [
            (
                "local_shipping",
                "LTL & FTL Trucking",
                "Flexible ground freight options for shipments of all sizes across the country.",
            ),
            (
                "sailing",
                "Ocean Freight",
                "Containerized (FCL) and less-than-container (LCL) options for global sea transport.",
            ),
            (
                "flight",
                "Air Cargo",
                "Priority air services for when speed is critical for your heavy or bulk shipments.",
            ),
            (
                "construction",
                "Specialized Handling",
                "Expertise in handling oversized, heavy, and high-value cargo with special equipment.",
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
            ui.label("Complex Shipment? No Problem.").classes(
                "text-3xl font-bold text-primary dark:text-white"
            )
            ui.label(
                "Contact our freight specialists for a custom logistics solution."
            ).classes("text-gray-600 dark:text-gray-400 mt-2 mb-6")
            ui.button(
                "Contact Freight Sales", on_click=lambda: ui.navigate.to("/contact")
            ).props(f"color='{ACCENT}'").classes("px-8 py-3 text-base font-bold")

    footer()
