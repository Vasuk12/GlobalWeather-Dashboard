import pandas as pd
from sqlalchemy import create_engine

# Path to the CSV file
csv_file_path = '/Applications/Full Stack Data Science Project/cleaned_weather_data.csv'
# MySQL database details
user = 'root'
password = 'vasu2101'
host = 'localhost'  # MySQL server host
database = 'GlobalWeatherDB'  # Database name
table_name = 'weather_data'  # Table name

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Convert AM/PM formatted time columns to datetime
time_columns = ['sunrise', 'sunset', 'moonrise', 'moonset']  # List of time columns to convert

for col in time_columns:
    # Create a function to safely convert time with error handling
    def convert_time(value):
        try:
            return pd.to_datetime(value, format='%I:%M %p').time()  # Convert to time format
        except (ValueError, TypeError):
            return None  # Return None for invalid entries

    # Apply the conversion function to the column
    df[col] = df[col].apply(convert_time)

df.drop('id', axis=1, inplace=True)  # If 'id' is auto-increment


# Create the MySQL connection string
connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
engine = create_engine(connection_string)

# Load the data into the MySQL table
df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("Data loaded successfully into the 'weather_data' table.")
