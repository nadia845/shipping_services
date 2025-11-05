from nicegui import ui


PRIMARY = "#1152d4"
BG_LIGHT = "#f6f6f8"
BG_DARK = "#101622"


@ui.page("/services")
def services_page():
    ui.colors(primary=PRIMARY)
    ui.query("body").style(
        f"background-color: {BG_LIGHT}; color: #0d121b; font-family: Manrope, sans-serif;"
    )

    # HEADER
    with ui.header().classes(
        "justify-between items-center px-6 py-3 bg-white shadow-sm"
    ):
        with ui.row().classes("items-center gap-2"):
            ui.icon("local_shipping").classes("text-3xl text-[{}]".format(PRIMARY))
            ui.label("LogisticsCo").classes("text-xl font-bold")
        with ui.row().classes("hidden md:flex gap-4 text-sm font-medium"):
            ui.link("Home", "#").classes("hover:text-[{}]".format(PRIMARY))
            ui.link("About Us", "#").classes("hover:text-[{}]".format(PRIMARY))
            ui.link("Services", "#").classes("text-[{}] font-bold".format(PRIMARY))
            ui.link("Tracking", "#").classes("hover:text-[{}]".format(PRIMARY))
        ui.button("Get a Quote", icon="arrow_forward", color=PRIMARY).classes(
            "text-white font-bold"
        )

    # HERO SECTION
    with ui.card().classes(
        "w-full p-0 mt-4 bg-cover bg-center text-white rounded-xl"
    ).style(
        'background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url("https://lh3.googleusercontent.com/aida-public/AB6AXuBUIhVQ5cmzHLad-egxWTx8DfJ54vkIWL8h3avImPHVrSY0MbFzjbl8IrhIgdQOqyl6_AOWiLdaIOHpMvBgSeCo5B5RQ0M2kpQD7JULA5zfnORk32bkPWsjEVXLDgcxA69slrZNshI03QUlmov-eqHTZwuGtWqxxgrIs7Dru7PFZ83iJLRn3XUUnbsQfBPmnoQi--4UT-_wmuOxardE7AGsiMJQ06-SgJa0nwKhijChX5KaQxdZX-iNUX22Pz8lclJFtUX4DrKj9gFL");'
    ):
        ui.space()
        ui.label("Comprehensive Logistics Solutions for Your Business").classes(
            "text-4xl font-extrabold leading-tight max-w-2xl"
        )
        ui.label(
            "From next-day domestic deliveries to complex international freight, discover a service tailored to your needs."
        ).classes("text-white/90 text-base max-w-2xl pb-8")

    # SERVICES SECTION
    ui.label("Our Shipping & Logistics Services").classes(
        "text-3xl font-bold text-center mt-12"
    )
    ui.label(
        "Explore our core services designed to meet your every shipping demand, from local deliveries to global supply chain management."
    ).classes("text-center text-gray-500 max-w-2xl mx-auto mb-8")

    with ui.row().classes("justify-center gap-6 px-4 py-6"):
        services = [
            {
                "icon": "rocket_launch",
                "title": "Domestic Express",
                "desc": "Fast and reliable next-day and two-day delivery options for time-sensitive shipments.",
                "features": [
                    "Weight Limit: Up to 70kg",
                    "Transit Time: Next-Day & Two-Day",
                    "Best For: Urgent parcels & documents",
                ],
            },
            {
                "icon": "public",
                "title": "International Freight",
                "desc": "Global reach for larger, complex cross-border shipments via Air & Sea, including customs support.",
                "features": [
                    "Weight Limit: No effective limit",
                    "Transit Time: Varies by destination",
                    "Best For: Large, cross-border shipments",
                ],
            },
            {
                "icon": "storefront",
                "title": "E-commerce Fulfillment",
                "desc": "Dedicated B2B & B2C services including warehousing, picking, packing, and store integrations.",
                "features": [
                    "Services: Warehousing, Pick & Pack",
                    "Integrations: Shopify, Magento & more",
                    "Best For: B2B & B2C online stores",
                ],
            },
        ]

        for s in services:
            with ui.card().classes(
                "w-80 h-auto flex flex-col justify-between p-6 shadow-sm hover:shadow-md transition-all"
            ):
                with ui.row().classes("items-center gap-3"):
                    ui.icon(s["icon"]).classes("text-[{}] text-3xl".format(PRIMARY))
                    ui.label(s["title"]).classes("text-lg font-bold")
                ui.label(s["desc"]).classes("text-sm text-gray-600 mt-2")
                for f in s["features"]:
                    with ui.row().classes(
                        "items-center gap-2 mt-2 text-sm text-gray-700"
                    ):
                        ui.icon("check_circle").classes("text-green-500 text-sm")
                        ui.label(f)
                ui.button("Learn More").classes(
                    "mt-4 bg-gray-200 text-black font-bold hover:bg-gray-300"
                )

    # CTA SECTION
    with ui.card().classes("text-center py-16 bg-white dark:bg-gray-900 mt-12"):
        ui.label("Have Complex Shipping Needs?").classes("text-3xl font-bold mb-2")
        ui.label(
            "Get in touch for a personalized logistics strategy tailored to your unique requirements."
        ).classes("text-gray-600 mb-6")
        ui.button("Contact Sales for a Custom Solution", color=PRIMARY).classes(
            "text-white font-bold px-6 py-3"
        )

    # FOOTER
    with ui.footer().classes(
        "bg-white dark:bg-gray-900 border-t border-gray-200 mt-12 px-8 py-6"
    ):
        with ui.row().classes("justify-between items-center w-full"):
            with ui.row().classes("items-center gap-2"):
                ui.icon("local_shipping").classes("text-[{}] text-2xl".format(PRIMARY))
                ui.label("LogisticsCo").classes("text-lg font-bold")
            ui.label("© 2023 LogisticsCo™. All Rights Reserved.").classes(
                "text-gray-500 text-sm"
            )
