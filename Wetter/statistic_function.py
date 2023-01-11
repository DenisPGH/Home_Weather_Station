import datetime

import pandas as pd
import matplotlib.pyplot as plt
from database_function import  TIME_DATE
import numpy as np
# date|hour|minute|temperature|humidity|pressure
from paths import PATH_DB


class History:
    def __init__(self):
        self.colums=['date','hour','minute','temperature','humidity','pressure']
        self.data=pd.read_csv(PATH_DB, sep='|', names=self.colums, skiprows=[0], header=None)
        self.interval='30min'
    def values_for_a_period(self,values,period):
        """

        :param values: 'temperature','humidity','pressure'
        :param period: how many days int
        :return: list:values, list:hours
        """

        now=datetime.datetime.today()
        start_period=(now-datetime.timedelta(days=period)).strftime('%Y-%m-%d %H:00:00')
        #date_rng = pd.date_range(start_period, now, freq=f'30min').strftime('%Y-%m-%d %H:%M:%S').tolist()
        date_rng = pd.date_range(start_period, now, freq=f'{self.interval}').strftime('%Y-%m-%d %H:%M').tolist()
        hr_return = self.data[self.data['date'].isin(date_rng)]['date'].values.tolist()
        val_return = self.data[self.data['date'].isin(date_rng)][values].values.tolist()
        #print(f" now: {now} , before {start_period}")
        #print(date_rng)
        #return [str(x) for x in val_return], [str(y) for y in hr_return]

        return val_return, hr_return

    def select_right_values(self,now,hours_yesterday,values_yesterday):
        """
        :param now: the current hours
        :param hours_yesterday: list with all hours from day before
        :param values_yesterday: list with all measured values for the day before
        :return: list hh, list val ==only the values outside the hours from today(0-24 hr insgesamt)
        """
        selected_hours=[]
        selected_values=[]
        yesterday_hr_val = dict(zip(hours_yesterday, values_yesterday))
        for hr,val in yesterday_hr_val.items():
            if hr >int(now):
                selected_hours.append(hr)
                selected_values.append(val)


        return selected_hours,selected_values


    def get_values(self,values:str,wished_day:str,yesterday:str,now,period=1):
        """
        get the wished values from the csv file
        :param now: the hour now
        :param values: 'temperature','humidity','pressure'
        :param wished_day: which day I want : '2023-01-01'
        :return: return [values: numbers,time:strings(0-24)] lists
        """

        val_return=self.data.loc[self.data['date']==wished_day][values].values.tolist()
        hr_return=self.data.loc[self.data['date']==wished_day]['hour'].values.tolist()

        val_return_yesterday_all = self.data.loc[self.data['date'] == yesterday][values].values.tolist()
        hr_return_yesterday_all = self.data.loc[self.data['date'] == yesterday]['hour'].values.tolist()
        hr_return_yesterday,val_return_yesterday=self.select_right_values(now,
                                                                          hr_return_yesterday_all,val_return_yesterday_all)

        # res_val=val_return_yesterday+val_return
        # res_hours=[str(x) for x in hr_return_yesterday+hr_return]
        res_val,res_hours=self.values_for_a_period(values,period)

        return res_val,res_hours






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
