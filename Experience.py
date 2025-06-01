import pandas as pd

# Load your data
df = pd.read_excel('SORTED_DATA_SET_with_gender.xlsx')

# Split the date range into two columns
df[['Start Date', 'End Date']] = df['linkedinJobDateRange'].str.split(' - ', expand=True)

# Replace 'Present' with today's date
df['End Date'] = df['End Date'].replace('Present', pd.Timestamp.today().strftime('%b %Y'))

# Convert to datetime
df['Start Date'] = pd.to_datetime(df['Start Date'], format='%b %Y')
df['End Date'] = pd.to_datetime(df['End Date'], format='%b %Y')

# Calculate experience in months or years
df['Experience (Months)'] = (df['End Date'].dt.year - df['Start Date'].dt.year) * 12 + (df['End Date'].dt.month - df['Start Date'].dt.month)
df['Experience (Years)'] = df['Experience (Months)'] / 12

# Save or use the dataframe as needed
df.to_excel('output_with_experience.xlsx', index=False)