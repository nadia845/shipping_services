
from nicegui import ui


def footer() -> None:
    with ui.column().classes('w-full bg-brand-900 mt-20'):
        with ui.row().classes('max-w-7xl w-full mx-auto justify-between px-10 py-10'):
            with ui.column().classes('gap-2'):
                ui.label('ShipX').classes('text-white text-lg font-semibold')
                ui.label('Shipping Simplified. Delivered Worldwide.').classes('text-gray-300 text-sm')
            with ui.column().classes('gap-2 text-gray-300'):
                ui.link('Home', '/').classes('hover:text-cta text-sm')
                ui.link('Services & Solutions', '/services').classes('hover:text-cta text-sm')
                ui.link('Quote & Contact', '/quote-contact').classes('hover:text-cta text-sm')
        ui.separator().classes('opacity-20')
        with ui.row().classes('max-w-7xl w-full mx-auto justify-between px-10 py-6 text-gray-400 text-xs'):
            ui.label('© 2025 ShipX Logistics LLC')
            ui.label('All trademarks are property of their respective owners')
