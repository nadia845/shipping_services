from nicegui import ui
from components.navbar import show_navbar as navbar


PRIMARY = "#0A2463"
ACCENT = "#FF6700"
TEXT_MUTED = "#4c669a"


@ui.page("/")
def home():
    navbar()
    # === Body styling ===
    ui.query("body").classes(
        "bg-[#f6f6f8] dark:bg-[#101622] font-[Manrope] min-h-screen overflow-x-hidden"
    )

    # HERO SECTION
    with ui.column().classes(
        "w-full p-8 flex flex-col justify-center items-center text-center min-h-[560px] bg-cover bg-center text-white"
    ).style(
        f'background-image: linear-gradient(rgba(10,36,99,0.6), rgba(10,36,99,0.8)), url("https://lh3.googleusercontent.com/aida-public/AB6AXuDZijy7LGZrAeFXfMez3-pBh1GMV23XXeynNbmPO1_IpJRk_2d9qZN8QdmvsiNwPcO3TmRImtmbWOrHvGrOBAElDzZEFYrFKRjuy-a2zCn8SDErsJdiKBXFusTPgR3MmZuph98zKIk5wTTkBiEUHkCvWtHtdvklw4xQo7oevtjLgEcLenT-kjoxf1t23q0E8aB89uwFBmJ7Ozikdw_MmS8wyrOR0V_4xaPey6PoxEYX1uUx3r6RdcmZj88O6sbGzBpLFyPSLZl8muQ6");'
    ):
        ui.label("Shipping Simplified. Delivered Worldwide.").classes(
            "text-5xl font-black"
        )
        ui.label(
            "Fast, secure logistics solutions for your business and personal needs."
        ).classes("text-lg text-white/90 max-w-2xl")
        with ui.row().classes("mt-6 w-full max-w-xl"):
            tracking_input = ui.input(placeholder="Enter your tracking number").classes(
                "w-full rounded-l-xl h-12 px-4 text-black"
            )
            ui.button(
                "Track", on_click=lambda: ui.notify(f"Tracking: {tracking_input.value}")
            ).classes("bg-[{}] text-white h-12 rounded-r-xl".format(ACCENT))
        ui.label("OR").classes("text-white/70 mt-2")
        ui.button("Get a Quick Quote", color=ACCENT).classes(
            "mt-4 px-8 py-3 text-base font-bold"
        )

    # WHY CHOOSE US SECTION
    with ui.column().classes(
        "py-20 bg-[#F8F9FA] dark:bg-[#101622] flex flex-col justify-center items-center text-center"
    ):
        ui.label("Why Choose Us?").classes(
            "text-4xl font-bold text-primary dark:text-white"
        )
        ui.label(
            "Delivering excellence with every package, providing reliable and efficient shipping solutions worldwide."
        ).classes("max-w-2xl mx-auto text-gray-600 dark:text-gray-400 mb-10")

        features = [
            (
                "public",
                "Global Network",
                "Connect your business to the world with our logistics network spanning continents.",
            ),
            (
                "location_on",
                "Real-Time Tracking",
                "Stay updated with live tracking of your shipments 24/7.",
            ),
            (
                "support_agent",
                "24/7 Support",
                "Our dedicated support team is always available to assist.",
            ),
        ]
        with ui.row().classes("justify-center gap-8 flex-wrap"):
            for icon, title, desc in features:
                with ui.card().classes("w-100 text-center shadow-md p-6"):
                    ui.icon(icon).classes("text-4xl text-primary mb-4")
                    ui.label(title).classes("text-lg font-bold")
                    ui.label(desc).classes("text-sm text-gray-600 dark:text-gray-400")

    # SERVICES SECTION
    with ui.column().classes(
        "py-20 bg-white dark:bg-black/20  flex flex-col justify-center items-center text-center w-full"
    ):
        ui.label("Our Core Services").classes(
            "text-4xl font-bold text-primary dark:text-white"
        )
        ui.label(
            "Explore our comprehensive logistics services designed for speed and reliability."
        ).classes("max-w-2xl mx-auto text-gray-600 dark:text-gray-400 mb-10")

        services = [
            {
                "title": "Domestic Shipping",
                "desc": "Reliable and timely delivery across the country for businesses and individuals.",
                "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuDwaQv2FiP7W2BjrAaMw60_VOlbRGOxTzwDjwqpPBiQy6IUQDuujzLS2WJ7jInkX7x23AXUjiucRUDUPlAxf6HtaGgZUGHQgIAotyIEFw5aw_VVBhsQg6g-XrJJKyMOYJhjRnYV2WlrR0LBh5MRXsKj--Eb6XwSe94Rlwmywbp_10g7lmSOIHHaKvtRgTOggUz4edR5zWIKcHlVgRKnsjWmcfOUoRj1RhN-7L1BpfP0zLmTIipNqP0xkEp3FpAnonFYzxdI79nQHh1T",
                "link": "/services/domestic-shipping",
            },
            {
                "title": "International Shipping",
                "desc": "Seamless global logistics with customs clearance support worldwide.",
                "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuBQ1A7zPB1xnPrnUr9LtV19kMqzoK0-VMRiSB2agLNbGuNIFOn3GEODdp-7UiTDASipFjx3HOPRBOM7BdjEUe6ka-8tJOBLsL9mXc7ZR4ODz6VECpEoYfbJaBX-c6ME7idAdHwTkoQDs8yrlA2hNVRHJ07SXXFAvEriazITPqPIaygsjUgUXY1v2RjWvPl7yGekgc0qpXP5G6JhwsbhYivEG8ofMVohtA90th2Ermhmn2Pcd3ZWEQ_cIqRsKQxhPx5bjK-U13h3wlNG",
                "link": "/services/international-shipping",
            },
            {
                "title": "Freight & Cargo",
                "desc": "Specialized shipping for heavy, bulk, or large items via air, sea, and land.",
                "img": "https://lh3.googleusercontent.com/aida-public/AB6AXuDwnQHkB80bjYfrnRSZUmJkHVsgeBaMZLyVzdQvujS-cUNz5BxcCZxMeoQe0Mv7Ss_uWHcKe4RzT2xGa256ErwaldpHHuRKdBmoDOSDzTaB6kMh1RMSnqyer1H8tMyDkqgqts7DsA0cV6QPSlIbD97fJb6KJuvZO_eqYvRXbfdUoIi0b7Q1Q4jnylRdzARQO3cYUAnwtpOUryHD7VomPQoa05hTNckWb-tmawNogWouTB1TnJEPmayPvDpACFpPmOS5o-1uIiodkZ_g",
                "link": "/services/freight-cargo",
            },
        ]

        with ui.row().classes("justify-center flex-wrap gap-8"):
            for s in services:
                with ui.card().classes("w-80 overflow-hidden shadow-md"):
                    ui.image(s["img"]).classes("h-48 w-full object-cover")
                    ui.label(s["title"]).classes("text-xl font-bold mt-3")
                    ui.label(s["desc"]).classes(
                        "text-sm text-gray-600 dark:text-gray-400 mb-3"
                    )
                    ui.link("Learn More →", s["link"]).classes(
                        "text-sm font-bold text-[{}] hover:underline".format(ACCENT)
                    )

    # FOOTER
    with ui.footer().classes("bg-[{}] text-white py-8 px-4".format(PRIMARY)):
        with ui.row().classes("justify-around flex-wrap gap-8"):
            ui.label("© 2025 SwiftShip Logistics. All Rights Reserved.").classes(
                "text-sm text-white/70"
            )
            with ui.column():
                ui.label("Company").classes("font-bold")
                for link in ["About Us", "Careers", "Press"]:
                    ui.link(link, "#").classes("text-white/70 hover:text-white text-sm")
            with ui.column():
                ui.label("Legal").classes("font-bold")
                for link in ["Privacy Policy", "Terms of Service", "Cookie Policy"]:
                    ui.link(link, "#").classes("text-white/70 hover:text-white text-sm")
            with ui.column():
                ui.label("Follow Us").classes("font-bold")
                with ui.row().classes("gap-4"):
                    for social in ["Facebook", "Twitter", "LinkedIn"]:
                        ui.link(social, "#").classes(
                            "text-white/70 hover:text-white text-sm"
                        )
