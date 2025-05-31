import pandas as pd
import gender_guesser.detector as gender

# Load your Excel file
df = pd.read_excel('Merged Data\SORTED DATA SET.xlsx')  # Adjust the filename/path if needed
 
# Initialize the gender detector
detector = gender.Detector()

# Assuming the column with names is called 'Name' — change if your column is different
df['Gender'] = df['fullName'].apply(lambda x: detector.get_gender(x.split()[0]))

# Optional: Simplify the result (e.g., male/female only)
def simplify_gender(g):
    if g in ['male', 'mostly_male']:
        return 'Male'
    elif g in ['female', 'mostly_female']:
        return 'Female'
    else:
        return 'Unknown'

df['Gender'] = df['Gender'].apply(simplify_gender)

# Save to a new Excel file
df.to_excel('SORTED_DATA_SET_with_gender.xlsx', index=False)
print("Gender column added and file saved.")
