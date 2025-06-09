import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load dataset from Excel file
excel_path = "Dataset.xlsx"
df = pd.read_excel(excel_path)

if 'Experience (Years)' in df.columns:
    df.rename(columns={'Experience (Years)': 'Experience'}, inplace=True)

app = dash.Dash(__name__)
app.title = "People Analytics Dashboard"

app.layout = html.Div([
    html.H1("People Analytics Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(id="gender-donut"),
        dcc.Graph(id="headcount-gauge"),
        dcc.Graph(id="domain-pie")
    ], style={"display": "flex", "justifyContent": "space-around"}),

    html.Div(id="avg-experience", style={"textAlign": "center", "fontSize": 24, "marginTop": 20}),

    html.Div([
        html.Div([
            html.Img(src="/assets/poster1.jpg", style={"width": "300px", "marginRight": "10px"}),
            html.Img(src="/assets/poster2.jpg", style={"width": "300px", "marginRight": "10px"}),
            html.Img(src="/assets/poster3.jpg", style={"width": "300px"}),
        ], style={"display": "flex", "overflowX": "scroll", "margin": "20px auto"})
    ], style={"textAlign": "center"}),

    html.Div([
        html.Img(src="/assets/logo.png", style={"height": "80px"})
    ], style={"textAlign": "center", "marginBottom": 20}),

    dcc.Graph(id="world-map")
])

@app.callback(
    Output("gender-donut", "figure"),
    Output("headcount-gauge", "figure"),
    Output("domain-pie", "figure"),
    Output("avg-experience", "children"),
    Output("world-map", "figure"),
    Input("gender-donut", "clickData"),
    Input("domain-pie", "clickData"),
    Input("world-map", "clickData"),
    prevent_initial_call=True
)
def update_dashboard(gender_click, domain_click, map_click):
    selected_gender = None
    selected_domain = None
    selected_location = None

    if gender_click and gender_click.get("points"):
        selected_gender = gender_click["points"][0]["label"]

    if domain_click and domain_click.get("points"):
        selected_domain = domain_click["points"][0]["label"]

    if map_click and map_click.get("points"):
        selected_location = map_click["points"][0]["location"]

    dff = df.copy()

    if selected_gender:
        dff = dff[dff["Gender"] == selected_gender]
    if selected_domain:
        dff = dff[dff["Domain"] == selected_domain]
    if selected_location:
        dff = dff[dff["Location"] == selected_location]

    donut = px.pie(dff, names="Gender", hole=0.4, title="Gender Distribution")
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=len(dff),
        title={"text": "Headcount"},
        gauge={"axis": {"range": [0, len(df)]}}
    ))
    pie = px.pie(dff, names="Domain", title="Domain Breakdown")
    avg_exp = f"Average Experience (Years): {dff['Experience'].mean():.2f}" if not dff.empty else "No data for selection"

    map_fig = px.scatter_geo(
        dff,
        locations="Location",
        locationmode="country names",
        title="Geographic Distribution",
        projection="natural earth"
    )

    return donut, gauge, pie, avg_exp, map_fig

if __name__ == '__main__':
    app.run(debug=True)
