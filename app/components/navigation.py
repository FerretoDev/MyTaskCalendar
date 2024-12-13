import flet as ft


def create_navigation_bar(current_index, on_change):
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
