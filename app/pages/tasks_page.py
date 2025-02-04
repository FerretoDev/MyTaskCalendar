from datetime import datetime, timedelta
from typing import Any, Callable, List

import flet as ft


class Task(ft.Column):
    def __init__(self, task_name, task_status_change, task_delete):
        super().__init__()
        self.completed = False
        self.task_name = task_name
        self.task_status_change = task_status_change
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Editar To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Eliminar To-Do",
                            on_click=self.delete_clicked,
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    # tooltip="Update To-Do",
                    tooltip="Actualizar To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        self.task_status_change(self)

    def delete_clicked(self, e):
        self.task_delete(self)


class TasksPage(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(
            hint_text="¿Qué necesita hacer?",
            on_submit=self.add_clicked,
            expand=True,
            # hint_text="¿Qué necesita hacer?", on_submit=self.add_clicked, expand=True
        )
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todo"),
                ft.Tab(text="Hoy"),
                ft.Tab(text="Mañana"),
                ft.Tab(text="Esta semana"),
                # ft.Tab(text="All"),
                # ft.Tab(text="Today"),
                # ft.Tab(text="Tomorrow"),
                # ft.Tab(text="This Week"),
            ],
        )

        self.items_left = ft.Text("0 elementos restantes")
        # self.items_left = ft.Text("0 items left")

        # self.width = 600
        self.controls = [
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                # text="Clear completed", on_click=self.clear_clicked
                                text="Eliminar completados",
                                on_click=self.clear_clicked,
                            ),
                        ],
                    ),
                ],
            ),
        ]

    def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_status_change, self.task_delete)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.update()

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        for task in self.tasks.controls:
            task_date = today  # Aquí podrías definir la fecha de cada tarea

            # Filtrado de tareas según la pestaña seleccionada
            task.visible = (
                status == "Todo"
                or (status == "Hoy" and task_date == today)
                or (status == "Mañana" and task_date == tomorrow)
                or (
                    status == "Esta semana"
                    and task_date >= today
                    and task_date < today + timedelta(days=7)
                )
                # status == "All"
                # or (status == "Today" and task_date == today)
                # or (status == "Tomorrow" and task_date == tomorrow)
                # or (
                #    status == "This Week"
                #    and task_date >= today
                #    and task_date < today + timedelta(days=7)
                # )
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} elementos activos restantes"
        # self.items_left.value = f"{count} active item(s) left"


class TaskListItem(ft.Container):
    def __init__(
        self, task_data: Any, on_status_changed: Callable, on_delete: Callable
    ) -> None:
        super().__init__()
        self.padding = 10
        self.border_radius = ft.border_radius.all(8)
        self.bgcolor = ft.colors.BLUE_50
        self.data = task_data

        self.content = ft.Row(
            controls=[
                ft.Checkbox(
                    value=task_data["completed"],
                    on_change=on_status_changed,
                ),
                ft.Text(task_data["title"], size=16, expand=True),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color=ft.colors.RED_400,
                    on_click=on_delete,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )


class TaskView(ft.Container):
    def __init__(self) -> None:
        super().__init__()
        self.tasks: List[Any] = []
        self.padding = 20
        self.content = self.build_task_view()

    def build_task_view(self) -> Any:
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.TextField(
                            hint_text="Nueva tarea...",
                            expand=True,
                            on_submit=self.add_task,
                        ),
                        ft.IconButton(
                            icon=ft.icons.ADD,
                            on_click=self.add_task,
                        ),
                    ],
                ),
                ft.Column(
                    controls=[
                        TaskListItem(
                            task_data=task,
                            on_status_changed=lambda e: self.toggle_task(task),
                            on_delete=lambda e: self.delete_task(task),
                        )
                        for task in self.tasks
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    spacing=10,
                ),
            ],
            spacing=20,
        )

    def add_task(self, e: Any) -> Any:
        new_task = {
            "title": e.control.value if hasattr(e.control, "value") else "",
            "completed": False,
            "date": datetime.now(),
        }
        if new_task["title"]:
            self.tasks.append(new_task)
            self.content = self.build_task_view()
            self.update()

    def toggle_task(self, task: Any) -> Any:
        task["completed"] = not task["completed"]
        self.content = self.build_task_view()
        self.update()

    def delete_task(self, task: Any) -> Any:
        self.tasks.remove(task)
        self.content = self.build_task_view()
        self.update()


def tasks_page() -> ft.Control:
    return ft.Column(
        controls=[
            TaskView(),
        ],
    )
