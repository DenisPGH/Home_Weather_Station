import pandas as pd
# date|hour|minute|temperature|humidity|pressure



class Histroy:
    def __init__(self):
        self.colums=['date','hour','minute','temperature','humidity','pressure']
        self.data=pd.read_csv("wetter_DB.csv",sep='|',names=self.colums,skiprows=[0],header=None)

    def get_values(self,values:str,wished_day):
        """

        :param values: 'temperature','humidity','pressure'
        :param wished_day: which day I want
        :return: return [values,time(0-24hr)]
        """
        val_return=self.data.loc[self.data['date']==wished_day][values]
        hr_return=self.data.loc[self.data['date']==wished_day]['hour']


        return val_return,hr_return



# h=Histroy()
# print(h.get_values('temperature','2023-01-01'))


class GraphHistory:
    def __init__(self):
        pass

    def graphic(self):
        pass
