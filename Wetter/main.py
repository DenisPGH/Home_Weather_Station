from database_function import DataBaseWetter
import datetime

db=DataBaseWetter()
actual_time=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

db.store_new_info([12,34,67],actual_time)