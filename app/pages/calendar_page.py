import calendar
from datetime import datetime
from typing import Any

import flet as ft


class CalendarDayButton(ft.Container):
    def __init__(self, text: str, day_clicked: Any, has_tasks: bool = False) -> None:
        super().__init__()
        self.bgcolor = ft.Colors.BLUE_100 if has_tasks else ft.Colors.WHITE
        self.border_radius = ft.border_radius.all(8)
        self.border = ft.border.all(1, ft.Colors.BLACK12)
        self.padding = 10
        self.data = text
        self.on_click = day_clicked
        self.content = ft.Column(
            controls=[
                ft.Text(text, size=16, weight=ft.FontWeight.BOLD),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )


class CalendarView(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.current_date = datetime.now()
        self.padding = 20
        self.content = self.build_calendar()

    def build_calendar(self) -> Any:
        month_calendar = calendar.monthcalendar(
            self.current_date.year, self.current_date.month
        )

        days_grid = ft.Column(spacing=10)
        week_days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

        # Cabecera con días de la semana
        days_grid.controls.append(
            ft.Row(
                controls=[
                    ft.Text(day, size=14, weight=ft.FontWeight.BOLD)
                    for day in week_days
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )

        # Días del mes
        for week in month_calendar:
            week_row = ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            for day in week:
                if day != 0:
                    week_row.controls.append(
                        CalendarDayButton(
                            text=str(day),
                            day_clicked=self.day_clicked,
                            has_tasks=False,  # Aquí podrías verificar si hay tareas
                        )
                    )
                else:
                    week_row.controls.append(ft.Container(width=40))
            days_grid.controls.append(week_row)

        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_LEFT, on_click=self.previous_month
                        ),
                        ft.Text(
                            self.current_date.strftime("%B %Y"),
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.ARROW_RIGHT, on_click=self.next_month
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                days_grid,
            ]
        )

    def day_clicked(self, e: Any) -> None:
        if e.page:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Día seleccionado: {e.control.data}"),
                duration=1000,
            )
            e.page.snack_bar.open = True
            e.page.update()

    def previous_month(self, e: Any) -> None:
        if self.current_date.month == 1:
            self.current_date = self.current_date.replace(
                year=self.current_date.year - 1, month=12
            )
        else:
            self.current_date = self.current_date.replace(
                month=self.current_date.month - 1
            )
        self.content = self.build_calendar()
        self.update()

    def next_month(self, e: Any) -> None:
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(
                year=self.current_date.year + 1, month=1
            )
        else:
            self.current_date = self.current_date.replace(
                month=self.current_date.month + 1
            )
        self.content = self.build_calendar()
        self.update()


def calendar_page() -> ft.Control:
    return ft.Column(
        controls=[
            CalendarView(),
        ],
    )
