import flet as ft


def task_item(title, time, is_completed):
    return ft.ListTile(
        leading=ft.Checkbox(value=is_completed),
        title=ft.Text(title),
        subtitle=ft.Text(time),
        trailing=ft.IconButton(icon=ft.icons.NOTIFICATIONS),
    )
