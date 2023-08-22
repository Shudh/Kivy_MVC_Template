from kivy.app import App

from Controller.datascreen import DataScreenController
from Controller.myscreen import MyScreenController
from Model.datascreen import DataScreenModel
from Model.myscreen import MyScreenModel


class ShudhMVC(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.model = MyScreenModel()
        # self.controller = MyScreenController(self.model)
        self.model = DataScreenModel()
        self.controller = DataScreenController(self.model)

    def build(self):
        return self.controller.get_screen()


ShudhMVC().run()
