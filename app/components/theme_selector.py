from typing import Callable, List, Optional

import flet as ft
from components.theme_manager import ThemeManager, ThemeMode

from components.types import ClickEventHandler, SettingItem


class ThemeSelector:
    """Handles theme selection functionality"""

    def __init__(self, theme_manager: Optional[ThemeManager]):
        self.theme_manager = theme_manager
        self._theme_names = {
            ThemeMode.LIGHT.value: "Claro",
            ThemeMode.DARK.value: "Oscuro",
            ThemeMode.SYSTEM.value: "Sistema",
        }

    def create_setting_item(self) -> SettingItem:
        current_theme = (
            self.theme_manager.current_theme.value
            if self.theme_manager
            else ThemeMode.LIGHT.value
        )

        theme_text = ft.Text(
            self._get_theme_name(current_theme), size=14, color=ft.Colors.PRIMARY
        )

        return SettingItem(
            title="Tema",
            icon=ft.Icons.DARK_MODE,
            description="Cambiar apariencia de la aplicación",
            trailing=self._create_theme_selector(theme_text),
            on_click=lambda e: self._show_theme_dialog(e, theme_text),
        )

    def _get_theme_name(self, theme_value: str) -> str:
        return self._theme_names.get(theme_value, "Desconocido")

    def _create_theme_selector(self, theme_text: ft.Text) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                controls=[
                    theme_text,
                    ft.Icon(ft.Icons.ARROW_DROP_DOWN, color=ft.Colors.PRIMARY),
                ],
                spacing=5,
                width=70,
                alignment=ft.MainAxisAlignment.START,
            )
        )

    def _show_theme_dialog(self, e: ft.ControlEvent, theme_text: ft.Text) -> None:
        dialog = self._create_theme_dialog(theme_text)
        page = e.page
        page.dialog = dialog
        dialog.open = True
        page.update()

    def _create_theme_dialog(self, theme_text: ft.Text) -> ft.AlertDialog:
        def handle_theme_selection(theme_value: str) -> ClickEventHandler:
            def handle(e: ft.ControlEvent) -> None:
                if self.theme_manager:
                    self.theme_manager.set_theme(ThemeMode(theme_value))
                theme_text.value = self._get_theme_name(theme_value)
                e.page.dialog.open = False
                e.page.update()

            return handle

        return ft.AlertDialog(
            modal=True,
            title=ft.Text("Seleccionar tema", size=20, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                content=ft.Column(
                    controls=self._create_theme_options(handle_theme_selection),
                    tight=True,
                ),
                padding=10,
            ),
        )

    def _create_theme_options(
        self, handler: Callable[[str], ClickEventHandler]
    ) -> List[ft.ListTile]:
        return [
            ft.ListTile(
                leading=ft.Icon(ft.icons.LIGHT_MODE),
                title=ft.Text("Tema Claro"),
                on_click=handler(ThemeMode.LIGHT.value),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.DARK_MODE),
                title=ft.Text("Tema Oscuro"),
                on_click=handler(ThemeMode.DARK.value),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.icons.SETTINGS_SYSTEM_DAYDREAM),
                title=ft.Text("Tema del Sistema"),
                on_click=handler(ThemeMode.SYSTEM.value),
            ),
        ]
