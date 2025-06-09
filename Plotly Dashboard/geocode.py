import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Load locations into DataFrame
locations = [
    "Chicago, Illinois, United States", "Carmel, IN", "Tempe, AZ", "Liérganes", "United States",
    "Düsseldorf", "Atlanta Metropolitan Area", "London", "San Francisco, CA", "Miami, FL",
    "Denver Metropolitan Area", "Las Vegas, NV", "Canada", "Singapore", "Hilversum", "San Diego, CA",
    "Cologne", "Washington, DC", "Greater Stockholm Metropolitan Area", "Champaign, IL", "Brooklyn, NY",
    "Sydney, NSW", "Cupertino, CA", "Greater Seattle Area", "Grand Rapids, MI", "London Area, United Kingdom",
    "Greater Toronto Area, Canada", "Belgrade", "Tampa, FL", "Philadelphia, PA", "Nashville, TN",
    "Europe", "Greater Malmö Metropolitan Area", "Providence, RI", "Richmond, VA", "Munich", "Portland, OR",
    "Austin, Texas Metropolitan Area", "Greater Houston", "Ireland", "New York, NY", "Fort Collins, CO",
    "Zurich", "New York City Metropolitan Area", "Two Rivers, WI", "Seattle, WA", "Vancouver, BC",
    "Pasadena, CA", "Antibes", "Miami-Fort Lauderdale Area", "Escondido, CA", "Cedar Park, TX", "Baton Rouge, LA",
    "Charleston, SC", "Phoenix, AZ", "Cork", "Greater Tokyo Area", "Blacksburg, VA", "San Francisco Bay Area",
    "Berlin", "Gothenburg", "São Paulo, SP", "Nashville Metropolitan Area", "Heidelberg", "Kolkata", "Hyderabad",
    "Minneapolis, MN", "Lisbon", "Toronto, ON", "San Angelo, TX", "Metro Jacksonville", "Irvine, CA", "Cracow",
    "Tracy, CA", "Lumberton, TX", "Falls Church, VA", "Boston, MA", "Greater Melbourne Area", "Denver, CO",
    "Novi, MI", "Middleton, WI", "Bentonville, AR", "Charlotte, NC", "Atlanta, GA", "Los Angeles, CA",
    "Sheboygan, WI", "Batavia, IL", "Los Gatos, CA", "Western Springs, IL", "Roseville, CA", "Wheaton, IL",
    "Des Moines, IA", "Greater Boston", "Washington DC-Baltimore Area", "Mundelein, IL", "San Jose, CA",
    "Saline, MI", "South Delhi", "Westwood, NJ", "Montreal, QC", "Belvidere, IL", "Madrid", "Houston, TX"
]

df = pd.DataFrame(locations, columns=["Location"])

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to handle rate limiting and errors
def get_coordinates(location):
    try:
        loc = geolocator.geocode(location)
        if loc:
            return pd.Series([loc.latitude, loc.longitude])
        else:
            return pd.Series([None, None])
    except GeocoderTimedOut:
        time.sleep(1)
        return get_coordinates(location)

# Apply geocoding
df[['Latitude', 'Longitude']] = df['Location'].apply(get_coordinates)

# Save to Excel
excel_path = "./Plotly Dashboard/Location_with_Coordinates.xlsx"
df.to_excel(excel_path, index=False)

excel_path
