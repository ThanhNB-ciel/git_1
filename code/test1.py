
# from google.colab import drive
# drive.mount('/content/gdrive')
from clickhouse_driver import Client
import pandas as pd
from datetime import date, timedelta, datetime
import json

clickhouse_info = {
    "host": "192.168.8.97",
    "user": "da_team",
    "password": "Ftech@123"
}
client = Client(host=clickhouse_info['host'], user=clickhouse_info['user'],
                password=clickhouse_info['password'], settings={'use_numpy': True})

for i in range(1):
    time = datetime.strftime(date(2022, 12, 1) + timedelta(i), "%Y%m%d")
    print(time)
    data = client.query_dataframe(f"""
        select   * from ss_match.t_{time}
                            """)
    # print(data.head(5))
    data.to_csv(f"{time}_match.csv")
#where uid = '{user_uid}' and toDate(game_time) between '{start_date}' and '{end_date}