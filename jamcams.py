import requests
import pandas as pd

def getData():
    request = requests.get("https://api.tfl.gov.uk/Place/Type/JamCam/").json()
    df = pd.DataFrame(request)
    return df



df = getData()

df.to_csv("test.csv")