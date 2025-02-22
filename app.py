# Importing libraries
import streamlit as st
import pandas as pd
import os
from io import BytesIO


# Setup our App
st.set_page_config(page_title="📊 Visualizing the Corrected Data", layout='wide')
st.title("Visualizing the Corrected Data")
st.write("🏪 Convert Data into CSV/Excel Format with Data Completion and Visualization")

# File upload
file_upload = st.file_uploader("⬆⬆ Upload File (CSV/EXCEL format):", type=["csv", "xlsx"], accept_multiple_files=True)

if file_upload:
    for file in file_upload:
        ext_file = os.path.splitext(file.name)[-1].lower()  # Corrected: use lower() for the extension check

        if ext_file == ".csv":
            df = pd.read_csv(file)
        elif ext_file == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"🚫File Type Not Supported: {ext_file}")
            continue

        # Display file info
        st.write(f"---File Name---: {file.name}")
        # To get file size, we need to read the content into memory
        file_size = len(file.getvalue()) / 1024  # Size in KB
        st.write(f"---File Size---: {file_size:.2f} KB")  # Display file size in KB

        # Displaying the first few rows of the dataframe
        st.write("📅 Showing the headings of data frame:")
        st.dataframe(df.head())

        # Option for Data Cleaning (to be implemented)
        st.subheader("📅Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicate Values from {file.name}"):
                    df.drop_duplicates(inplace =True)
                    st.write("Duplicates No Longer Exist in Data")

            with col2:
                if st.button(f"🐱‍🐉Fill Missing Values of the file {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Data missing is corrected")


        #Choosing a specific column 
        st.subheader("🎓Choose which columns to select:")
        columns =  st.multiselect(f"Choose Columns for {file.name}", df.columns, default=df.columns)
        df  = df[columns]

        #Create Column Data Visualization
        st.subheader("Visualize Data Graphically")
        if st.checkbox(f"📂 Show the Data of file: {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

        #Convert file from CSV to Excel format
        st.subheader("🏪 Options to Covert file")
        conversion_type = st.radio(f"Converting file: {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(ext_file, ".csv")
                mime_type = "text/csv"
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(ext_file, ".xlsx")
                mime_type = "appliocation/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            #Download Converted file
            st.download_button(
                label =f"Download {file_name} as {conversion_type}", 
                data=buffer,
                file_name=file_name, 
                mime=mime_type
            )
st.success("✌ All data files have been processed!")        




