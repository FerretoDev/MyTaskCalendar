import flet as ft
from components.calendar import CalendarPage


def calendar_page():
    return ft.Container(
        CalendarPage(),
        ft.Text("HO"),
    )
