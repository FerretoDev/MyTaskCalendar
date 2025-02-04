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
            ft.Text(self.title, size=20, weight=ft.FontWeight.BOLD),
            ft.Card(
                content=ft.Column(
                    controls=[self._create_setting_item(item) for item in self.items]
                )
            ),
        ]

    def _create_setting_item(self, item: SettingItem) -> ft.ListTile:
        return ft.ListTile(
            leading=ft.Icon(item.icon),
            title=ft.Text(item.title),
            subtitle=ft.Text(item.description) if item.description else None,
            trailing=item.trailing,
            on_click=item.on_click,
        )
