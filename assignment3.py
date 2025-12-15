import streamlit as st
import pandas as pd
import pandasql as ps

# upload a CSV file
data_file = st.file_uploader("Upload a CSV file", type=["csv"])
# load it as dataframe
if data_file:
    df = pd.read_csv(data_file)
    # display the dataframe
    st.dataframe(df)
    # SQL query to group by 'job' and sum 'sal'
    query =input("Enter sql: ")
    result = ps.sqldf(query, {"data": df})
    print("\nQuery Result:")
    print(result)