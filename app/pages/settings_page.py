# settings/settings_page.py
from typing import Optional

import flet as ft
from components.theme_manager import ThemeManager

from components.section import SettingsSection
from components.theme_selector import ThemeSelector
from components.dialogs.notifications import NotificationsDialog
from components.types import SettingItem


class SettingsPage(ft.Column):
    """Main settings page component that orchestrates all settings sections"""

    def __init__(self, theme_manager: Optional[ThemeManager] = None):
        super().__init__()
        self.theme_manager = theme_manager
        self.theme_selector = ThemeSelector(theme_manager)
        self.expand = True  # Asegura que el Column ocupe todo el espacio disponible
        self.scroll = ft.ScrollMode.HIDDEN  # Habilita el scroll en el Column principal
        self._initialize_settings()

    def _initialize_settings(self) -> None:
        self.settings_sections = {
            "Apariencia": [
                self.theme_selector.create_setting_item(),
                SettingItem(
                    title="Color de acento",
                    icon=ft.Icons.COLOR_LENS,
                    description="Personaliza el color principal de la aplicación",
                ),
            ],
            "Sincronización": [
                SettingItem(
                    title="Sincronizar con calendario",
                    icon=ft.Icons.SYNC,
                    description="Conectar con calendario del sistema",
                    trailing=ft.Switch(value=True),
                ),
                SettingItem(
                    title="Backup automático",
                    icon=ft.Icons.BACKUP,
                    description="Guardar copia de seguridad diaria",
                    trailing=ft.Switch(value=True),
                ),
            ],
            "Notificaciones": [
                SettingItem(
                    title="Notificaciones",
                    icon=ft.Icons.NOTIFICATIONS,
                    description="Gestionar notificaciones",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                    on_click=lambda e: NotificationsDialog.show(e.page),
                ),
                SettingItem(
                    title="Sonidos",
                    icon=ft.Icons.VOLUME_UP,
                    description="Sonidos de notificación",
                    trailing=ft.Switch(value=True),
                ),
            ],
            "Información": [
                SettingItem(
                    title="Soporte",
                    icon=ft.Icons.HELP_OUTLINE,
                    description="Obtener ayuda",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                ),
                SettingItem(
                    title="Política de privacidad",
                    icon=ft.Icons.PRIVACY_TIP,
                    description="Ver política de privacidad",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                ),
                SettingItem(
                    title="Versión", icon=ft.Icons.INFO_OUTLINE, description="1.0.0"
                ),
            ],
        }

    def build(self) -> ft.Control:
        settings_list = ft.Column(
            controls=[
                SettingsSection(title, items)
                for title, items in self.settings_sections.items()
            ],
            spacing=20,
        )

        # Wrap the settings list in a Container with padding
        content_container = ft.Container(
            content=settings_list,
            padding=20,
        )

        return content_container


def create_settings_page(theme_manager: Optional[ThemeManager] = None) -> ft.Control:
    """Factory function to create the settings page"""
    return SettingsPage(theme_manager)
