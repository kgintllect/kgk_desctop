from dataclasses import dataclass

import PySimpleGUI as sg

from ui.menu import MainMenu

layout = [
    [MainMenu()]
]


@dataclass
class App:
    title: str
    finalize: bool = True

    def __post_init__(self):
        self.window = sg.Window(
            self.title,
            layout,
            self.finalize,
            location=(0, 0),
            size=(1280, 640),
            keep_on_top=True,
        )

    def run(self):
        while True:
            event, values = self.window.read()
            MainMenu.set_events(self.window, event)
            if event in [None, 'Quit']:
                break

        self.window.close()
