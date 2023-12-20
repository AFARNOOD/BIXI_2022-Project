{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a638de81",
   "metadata": {},
   "source": [
    "<h1>Exploring the Impact of Climate on BIXI Bike Sharing Trips in Montreal"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc29c9ea",
   "metadata": {},
   "source": [
    "[picture]</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59c95a08",
   "metadata": {},
   "source": [
    "<h2> Introduction"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21f68bd0",
   "metadata": {},
   "source": [
    "BIXI, Montreal's bike-sharing system, is a convenient and sustainable mode of transportation for many residents and visitors. This capstone project aims to analyze the patterns of BIXI bike trips and investigate how climate factors, especially temperature, influence users' decisions in utilizing this service."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b744691",
   "metadata": {},
   "source": [
    "<h2> Objective"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ebad08ac",
   "metadata": {},
   "source": [
    "The primary objective of this project is to understand the relationship between trip duration and climate/weather factors, with a specific focus on temperature. By leveraging machine learning techniques, we aim to uncover insights that can contribute to improving the overall experience and efficiency of BIXI bike sharing."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0f7ebad1",
   "metadata": {},
   "source": [
    "<h2> Methodology"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7309b7de",
   "metadata": {},
   "source": [
    "Machine learning techniques will be employed to analyze and model the relationship between trip duration and climate factors. By training models on the acquired dataset, we aim to uncover patterns and correlations that may not be immediately apparent through traditional analysis methods."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3dcd32d1",
   "metadata": {},
   "source": [
    "<h2> Expected Outcomes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1547f3b9",
   "metadata": {},
   "source": [
    "The project seeks to reveal valuable insights into user behavior and preferences concerning BIXI bike trips under varying climate conditions. The outcome may assist in optimizing the bike-sharing system's operations, promoting usage during favorable weather, and potentially influencing service enhancements."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bfece30d",
   "metadata": {},
   "source": [
    "<h2> Dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "30836530",
   "metadata": {},
   "source": [
    "For this analysis, the dataset used includes all BIXI trips performed throughout the year 2022. This comprehensive dataset provides detailed specifications of each trip, allowing for a thorough examination of user behavior. In addition to BIXI data, climate data for Montreal in 2022 has been incorporated to enhance the analysis by considering temperature variations."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "390d90ac",
   "metadata": {},
   "source": [
    "<h3> Data Collection"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f788c23a",
   "metadata": {},
   "source": [
    "To conduct this analysis, data has been acquired from both the BIXI website, covering the bike-sharing system specifics, and Montreal's climate data to capture the relevant weather conditions. This dual-source approach ensures a comprehensive understanding of how climate factors interact with BIXI bike trips.\n",
    "\n",
    "**1. Climate Data:** weather_data --Daily and hourly weather observations for Montreal - Trudeau Airport (CYUL) in weather_data from Environment and Climate Change Canada (ECCC). I chose the year 2022 data set.\n",
    "\n",
    "Data Source: https://www.canada.ca/en/environment-climate-change.html\n",
    "\n",
    "**2. BIXI Data source:** Bixi bike share open data for each month/year of their season from 2014 to 2023. I chose the year 2022 data set.\n",
    "\n",
    "Data Source: https://bixi.com/en/open-data/"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d790861",
   "metadata": {},
   "source": [
    "<h3> Features Description"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "87de3b5f",
   "metadata": {},
   "source": [
    "**1. Climate Data:**\n",
    "\n",
    "- date: The date corresponding to the weather observations.\n",
    "Data Type: Date/Time\n",
    "\n",
    "- max_temperature:  The highest recorded temperature on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_hourly_temperature: The average temperature calculated based on hourly observations throughout the day.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_temperature The overall average temperature for the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- min_temperature The lowest recorded temperature on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- max_humidex: The highest humidex value, which combines temperature and humidity to represent perceived temperature.\n",
    "Data Type: Float\n",
    "\n",
    "- min_windchill: The lowest wind chill factor, representing the perceived decrease in temperature due to wind.\n",
    "Data Type: Float\n",
    "\n",
    "- max_relative_humidity The highest recorded relative humidity on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_hourly_relative_humidity: The average relative humidity calculated based on hourly observations throughout the day.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_relative_humidity: The overall average relative humidity for the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_cloud_cover_4: The average cloud cover at 4 different levels throughout the day.\n",
    "Data Type: Float\n",
    "\n",
    "- min_cloud_cover_4: The minimum cloud cover at 4 different levels on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- max_cloud_cover_8: The maximum cloud cover at 8 different levels on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_hourly_cloud_cover_8: The average cloud cover at 8 different levels calculated based on hourly observations throughout the day.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_cloud_cover_8: The overall average cloud cover at 8 different levels for the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- min_cloud_cover_8: The minimum cloud cover at 8 different levels on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- max_cloud_cover_10: The maximum cloud cover at 10 different levels on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_hourly_cloud_cover_10: The average cloud cover at 10 different levels calculated based on hourly observations throughout the day.\n",
    "Data Type: Float\n",
    "\n",
    "- avg_cloud_cover_10: The overall average cloud cover at 10 different levels for the given date.\n",
    "Data Type: Float\n",
    "\n",
    "- min_cloud_cover_10: The minimum cloud cover at 10 different levels on the given date.\n",
    "Data Type: Float\n",
    "\n",
    "<br>\n",
    "<br>\n",
    "\n",
    "**2. BIXI Data Source**\n",
    "\n",
    "**- STARTSTATIONNAME:** The name of the station from which the bike trip originated.\n",
    "Data Type: String\n",
    "\n",
    "**- STARTSTATIONARRONDISSEMENT:** The borough or district (arrondissement) where the starting station is located.\n",
    "Data Type: String\n",
    "\n",
    "**- STARTSTATIONLATITUDE:** The latitude coordinates of the starting station's location.\n",
    "Data Type: Float\n",
    "\n",
    "**- STARTSTATIONLONGITUDE:** The longitude coordinates of the starting station's location.\n",
    "Data Type: Float\n",
    "\n",
    "**- ENDSTATIONNAME:** The name of the station where the bike trip concluded.\n",
    "Data Type: String\n",
    "\n",
    "**- ENDSTATIONARRONDISSEMENT:** The borough or district (arrondissement) where the ending station is located.\n",
    "Data Type: String\n",
    "\n",
    "**- ENDSTATIONLATITUDE:** The latitude coordinates of the ending station's location.\n",
    "Data Type: Float\n",
    "\n",
    "**- ENDSTATIONLONGITUDE:** The longitude coordinates of the ending station's location.\n",
    "Data Type: Float\n",
    "\n",
    "**- STARTTIMEMS:** The timestamp indicating the start time of the bike trip, measured in milliseconds since a reference point.\n",
    "Data Type: Integer (Timestamp in milliseconds)\n",
    "\n",
    "**- ENDTIMEMS:** The timestamp indicating the end time of the bike trip, measured in milliseconds since a reference point.\n",
    "Data Type: Integer (Timestamp in milliseconds)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c62a509c",
   "metadata": {},
   "source": [
    "<h2> Tech Stack and concepts"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fae8cd97",
   "metadata": {},
   "source": [
    "\n",
    "* Python\n",
    "* Scikit-learn\n",
    "* XGBoost\n",
    "* Machine Learning Pipeline\n",
    "* FastAPI"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ba13e4b",
   "metadata": {},
   "source": [
    "<h2> Setup"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f375f828",
   "metadata": {},
   "source": [
    "Clone the project repo and open it.\n",
    "\n",
    "If you want to reproduce results by running notebooks or train.py, you need to download data, create a virtual environment and install the dependencies."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ee8e200",
   "metadata": {},
   "source": [
    "<h3> Download Data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ead4a2db",
   "metadata": {},
   "source": [
    "For notebooks:\n",
    "\n",
    "   1. To download data use this notebook or this script\n",
    "   2. When you run notebook be ready that it'll eat memory and take 10-15 minutes of your time\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {
    "height": "414.162px",
    "width": "226.179px"
   },
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
