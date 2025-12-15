
import streamlit as st
import pandas as pd
import numpy as np
import pandasql as ps

filepath = "emp_hdr.csv"
df = pd.read_csv(filepath)
print("Dataframe Column Types:")
print(df.dtypes)
print("\nEmp Data:")
print(df)
# query = "SELECT * FROM data WHERE sal BETWEEN 1000 AND 2000 ORDER BY sal"
query = "SELECT job, SUM(sal) total FROM data GROUP BY job"
result = ps.sqldf(query, {"data": df})
print("\nQuery Result:")
print(result)