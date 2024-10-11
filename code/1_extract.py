import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
states = "https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv"
statenames = pd.read_csv(states)
states.to_csv('cache/states.csv', index=False)


url = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv"
survey = pd.read_csv(url)
survey["year"] = survey["Timestamp"].apply(pl.extract_year_mdy)
survey.to_csv('cache/survey.csv', index=False)

for year in survey["year"].unique():
    url = f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={year}&displayColumn=0"
    col_year = pd.read_html(url)[1]
    col_year["year"] = year
    col_year.to_csv(f"cache/col_{year}.csv", index=False)