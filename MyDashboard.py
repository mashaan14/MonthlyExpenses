#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:20:27 2021

@author: mashaan
"""


import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import calendar

##############################################################################

# Load data
df_Transactions = pd.read_csv('Transactions.csv', parse_dates=True)
df_Transactions['Date'] = pd.to_datetime(df_Transactions['Date'])
df_Transactions['month'] = pd.DatetimeIndex(df_Transactions['Date']).month

dates = ['4/01/19','5/01/19','6/01/19','7/01/19','8/01/19','9/01/19','10/01/19']

##############################################################################

# Initialize the app
app = dash.Dash(external_stylesheets=[dbc.themes.SPACELAB])
# app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

##############################################################################
df1 = df_Transactions[(df_Transactions['Date'] >= dates[0]) & (df_Transactions['Date'] < dates[1])]
df2 = df_Transactions[(df_Transactions['Date'] >= dates[1]) & (df_Transactions['Date'] < dates[2])]
df3 = df_Transactions[(df_Transactions['Date'] >= dates[2]) & (df_Transactions['Date'] < dates[3])]
df4 = df_Transactions[(df_Transactions['Date'] >= dates[3]) & (df_Transactions['Date'] < dates[4])]
df5 = df_Transactions[(df_Transactions['Date'] >= dates[4]) & (df_Transactions['Date'] < dates[5])]
df6 = df_Transactions[(df_Transactions['Date'] >= dates[5]) & (df_Transactions['Date'] < dates[6])]

df1_title = 'Five months ago'
df2_title = 'Four months ago'
df3_title = 'Three months ago'
df4_title = 'Two months ago'
df5_title = 'A month ago'
df6_title = 'Current month'

df1['Source'] = 'Five months ago'
df2['Source'] = 'Four months ago'
df3['Source'] = 'Three months ago'
df4['Source'] = 'Two months ago'
df5['Source'] = 'A month ago'
df6['Source'] = 'Current month'

df_final = pd.concat([df1,df2,df3,df4,df5,df6])

graph_00=px.bar(df_final, x="Category",y="Amount",color='Source',barmode='group',hover_data=["Date", "Category", "Description", "Amount"])
graph_00.update_layout(template='seaborn',showlegend=True)  
card_graph_00 = dbc.Card(
    dcc.Graph(figure=graph_00,config={'displayModeBar': False}) 
)
##############################################################################
graph_01=px.bar(df_final, x="Amount",y="Source",barmode='group',hover_data=["Date", "Category", "Description", "Amount"])
graph_01.update_layout(template='seaborn',showlegend=True)  
card_graph_01 = dbc.Card(
    dcc.Graph(figure=graph_01,config={'displayModeBar': False}) 
)
##############################################################################
graph_02=px.box(df_final, x="Category",y="Amount",color='Source',points=False)
graph_02.update_layout(template='seaborn',showlegend=True)  
card_graph_02 = dbc.Card(
    dcc.Graph(figure=graph_02,config={'displayModeBar': False}) 
)
##############################################################################
graph_03=px.histogram(df_final, x="Amount",color='Source',marginal="rug",hover_data=["Date", "Category", "Description", "Amount"])
graph_03.update_layout(template='seaborn',showlegend=True,barmode='overlay')  
graph_03.update_traces(opacity=0.75)
card_graph_03 = dbc.Card(
    dcc.Graph(figure=graph_03,config={'displayModeBar': False}) 
)

##############################################################################
            
app.layout = html.Div([
    dbc.Row([dbc.Col(card_graph_00, width=12)]),
    
    dbc.Row([dbc.Col(card_graph_02, width=12)]),
    
    dbc.Row([dbc.Col(card_graph_01, width=12)]),
    
    dbc.Row([dbc.Col(card_graph_03, width=12)]),
        
])

##############################################################################

if __name__ == '__main__':
    app.run_server(debug=False)