from dataclasses import dataclass
from typing import Callable, Optional, TypeVar, Union

import flet as ft

Control = TypeVar("Control", bound=ft.Control)
ClickEventHandler = Callable[[ft.ControlEvent], None]


@dataclass
class SettingItem:
    """Represents a single setting item with its properties"""

    title: str
    icon: str
    description: Optional[str] = None
    trailing: Optional[Control] = None
    on_click: Optional[ClickEventHandler] = None
