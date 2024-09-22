import datetime as dt
import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
from matplotlib import pyplot
from sklearn.neighbors import LocalOutlierFactor

# Path to the dataset. This is specific to the NAB dataset structure. 
# Taken from Kaggle(https://www.kaggle.com/datasets/boltzmannbrain/nab/data)
dirname = "archive/realTraffic/realTraffic/"
filename = "speed_t4013.csv"

# Loading the dataset from the CSV file into a pandas DataFrame
try:
    data = pd.read_csv(dirname + filename)
except FileNotFoundError:
    print(f"File {filename} not found in directory {dirname}")
    exit()
except pd.errors.EmptyDataError:
    print(f"File {filename} is empty or contains no data.")
    exit()

# Quick preview of the data
print(data.head())

# Defining the columns that we will use for timestamp and value
timestamp_col = 'timestamp'
value_col = 'value'

# Validating if required columns are present in the data
if timestamp_col not in data.columns or value_col not in data.columns:
    print(f"Error: Required columns '{timestamp_col}' and/or '{value_col}' are missing.")
    exit()

# Converting the timestamp column to datetime format for proper handling of time series data
# Probably present as String datatype
data[timestamp_col] = pd.to_datetime(data[timestamp_col])

# Visualizing the original data over time
plt.figure(figsize=(10, 6))
plt.plot(data[timestamp_col], data[value_col], label="Value over Time", color='blue')
plt.title('Value over Time')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()

# --- Algorithm Explanation ---
# Local Outlier Factor (LOF) is an unsupervised anomaly detection algorithm that computes the 
# local density deviation of a given data point with respect to its neighbors.
# It is effective in detecting anomalies in time series where we expect most data to follow
# a normal pattern, and anomalies to be rare and deviant.
# LOF works by comparing the local density of a point to its neighbors. If the density of 
# a point is much lower than its neighbors, it is considered an outlier (anomaly).

# We understand that supervised data requires labelled data which is expensive
# Thus unsupervised algorithm is the better alternative

# Applying Local Outlier Factor (LOF) for anomaly detection.
# Parameters: 
# - n_neighbors: Number of neighbors to compare the local density (default: 20).
# - contamination: The expected proportion of anomalies in the dataset (default: 0.05 for 5% anomalies).
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)

# Computing anomaly scores using the LOF algorithm. This returns -1 for anomalies, 1 for normal points.
try:
    data['anomaly_score'] = lof.fit_predict(data[[value_col]])
except ValueError as e:
    print(f"Error in LOF fitting: {e}")
    exit()

# Marking anomalies where LOF assigns -1, indicating a likely anomaly.
data['anomaly'] = data['anomaly_score'] == -1

# Visualizing the anomalies on the time series plot
plt.figure(figsize=(10, 6))
plt.plot(data[timestamp_col], data[value_col], label="Value", color='blue')
plt.scatter(data[timestamp_col][data['anomaly']], 
            data[value_col][data['anomaly']], 
            color='red', label='Anomalies', marker='x')  # Anomalies are marked with red 'x'
plt.title('Anomaly Detection using LOF')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()

# Displaying the detected anomalies (timestamp and value)
anomalies = data[data['anomaly']]
print("Detected Anomalies:")
print(anomalies[[timestamp_col, value_col]])

# --- Statistical Analysis of Detected Anomalies ---
# Calculating statistics on the detected anomalies
num_anomalies = len(anomalies)  # Total number of detected anomalies
total_data_points = len(data)  # Total number of data points
percentage_anomalies = (num_anomalies / total_data_points) * 100  # Percentage of anomalies detected
average_anomaly_value = anomalies[value_col].mean() if num_anomalies > 0 else 0  # Average value of anomalies

# Displaying the statistics
print("Anomaly Detection Statistics:")
print(f"Total Data Points: {total_data_points}")
print(f"Detected Anomalies: {num_anomalies}")
print(f"Percentage of Anomalies: {percentage_anomalies:.2f}%")
print(f"Average Anomaly Value: {average_anomaly_value:.2f}")

# --- Robust Error Handling and Validation ---
# The code includes:
# 1. Error handling for file loading (file not found, empty files).
# 2. Data validation to check if required columns (timestamp and value) are present.
# 3. Exception handling in case the LOF algorithm encounters issues (e.g., insufficient data).

