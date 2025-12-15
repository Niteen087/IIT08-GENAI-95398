import streamlit as st
import pandas as pd
import pandasql as ps

st.title("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")  
 
if st.button("Login"):
    if username == "admin" and password == "password":
        st.success("Login successful!")
        
        # upload a CSV file
        data_file = st.file_uploader("Upload a CSV file", type=["csv"])
        # load it as dataframe
        if data_file:
            df = pd.read_csv(data_file)
            # display the dataframe
            st.dataframe(df)
            # SQL query to group by 'job' and sum 'sal'
            query = st.text_input("Enter SQL query:", "SELECT job, SUM(sal) as total FROM data GROUP BY job")
            if st.button("Run Query"):
                result = ps.sqldf(query, {"data": df})
                st.write("Query Result:")
                st.dataframe(result)
    else:
        st.error("Invalid username or password")