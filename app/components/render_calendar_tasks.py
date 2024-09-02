import flet as ft

from .task_item import task_item


def render_calendar_tasks():
    return ft.Column(
        controls=[
            task_item("Gym", "8:00 AM", True),
        ],
    )
