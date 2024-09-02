import datetime
import locale

import flet as ft

locale.setlocale(locale.LC_TIME, "es_CR.UTF-8")


def render_today_date():
    return ft.Text(
        str(datetime.date.today().strftime("Hoy, %d de %B")),
        size=16,
        weight=ft.FontWeight.NORMAL,
        text_align=ft.TextAlign.CENTER,
    )
