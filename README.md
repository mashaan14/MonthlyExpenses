# Monthly Expenses Analysis using Dash in python

The code in `MyDashboard.py` produces a web page with four plots to analyse the transactions in the csv file `Transactions.csv`.
The transactions dataset was retrieved from Kaggle website, and can be found on this link:
[https://www.kaggle.com/bukolafatunde/personal-finance?select=personal_transactions.csv](https://www.kaggle.com/bukolafatunde/personal-finance?select=personal_transactions.csv)

*note: some records were removed form the original csv file*

## Installation

To run this code, the following packages has to be installed:
```python
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output
```

## Usage

Run the code in Python, then open this address (http://127.0.0.1:8050/) in your browser to play with the web application.


## Output

<p align="center">
  <img width="1200" src=ScreenShot01.png>
</p>

<p align="center">
  <img width="1200" src=ScreenShot02.png>
</p>

## Disclaimer

This code was developed for educational purposes only. It is provided as is with no warranty.
