import os
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout

from Utility.observer import Observer

# class DataFrameWidget(GridLayout):
#     def __init__(self, df, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = len(df.columns)  # number of columns
#         self.rows = len(df.index) + 1  # number of rows
#         for col_name in df.columns:
#             self.add_widget(Label(text=col_name))
#         for _, row in df.iterrows():
#             for val in row:
#                 self.add_widget(Label(text=str(val)))

class DataFrameWidget(GridLayout):
    rows_per_page = NumericProperty(10)
    current_page = NumericProperty(0)

    def __init__(self, df, **kwargs):
        super().__init__(**kwargs)
        self.df = df
        self.cols = len(df.columns)
        self.update_view()

    def trim_text(self, text, max_length=7):
        if len(text) > max_length:
            return text[:max_length - 3] + "..."
        return text

    def update_view(self):
        self.clear_widgets()
        start_row = self.current_page * self.rows_per_page
        end_row = start_row + self.rows_per_page
        displayed_data = self.df.iloc[start_row:end_row]

        for col_name in self.df.columns:
            self.add_widget(Label(text=col_name))
        for _, row in displayed_data.iterrows():
            for val in row:
                self.add_widget(Label(text=self.trim_text(str(val))))

    def next_page(self):
        if (self.current_page + 1) * self.rows_per_page < len(self.df):
            self.current_page += 1
            self.update_view()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_view()


class DataScreenView(Screen, Observer):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)

    def set_dates(self):
        from_date = self.ids.from_date_input.text
        to_date = self.ids.to_date_input.text
        self.controller.set_dates(from_date, to_date)

    def model_is_changed(self):
        # Display the data in a grid
        # data = self.model._df.head()
        data = self.model._df
        # Create the DataFrameWidget
        df_widget = DataFrameWidget(data)
        # Clear previous widgets and add the new DataFrameWidget
        self.ids.result_grid.clear_widgets()
        self.ids.result_grid.add_widget(df_widget)


Builder.load_file(os.path.join(os.path.dirname(__file__), "datascreen.kv"))
