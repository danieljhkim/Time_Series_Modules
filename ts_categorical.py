import pandas as pd
import numpy as np

class TimeSeriesCategorical():
    
    def __init__(self, date_indexed_series):
        self.data = date_indexed_series
        self.data['Date'] = pd.to_datetime(self.data.index)
        
    def yearly(self):
        self.data['Year']= self.data['Date'].apply(lambda x: x.year).astype('category')
        grouped_monthly = self.data.groupby('Year').mean()
        return grouped_monthly
    
    def monthly(self):
        self.data['Month']= self.data['Date'].apply(lambda x: x.month).astype('category')
        grouped_monthly = self.data.groupby('Month').mean()
        return grouped_monthly
    
    def mdaily(self):
        self.data['Month_days']= self.data['Date'].apply(lambda x: x.day).astype('category')
        grouped_monthly = self.data.groupby('Month_days').mean()
        return grouped_monthly
    
    def dweekly(self):
        self.data['Week_days']= self.data['Date'].apply(lambda x: x.day_name()).astype('category')
        grouped_monthly = self.data.groupby('Week_days').mean()
        return grouped_monthly
