import pandas as pd


class DataReader:
    """
    Class responsible to read data from csv files
    """
    data_files = ['news.csv', 'created_news.csv']

    def read(self):
        data = pd.DataFrame()
        for file in self.data_files:
            if data.empty:
                data = pd.read_csv(file)
            else:
                new_data = pd.read_csv("news.csv")

                if new_data.empty:
                    continue
                data = pd.concat([data, new_data])
        return data


class DataSaver:
    """
    Class resposible for saving data to csv files
    """
    pass