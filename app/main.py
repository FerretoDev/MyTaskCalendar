import flet as ft
from components import create_navigation_bar
from pages import calendar_page, settings_page, tasks_page
from utils import app_theme

# from utils.constants import Constants


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Calendario y Tareas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = app_theme
    # print("Ruta inicial: ", page.route)

    def on_navigation_change(index):
        page.views.clear()

        # Determinar si se muestra el botón de configuración
        appbar_actions = []
        if index != 2:  # Si no es la pestaña de configuración
            appbar_actions.append(
                ft.IconButton(
                    ft.icons.SETTINGS,
                    on_click=lambda e: on_navigation_change(
                        2
                    ),  # Cambiar a página de Configuración
                )
            )

        # Navegación y carga de la vista correspondiente
        page.views.append(
            ft.View(
                routes[index],
                controls=[
                    create_navigation_bar(
                        index, on_navigation_change
                    ),  # Barra de navegación
                    pages[index],  # El contenido de la página actual
                ],
                appbar=ft.AppBar(
                    center_title=True,
                    adaptive=True,
                    title=ft.Text(titles[index]),
                    actions=appbar_actions,
                ),
                floating_action_button=ft.FloatingActionButton(
                    content=ft.Icon(ft.icons.ADD), bgcolor=ft.colors.ORANGE
                ),
            )
        )
        page.update()

    # Rutas y títulos de las páginas
    routes: list[str] = ["calendar", "tasks", "settings"]
    titles: list[str] = ["Calendario", "Tareas", "Configuración"]

    # Lista de páginas
    pages = [calendar_page(), tasks_page(), settings_page()]

    # Mostrar la primera página (Calendario)
    on_navigation_change(0)

    # Start the app
    page.update()


ft.app(target=main)
