import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Load enhanced dataset with lat/lon
df = pd.read_excel("Dataset_with_coords.xlsx")

if 'Experience (Years)' in df.columns:
    df.rename(columns={'Experience (Years)': 'Experience'}, inplace=True)

app = dash.Dash(__name__)
app.title = "People Analytics Dashboard"

app.layout = html.Div([
    html.H1("People Analytics Dashboard", style={"textAlign": "center"}),

    dcc.Store(id="filter-store", data={"gender": None, "domain": None, "location": None}),

    html.Button("Reset Filters", id="reset-button", n_clicks=0, style={"margin": "10px auto", "display": "block"}),

    html.Div([
        dcc.Graph(id="gender-donut"),
        dcc.Graph(id="headcount-gauge"),
        dcc.Graph(id="domain-pie")
    ], style={"display": "flex", "justifyContent": "space-around", "flexWrap": "wrap"}),

    html.Div(id="avg-experience", style={"textAlign": "center", "fontSize": 24, "marginTop": 20}),

    html.Div([
        html.Img(src="/assets/logo.png", style={"height": "80px"})
    ], style={"textAlign": "center", "marginBottom": 20}),

    dcc.Graph(id="world-map", style={"height": "600px", "marginTop": 20}),
])

@app.callback(
    Output("filter-store", "data"),
    Input("gender-donut", "clickData"),
    Input("domain-pie", "clickData"),
    Input("world-map", "clickData"),
    Input("reset-button", "n_clicks"),
    State("filter-store", "data"),
    prevent_initial_call=True
)
def update_filter_store(gender_click, domain_click, map_click, reset_clicks, current_filters):
    ctx = dash.callback_context
    if not ctx.triggered:
        return current_filters
    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == "reset-button":
        return {"gender": None, "domain": None, "location": None}

    if gender_click and gender_click.get("points"):
        current_filters["gender"] = gender_click["points"][0]["label"]
    if domain_click and domain_click.get("points"):
        current_filters["domain"] = domain_click["points"][0]["label"]
    if map_click and map_click.get("points"):
        current_filters["location"] = map_click["points"][0]["hovertext"]

    return current_filters

@app.callback(
    Output("gender-donut", "figure"),
    Output("headcount-gauge", "figure"),
    Output("domain-pie", "figure"),
    Output("avg-experience", "children"),
    Output("world-map", "figure"),
    Input("filter-store", "data")
)
def update_dashboard(filters):
    dff = df.copy()
    if filters["gender"]:
        dff = dff[dff["Gender"] == filters["gender"]]
    if filters["domain"]:
        dff = dff[dff["Domain"] == filters["domain"]]
    if filters["location"]:
        dff = dff[dff["Location"] == filters["location"]]

    donut = px.pie(dff, names="Gender", hole=0.4, title="Gender Distribution")
    pie = px.pie(dff, names="Domain", title="Domain Breakdown")
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=len(dff),
        title={"text": "Headcount"},
        gauge={"axis": {"range": [0, len(df)]}}
    ))
    avg_exp = f"Average Experience (Years): {dff['Experience'].mean():.2f}" if not dff.empty else "No data for selection"

    map_fig = px.scatter_geo(
        dff,
        lat='Latitude',
        lon='Longitude',
        text="Location",
        color='Domain',
        title="Geographic Distribution",
        projection="natural earth"
    )
    map_fig.update_traces(marker=dict(size=8, line=dict(width=1, color='white')))

    return donut, gauge, pie, avg_exp, map_fig

if __name__ == '__main__':
    app.run(debug=True)
