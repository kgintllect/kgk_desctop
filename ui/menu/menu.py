import PySimpleGUI as sg

from ui.menu.events import menu_events

procurements = [
    ["&Purchase ", ["a_sdf", "b"]],
    "C",
    "d",
    "Close",
]


stores = []

human_resource = []

drill_down = []

planned_maintenance = []


MENU_TITLES = [
    ["Procurement", procurements],
    ["Stores", stores],
    ["Human Resource", human_resource],
    ["Drill Down", drill_down],
    ["Planned Maintenance", planned_maintenance],
]

# MainMenu = sg.Menu(MENU_TITLES)


class MainMenu(sg.Menu):
    event_callbacks = menu_events

    def __init__(self, *args, **kwargs):
        super().__init__(MENU_TITLES, *args, **kwargs)

    @classmethod
    def set_events(cls, window, event):
        if event in cls.event_callbacks:
            cls.event_callbacks[event](window)


