
import sqlite3
from copy import copy

from database_function import DataBaseWetter
from paths import PATH_SQLite


class SQLiteSensor:
    def __init__(self):
        self.NAME_DB = PATH_SQLite
        self.NAME_TABLE = "Sensor"
        self.con = sqlite3.connect(self.NAME_DB)
        self.cur = self.con.cursor()
        self.csv_db=DataBaseWetter()


    def drop_table(self):
        """
       delete table in the db
        :return:
        """
        self.cur.execute(f''' DROP TABLE {self.NAME_TABLE}''')
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

    def adding_new__row__into__table(self, date,hh,mm,temp,hum,press):
        """
        create a new row
        :param date:
        :param hh:
        :param mm:
        :param temp:
        :param hum:
        :param pressure:
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
        all=copy(self.csv_db.return_info_db())
        for a in all:
            a_list=a.split("|")
            date=a_list[0]
            hh=a_list[1]
            mm=a_list[2]
            temp=a_list[3]
            hum=a_list[4]
            pres=a_list[5]
            self.adding_new__row__into__table(date,hh,mm,temp,hum,pres.strip())

    def return_info_for_period(self,parameter):
        """
        return the parameter and the times for the specific period
        :param parameter:
        :return:
        """
        self.cur.execute(f"select datetime_,{parameter} from {self.NAME_TABLE}")
        result = self.cur.fetchall()
        print('INFO:')
        for node in result:
            print(node)
        return



if __name__=='__main__':
    db=SQLiteSensor()
    #db.csv__to_sqlite()
    #db.print_all_info_from_table()
    db.return_info_for_period('humidity')
    #db.drop_table()
    #db.create_table()
    # db.adding_new__row__into__table('2022-02-02','18','30',300,200,1000)
    # db.adding_new__row__into__table('2022-02-02','18','30',300,200,1000)
    # db.adding_new__row__into__table('2022-02-02','18','30',300,200,1000)
    # db.print_all_info_from_table()

















