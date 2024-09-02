import flet as ft
from components.calendar import Calendar
from components.date_component import render_today_date
from components.render_calendar_tabs import render_calendar_tabs
from components.render_calendar_tasks import render_calendar_tasks


def calendar_page():
    return ft.Column(
        controls=[
            Calendar(),
            ft.Divider(),
            render_calendar_tabs(),
            render_today_date(),
            render_calendar_tasks(),
        ],
    )
