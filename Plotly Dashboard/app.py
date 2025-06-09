import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load data
excel_path = "Plotly Dashboard/Dataset.xlsx"
df = pd.read_excel(excel_path)

# Rename column for easier access
if 'Experience(Years)' in df.columns:
    df.rename(columns={'Experience(Years)': 'Experience'}, inplace=True)

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "People Analytics Dashboard"

# Define the layout of the app
app.layout = html.Div([
    html.H1("People Analytics Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(id="gender-donut"),
        dcc.Graph(id="headcount-gauge"),
        dcc.Graph(id="domain-pie")
    ], style={"display": "flex", "flexDirection": "row", "justifyContent": "space-around"}),
    
    html.Div(id="avg-experience", style={"textAlign": "center", "fontSize": 24, "marginTop": 20}),
    
    html.Div([
        html.Div([ 
            html.Img(src="/assets/poster1.jpg.jpeg", style={"width": "300px", "marginRight": "10px"}),
            html.Img(src="/assets/poster2.jpg.jpeg", style={"width": "300px", "marginLeft": "10px"}),
            html.Img(src="/assets/poster3.jpg.jpeg", style={"width": "300px"}),
        ], style={"display": "flex", "overflowX": "scroll", "margin": "20px auto"})
    ], style={"textAlign": "center"}),
    
    html.Div([
        html.Img(src="/assets/logo.png", style={"height": "80px"})
    ], style={"textAlign": "center", "margin": 20}),
    
    dcc.Graph(id="world-map")
])

# Callback to update the figures
@app.callback(
    Output("gender-donut", "figure"),
    Output("headcount-gauge", "figure"),
    Output("domain-pie", "figure"),
    Output("avg-experience", "children"),
    Output("world-map", "figure"),
    Input("gender-donut", "clickData"),
    Input("headcount-gauge", "clickData"),
    Input("domain-pie", "clickData"),
    Input("avg-experience", "children"),
    Input("world-map", "clickData")
)
def update_graphs(gender_click, headcount_click, domain_click, avg_exp, world_click):
    gender_fig = px.pie(df, names='Gender', values='Count', title='Gender Distribution')
    headcount_fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=df['Count'].sum(),
        title={"text": "Total Headcount"},
        gauge={"axis": {"range": [None, df['Count'].max()]}}
    ))
    domain_fig = px.pie(df, names='Domain', values='Count', title='Domain Distribution')
    avg_exp_text = f"Average Experience: {df['Experience'].mean():.1f} years"
    world_map_fig = px.choropleth(df, locations="Country", locationmode="country names",
                                  color="Count", hover_name="Country", title="World Map")
    return gender_fig, headcount_fig, domain_fig, avg_exp_text, world_map_fig

if __name__ == '__main__':
    app.run_server(debug=True)