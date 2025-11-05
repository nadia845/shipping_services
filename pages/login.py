from nicegui import ui

@ui.page("/login")
def login_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')

    with ui.element("div").classes(
        "relative flex min-h-screen w-full flex-col bg-[#f6f6f8] dark:bg-[#101622] overflow-x-hidden font-[Manrope,sans-serif]"
    ):
        with ui.element("div").classes("flex flex-1 w-full"):
            
            # -------- Left Side (Form Section) --------
            with ui.element("div").classes(
                "flex flex-1 flex-col justify-center items-center p-4 sm:p-6 lg:p-8"
            ):
                with ui.element("div").classes("w-full max-w-md"):

                    # Header
                    with ui.row().classes("flex items-center justify-center sm:justify-start p-4 pb-6"):
                        with ui.row().classes("flex items-center gap-3"):
                            ui.icon("local_shipping").classes("text-[#0A2463] text-4xl")
                            ui.label("ShipSwift").classes(
                                "text-[#0A2463] dark:text-white text-2xl font-bold leading-tight tracking-tight"
                            )

                    # Headline
                    ui.label("Access Your Dashboard").classes(
                        "text-[#0d121b] dark:text-white tracking-tight text-[32px] font-bold leading-tight px-4 text-center sm:text-left pb-1 pt-6"
                    )

                    # Subtext
                    ui.label("Log in to track shipments and manage your account.").classes(
                        "text-[#4c669a] dark:text-gray-300 text-base font-normal leading-normal pb-6 pt-1 px-4 text-center sm:text-left"
                    )

                    # Toggle Buttons
                    with ui.row().classes("flex px-4 py-3"):
                        with ui.element("div").classes(
                            "flex h-12 flex-1 items-center justify-center rounded-lg bg-[#e7ebf3] dark:bg-gray-800 p-1"
                        ):
                            ui.button("Login").props("flat").classes(
                                "flex-1 h-full text-[#0A2463] text-sm font-medium bg-[#f6f6f8] dark:bg-[#101622] shadow-sm"
                            )
                            ui.button("Register").props("flat").classes(
                                "flex-1 h-full text-[#4c669a] text-sm font-medium"
                            )

                    # Login Fields
                    with ui.element("div").classes("space-y-4 px-4 py-3 w-full"):
                        ui.input(label="Email or Username", placeholder="Enter your email or username") \
                            .props("outlined dense") \
                            .classes("w-full rounded-lg h-12 border border-[#cfd7e7] dark:border-[#2a3b5a] bg-[#f6f6f8] dark:bg-gray-800 focus:border-[#0A2463]")

                        ui.input(label="Password", placeholder="Enter your password", password=True, password_toggle_button=True) \
                            .props("outlined dense") \
                            .classes("w-full rounded-lg h-12 border border-[#cfd7e7] dark:border-[#2a3b5a] bg-[#f6f6f8] dark:bg-gray-800 focus:border-[#0A2463]")

                        ui.link("Forgot Password?", "#").classes(
                            "text-sm font-medium text-[#0A2463] hover:underline text-right block"
                        )

                    # Login Button
                    ui.button("Login").props("no-caps").classes(
                        "h-12 w-full rounded-lg bg-[#0A2463] text-white font-semibold text-base shadow-sm hover:bg-[#0A2463]/90 transition-colors mt-4"
                    )

                    # Divider
                    with ui.element("div").classes("relative px-4 py-4 w-full"):
                        ui.element("div").classes(
                            "absolute inset-0 flex items-center"
                        ).style("border-top: 1px solid #cfd7e7")
                        with ui.element("div").classes("relative flex justify-center"):
                            ui.label("Or continue with").classes(
                                "bg-[#f6f6f8] dark:bg-[#101622] px-2 text-sm text-[#4c669a]"
                            )

                    # Social Buttons
                    with ui.row().classes("grid grid-cols-1 sm:grid-cols-2 gap-4 px-4 py-3 w-full"):
                        ui.button("Sign in with Google", icon="fa-brands fa-google").props("flat").classes(
                            "h-12 w-full justify-center gap-2 border border-[#cfd7e7] dark:border-[#2a3b5a] bg-[#f6f6f8] dark:bg-gray-800 text-[#0d121b] dark:text-white shadow-sm"
                        )
                        ui.button("Sign in with LinkedIn", icon="fa-brands fa-linkedin").props("flat").classes(
                            "h-12 w-full justify-center gap-2 border border-[#cfd7e7] dark:border-[#2a3b5a] bg-[#f6f6f8] dark:bg-gray-800 text-[#0d121b] dark:text-white shadow-sm"
                        )

                    # Footer
                    ui.label(
                        "© 2024 ShipSwift Inc. All rights reserved.\nPrivacy Policy • Contact Support"
                    ).classes("text-xs text-[#4c669a] dark:text-gray-400 text-center px-4 pt-6 pb-2")

            # -------- Right Side (Hero Section) --------
            with ui.element("div").classes(
                "hidden lg:flex flex-1 items-center justify-center bg-[#0A2463]/5 dark:bg-[#0A2463]/10 relative overflow-hidden"
            ):
                ui.element("div").classes(
                    "absolute inset-0 bg-cover bg-center"
                ).style(
                    "background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuClLBWzrH4iTZThmKoCg_6H_XC3fSLyEvLdRhOBfE90VOnnXxDx7sPBanBtrJgXJbetKtTWNMrLrr85s7s2TsiK0llUDrNlVCkdNmzBAL93JOp8YA9ZLL5t9jU51XzGCCI4YFwmm_mR28xdMMaWOC0GNci3CpKfVz1FsZR7Mr-fVb2a7IRpUsm70Gd_SftrAU6UiG-KDr2JWhhaWLcXs4hP_T9DHUiF0HzKJ34Q-W75pfjeuvbZHmOYXcUcGvBtYYY3rN8fmjnzXCos'); background-color: rgba(10,36,99,0.8); mix-blend-mode: multiply;"
                )

                with ui.element("div").classes("relative z-10 max-w-lg p-12 text-white"):
                    ui.label("Streamline Your Logistics with ShipSwift").classes("text-4xl font-bold leading-tight mb-4")
                    ui.label(
                        "Join thousands of businesses who trust us to deliver their promises. Track, manage, and optimize your shipments with our powerful dashboard."
                    ).classes("text-lg opacity-90")
