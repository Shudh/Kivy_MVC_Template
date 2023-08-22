from View.datascreen import DataScreenView

class DataScreenController:
    """
    The `MyScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    """
    def __init__(self, model):
        self.model = model
        self.view = DataScreenView(controller=self, model=self.model)

    def get_screen(self):
        return self.view

    def set_dates(self, from_date, to_date):
        self.model.from_date = from_date
        self.model.to_date = to_date
