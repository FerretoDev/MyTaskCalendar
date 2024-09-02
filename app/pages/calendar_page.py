import datetime
import locale

import flet as ft
from components.calendar import Calendar
from components.create_task_item import create_task_item


def tabs():
    return ft.Tabs(
        selected_index=0,
        tabs=[
            ft.Tab(text="Mes"),
            ft.Tab(text="Semana"),
        ],
        expand=True,
    )


locale.setlocale(locale.LC_TIME, "es_CR.UTF-8")


def date_title():
    return ft.Text(
        str(datetime.date.today().strftime("Hoy, %d de %B")),
        size=16,
        weight=ft.FontWeight.BOLD,
    )


def tasks():
    return ft.Column(
        controls=[
            create_task_item("Gym", "8:00 AM", True),
        ]
    )


def calendar_page():
    return ft.Column(
        controls=[
            Calendar(),
            ft.Divider(),
            tabs(),
            date_title(),
            tasks(),
        ]
    )
