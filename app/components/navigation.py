from dataclasses import dataclass
from typing import Callable

import flet as ft


@dataclass
class NavigationItem:
    router: str
    label: str
    icon: ft.Icons
    page_builder: Callable


class AppNavigation:
    def __init__(self):
        self.routes = [
            NavigationItem(
                "calendar",
                "Calendario",
                ft.Icons.CALENDAR_MONTH,
                calendar_page,
            ),
            NavigationItem(
                "tasks",
                "Tareas",
                ft.Icons.TASK,
                tasks_page,
            ),
            NavigationItem(
                "settings",
                "Configuración",
                ft.Icons.SETTINGS,
                settings_page,
            ),
        ]

    def create_navigation_bar(self, current_index: int, on_change: Callable):
        return ft.NavigationBar(
            selected_index=current_index,
            on_change=lambda e: on_change(e.control.selected_index),
            adaptive=True,
            destinations=[
                ft.NavigationBarDestination(
                    icon=route.icon,
                    label=route.label,
                )
                for route in self.routes
            ],
        )

    def get_route_info(self, route: str):
        return self.routes[self.routes.index(route)]
