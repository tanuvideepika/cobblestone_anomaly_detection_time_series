# Anomaly Detection in Time Series Data Using Local Outlier Factor (LOF)

This project demonstrates an implementation of **anomaly detection** on time-series data using the **Local Outlier Factor (LOF)** algorithm. The dataset used is part of the **NAB Data Corpus** from Numenta, which includes real-world traffic data and system metrics. The project is designed to detect anomalies in time-series data streams, providing insights into unusual behaviors like system failures or traffic pattern deviations.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Algorithm Used](#algorithm-used)
- [How to Run the Project](#how-to-run-the-project)
- [Results and Statistics](#results-and-statistics)
- [References](#references)

---

## Project Overview
The project aims to detect anomalies in real-time time-series data, with a focus on:
- Identifying anomalies using **Local Outlier Factor (LOF)**.
- Visualizing the time-series data along with detected anomalies.
- Providing statistics on the detected anomalies.

The project also includes robust error handling and documentation to ensure ease of understanding and reproducibility.

## Dataset
The dataset used for this project is the **realTraffic/speed_t4013.csv** from the **NAB Data Corpus** (Numenta Anomaly Benchmark). It contains traffic data collected in real-time from the Twin Cities Metro area in Minnesota, including metrics such as speed and travel time from specific sensors.

### Sample of the Data
```bash
  timestamp,value
2015-09-01 11:25:00,58
2015-09-01 11:30:00,63
2015-09-01 11:35:00,63
2015-09-01 11:40:00,64
2015-09-01 11:55:00,58
```

## Algorithm Used
The **Local Outlier Factor (LOF)** algorithm was used for detecting anomalies. LOF works by measuring the local density of data points and identifying anomalies as those that have a significantly lower density than their neighbors. This makes it suitable for detecting anomalies in time-series data, where outliers often have unique, low-density characteristics.

### Why LOF?
- **Unsupervised**: Does not require labeled training data.
- **Local Density Comparison**: Works well in detecting contextual outliers, which is important for time-series data.
- **Flexibility**: Can adapt to data with concept drift or seasonal variations.

## How to Run the Project

### Clone the Repository
First, clone this repository to your local machine:
```bash
  git clone https://github.com/tanuvideepika/cobblestone_anomaly_detection_time_series.git
  cd cobblestone_anomaly_detection_time_series
```
### Install Dependencies
Make sure to install the required dependencies:
```bash
  pip install -r requirements.txt
```
### Running the Code
You can run the script in VS Code, Jupyter Notebook, or any Python environment. The script loads the dataset, applies the LOF algorithm, and outputs anomaly statistics and visualizations.
```bash
  python main.py
```
### Results and Statistics
After running the script, you will see a graph that visualizes the time-series data with detected anomalies. Red x markers indicate the anomalies. The following statistics will also be printed:

Total number of data points.
Total number of anomalies detected.
Percentage of anomalies.
Average value of anomalies.
Example Output:
```bash
  Anomaly Detection Statistics:
  Total Data Points: 5000
  Detected Anomalies: 250
  Percentage of Anomalies: 5.00%
  Average Anomaly Value: 68.25
```
## References
- **NAB Dataset**: Numenta Anomaly Benchmark (NAB) - [NAB Dataset](https://www.kaggle.com/datasets/boltzmannbrain/nab/data)
- **Local Outlier Factor**: Documentation for Local Outlier Factor in scikit-learn - [scikit-learn LOF](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.LocalOutlierFactor.html)
- **Matplotlib**: Official documentation for the Python plotting library - [Matplotlib](https://matplotlib.org/)
- **Pandas**: Data analysis library for Python - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- **Numpy**: Fundamental package for numerical computing in Python - [NumPy Documentation](https://numpy.org/doc/stable/)

