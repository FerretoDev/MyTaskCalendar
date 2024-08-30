import datetime
import flet as ft


class Calendar(ft.Row):
    def __init__(self):
        super().__init__()
        self.selected_date = ft.Text("No date selected")
        self.date_picker = None

    def handle_change(self, e):
        # Actualiza el texto con la fecha seleccionada
        self.selected_date.value = (
            f"Date selected: {e.control.value.strftime('%Y-%m-%d')}"
        )
        self.update()

    def handle_dismissal(self, e):
        self.selected_date.value = "DatePicker dismissed"
        self.update()

    def build(self):
        # Botón para abrir el DatePicker
        return ft.Column(
            controls=[
                ft.ElevatedButton(
                    "Pick date",
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=self.open_date_picker,
                ),
                self.selected_date,  # Muestra la fecha seleccionada
            ]
        )

    def open_date_picker(self, e):
        # Configura el DatePicker dentro del contexto del control y muestra el calendario en la página correcta
        if not self.date_picker:
            self.date_picker = ft.DatePicker(
                first_date=datetime.datetime(year=2023, month=10, day=1),
                last_date=datetime.datetime(year=2024, month=10, day=1),
                on_change=self.handle_change,
                on_dismiss=self.handle_dismissal,
            )
            # Añadimos el DatePicker a los controles del calendario
            self.controls.append(self.date_picker)
        self.date_picker.open = True
        self.update()
