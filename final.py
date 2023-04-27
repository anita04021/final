#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:36 2023

@author: anitabaculima
"""
import sqlite3
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import streamlit as st

# create a connection to the database
connection = sqlite3.connect("ecsel_database.db")

# query the "countries" table and store the results in a DataFrame
df_countries = pd.read_sql_query("SELECT * FROM countries", connection)

# close the database connection
connection.close()

# create a dictionary of country acronyms and names
country_dict = dict(zip(df_countries["Acronym"], df_countries["Country"]))

# create a dropdown widget for the user to select a country acronym
dropdown_country = widgets.Dropdown(options=country_dict.keys())

# display the dropdown widget
visual = display(dropdown_country)

# get the selected country acronym from the dropdown and print the corresponding country name
selected_country_acronym = dropdown_country.value
selected_country_name = country_dict[selected_country_acronym]
print(f"The selected country acronym is '{selected_country_acronym}' and the corresponding country name is '{selected_country_name}'.")

st.write(visual)