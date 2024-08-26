import flet as ft

from components import create_navigation_bar
from pages import calendar_page, tasks_page, settings_page

# from pages.calendar_page import CalendarPage
from utils import app_theme


def main(page: ft.Page):
    page.title = "Calendario y Tareas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = app_theme
    print("Ruta inicial: ", page.route)

    def on_navigation_change(index):

        page.views.clear()

        page.views.append(
            ft.View(
                routes[index],
                controls=[
                    create_navigation_bar(
                        index, on_navigation_change
                    ),  # Agregar los tabs como control
                    pages[index],  # El contenido de la página actual
                ],
                appbar=ft.AppBar(
                    center_title=True,
                    adaptive=True,
                    title=ft.Text(titles[index]),
                    # bgcolor=ft.colors.RED,
                    actions=[ft.IconButton(ft.icons.SETTINGS, on_click=routes[index])],
                ),
                floating_action_button=ft.FloatingActionButton(
                    content=ft.Icon(ft.icons.ADD), bgcolor=ft.colors.ORANGE
                ),
            )
        )
        page.update()

    # Rutas y títulos de las páginas
    routes = ["calendar", "tasks", "settings"]

    titles = ["Calendario", "Tareas", "Configuración"]

    # Lista de páginas
    pages = [calendar_page(), tasks_page(), settings_page()]

    # Mostrar la primera página (Calendario)
    on_navigation_change(0)

    # Start the app
    page.update()


ft.app(target=main)
