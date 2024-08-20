import flet as ft


def tasks_page():
    return ft.ListView(
        controls=[
            ft.ListTile(title=ft.Text("Tarea 1 - Proyecto A")),
            ft.ListTile(title=ft.Text("Tarea 2 - Proyecto B")),
            ft.ListTile(title=ft.Text("Tarea 3 - Proyecto C")),
        ]
    )
