from sqlite_db import create_connection
import pandas as pd
import numpy as np

create_connection()

live_advert = pd.DataFrame(
    {
        "country": ["za", "ao", "uk", "de", "uk", "uk"],
        "ads": [np.nan, 100, 1000, 300, np.nan, 10],
        "bucket": ["other", "alpha", "top", "top", "other", "top"],
    }
)

#  print(live_advert)
#  print(live_advert.groupby("bucket").sum())
#  print(live_advert.sort_values(by="country", ascending=False))

print(live_advert.groupby(["country", "bucket"]).sum())
