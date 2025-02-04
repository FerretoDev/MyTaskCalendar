import flet as ft


class NotificationsDialog:
    """Handles notifications settings dialog"""

    @staticmethod
    def show(page: ft.Page) -> None:
        def close_dialog(_: ft.ControlEvent) -> None:
            dialog.open = False
            page.update()

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

        page.dialog = dialog
        dialog.open = True
        page.update()
