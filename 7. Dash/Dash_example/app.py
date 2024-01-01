import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px

# Import the CSV file
df = pd.read_csv('/Users/aamiradeeb/Documents/A231/SQIT5053/W7/Dash_example/data.csv')

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')

# Group by 'Date' and find the mean of 'Total Defect Qty'
df_grouped_day = df.groupby(df['Date'].dt.date)['Total Defect Qty'].mean().reset_index()
df_grouped_day['Date'] = pd.to_datetime(df_grouped_day['Date'])

# Group by 'Month' for Bar Chart
df['Month'] = df['Date'].dt.to_period('M')
df_grouped_month = df.groupby(df['Month'])['Total Defect Qty'].mean().reset_index()
df_grouped_month['Month'] = df_grouped_month['Month'].dt.to_timestamp()

# Group by 'Year' for Pie Chart
df['Year'] = df['Date'].dt.to_period('Y')
df_grouped_year = df.groupby(df['Year'])['Total Defect Qty'].mean().reset_index()
df_grouped_year['Year'] = df_grouped_year['Year'].dt.to_timestamp()

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1('Average Total Defect Qty'),
    html.Div([
        dcc.Dropdown(
            id='chart-type',
            options=[
                {'label': 'Time Series Line Chart', 'value': 'line'},
                {'label': 'Bar Chart', 'value': 'bar'},
                {'label': 'Pie Chart', 'value': 'pie'},
                {'label': 'Heatmap', 'value': 'heatmap'}
            ],
            value='line'
        )
    ]),
    dcc.Graph(id='chart'),
])

# Define callback to update chart
@app.callback(
    Output('chart', 'figure'),
    [Input('chart-type', 'value')]
)
def update_chart(selected_chart):
    if selected_chart == 'line':
        return px.line(df_grouped_day, x='Date', y='Total Defect Qty')
    elif selected_chart == 'bar':
        return px.bar(df_grouped_month, x='Month', y='Total Defect Qty')
    elif selected_chart == 'pie':
        return px.pie(df_grouped_year, names='Year', values='Total Defect Qty')
    elif selected_chart == 'heatmap':
        df_heatmap = df.pivot_table(index=df['Date'].dt.month, columns=df['Date'].dt.year, values='Total Defect Qty', aggfunc='mean')
        return px.imshow(df_heatmap)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
