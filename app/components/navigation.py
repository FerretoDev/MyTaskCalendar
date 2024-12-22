from typing import Callable

import flet as ft


def create_navigation_bar(
    current_index: int, on_change: Callable[[int], None]
) -> ft.NavigationBar:
    """
    Crea la barra de navegación de la aplicación.

    Args:
        current_index: Índice de la página actual
        on_change: Función callback para manejar cambios de navegación

    Returns:
        Barra de navegación configurada
    """
    return ft.NavigationBar(
        selected_index=current_index,
        on_change=lambda e: on_change(e.control.selected_index),
        adaptive=True,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.CALENDAR_MONTH, label="Calendario"
            ),
            ft.NavigationBarDestination(icon=ft.Icons.TASK, label="Tareas"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Configuración"),
        ],
    )
