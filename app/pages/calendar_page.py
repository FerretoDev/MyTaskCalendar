import flet as ft
from components.calendar import Calendar


def calendar_page():
    return ft.Column(
        controls=[
            # calendar(year, w=2, l=1, c=6, m=3)
            # calendar,
            Calendar(),
            ft.Text("HO"),
            ft.Divider(),
        ]
    )
