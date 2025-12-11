# settings/settings_page.py
from typing import Optional

import flet as ft
from components.dialogs.notifications import NotificationsDialog
from components.section import SettingsSection
from components.theme_manager import ThemeManager
from components.theme_selector import ThemeSelector
from components.types import SettingItem


class SettingsPage(ft.Column):
    """Main settings page component that orchestrates all settings sections"""

    def __init__(self, theme_manager: Optional[ThemeManager] = None):
        super().__init__()
        self.theme_manager = theme_manager
        self.theme_selector = ThemeSelector(theme_manager)
        self.expand = True  # Asegura que el Column ocupe todo el espacio disponible
        self.scroll = ft.ScrollMode.AUTO  # Habilita el scroll en el Column principal

        # Estado de configuraciones
        self.sync_calendar_enabled = True
        self.auto_backup_enabled = True
        self.sounds_enabled = True

        self._initialize_settings()
        self._build_controls()

    def _handle_sync_calendar(self, e: ft.ControlEvent) -> None:
        """Maneja el cambio en la sincronización del calendario"""
        self.sync_calendar_enabled = e.control.value
        if e.page:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    f"Sincronización {'activada' if e.control.value else 'desactivada'}"
                ),
                duration=2000,
            )
            e.page.snack_bar.open = True
            e.page.update()

    def _handle_auto_backup(self, e: ft.ControlEvent) -> None:
        """Maneja el cambio en el backup automático"""
        self.auto_backup_enabled = e.control.value
        if e.page:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    f"Backup automático {'activado' if e.control.value else 'desactivado'}"
                ),
                duration=2000,
            )
            e.page.snack_bar.open = True
            e.page.update()

    def _handle_sounds(self, e: ft.ControlEvent) -> None:
        """Maneja el cambio en los sonidos"""
        self.sounds_enabled = e.control.value
        if e.page:
            e.page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    f"Sonidos {'activados' if e.control.value else 'desactivados'}"
                ),
                duration=2000,
            )
            e.page.snack_bar.open = True
            e.page.update()

    def _handle_accent_color(self, e: ft.ControlEvent) -> None:
        """Maneja el diálogo de selección de color de acento"""
        self._show_accent_color_dialog(e)

    def _handle_support(self, e: ft.ControlEvent) -> None:
        """Muestra información de soporte"""
        self._show_support_dialog(e)

    def _handle_privacy_policy(self, e: ft.ControlEvent) -> None:
        """Muestra la política de privacidad"""
        self._show_privacy_dialog(e)

    def _show_accent_color_dialog(self, e: ft.ControlEvent) -> None:
        """Muestra el diálogo de selección de color de acento"""
        if not e.page:
            return

        dialog_ref = None

        def close_dialog(_: ft.ControlEvent) -> None:
            if dialog_ref:
                dialog_ref.open = False
                e.page.update()

        def select_color(color: str, color_value: str):
            def handler(_: ft.ControlEvent) -> None:
                if dialog_ref:
                    dialog_ref.open = False

                # Aplicar el color de acento
                if self.theme_manager:
                    # Mapear nombres de colores a color_scheme_seed
                    color_map: dict[str, str] = {
                        "Azul": "blue",
                        "Verde": "green",
                        "Naranja": "orange",
                        "Morado": "purple",
                        "Rosa": "pink",
                        "Rojo": "red",
                    }
                    self.theme_manager.set_accent_color(color_map.get(color, "blue"))

                e.page.snack_bar = ft.SnackBar(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                width=20,
                                height=20,
                                bgcolor=color_value,
                                border_radius=ft.border_radius.all(10),
                            ),
                            ft.Text(f"Color {color} aplicado"),
                        ],
                        spacing=10,
                    ),
                    duration=2000,
                )
                e.page.snack_bar.open = True
                e.page.update()

            return handler

        colors = [
            ("Azul", ft.Colors.BLUE_400),
            ("Verde", ft.Colors.GREEN_400),
            ("Naranja", ft.Colors.ORANGE_400),
            ("Morado", ft.Colors.PURPLE_400),
            ("Rosa", ft.Colors.PINK_400),
            ("Rojo", ft.Colors.RED_400),
        ]

        dialog_ref = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                "Seleccionar color de acento",
                size=20,
                weight=ft.FontWeight.BOLD,
            ),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ListTile(
                            leading=ft.Container(
                                width=40,
                                height=40,
                                bgcolor=color_value,
                                border_radius=ft.border_radius.all(20),
                                shadow=ft.BoxShadow(
                                    spread_radius=1,
                                    blur_radius=5,
                                    color=ft.Colors.with_opacity(0.3, color_value),
                                    offset=ft.Offset(0, 2),
                                ),
                            ),
                            title=ft.Text(color_name, weight=ft.FontWeight.W_500),
                            on_click=select_color(color_name, color_value),
                            hover_color=ft.Colors.BLUE_50,
                        )
                        for color_name, color_value in colors
                    ],
                    tight=True,
                    spacing=5,
                ),
                padding=10,
            ),
            actions=[
                ft.TextButton("Cerrar", on_click=close_dialog),
            ],
        )

        e.page.overlay.append(dialog_ref)
        dialog_ref.open = True
        e.page.update()

    def _show_support_dialog(self, e: ft.ControlEvent) -> None:
        """Muestra el diálogo de soporte"""

        def close_dialog(_: ft.ControlEvent) -> None:
            dialog.open = False
            e.page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Soporte"),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "¿Necesitas ayuda?",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Divider(),
                        ft.Text("Correo: soporte@mytaskcalendar.com"),
                        ft.Text("Teléfono: +34 123 456 789"),
                        ft.Text("Horario: Lun-Vie 9:00-18:00"),
                    ],
                    spacing=10,
                ),
                padding=10,
            ),
            actions=[
                ft.TextButton("Cerrar", on_click=close_dialog),
            ],
        )

        e.page.dialog = dialog
        dialog.open = True
        e.page.update()

    def _show_privacy_dialog(self, e: ft.ControlEvent) -> None:
        """Muestra el diálogo de política de privacidad"""

        def close_dialog(_: ft.ControlEvent) -> None:
            dialog.open = False
            e.page.update()

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Política de privacidad"),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Resumen de privacidad",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Divider(),
                        ft.Text(
                            "• Tus datos se almacenan localmente en tu dispositivo",
                            size=14,
                        ),
                        ft.Text(
                            "• No compartimos tu información con terceros",
                            size=14,
                        ),
                        ft.Text(
                            "• Puedes exportar o eliminar tus datos en cualquier momento",
                            size=14,
                        ),
                        ft.Text(
                            "• Cumplimos con el RGPD y normativas de privacidad",
                            size=14,
                        ),
                    ],
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                ),
                padding=10,
                height=300,
            ),
            actions=[
                ft.TextButton("Cerrar", on_click=close_dialog),
            ],
        )

        e.page.dialog = dialog
        dialog.open = True
        e.page.update()

    def _initialize_settings(self) -> None:
        self.settings_sections = {
            "Apariencia": [
                self.theme_selector.create_setting_item(),
                SettingItem(
                    title="Color de acento",
                    icon=ft.Icons.COLOR_LENS,
                    description="Personaliza el color principal de la aplicación",
                    trailing=ft.Icon(
                        ft.Icons.ARROW_FORWARD_IOS,
                        size=16,
                        color=ft.Colors.GREY_400,
                    ),
                    on_click=self._handle_accent_color,
                ),
            ],
            "Sincronización": [
                SettingItem(
                    title="Sincronizar con calendario",
                    icon=ft.Icons.SYNC,
                    description="Conectar con calendario del sistema",
                    trailing=ft.Switch(
                        value=self.sync_calendar_enabled,
                        on_change=self._handle_sync_calendar,
                    ),
                ),
                SettingItem(
                    title="Backup automático",
                    icon=ft.Icons.BACKUP,
                    description="Guardar copia de seguridad diaria",
                    trailing=ft.Switch(
                        value=self.auto_backup_enabled,
                        on_change=self._handle_auto_backup,
                    ),
                ),
            ],
            "Notificaciones": [
                SettingItem(
                    title="Notificaciones",
                    icon=ft.Icons.NOTIFICATIONS,
                    description="Gestionar notificaciones",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=16),
                    on_click=lambda e: NotificationsDialog.show(e.page),
                ),
                SettingItem(
                    title="Sonidos",
                    icon=ft.Icons.VOLUME_UP,
                    description="Sonidos de notificación",
                    trailing=ft.Switch(
                        value=self.sounds_enabled,
                        on_change=self._handle_sounds,
                    ),
                ),
            ],
            "Información": [
                SettingItem(
                    title="Soporte",
                    icon=ft.Icons.HELP_OUTLINE,
                    description="Obtener ayuda",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=16),
                    on_click=self._handle_support,
                ),
                SettingItem(
                    title="Política de privacidad",
                    icon=ft.Icons.PRIVACY_TIP,
                    description="Ver política de privacidad",
                    trailing=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=16),
                    on_click=self._handle_privacy_policy,
                ),
                SettingItem(
                    title="Versión", icon=ft.Icons.INFO_OUTLINE, description="1.0.0"
                ),
            ],
        }

    def _build_controls(self) -> None:
        # Título de la página
        page_title = ft.Container(
            content=ft.Text(
                "Configuración",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_900,
            ),
            padding=ft.padding.only(bottom=10),
        )

        settings_list = ft.Column(
            controls=[
                SettingsSection(title, items)
                for title, items in self.settings_sections.items()
            ],
            spacing=25,
        )

        # Wrap the settings list in a Container with padding
        content_container = ft.Container(
            content=ft.Column(
                controls=[
                    page_title,
                    settings_list,
                ],
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=20,
            expand=True,
        )

        self.controls = [content_container]


def create_settings_page(theme_manager: Optional[ThemeManager] = None) -> ft.Control:
    """Factory function to create the settings page"""
    return SettingsPage(theme_manager=theme_manager)
