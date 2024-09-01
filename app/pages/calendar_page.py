import flet as ft
from components.calendar import Calendar


def calendar_page():
    return ft.Column(
        controls=[
            Calendar(),
            ft.Divider(),
            ft.Row(
                controls=[
                    ft.Text("Semana"),
                    ft.Text("Mes"),
                ],
            ),
            ft.Divider(),
        ]
    )
