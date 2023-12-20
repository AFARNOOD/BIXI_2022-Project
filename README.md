# Exploring the Impact of Climate on BIXI Bike Sharing Trips in Montreal


![Alt text](https://github.com/AFARNOOD/BIXI_2022-Project/blob/main/imgs/Picture1.jpg)


## 1. Introduction

BIXI, Montreal's bike-sharing system, is a convenient and sustainable mode of transportation for many residents and visitors. This capstone project aims to analyze the patterns of BIXI bike trips and investigate how climate factors, especially temperature, influence users' decisions in utilizing this service.

## 2. Objective

The primary objective of this project is to understand the relationship between trip duration and climate/weather factors, with a specific focus on temperature. By leveraging machine learning techniques, we aim to uncover insights that can contribute to improving the overall experience and efficiency of BIXI bike sharing.

## 3. Methodology

Machine learning techniques will be employed to analyze and model the relationship between trip duration and climate factors. By training models on the acquired dataset, we aim to uncover patterns and correlations that may not be immediately apparent through traditional analysis methods.

## 4. Expected Outcomes

The project seeks to reveal valuable insights into user behavior and preferences concerning BIXI bike trips under varying climate conditions. The outcome may assist in optimizing the bike-sharing system's operations, promoting usage during favorable weather, and potentially influencing service enhancements.

## 5. Dataset

For this analysis, the dataset used includes all BIXI trips performed throughout the year 2022. This comprehensive dataset provides detailed specifications of each trip, allowing for a thorough examination of user behavior. In addition to BIXI data, climate data for Montreal in 2022 has been incorporated to enhance the analysis by considering temperature variations.

### 5.1. Data Collection

To conduct this analysis, data has been acquired from both the BIXI website, covering the bike-sharing system specifics, and Montreal's climate data to capture the relevant weather conditions. This dual-source approach ensures a comprehensive understanding of how climate factors interact with BIXI bike trips.

**1. Climate Data:** weather_data --Daily and hourly weather observations for Montreal - Trudeau Airport (CYUL) in weather_data from Environment and Climate Change Canada (ECCC). I chose the year 2022 data set.

Data Source: https://www.canada.ca/en/environment-climate-change.html

**2. BIXI Data source:** Bixi bike share open data for each month/year of their season from 2014 to 2023. I chose the year 2022 data set.

Data Source: https://bixi.com/en/open-data/

## 6. Objective

The primary objective of this project is to understand the relationship between trip duration and climate/weather factors, with a specific focus on temperature. By leveraging machine learning techniques, we aim to uncover insights that can contribute to improving the overall experience and efficiency of BIXI bike sharing.

## 7. Methodology

Machine learning techniques will be employed to analyze and model the relationship between trip duration and climate factors. By training models on the acquired dataset, we aim to uncover patterns and correlations that may not be immediately apparent through traditional analysis methods.

## 8. Expected Outcomes

The project seeks to reveal valuable insights into user behavior and preferences concerning BIXI bike trips under varying climate conditions. The outcome may assist in optimizing the bike-sharing system's operations, promoting usage during favorable weather, and potentially influencing service enhancements.

## 9. Dataset

For this analysis, the dataset used includes all BIXI trips performed throughout the year 2022. This comprehensive dataset provides detailed specifications of each trip, allowing for a thorough examination of user behavior. In addition to BIXI data, climate data for Montreal in 2022 has been incorporated to enhance the analysis by considering temperature variations.

### 9.1. Data Collection

To conduct this analysis, data has been acquired from both the BIXI website, covering the bike-sharing system specifics, and Montreal's climate data to capture the relevant weather conditions. This dual-source approach ensures a comprehensive understanding of how climate factors interact with BIXI bike trips.

**1. Climate Data:** weather_data --Daily and hourly weather observations for Montreal - Trudeau Airport (CYUL) in weather_data from Environment and Climate Change Canada (ECCC). I chose the year 2022 data set.

Data Source: https://www.canada.ca/en/environment-climate-change.html

**2. BIXI Data:** Bixi bike share open data for each month/year of their season from 2014 to 2023. I chose the year 2022 data set.

Data Source: https://bixi.com/en/open-data/

### 9.2. Features Description

**1. Climate Data:**

**- date:** The date corresponding to the weather observations.
Data Type: Date/Time
<br> **- max_temperature:**  The highest recorded temperature on the given date.
Data Type: Float
<br> **- avg_hourly_temperature:** The average temperature calculated based on hourly observations throughout the day.
Data Type: Float
<br> **- avg_temperature:** The overall average temperature for the given date.
Data Type: Float
<br> **- min_temperature:** The lowest recorded temperature on the given date.
Data Type: Float
<br> **- max_humidex:** The highest humidex value, which combines temperature and humidity to represent perceived temperature.
Data Type: Float
<br> **- min_windchill:** The lowest wind chill factor, representing the perceived decrease in temperature due to wind.
Data Type: Float
<br> **- max_relative_humidity:** The highest recorded relative humidity on the given date.
Data Type: Float
<br> **- avg_hourly_relative_humidity:** The average relative humidity calculated based on hourly observations throughout the day.
Data Type: Float
<br> **- avg_relative_humidity:** The overall average relative humidity for the given date.
Data Type: Float
<br>**- avg_cloud_cover:** The average cloud cover at 4 different levels throughout the day.
Data Type: Float
<br> **- min_cloud_cover:** The minimum cloud cover at 4 different levels on the given date.
Data Type: Float
<br> **- max_cloud_cover:** The maximum cloud cover at 8 different levels on the given date.
Data Type: Float
<br> **- avg_hourly_cloud_cover:** The average cloud cover at 8 different levels calculated based on hourly observations throughout the day.
Data Type: Float
<br> **- avg_cloud_cover:** The overall average cloud cover at 8 different levels for the given date.
Data Type: Float
<br> **- min_cloud_cover:** The minimum cloud cover at 8 different levels on the given date.
Data Type: Float
<br> **- max_cloud_cover:** The maximum cloud cover at 10 different levels on the given date.
Data Type: Float
<br> **- avg_hourly_cloud_cover:** The average cloud cover at 10 different levels calculated based on hourly observations throughout the day.
Data Type: Float
<br> **- avg_cloud_cover:** The overall average cloud cover at 10 different levels for the given date.
Data Type: Float
<br> **- min_cloud_cover_10:** The minimum cloud cover at 10 different levels on the given date.
Data Type: Float


**2. BIXI Data:**

**- STARTSTATIONNAME:** The name of the station from which the bike trip originated.
Data Type: String
<br> **- STARTSTATIONARRONDISSEMENT:** The borough or district (arrondissement) where the starting station is located.
Data Type: String
<br> **- STARTSTATIONLATITUDE:** The latitude coordinates of the starting station's location.
Data Type: Float
<br> **- STARTSTATIONLONGITUDE:** The longitude coordinates of the starting station's location.
Data Type: Float
<br> **- ENDSTATIONNAME:** The name of the station where the bike trip concluded.
Data Type: String
<br> **- ENDSTATIONARRONDISSEMENT:** The borough or district (arrondissement) where the ending station is located.
Data Type: String
<br> **- ENDSTATIONLATITUDE:** The latitude coordinates of the ending station's location.
Data Type: Float
<br> **- ENDSTATIONLONGITUDE:** The longitude coordinates of the ending station's location.
Data Type: Float
<be> **- STARTTIMEMS:** The timestamp indicating the start time of the bike trip, measured in milliseconds since a reference point.
Data Type: Integer (Timestamp in milliseconds)
<br> **- ENDTIMEMS:** The timestamp indicating the end time of the bike trip, measured in milliseconds since a reference point.
Data Type: Integer (Timestamp in milliseconds)

## 10. Tech Stack and concepts


* Python
* Scikit-learn
* XGBoost
* Machine Learning Pipeline
* FastAPI

## 11. Setup

Clone the project repo and open it.

If you want to reproduce results by running notebooks or train.py, you need to download data, create a virtual environment and install the dependencies.

### 11.1. Download Data

For notebooks:

   1. To download data use this notebook or this script
   2. When you run notebook be ready that it'll eat memory and take 10-15 minutes of your time

