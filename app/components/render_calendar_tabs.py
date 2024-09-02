import flet as ft


def render_calendar_tabs():
    return ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Mes"),
            ft.Tab(text="Semana"),
        ],
        expand=True,
    )
