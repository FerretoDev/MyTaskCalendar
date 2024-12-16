from enum import Enum

import flet as ft


class AppThemeMode(Enum):
    LIGHT = ft.ThemeMode.LIGHT
    DARK = ft.ThemeMode.DARK
    SYSTEM = ft.ThemeMode.SYSTEM


def create_theme_toggle(page: ft.Page):
    themes_modes = list(AppThemeMode)
    current_theme_mode = 0

    def cycle_theme(_):
        nonlocal current_theme_index
        current_theme_index = (current_theme_index + 1) % len(themes_modes)
        new_theme = themes_modes[current_theme_index]
        page.theme_mode = new_theme.value
        page.update()

    return ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="Toggle theme",
        on_click=cycle_theme,
    )
