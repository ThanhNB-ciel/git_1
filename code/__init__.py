from clickhouse_driver import Client
import pandas as pd
import json 

clickhouse_info = {
"host": "192.168.8.96",
"user": "da_team",
"password": "Ftech@123"
}
client = Client(host=clickhouse_info['host'], user=clickhouse_info['user'],
password=clickhouse_info['password'], settings={'use_numpy': True})


print(client.query_dataframe(f"""
select   uid, game_time, end_time from da_cdp_funzy.partner_game_result limit 100
                     """))


import requests

# requests.get("hee")