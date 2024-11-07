import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/vasukhare/Downloads/archive (7)/GlobalWeatherRepository.csv')

print("Missing values per column:")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df['last_updated'] = pd.to_datetime(df['last_updated'])


# def remove_outliers_iqr(data, column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     filtered_data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
#     print(f"Outliers removed in {column}: {len(data) - len(filtered_data)}")
#     return filtered_data

# print("\nDataset shape before outlier removal:", df.shape)
# df = remove_outliers_iqr(df, 'temperature_celsius')
# df = remove_outliers_iqr(df, 'humidity')
# df = remove_outliers_iqr(df, 'precip_mm')
# print("Dataset shape after outlier removal:", df.shape)


df[categorical_cols] = df[categorical_cols].astype('category')

for col in df.select_dtypes(include=['float64']).columns:
    if (df[col] % 1 == 0).all():  
        df[col] = df[col].astype('int64')

df.insert(0, 'id', range(1, len(df) + 1))
print("\nData types after conversion:")
print(df.dtypes)

print("\nCleaned data summary:")

mean_temp_c = df['temperature_celsius'].mean()
max_temp_c = df['temperature_celsius'].max()
min_temp_c = df['temperature_celsius'].min()

mean_humidity = df['humidity'].mean()
max_humidity = df['humidity'].max()
min_humidity = df['humidity'].min()

print(f"\nMean Temperature (°C): {mean_temp_c:.2f}")
print(f"Max Temperature (°C): {max_temp_c:.2f}")
print(f"Min Temperature (°C): {min_temp_c:.2f}")
print(f"Mean Humidity (%): {mean_humidity:.2f}")
print(f"Max Humidity (%): {max_humidity:.2f}")
print(f"Min Humidity (%): {min_humidity:.2f}")

df.to_csv('cleaned_weather_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_weather_data.csv'")

top_5_hottest = df.nlargest(5, 'temperature_celsius')
top_5_coldest = df.nsmallest(5, 'temperature_celsius')

print("\nTop 5 Hottest Locations:")
print(top_5_hottest[['location_name', 'temperature_celsius']])

print("\nTop 5 Coldest Locations:")
print(top_5_coldest[['location_name', 'temperature_celsius']])

region_summary = df.groupby('location_name').agg({
    'temperature_celsius': ['mean', 'max', 'min'],
    'humidity': ['mean', 'max', 'min'],
    'precip_mm': ['mean', 'max', 'min']
}).reset_index()

print("\nLocation Summary:")
print(region_summary)

plt.figure(figsize=(10, 6))
plt.hist(df['temperature_celsius'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Histogram of Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

region = 'New Delhi'  
region_data = df[df['location_name'] == region].sort_values('last_updated')

plt.figure(figsize=(10, 6))
plt.plot(region_data['last_updated'], region_data['temperature_celsius'], marker='o', linestyle='-', color='b')
plt.title(f'Temperature Changes Over Time in {region}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

