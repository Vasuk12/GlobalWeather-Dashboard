import pandas as pd
from sqlalchemy import create_engine

csv_file_path = '/Applications/Full Stack Data Science Project/cleaned_weather_data.csv'

# MySQL database details
user = ''
password = ''
host = ''  # MySQL server host
database = 'GlobalWeatherDB'  # Database name
table_name = 'weather_data'  # Table name


df = pd.read_csv(csv_file_path)

time_columns = ['sunrise', 'sunset', 'moonrise', 'moonset']  

for col in time_columns:
    def convert_time(value):
        try:
            return pd.to_datetime(value, format='%I:%M %p').time()  
        except (ValueError, TypeError):
            return None  
    
    df[col] = df[col].apply(convert_time)

df.drop('id', axis=1, inplace=True)  



connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"
engine = create_engine(connection_string)


df.to_sql(table_name, con=engine, if_exists='append', index=False)

print("Data loaded successfully into the 'weather_data' table.")
