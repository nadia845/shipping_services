from nicegui import ui


@ui.page("/signup")
def signup_page():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")

    with ui.element("div").classes(
        "relative flex min-h-screen w-full flex-col overflow-x-hidden md:flex-row font-[Manrope] bg-[#f6f6f8]"
    ):
        # --- LEFT PANEL: Branding ---
        with ui.element("div").classes(
            "hidden md:flex md:w-1/2 lg:w-5/12 bg-[#0A2463] p-8 lg:p-12 flex-col justify-between"
        ):
            with ui.row().classes("items-center gap-3"):
                ui.icon("local_shipping").classes("text-white text-3xl")
                ui.label("SwiftShip").classes("text-white text-xl font-bold")

            with ui.column().classes("text-white mt-12"):
                ui.label("Your Trusted Logistics Partner.").classes(
                    "text-4xl lg:text-5xl font-bold leading-tight mb-4"
                )
                ui.label(
                    "Streamline your shipments with real-time tracking, reliable service, and competitive rates."
                ).classes("text-lg text-white/80")

        # --- RIGHT PANEL: Signup Form ---
        with ui.element("div").classes(
            "flex-1 flex items-center justify-center bg-[#f6f6f8] p-4 sm:p-6 md:p-8"
        ):
            with ui.column().classes("w-full max-w-md mx-auto"):
                ui.label("Get Started in Seconds").classes(
                    "text-[#0d121b] text-3xl font-bold leading-tight"
                )
                ui.label(
                    "Create an account to track packages and manage your shipments."
                ).classes("text-[#4c669a] text-base pt-1")

                # --- Social buttons ---
                with ui.row().classes("gap-3 mt-6"):
                    ui.button(
                        "Sign up with Google",
                        icon="mdi-google",
                    ).classes(
                        "flex-1 h-12 text-[#0d121b] font-bold bg-white border border-gray-200 hover:bg-gray-50"
                    )
                    ui.button(
                        "Sign up with LinkedIn",
                        icon="mdi-linkedin",
                    ).classes(
                        "flex-1 h-12 text-[#0d121b] font-bold bg-white border border-gray-200 hover:bg-gray-50"
                    )

                ui.separator().classes("my-6 opacity-50")

                # --- Form Inputs ---
                full_name = (
                    ui.input("Full Name")
                    .props("outlined")
                    .classes("rounded-lg h-12 text-base bg-white my-2")
                )
                email = (
                    ui.input("Email Address")
                    .props("outlined")
                    .classes("rounded-lg h-12 text-base bg-white my-2")
                )
                password = (
                    ui.input(
                        "Create Password", password=True, password_toggle_button=True
                    )
                    .props("outlined")
                    .classes("rounded-lg h-12 text-base bg-white my-2")
                )
                confirm = (
                    ui.input(
                        "Confirm Password", password=True, password_toggle_button=True
                    )
                    .props("outlined")
                    .classes("rounded-lg h-12 text-base bg-white my-2")
                )
                company = (
                    ui.input("Company Name (Optional)")
                    .props("outlined")
                    .classes("rounded-lg h-12 text-base bg-white my-2")
                )

                ui.checkbox(
                    "By creating an account, you agree to our Terms of Service and Privacy Policy."
                ).classes("text-sm text-gray-600 mt-2")

                ui.button("Create Account", color="#1152d4").classes(
                    "w-full h-12 mt-4 text-white text-base font-bold"
                )

                with ui.row().classes("justify-center mt-6 text-sm text-[#4c669a]"):
                    ui.label("Already have an account?")
                    ui.link("Log In", "/login").classes(
                        "font-bold text-[#1152d4] hover:underline"
                    )
