import flet as ft


class NotificationsDialog:
    """Handles notifications settings dialog"""

    @staticmethod
    def show(page: ft.Page) -> None:
        # Estado de las notificaciones
        reminders_enabled = True
        events_enabled = True
        updates_enabled = False

        def close_dialog(_: ft.ControlEvent) -> None:
            dialog.open = False
            page.update()

        def save_settings(_: ft.ControlEvent) -> None:
            dialog.open = False
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Configuración de notificaciones guardada"),
                duration=2000,
                bgcolor=ft.Colors.GREEN_700,
            )
            page.snack_bar.open = True
            page.update()

        reminders_checkbox = ft.Checkbox(
            label="Recordatorios de tareas",
            value=reminders_enabled,
        )
        events_checkbox = ft.Checkbox(
            label="Eventos próximos",
            value=events_enabled,
        )
        updates_checkbox = ft.Checkbox(
            label="Actualizaciones",
            value=updates_enabled,
        )

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(
                "Configuración de notificaciones",
                size=20,
                weight=ft.FontWeight.BOLD,
            ),
            content=ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Selecciona qué notificaciones deseas recibir:",
                            size=14,
                            color=ft.Colors.GREY_700,
                        ),
                        ft.Divider(),
                        reminders_checkbox,
                        events_checkbox,
                        updates_checkbox,
                        ft.Divider(),
                        ft.Text(
                            "Las notificaciones te ayudarán a no olvidar tus tareas importantes.",
                            size=12,
                            color=ft.Colors.GREY_600,
                            italic=True,
                        ),
                    ],
                    tight=True,
                    spacing=10,
                ),
                padding=10,
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dialog),
                ft.ElevatedButton(
                    "Guardar",
                    on_click=save_settings,
                    bgcolor=ft.Colors.BLUE_700,
                    color=ft.Colors.WHITE,
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()
