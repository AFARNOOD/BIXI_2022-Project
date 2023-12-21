#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import necessary libraries
import os
import zipfile
import pandas as pd

from src.config_reader import read_config, parse_data_config
from wwo_hist import retrieve_hist_data

class DataDownloader:
    def __init__(self, data_params: dict = None):
        self.data_params = data_params
        self.get_trips_data()
        self.get_weather_data()

    def get_trips_data(self):
        # ... Your existing code for downloading and processing BIXI data ...

    def get_weather_data(self):
        try:
            os.chdir(self.data_params["wwo_hist_folder"])
            hist_weather_data = retrieve_hist_data(
                self.data_params["api_key"],
                self.data_params["location_list"],
                self.data_params["start_date"],
                self.data_params["end_date"],
                self.data_params["frequency"],
                location_label=False,
                export_csv=True,
                store_df=True
            )
        except Exception as e:
            print(f"Error in get_weather_data: {str(e)}")

if __name__ == "__main__":
  

