import pandas as pd
import matplotlib.pyplot as plt
from database_function import HELPER
import numpy as np
# date|hour|minute|temperature|humidity|pressure



class History:
    def __init__(self):
        self.h=HELPER()
        self.colums=['date','hour','minute','temperature','humidity','pressure']
        self.data=pd.read_csv(self.h.return_DB(),sep='|',names=self.colums,skiprows=[0],header=None)
        self.hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    def select_right_values(self,now,hours_yesterday,values_yesterday):
        """
        :param now: the current hours
        :param hours_yesterday: list with all hours from day before
        :param values_yesterday: list with all measured values for the day before
        :return: list hh, list val ==only the values outside the hours from today(24 hr insgesamt)
        """
        selected_hours=[]
        selected_values=[]
        yesterday_hr_val = dict(zip(hours_yesterday, values_yesterday))
        for hr,val in yesterday_hr_val.items():
            if hr >int(8):
                selected_hours.append(hr)
                selected_values.append(val)

        return selected_hours,selected_values


    def get_values(self,values:str,wished_day:str,yesterday:str,now):
        """
        get the wished values from the csv file
        :param now: the hour now
        :param values: 'temperature','humidity','pressure'
        :param wished_day: which day I want : '2023-01-01'
        :return: return [values,time(0-24hr)] lists
        """
        val_return=self.data.loc[self.data['date']==wished_day][values].values.tolist()
        hr_return=self.data.loc[self.data['date']==wished_day]['hour'].values.tolist()

        val_return_yesterday_all = self.data.loc[self.data['date'] == yesterday][values].values.tolist()
        hr_return_yesterday_all = self.data.loc[self.data['date'] == yesterday]['hour'].values.tolist()
        hr_return_yesterday,val_return_yesterday=self.select_right_values(now,
                                                                          hr_return_yesterday_all,val_return_yesterday_all)
        return val_return_yesterday+val_return,hr_return_yesterday+hr_return






class GraphHistory:
    def __init__(self):
        self.history=History()


    def show_graphic(self,parameter,today):
        """
        visulate the data from the csv file in plot

        :param today: date format "2023-01-01"
        :param parameter: 'temperature','humidity','pressure'
        :return:
        """
        ys,xs=self.history.get_values(parameter,today)
        print(ys,xs)
        plt.clf()
        plt.plot(xs,ys,'bo-')
        plt.xlabel('Hours')
        plt.ylabel('Temperatures')
        plt.title(f"Information for {parameter.capitalize()}")
        for x, y in zip(xs, ys):
            label = "{:.2f}".format(y)

            plt.annotate(label,  # this is the text
                         (x, y),  # these are the coordinates to position the label
                         textcoords="offset points",  # how to position the text
                         xytext=(0, 10),  # distance from text to points (x,y)
                         ha='center')  # horizontal alignment can be left, right or cente
        plt.show()






# if __name__ == "__main__":
#     pass
    # h=Histroy()
    # print(h.get_values('temperature','2023-01-01'))
    # gh=GraphHistory()
    # gh.show_graphic('temperature','2023-01-01')
