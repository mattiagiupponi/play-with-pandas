from sqlite_db import DbHook
import pandas as pd

db_connection = DbHook().get_connection()

countries = pd.read_sql_query("select name,continent,population from country", db_connection)

print("QUERY AS DATAFRAME")
print(countries)
print("######")
print("SUM OF POPULATION BY CONTINENT")
print(countries.groupby("continent").sum())
print("######")
print("ORDER BY COUNTRY NAME DESC")
print(countries.sort_values(by="name", ascending=False))
print("######")
print("SUM OF POPULATION BY COUNTRY NAME AND CONTINENT")
print(countries.groupby(["name", "continent"]).sum())

