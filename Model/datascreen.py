import pandas as pd

class DataScreenModel:
    standard_date_time_format = '%a %b %d %Y %H:%M:%S'
    def __init__(self):
        self._from_date = None
        self._to_date = None
        self._df = pd.DataFrame()
        self._observers = []

    @property
    def from_date(self):
        return self._from_date

    @property
    def to_date(self):
        return self._to_date

    @from_date.setter
    def from_date(self, value):
        self._from_date = value
        self.load_data()

    @to_date.setter
    def to_date(self, value):
        self._to_date = value
        self.load_data()

    @staticmethod
    def parse_date_to_standard_format(date_str):
        date_str = date_str.split(" GMT")[0]
        return pd.to_datetime(date_str, format=DataScreenModel.standard_date_time_format)

    def load_data(self):
        if self._from_date and self._to_date:
            # Assuming the file path is 'data.csv', adjust accordingly
            self._data_file = 'NIFTY50_20230804150000000 _ 20230727091500000.csv'
            self._df = pd.read_csv(self._data_file)
            self._df['Date'] = self._df['Date'].apply(self.parse_date_to_standard_format)
            self._df.set_index('Date', inplace=True)
            # Filter the dataframe based on the date range
            # 2023-07-28
            self._df = self._df[(self._df.index >= self._from_date) & (self._df.index <= self._to_date)]
            self.notify_observers()

    # ... [Other observer related methods remain the same]

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for x in self._observers:
            x.model_is_changed()
