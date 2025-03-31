import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page


    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        #ROW1
        self._ddLingua = ft.Dropdown(label="Select language",
                         options=[ft.dropdown.Option("italian"), ft.dropdown.Option("english"), ft.dropdown.Option("spanish")],
                         on_change=self.__controller.handleVerificaLingua,
                         width=self.page.width)#aggiorna output in base alla scelta

        #ROW2
        self._ddTipoRicerca = ft.Dropdown(label="Search Modality",
                                          options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"), ft.dropdown.Option("Dicotomic")],
                                          on_change=self.__controller.handleVerificaTipoRicerca,
                                          width=200)
        self._txtIn = ft.TextField(label="Add your sentence here", width=460)
        self._btnSpellCheck = ft.ElevatedButton(text="Spell Check",
                                                on_click=self.__controller.handleSpellCheck)
        row2 = ft.Row(controls=[self._ddTipoRicerca, self._txtIn, self._btnSpellCheck],
                      alignment=ft.MainAxisAlignment.CENTER,
                      )

        #ROW3
        self._txtOut = ft.ListView(expand=True, spacing=10)

        self.page.add(self._ddLingua, row2, self._txtOut)

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
