import calendar
from datetime import datetime
from typing import Any

import flet as ft


class CalendarDayButton(ft.Container):
    def __init__(
        self,
        text: str,
        day_clicked: Any,
        has_tasks: bool = False,
        is_today: bool = False,
        is_weekend: bool = False,
    ) -> None:
        super().__init__()

        # Determinar el color de fondo según el estado
        if is_today:
            self.bgcolor = ft.Colors.PRIMARY
            text_color = ft.Colors.ON_PRIMARY
        elif has_tasks:
            self.bgcolor = (
                ft.Colors.SECONDARY_CONTAINER
                if hasattr(ft.Colors, "SECONDARY_CONTAINER")
                else ft.Colors.BLUE_100
            )
            text_color = (
                ft.Colors.ON_SECONDARY_CONTAINER
                if hasattr(ft.Colors, "ON_SECONDARY_CONTAINER")
                else ft.Colors.BLUE_900
            )
        elif is_weekend:
            self.bgcolor = ft.Colors.GREY_100
            text_color = ft.Colors.GREY_700
        else:
            self.bgcolor = None  # Usar color de superficie del tema
            text_color = None  # Usar color de texto del tema

        self.border_radius = ft.border_radius.all(12)
        self.border = ft.border.all(
            1.5, ft.Colors.BLUE_200 if is_today else ft.Colors.GREY_200
        )
        self.padding = 12
        self.data = text
        self.on_click = day_clicked
        self.animate = ft.Animation(200, ft.AnimationCurve.EASE_OUT)
        self.ink = True

        # Sombra sutil
        self.shadow = ft.BoxShadow(
            spread_radius=0,
            blur_radius=4,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 2),
        )

        # Efecto hover
        self.on_hover = self._on_hover

        self.content = ft.Column(
            controls=[
                ft.Text(
                    text,
                    size=16,
                    weight=ft.FontWeight.BOLD if is_today else ft.FontWeight.W_500,
                    color=text_color,
                ),
                # Indicador de tareas
                ft.Container(
                    content=ft.Icon(
                        ft.Icons.CIRCLE,
                        size=6,
                        color=ft.Colors.BLUE_600,
                    ),
                    visible=has_tasks and not is_today,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
        )

    def _on_hover(self, e: Any) -> None:
        if e.data == "true":
            self.scale = 1.05
            self.shadow = ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_400),
                offset=ft.Offset(0, 4),
            )
        else:
            self.scale = 1.0
            self.shadow = ft.BoxShadow(
                spread_radius=0,
                blur_radius=4,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
                offset=ft.Offset(0, 2),
            )
        self.update()


class CalendarView(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.current_date = datetime.now()
        self.padding = 20
        self.border_radius = ft.border_radius.all(16)
        self.bgcolor = None  # Usar color del tema
        self.shadow = ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            offset=ft.Offset(0, 4),
        )
        self.content = self.build_calendar()

    def build_calendar(self) -> Any:
        month_calendar = calendar.monthcalendar(
            self.current_date.year, self.current_date.month
        )

        days_grid = ft.Column(spacing=8)
        week_days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

        today = datetime.now()

        # Cabecera con días de la semana mejorada
        days_grid.controls.append(
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            day,
                            size=13,
                            weight=ft.FontWeight.W_600,
                            color=ft.Colors.BLUE_700 if i >= 5 else ft.Colors.GREY_700,
                        ),
                        expand=1,
                        alignment=ft.alignment.center,
                    )
                    for i, day in enumerate(week_days)
                ],
                spacing=8,
            )
        )

        # Separador
        days_grid.controls.append(ft.Divider(height=16, color=ft.Colors.GREY_200))

        # Días del mes
        for week in month_calendar:
            week_row = ft.Row(spacing=8)
            for day_index, day in enumerate(week):
                if day != 0:
                    is_today = (
                        day == today.day
                        and self.current_date.month == today.month
                        and self.current_date.year == today.year
                    )
                    is_weekend = day_index >= 5

                    week_row.controls.append(
                        ft.Container(
                            content=CalendarDayButton(
                                text=str(day),
                                day_clicked=self.day_clicked,
                                has_tasks=False,  # Aquí podrías verificar si hay tareas
                                is_today=is_today,
                                is_weekend=is_weekend,
                            ),
                            expand=1,
                        )
                    )
                else:
                    week_row.controls.append(ft.Container(expand=1))
            days_grid.controls.append(week_row)

        # Encabezado del mes con estilo mejorado
        month_header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_LEFT,
                        icon_size=28,
                        icon_color=ft.Colors.BLUE_700,
                        on_click=self.previous_month,
                        tooltip="Mes anterior",
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    self.current_date.strftime("%B").capitalize(),
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.BLUE_900,
                                ),
                                ft.Text(
                                    str(self.current_date.year),
                                    size=14,
                                    color=ft.Colors.GREY_600,
                                ),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=2,
                        ),
                        expand=1,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.CHEVRON_RIGHT,
                        icon_size=28,
                        icon_color=ft.Colors.BLUE_700,
                        on_click=self.next_month,
                        tooltip="Mes siguiente",
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=ft.padding.only(bottom=20),
        )

        return ft.Column(
            controls=[
                month_header,
                days_grid,
            ],
            spacing=10,
        )

    def day_clicked(self, e: Any) -> None:
        if e.page:
            selected_date = datetime(
                self.current_date.year,
                self.current_date.month,
                int(e.control.data),
            )
            formatted_date = selected_date.strftime("%d de %B de %Y")

            e.page.snack_bar = ft.SnackBar(
                content=ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.EVENT, color=ft.Colors.WHITE),
                        ft.Text(
                            f"Fecha seleccionada: {formatted_date}",
                            color=ft.Colors.WHITE,
                        ),
                    ],
                    spacing=10,
                ),
                bgcolor=ft.Colors.BLUE_700,
                duration=2000,
                behavior=ft.SnackBarBehavior.FLOATING,
                action="Cerrar",
                action_color=ft.Colors.BLUE_100,
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
    return ft.Container(
        content=ft.Column(
            controls=[
                CalendarView(),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        padding=20,
        expand=True,
    )
