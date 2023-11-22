import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the dataset
url = "/content/day.csv"  # Gantilah link dengan link dataset yang sesuai
bike_data = pd.read_csv(url)

# Inisialisasi aplikasi Dash
app = dash.Dash(__name__)

# Layout dari dashboard
app.layout = html.Div([
    html.H1("Bike Sharing Dashboard"),
    
    # Grafik tren rata-rata sepeda yang disewa per jam
    dcc.Graph(
        id='hourly-trend',
        figure=px.line(bike_data, x='hr', y='cnt', title='Tren Rata-rata Jumlah Sepeda yang Disewa per Jam')
    ),

    # Grafik jumlah total sepeda yang disewa selama peristiwa Hurricane Sandy
    dcc.Graph(
        id='sandy-event',
        figure=px.line(bike_data[(bike_data['dteday'] >= '2012-10-29') & (bike_data['dteday'] <= '2012-10-31')],
                       x='dteday', y='cnt', title='Jumlah Total Sepeda yang Disewa Selama Periode Hurricane Sandy')
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
