import flet as ft


class SettingsPage(ft.Column):
    def __init__(self):
        super().__init__()

        # Estado inicial del tema (True para Light, False para Dark)
        self.is_light_theme = True
        self.theme_switch = ft.Switch(
            value=self.is_light_theme, on_change=self.toggle_theme
        )
        self.theme_text = ft.Text("Light")  # Texto inicial es "Light"

    def build(self):
        # Tema (Light/Dark)
        theme_row = ft.Row(
            controls=[
                ft.Icon(ft.icons.WB_SUNNY_OUTLINED),  # Icono de sol para el tema
                ft.Text("Theme"),
                self.theme_text,  # Texto que indica el estado del tema
                self.theme_switch,  # Switch para cambiar el tema
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # Switch para sincronizar con el calendario
        sync_calendar_row = ft.Row(
            controls=[
                ft.Text("Sync with calendar"),
                ft.Switch(value=True),  # Switch activado
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        # Opción de notificaciones
        notifications_row = ft.ListTile(
            title=ft.Text("Notifications"),
            trailing=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
        )

        # Opción de soporte
        support_row = ft.ListTile(
            title=ft.Text("Support"),
            trailing=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
        )

        # Opción de política de privacidad
        privacy_policy_row = ft.ListTile(
            title=ft.Text("Privacy Policy"),
            trailing=ft.Icon(ft.icons.ARROW_FORWARD_IOS),
        )

        return ft.Column(
            controls=[
                theme_row,
                sync_calendar_row,
                notifications_row,
                support_row,
                privacy_policy_row,
            ],
            expand=True,
            spacing=20,
        )

    def toggle_theme(self, e):
        # Cambiar el tema cuando el switch se activa o desactiva
        self.is_light_theme = self.theme_switch.value  # Actualiza el estado
        self.theme_text.value = (
            "Light" if self.is_light_theme else "Dark"
        )  # Actualiza el texto

        # Cambiar el tema de la página
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT if self.is_light_theme else ft.ThemeMode.DARK
        )
        self.page.update()  # Actualiza la página para aplicar el tema


def settings_page():
    return SettingsPage()
