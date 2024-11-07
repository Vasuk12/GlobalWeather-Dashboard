import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('/Users/vasukhare/Downloads/archive (7)/GlobalWeatherRepository.csv')

# 1. Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# 2. Handle missing values
# Fill numeric columns with median values
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Fill categorical columns with the most frequent value (mode)
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# 3. Convert date columns to datetime format
df['last_updated'] = pd.to_datetime(df['last_updated'])

# 4. Outlier detection using IQR with shape verification
# def remove_outliers_iqr(data, column):
#     Q1 = data[column].quantile(0.25)
#     Q3 = data[column].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR
#     filtered_data = data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]
#     print(f"Outliers removed in {column}: {len(data) - len(filtered_data)}")
#     return filtered_data

# # Apply outlier removal to specific columns and check shape before and after
# print("\nDataset shape before outlier removal:", df.shape)
# df = remove_outliers_iqr(df, 'temperature_celsius')
# df = remove_outliers_iqr(df, 'humidity')
# df = remove_outliers_iqr(df, 'precip_mm')
# print("Dataset shape after outlier removal:", df.shape)


# 5. Convert columns to appropriate data types
# Convert categorical columns to 'category' dtype
df[categorical_cols] = df[categorical_cols].astype('category')

# Convert numeric columns with only whole numbers to 'int' dtype if no missing values are present
for col in df.select_dtypes(include=['float64']).columns:
    if (df[col] % 1 == 0).all():  # Check if all values are whole numbers
        df[col] = df[col].astype('int64')

# 4. Add ID column starting from 1
df.insert(0, 'id', range(1, len(df) + 1))
# Check the data types after conversion
print("\nData types after conversion:")
print(df.dtypes)

# Display the cleaned dataset summary
print("\nCleaned data summary:")
# print(df.describe())

mean_temp_c = df['temperature_celsius'].mean()
max_temp_c = df['temperature_celsius'].max()
min_temp_c = df['temperature_celsius'].min()

mean_humidity = df['humidity'].mean()
max_humidity = df['humidity'].max()
min_humidity = df['humidity'].min()

# Display specific statistics for temperature and humidity
print(f"\nMean Temperature (°C): {mean_temp_c:.2f}")
print(f"Max Temperature (°C): {max_temp_c:.2f}")
print(f"Min Temperature (°C): {min_temp_c:.2f}")
print(f"Mean Humidity (%): {mean_humidity:.2f}")
print(f"Max Humidity (%): {max_humidity:.2f}")
print(f"Min Humidity (%): {min_humidity:.2f}")

# Save the cleaned data
df.to_csv('cleaned_weather_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_weather_data.csv'")


import matplotlib.pyplot as plt

# Generate a summary based on the global weather dataset
top_5_hottest = df.nlargest(5, 'temperature_celsius')
top_5_coldest = df.nsmallest(5, 'temperature_celsius')

print("\nTop 5 Hottest Locations:")
print(top_5_hottest[['location_name', 'temperature_celsius']])

print("\nTop 5 Coldest Locations:")
print(top_5_coldest[['location_name', 'temperature_celsius']])

# Group the data by region and compute the average, maximum, and minimum temperature
region_summary = df.groupby('location_name').agg({
    'temperature_celsius': ['mean', 'max', 'min'],
    'humidity': ['mean', 'max', 'min'],
    'precip_mm': ['mean', 'max', 'min']
}).reset_index()

print("\nLocation Summary:")
print(region_summary)

# Plot histogram of temperatures
plt.figure(figsize=(10, 6))
plt.hist(df['temperature_celsius'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Histogram of Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot line graph showing changes in temperature over time for a specific region
region = 'New Delhi'  
region_data = df[df['location_name'] == region].sort_values('last_updated')

plt.figure(figsize=(10, 6))
plt.plot(region_data['last_updated'], region_data['temperature_celsius'], marker='o', linestyle='-', color='b')
plt.title(f'Temperature Changes Over Time in {region}')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

