import flet as ft


def main(page: ft.Page):
    page.title = "Mi App Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(ft.TextField(label="Nombre del proyecto"))


if __name__ == "__main__":
    ft.app(target=main)
