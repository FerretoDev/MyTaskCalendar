import flet as ft

app_theme = ft.Theme(
    color_scheme=ft.ColorScheme(
        primary=ft.colors.BLUE,
        secondary=ft.colors.ORANGE,
        background=ft.colors.WHITE,
        on_background=ft.colors.BLACK,
        surface=ft.colors.GREY,
        on_surface=ft.colors.WHITE,
        error=ft.colors.RED,
        on_error=ft.colors.WHITE,
    ),
    text_theme=ft.TextTheme(
        title_large=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD),
    ),
    font_family="Cascadia Code",
)
