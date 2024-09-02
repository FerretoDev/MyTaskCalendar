import flet as ft


def settings_page():
    return ft.Column(
        adaptive=True,
        controls=[
            ft.Text("Configuración aquí", size=24, color=ft.colors.BLACK),
            ft.Switch(label="Notificaciones"),
            ft.Switch(label="Sincronización con la nube"),
        ],
    )
