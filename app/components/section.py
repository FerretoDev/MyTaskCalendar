from typing import List

import flet as ft
from components.types import SettingItem


class SettingsSection(ft.Column):
    """A reusable section component for settings"""

    def __init__(self, title: str, items: List[SettingItem], spacing: int = 10):
        super().__init__()
        self.title = title
        self.items = items
        self.spacing = spacing
        self.controls = self._build()

    def _build(self) -> List[ft.Control]:
        return [
            ft.Text(
                self.title,
                size=18,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
            ),
            ft.Card(
                elevation=2,
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            self._create_setting_item(item) for item in self.items
                        ],
                        spacing=0,
                    ),
                    padding=5,
                ),
            ),
        ]

    def _create_setting_item(self, item: SettingItem) -> ft.ListTile:
        return ft.ListTile(
            leading=ft.Icon(
                item.icon,
                color=ft.Colors.BLUE_700,
                size=24,
            ),
            title=ft.Text(
                item.title,
                weight=ft.FontWeight.W_500,
                size=15,
            ),
            subtitle=(
                ft.Text(
                    item.description,
                    size=12,
                    color=ft.Colors.GREY_600,
                )
                if item.description
                else None
            ),
            trailing=item.trailing,
            on_click=item.on_click,
            hover_color=ft.Colors.BLUE_50,
        )
