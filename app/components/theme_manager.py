from enum import Enum
from typing import Callable, Optional

import flet as ft


class ThemeMode(Enum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"


class ThemeManager:
    def __init__(
        self,
        page: ft.Page,
        on_theme_changed: Optional[Callable[["ThemeMode"], None]] = None,
    ):
        self.page = page
        self.current_theme = ThemeMode.LIGHT
        self.accent_color = "blue"  # Color de acento por defecto
        self.on_theme_changed = on_theme_changed
        self._load_saved_preferences()

    def _load_saved_preferences(self) -> None:
        """Carga las preferencias guardadas del usuario"""
        # Intentar cargar desde client_storage si está disponible
        if hasattr(self.page, "client_storage"):
            try:
                saved_theme = self.page.client_storage.get("theme_mode")
                saved_color = self.page.client_storage.get("accent_color")

                if saved_theme:
                    self.current_theme = ThemeMode(saved_theme)
                if saved_color:
                    self.accent_color = saved_color
            except Exception:
                # Si hay error, usar valores por defecto
                pass

    def _save_preferences(self) -> None:
        """Guarda las preferencias del usuario"""
        if hasattr(self.page, "client_storage"):
            try:
                self.page.client_storage.set("theme_mode", self.current_theme.value)
                self.page.client_storage.set("accent_color", self.accent_color)
            except Exception:
                # Silenciosamente ignorar errores de almacenamiento
                pass

    def get_current_theme(self) -> ThemeMode:
        """Devuelve el tema actual"""
        return self.current_theme

    def get_accent_color(self) -> str:
        """Devuelve el color de acento actual"""
        return self.accent_color

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

        # Mapear el tema correctamente y configurar ambos temas (light y dark)
        self.page.theme = self._create_light_theme()
        self.page.dark_theme = self._create_dark_theme()

        if theme_mode == ThemeMode.DARK:
            self.page.theme_mode = ft.ThemeMode.DARK
        elif theme_mode == ThemeMode.SYSTEM:
            self.page.theme_mode = ft.ThemeMode.SYSTEM
        else:  # LIGHT
            self.page.theme_mode = ft.ThemeMode.LIGHT

        if self.on_theme_changed:
            self.on_theme_changed(theme_mode)

        self._save_preferences()
        self.page.update()

    def set_accent_color(self, color: str) -> None:
        """Establece el color de acento de la aplicación"""
        self.accent_color = color
        self._save_preferences()
        # Re-aplicar el tema actual con el nuevo color
        self.set_theme(self.current_theme)

    def _create_light_theme(self) -> ft.Theme:
        """Crea el tema claro personalizado"""
        return ft.Theme(
            color_scheme_seed=self.accent_color,
            visual_density=ft.VisualDensity.COMFORTABLE,
            use_material3=True,
        )

    def _create_dark_theme(self) -> ft.Theme:
        """Crea el tema oscuro personalizado"""
        return ft.Theme(
            color_scheme_seed=self.accent_color,
            visual_density=ft.VisualDensity.COMFORTABLE,
            use_material3=True,
        )

    def create_theme_toggle(self) -> ft.IconButton:
        """Crea un botón para alternar el tema"""
        icon = (
            ft.Icons.DARK_MODE
            if self.current_theme == ThemeMode.LIGHT
            else ft.Icons.LIGHT_MODE
        )
        return ft.IconButton(
            icon=icon,
            tooltip="Cambiar tema",
            on_click=lambda _: self.toggle_theme(),
        )
