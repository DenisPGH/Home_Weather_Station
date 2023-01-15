
import sqlite3
from copy import copy
import datetime

from database_function import DataBaseWetter
from paths import PATH_SQLite


class SQLiteSensor:
    def __init__(self):
        self.NAME_DB = PATH_SQLite
        self.NAME_TABLE = "Sensor"
        self.con = sqlite3.connect(self.NAME_DB)
        self.cur = self.con.cursor()
        self.csv_db=DataBaseWetter()
        self.NAME_TABLE_OUTSIDE='Outside'
        self.NAME_TABLE_CPU='CPU'


    def drop_table(self,table):
        """
       delete table in the db
        :return:
        """
        self.cur.execute(f''' DROP TABLE {table}''')
        self.con.commit()

    def create_table(self):
        """
        table in DB which store each new values
        :return:
        """
        self.cur.execute(f'''CREATE TABLE {self.NAME_TABLE}
                         (id integer primary key,
                          datetime_ DATE, 
                          hh text,
                          mm text, 
                          temperature integer, 
                          humidity integer ,
                           pressure integer )''')
        self.con.commit()

    def print_all_info_from_table(self):
        """
        return all info from the db-node table
        :return: nothing
        """
        self.cur.execute(f"select * from {self.NAME_TABLE}")
        result = self.cur.fetchall()
        print('INFO:')
        for node in result:
            print(node)
        return

    def store_new_info__into__table(self, date:str, hh:str, mm:str, temp:int, hum:int, press:int):
        """
        create a new row
        :param date: str '2023-01-08 01:00'
        :param hh: str
        :param mm: str
        :param temp: int
        :param hum: int
        :param pressure: int
        :return:
        """

        self.cur.execute(f'''INSERT INTO {self.NAME_TABLE} (datetime_ ,hh,mm,temperature,humidity,pressure)
                               VALUES (?,?,?,?,?,?);''',
                         (date,hh,mm,temp,hum,press))
        self.con.commit()

    def close(self):
        """
        close connection to the DB IMPORTANT
        """
        self.con.close()

    def clear_table(self):
        """
        clear the rows into table
        :return:
        """
        self.cur.execute(f"""DELETE FROM {self.NAME_TABLE}""")
        self.con.commit()

    def csv__to_sqlite(self):
        """read csv and store all into table"""
        self.clear_table()
        all=self.csv_db.return_info_db()
        for a in all:
            a_list=a.split("|")
            date=a_list[0]
            hh=a_list[1]
            mm=a_list[2]
            temp=a_list[3]
            hum=a_list[4]
            pres=a_list[5]
            self.store_new_info__into__table(date, hh, mm, temp, hum, pres.strip())

    def return_info_for_period(self,parameter,table,period=1,):
        """
        return the parameter and the times for the specific period
        :param period: how many days int
        :param parameter: 'temperature','humidity','pressure'
        :return: list dates , list values
        """
        now = datetime.datetime.today()
        start_period = (now - datetime.timedelta(days=period)).strftime('%Y-%m-%d %H:00:00')
        # start_period='2023-01-08 01:00:00'
        # end_period='2023-01-08 06:00:00'
        command=f"SELECT datetime_,{parameter} FROM {table}" \
                f" WHERE datetime_ BETWEEN '{start_period}' AND '{now}'"
        self.cur.execute(command)
        result = self.cur.fetchall()
        x,y=[],[]
        for node in result:
            x.append(node[0])
            y.append(node[1])
            # print(node)
        return x,y


    def create_table_outside(self):
        """
        table for storing the value from the temperature outside in DB
        :return:
        """
        self.cur.execute(f'''CREATE TABLE {self.NAME_TABLE_OUTSIDE}
                         (id integer primary key,
                          datetime_ DATE, 
                          temperature_outside integer)''')
        self.con.commit()

    def add_to_table_outside(self, date:str, temp_outside:str,):
        """
        create a new row
        :param date: str '2023-01-08 01:00'
        :param temp: str

        :return:
        """

        self.cur.execute(f'''INSERT INTO {self.NAME_TABLE_OUTSIDE} (datetime_ ,temperature_outside)
                               VALUES (?,?);''',
                         (date,temp_outside,))
        self.con.commit()

    def print_all_info_from_table_outside(self):
        """
        return all info from the table outside
        :return: nothing
        """
        self.cur.execute(f"select * from {self.NAME_TABLE_OUTSIDE}")
        result = self.cur.fetchall()
        print('INFO:')
        for node in result:
            print(node)
        return



if __name__=='__main__':
    db=SQLiteSensor()
    #db.drop_table(db.NAME_TABLE_OUTSIDE)
    #db.create_table_outside()
    db.print_all_info_from_table_outside()
    #db.csv__to_sqlite()
    #db.print_all_info_from_table()
    #a=db.return_info_for_period('humidity',6)
    #print(a)
    #db.drop_table()
    #db.create_table()
    # db.adding_new__row__into__table('2022-02-02','18','30',300,200,1000)
    # db.adding_new__row__into__table('2022-02-02','18','30',300,200,1000)
    # db.adding_new__row__into__table('2022-02-02','18','30',300,200,1000)
    # db.print_all_info_from_table()

















