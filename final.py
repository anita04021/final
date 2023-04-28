#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:36 2023

@author: anitabaculima
"""
import sqlite3
import pandas as pd
import streamlit as st

# create a connection to the database
connection = sqlite3.connect("ecsel_database.db")

df_countries = pd.read_sql("SELECT * FROM countries", connection)

connection.close()

country_dict = dict(zip(df_countries["Acronym"], df_countries["Country"]))


st.write(df_countries)