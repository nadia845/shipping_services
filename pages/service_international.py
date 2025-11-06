from nicegui import ui
from components.navbar import show_navbar as navbar
from components.footer import footer


PRIMARY = "#0A2463"
ACCENT = "#FF6700"


@ui.page("/services/international-shipping")
def international_shipping_page():
    """UI for the International Shipping service page."""
    navbar()
    ui.query("body").classes("bg-[#f6f6f8] dark:bg-[#101622] font-[Manrope]")

    # --- Hero Section ---
    with ui.column().classes(
        "w-full p-8 lg:p-16 flex flex-col justify-center items-center text-center min-h-[400px] bg-cover bg-center text-white"
    ).style(
        f'background-image: linear-gradient(rgba(10,36,99,0.7), rgba(10,36,99,0.8)), url("https://lh3.googleusercontent.com/aida-public/AB6AXuBQ1A7zPB1xnPrnUr9LtV19kMqzoK0-VMRiSB2agLNbGuNIFOn3GEODdp-7UiTDASipFjx3HOPRBOM7BdjEUe6ka-8tJOBLsL9mXc7ZR4ODz6VECpEoYfbJaBX-c6ME7idAdHwTkoQDs8yrlA2hNVRHJ07SXXFAvEriazITPqPIaygsjUgUXY1v2RjWvPl7yGekgc0qpXP5G6JhwsbhYivEG8ofMVohtA90th2Ermhmn2Pcd3ZWEQ_cIqRsKQxhPx5bjK-U13h3wlNG");'
    ):
        ui.label("International Shipping").classes("text-5xl font-black")
        ui.label(
            "Seamless global logistics with customs clearance support worldwide."
        ).classes("text-lg text-white/90 max-w-2xl mt-4")

    # --- Main Content ---
    with ui.column().classes("w-full max-w-4xl mx-auto py-16 px-4"):
        ui.label("Service Overview").classes(
            "text-3xl font-bold text-primary dark:text-white"
        )
        ui.label(
            "Expand your reach with our comprehensive international shipping solutions. We simplify the complexities of cross-border logistics, offering a range of services from express courier to air and ocean freight. Our expert team provides customs brokerage assistance to ensure your shipments clear customs smoothly and efficiently."
        ).classes("text-gray-600 dark:text-gray-400 mt-4 text-base")

        # --- Key Features ---
        ui.label("Key Features").classes(
            "text-3xl font-bold text-primary dark:text-white mt-12"
        )
        features = [
            (
                "flight_takeoff",
                "Air Freight",
                "Fast and reliable air cargo for time-sensitive international shipments.",
            ),
            (
                "waves",
                "Ocean Freight",
                "Cost-effective solutions for large, heavy, or non-urgent shipments via sea.",
            ),
            (
                "gavel",
                "Customs Clearance",
                "Expert assistance with customs documentation, duties, and taxes to avoid delays.",
            ),
            (
                "public",
                "Global Network",
                "Leverage our extensive network of partners to ship to over 220 countries and territories.",
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
            ui.label("Go Global Today").classes(
                "text-3xl font-bold text-primary dark:text-white"
            )
            ui.label(
                "Get a personalized quote for your international shipping needs."
            ).classes("text-gray-600 dark:text-gray-400 mt-2 mb-6")
            ui.button(
                "Request an International Quote",
                on_click=lambda: ui.navigate.to("/contact"),
            ).props(f"color='{ACCENT}'").classes("px-8 py-3 text-base font-bold")

    footer()
