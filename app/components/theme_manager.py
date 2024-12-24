from enum import Enum
from typing import Callable, Optional

import flet as ft


class ThemeMode(Enum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"


class ThemeManager:
    def __init__(self, page: ft.Page, on_theme_changed: Optional[Callable] = None):
        self.page = page
        self.current_theme = ThemeMode.LIGHT
        self.on_theme_changed = on_theme_changed

    def toggle_theme(self) -> None:
        """Alterna entre tema claro y oscuro"""
        if self.current_theme == ThemeMode.LIGHT:
            self.set_theme(ThemeMode.DARK)
        else:
            self.set_theme(ThemeMode.LIGHT)

    def set_theme(self, theme_mode: ThemeMode) -> None:
        """
        Establece el tema específico

        Args:
            theme_mode: Modo de tema a establecer
        """
        self.current_theme = theme_mode
        self.page.theme_mode = (
            ft.ThemeMode.DARK if theme_mode == ft.ThemeMode.DARK else ft.ThemeMode.LIGHT
        )

        # Aplicar colores y estilos específicos según el tema
        if theme_mode == ThemeMode.DARK:
            self.page.theme = self._create_dark_theme()
        else:
            self.page.theme = self._create_light_theme()

        if self.on_theme_changed:
            self.on_theme_changed(theme_mode)

        self.page.update()

    def _create_light_theme(self) -> ft.Theme:
        """Crea el tema claro personalizado"""
        return ft.Theme(
            color_scheme_seed="blue",
            visual_density=ft.VisualDensity.COMFORTABLE,
            use_material3=True,
        )

    def _create_dark_theme(self) -> ft.Theme:
        """Crea el tema oscuro personalizado"""
        return ft.Theme(
            color_scheme_seed="blue",
            visual_density=ft.VisualDensity.COMFORTABLE,
            use_material3=True,
            color_scheme=ft.ColorScheme(
                primary=ft.Colors.BLUE,
                on_primary=ft.Colors.WHITE,
                primary_container=ft.Colors.BLUE_900,
                surface_tint=ft.Colors.BLUE_700,
            ),
        )

    def create_theme_toggle(self) -> ft.IconButton:
        """Crea un botón para alternar el tema"""
        return ft.IconButton(
            icon=ft.Icons.DARK_MODE,
            tooltip="Cambiar tema",
            on_click=lambda _: self.toggle_theme(),
        )
