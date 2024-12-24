from dataclasses import dataclass
from typing import Callable, List, Optional

import flet as ft
from components.theme_manager import ThemeManager, ThemeMode


@dataclass
class SettingItem:
    """Estructura para items de configuración"""

    title: str
    icon: str
    description: Optional[str] = None
    trailing: Optional[ft.Control] = None
    on_click: Optional[Callable] = None


class SettingsPage(ft.Column):
    def __init__(self, theme_manager: Optional[ThemeManager] = None):
        super().__init__()
        self.theme_manager = theme_manager
        self._initialize_settings()

    def _initialize_settings(self) -> None:
        """Inicializa las configuraciones disponibles"""
        self.settings_sections = {
            "Apariencia": [
                self._create_theme_setting(),
                SettingItem(
                    title="Color de acento",
                    icon=ft.Icons.COLOR_LENS,
                    description="Personaliza el color principal de la aplicación",
                    on_click=self._show_color_picker,
                ),
            ],
            "Sincronización": [
                SettingItem(
                    title="Sincronizar con calendario",
                    icon=ft.Icons.SYNC,
                    description="Conectar con calendario del sistema",
                    trailing=ft.Switch(value=True, on_change=self._handle_sync_change),
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
                    on_click=self._show_notifications_dialog,
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
                    on_click=self._show_support_dialog,
                ),
                SettingItem(
                    title="Política de privacidad",
                    icon=ft.Icons.PRIVACY_TIP,
                    description="Ver política de privacidad",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS),
                    on_click=self._show_privacy_policy,
                ),
                SettingItem(
                    title="Versión",
                    icon=ft.Icons.INFO_OUTLINE,
                    description="1.0.0",
                ),
            ],
        }

    def _create_theme_setting(self) -> SettingItem:
        """Crea el item de configuración del tema"""
        theme_switch = ft.Dropdown(
            value=(
                self.theme_manager.current_theme.value
                if self.theme_manager
                else ThemeMode.LIGHT.value
            ),
            options=[
                ft.dropdown.Option(ThemeMode.LIGHT.value, "Claro"),
                ft.dropdown.Option(ThemeMode.DARK.value, "Oscuro"),
                ft.dropdown.Option(ThemeMode.SYSTEM.value, "Sistema"),
            ],
            on_change=self._handle_theme_change,
        )

        return SettingItem(
            title="Tema",
            icon=ft.Icons.DARK_MODE,
            # description="Cambiar apariencia de la aplicación",
            trailing=theme_switch,
        )

    def build(self) -> ft.Control:
        settings_list = ft.Column(
            controls=[
                self._create_section(title, items)
                for title, items in self.settings_sections.items()
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        )

        return ft.Container(content=settings_list, padding=20, expand=True)

    def _create_section(self, title: str, items: list[SettingItem]) -> ft.Column:
        """Crea una sección de configuraciones"""
        return ft.Column(
            controls=[
                ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
                ft.Card(
                    content=ft.Column(
                        controls=[self._create_setting_item(item) for item in items],
                    ),
                ),
            ],
            spacing=10,
        )

    def _create_setting_item(self, item: SettingItem) -> ft.ListTile:
        """Crea un item de configuración"""
        return ft.ListTile(
            leading=ft.Icon(item.icon),
            title=ft.Text(item.title),
            subtitle=ft.Text(item.description) if item.description else None,
            trailing=item.trailing,
            on_click=item.on_click,
        )

    def _handle_theme_change(self, e) -> None:
        """Maneja el cambio de tema"""
        if self.theme_manager:
            self.theme_manager.set_theme(ThemeMode(e.control.value))

    def _handle_sync_change(self, e) -> None:
        """Maneja el cambio en la sincronización"""
        # Implementar lógica de sincronización
        pass

    def _show_notifications_dialog(self, e) -> None:
        """Muestra el diálogo de configuración de notificaciones"""

        def close_dialog(_):
            dialog.open = False
            self.page.update()

        dialog = ft.AlertDialog(
            title=ft.Text("Configuración de notificaciones"),
            content=ft.Column(
                controls=[
                    ft.Checkbox(label="Recordatorios de tareas"),
                    ft.Checkbox(label="Eventos próximos"),
                    ft.Checkbox(label="Actualizaciones"),
                ],
                tight=True,
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.TextButton("Guardar", on_click=close_dialog),
            ],
        )

        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def _show_color_picker(self, e) -> None:
        """Muestra el selector de color de acento"""
        # Implementar selector de color
        pass

    def _show_support_dialog(self, e) -> None:
        """Muestra el diálogo de soporte"""
        # Implementar diálogo de soporte
        pass

    def _show_privacy_policy(self, e) -> None:
        """Muestra la política de privacidad"""
        # Implementar vista de política de privacidad
        pass


# def settings_page():
#
#   return SettingsPage()


def settings_page(theme_manager: Optional[ThemeManager] = None) -> ft.Control:
    """Crea la página de configuraciones"""
    return SettingsPage(theme_manager)
