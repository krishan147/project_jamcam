import json
import pandas as pd
import ast
from bs4 import BeautifulSoup
import re

list_df = []

with open('clearchannel.har', 'r') as f:
    data = f.read()
    parsed = json.loads(data)
    entries = parsed["log"]["entries"][10]["response"]["content"]["text"]
    entries = ast.literal_eval(entries)

    for entry in entries:

        entry_pin = entry["pin"]
        soup = BeautifulSoup(entry_pin, 'html5lib')
        elem = soup.findAll(text=True, )

        latitude = (((elem[0].split(","))[0]).replace("L.marker([", "")).replace(" ", "")
        longitude = (((elem[0].split(","))[1]).replace("]", "")).replace(" ", "")

        panel_id = (elem[2]).replace(" ", "")
        site_id = elem[4]
        adtype = elem[6]
        address = elem[8]
        postcode = elem[10]

        df = pd.DataFrame(data ={
        "latitude":[latitude],
        "longitude":[longitude],
        "adtype":[adtype],
        "address":[address],
        "postcode":[postcode],
        "panel_id":[panel_id],
        "site_id":[site_id]
        })

        list_df.append(df)

df_concat = pd.concat(list_df)

df_concat.to_csv("results.csv")