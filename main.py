from nicegui import ui, app

# Importing the page modules is enough for NiceGUI to discover the pages
from pages import home
from pages import signup
from pages import login
from pages import contact
from pages import services
from pages import service_domestic
from pages import service_international
from pages import service_freight
from pages import tracking

app.add_static_files("/assets", "assets")
# Start the NiceGUI application

ui.run()
