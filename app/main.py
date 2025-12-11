from typing import List

import flet as ft
from components.navigation import create_navigation_bar

# from components.settings.settings_page import SettingsPage
from components.theme_manager import ThemeManager, ThemeMode
from pages import SettingsPage, calendar_page, create_settings_page, tasks_page


def main(page: ft.Page) -> None:
    # Inicializar el administrador de temas
    theme_manager = ThemeManager(page)

    def on_navigation_change(
        index: int, routes: List[str], titles: List[str], pages: List[ft.Control]
    ) -> None:
        page.views.clear()

        appbar_actions: List[ft.Control] = []
        # appbar_actions: List[ft.Control] = [theme_manager.create_theme_toggle()]
        if index != 2:  # Si no es la pestaña de configuración
            appbar_actions.append(
                ft.IconButton(
                    ft.Icons.SETTINGS,
                    on_click=lambda _: on_navigation_change(2, routes, titles, pages),
                )
            )

        page.views.append(
            ft.View(
                route=routes[index],
                controls=[
                    create_navigation_bar(
                        index, lambda e: on_navigation_change(e, routes, titles, pages)
                    ),
                    pages[index],
                ],
                appbar=ft.AppBar(
                    center_title=True,
                    # adaptive=True,
                    title=ft.Text(titles[index]),
                    actions=appbar_actions,
                ),
                floating_action_button=(
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=lambda _: on_navigation_change(
                            1, routes, titles, pages
                        ),
                        tooltip="Add a task",
                    )
                    if index != 2
                    else None
                ),
            )
        )
        page.update()

    # Configuración inicial de la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Calendario y Tareas"

    # Inicializar el tema
    page.theme_mode = theme_manager.set_theme(ThemeMode.LIGHT)

    # Rutas y títulos de las páginas
    routes: List[str] = ["calendar", "tasks", "settings"]
    titles: List[str] = ["Calendario", "Tareas", "Configuración"]
    pages: List[ft.Control] = [
        calendar_page(),
        tasks_page(),
        create_settings_page(theme_manager=theme_manager),
    ]

    # Iniciar con la página de calendario
    on_navigation_change(0, routes, titles, pages)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
