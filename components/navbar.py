from nicegui import ui


def show_navbar():
  with ui.header().classes('bg-white text-black dark:bg-[#101622] dark:text-white shadow-md px-8 py-4 flex justify-between items-center'):
        with ui.row().classes('items-center gap-2'):
            ui.icon('local_shipping').classes('text-3xl text-primary')
            ui.label('SwiftShip').classes('text-xl font-bold')
        with ui.row().classes('hidden md:flex gap-6'):
            ui.link('Services', '#').classes('font-bold text-primary border-b-2 border-primary pb-1')
            ui.link('About Us', '#').classes('font-bold text-gray-500 hover:text-primary')
            ui.link('Contact', '#').classes('font-bold text-gray-500 hover:text-primary')
        with ui.row().classes('items-center gap-4'):
            ui.link('Login', '#').classes('text-gray-500 hover:text-primary')
            ui.link('Sign Up', '#').classes('px-4 py-2 rounded-lg bg-primary/10 text-primary font-bold hover:bg-primary/20')
