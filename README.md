<h1>BIXI Project

<font color=green>[picture]</font>

<h2>Table of Contents

<font color=green>[table of content]</font>

<h2> 1. Define the Problem

<font color=green>[define the problem]</font>

<h2> 2. Gather the Data

<font color=green>[text]</font>

<h2> 3. Preparing the Data

<h3> 3.1. Import Libraries

The following code is written in Python 3.7. Below is the list of libraries used.


```python
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sklearn
import itertools
import copy
import csv
import openpyxl

```

<h3> 3.2. Load Data Modeling Libraries

These are the most common machine learning and data visualization libraries.


```python
#Visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Common Model Algorithms
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
#from xgboost import XGBClassifier

#Common Model Helpers
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
from sklearn import metrics
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score
```

<h3> <font color= black>3.3.</font> Data dictionary
    

The data dictionary for the data sets are as follows:

**BIXI rides** 2022 (title in format OD_yyyy-mm)

**Montreal 2018 Temperature** (The climate records come from the Government of Canada website. To simplify the analysis, I will only be using the weather data from the McTavish reservoir station as a proxy for all the weather patterns of the different areas of the island of Montreal.)

Climate data from:

https://www.canada.ca/en/environment-climate-change.html

Bixi data from:

https://bixi.com/en/open-data/

<font color=green>[some tables about the data]</font>
<br> <font color=green>[some tables about the data]</font>

<h3> 3.4 Data Set Restructuring


```python
# read BIXI data set
dfBIXI = pd.read_csv('DonneesOuverte2022.csv')
```


```python
dfBIXI
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STARTSTATIONNAME</th>
      <th>STARTSTATIONARRONDISSEMENT</th>
      <th>STARTSTATIONLATITUDE</th>
      <th>STARTSTATIONLONGITUDE</th>
      <th>ENDSTATIONNAME</th>
      <th>ENDSTATIONARRONDISSEMENT</th>
      <th>ENDSTATIONLATITUDE</th>
      <th>ENDSTATIONLONGITUDE</th>
      <th>STARTTIMEMS</th>
      <th>ENDTIMEMS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St-Urbain / René-Lévesque</td>
      <td>Ville-Marie</td>
      <td>45.507838</td>
      <td>-73.563136</td>
      <td>Mansfield / Ste-Catherine</td>
      <td>Ville-Marie</td>
      <td>45.501399</td>
      <td>-73.571786</td>
      <td>1653343831220</td>
      <td>1.653344e+12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Roy / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.515616</td>
      <td>-73.575808</td>
      <td>Dorion / Rachel</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.531634</td>
      <td>-73.568246</td>
      <td>1653343831410</td>
      <td>1.653345e+12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lajeunesse / Villeray</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.542119</td>
      <td>-73.622547</td>
      <td>Leman / de Chateaubriand</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.547218</td>
      <td>-73.631103</td>
      <td>1653343832935</td>
      <td>1.653344e+12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Parc Plage</td>
      <td>Ville-Marie</td>
      <td>45.502828</td>
      <td>-73.527793</td>
      <td>de la Commune / King</td>
      <td>Ville-Marie</td>
      <td>45.497515</td>
      <td>-73.552571</td>
      <td>1653343837732</td>
      <td>1.653347e+12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Marie-Anne / de la Roche</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527758</td>
      <td>-73.576185</td>
      <td>Métro Laurier (Bibaud / Rivard)</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527839</td>
      <td>-73.589575</td>
      <td>1653343832286</td>
      <td>1.653344e+12</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8967922</th>
      <td>St-Charles / Thomas-Keefer</td>
      <td>Le Sud-Ouest</td>
      <td>45.477605</td>
      <td>-73.573775</td>
      <td>de la Commune / St-Sulpice</td>
      <td>Ville-Marie</td>
      <td>45.504242</td>
      <td>-73.553470</td>
      <td>1661014205935</td>
      <td>1.661016e+12</td>
    </tr>
    <tr>
      <th>8967923</th>
      <td>de Lanaudière / Laurier</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.533314</td>
      <td>-73.583737</td>
      <td>Duluth / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.516876</td>
      <td>-73.579460</td>
      <td>1661014216698</td>
      <td>1.661015e+12</td>
    </tr>
    <tr>
      <th>8967924</th>
      <td>de Bordeaux / Marie-Anne</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.533409</td>
      <td>-73.570657</td>
      <td>Gauthier / Papineau</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.529666</td>
      <td>-73.567336</td>
      <td>1661014214254</td>
      <td>1.661014e+12</td>
    </tr>
    <tr>
      <th>8967925</th>
      <td>Prince-Arthur / du Parc</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.510590</td>
      <td>-73.575470</td>
      <td>Vallières / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.518967</td>
      <td>-73.583616</td>
      <td>1661014213535</td>
      <td>1.661015e+12</td>
    </tr>
    <tr>
      <th>8967926</th>
      <td>U. Concordia - Campus Loyola (Sherbrooke / Wes...</td>
      <td>Côte-des-Neiges - Notre-Dame-de-Grâce</td>
      <td>45.457509</td>
      <td>-73.639485</td>
      <td>Parc de la Confédération (Fielding / West Hill)</td>
      <td>Côte-des-Neiges - Notre-Dame-de-Grâce</td>
      <td>45.471882</td>
      <td>-73.640022</td>
      <td>1661014219848</td>
      <td>1.661015e+12</td>
    </tr>
  </tbody>
</table>
<p>8967927 rows × 10 columns</p>
</div>




```python
# read Temparature data set
dfTEMP = pd.read_csv('Montreal_weather-2022.csv')
```


```python
dfTEMP
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>max_temperature</th>
      <th>avg_hourly_temperature</th>
      <th>avg_temperature</th>
      <th>min_temperature</th>
      <th>max_humidex</th>
      <th>min_windchill</th>
      <th>max_relative_humidity</th>
      <th>avg_hourly_relative_humidity</th>
      <th>avg_relative_humidity</th>
      <th>...</th>
      <th>avg_cloud_cover_4</th>
      <th>min_cloud_cover_4</th>
      <th>max_cloud_cover_8</th>
      <th>avg_hourly_cloud_cover_8</th>
      <th>avg_cloud_cover_8</th>
      <th>min_cloud_cover_8</th>
      <th>max_cloud_cover_10</th>
      <th>avg_hourly_cloud_cover_10</th>
      <th>avg_cloud_cover_10</th>
      <th>min_cloud_cover_10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>12/31/2022</td>
      <td>7.2</td>
      <td>5.94</td>
      <td>5.25</td>
      <td>3.3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>99.6</td>
      <td>98.5</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.3</td>
      <td>6.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12/30/2022</td>
      <td>8.6</td>
      <td>6.32</td>
      <td>6.25</td>
      <td>3.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>96</td>
      <td>86.7</td>
      <td>88.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>12/29/2022</td>
      <td>6.3</td>
      <td>1.17</td>
      <td>0.64</td>
      <td>-5.0</td>
      <td>NaN</td>
      <td>-8.0</td>
      <td>94</td>
      <td>83.1</td>
      <td>80.5</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.8</td>
      <td>6.5</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12/28/2022</td>
      <td>0.0</td>
      <td>-2.04</td>
      <td>-2.00</td>
      <td>-4.0</td>
      <td>NaN</td>
      <td>-10.0</td>
      <td>94</td>
      <td>87.8</td>
      <td>87.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.5</td>
      <td>6.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>12/27/2022</td>
      <td>-3.4</td>
      <td>-6.22</td>
      <td>-6.65</td>
      <td>-9.9</td>
      <td>NaN</td>
      <td>-16.0</td>
      <td>87</td>
      <td>77.1</td>
      <td>77.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.8</td>
      <td>6.5</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>360</th>
      <td>1/5/2022</td>
      <td>2.0</td>
      <td>-3.05</td>
      <td>-2.54</td>
      <td>-7.1</td>
      <td>NaN</td>
      <td>-13.0</td>
      <td>94</td>
      <td>81.7</td>
      <td>84.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.3</td>
      <td>4.5</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>361</th>
      <td>1/4/2022</td>
      <td>-2.9</td>
      <td>-8.36</td>
      <td>-10.30</td>
      <td>-17.7</td>
      <td>NaN</td>
      <td>-25.0</td>
      <td>83</td>
      <td>76.3</td>
      <td>75.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.3</td>
      <td>5.0</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>362</th>
      <td>1/3/2022</td>
      <td>-13.6</td>
      <td>-16.14</td>
      <td>-17.00</td>
      <td>-20.4</td>
      <td>NaN</td>
      <td>-26.0</td>
      <td>83</td>
      <td>72.6</td>
      <td>72.5</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>363</th>
      <td>1/2/2022</td>
      <td>-2.4</td>
      <td>-8.12</td>
      <td>-8.69</td>
      <td>-15.0</td>
      <td>NaN</td>
      <td>-21.0</td>
      <td>89</td>
      <td>78.3</td>
      <td>78.5</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>6.5</td>
      <td>4.0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>364</th>
      <td>1/1/2022</td>
      <td>1.4</td>
      <td>0.28</td>
      <td>-0.55</td>
      <td>-2.5</td>
      <td>NaN</td>
      <td>-8.0</td>
      <td>98</td>
      <td>94.8</td>
      <td>85.0</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>7.8</td>
      <td>6.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>365 rows × 72 columns</p>
</div>



**Organazing BIXI Data**


```python
# Assuming your DataFrame is named df and the "time" column is in milliseconds
# Replace 'your_time_column' with the actual name of your "time" column

# Convert milliseconds to datetime
dfBIXI['datetime'] = pd.to_datetime(dfBIXI['STARTTIMEMS'], unit='ms')

# Extract year, day, and hour into separate columns
dfBIXI['year'] = dfBIXI['datetime'].dt.year
dfBIXI['month'] = dfBIXI['datetime'].dt.month
dfBIXI['day'] = dfBIXI['datetime'].dt.day
dfBIXI['hour'] = dfBIXI['datetime'].dt.hour

# Drop the original "time" and "datetime" columns if needed
dfBIXI = dfBIXI.drop([ 'datetime'], axis=1)

# Display the updated DataFrame
dfBIXI.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STARTSTATIONNAME</th>
      <th>STARTSTATIONARRONDISSEMENT</th>
      <th>STARTSTATIONLATITUDE</th>
      <th>STARTSTATIONLONGITUDE</th>
      <th>ENDSTATIONNAME</th>
      <th>ENDSTATIONARRONDISSEMENT</th>
      <th>ENDSTATIONLATITUDE</th>
      <th>ENDSTATIONLONGITUDE</th>
      <th>STARTTIMEMS</th>
      <th>ENDTIMEMS</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St-Urbain / René-Lévesque</td>
      <td>Ville-Marie</td>
      <td>45.507838</td>
      <td>-73.563136</td>
      <td>Mansfield / Ste-Catherine</td>
      <td>Ville-Marie</td>
      <td>45.501399</td>
      <td>-73.571786</td>
      <td>1653343831220</td>
      <td>1.653344e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Roy / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.515616</td>
      <td>-73.575808</td>
      <td>Dorion / Rachel</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.531634</td>
      <td>-73.568246</td>
      <td>1653343831410</td>
      <td>1.653345e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lajeunesse / Villeray</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.542119</td>
      <td>-73.622547</td>
      <td>Leman / de Chateaubriand</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.547218</td>
      <td>-73.631103</td>
      <td>1653343832935</td>
      <td>1.653344e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Parc Plage</td>
      <td>Ville-Marie</td>
      <td>45.502828</td>
      <td>-73.527793</td>
      <td>de la Commune / King</td>
      <td>Ville-Marie</td>
      <td>45.497515</td>
      <td>-73.552571</td>
      <td>1653343837732</td>
      <td>1.653347e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Marie-Anne / de la Roche</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527758</td>
      <td>-73.576185</td>
      <td>Métro Laurier (Bibaud / Rivard)</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527839</td>
      <td>-73.589575</td>
      <td>1653343832286</td>
      <td>1.653344e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
</div>



**Organasing Montreal Temparature Data**




```python
# Assuming TEMPdf is your DataFrame
# Convert the 'date' column to datetime format
dfTEMP['date'] = pd.to_datetime(dfTEMP['date'], format='%m/%d/%Y')

# Create new columns 'TEMPyear', 'TEMPmonth', 'TEMPday'
dfTEMP['year'] = dfTEMP['date'].dt.year
dfTEMP['month'] = dfTEMP['date'].dt.month
dfTEMP['day'] = dfTEMP['date'].dt.day

# Display the updated DataFrame
dfTEMP.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>max_temperature</th>
      <th>avg_hourly_temperature</th>
      <th>avg_temperature</th>
      <th>min_temperature</th>
      <th>max_humidex</th>
      <th>min_windchill</th>
      <th>max_relative_humidity</th>
      <th>avg_hourly_relative_humidity</th>
      <th>avg_relative_humidity</th>
      <th>...</th>
      <th>avg_hourly_cloud_cover_8</th>
      <th>avg_cloud_cover_8</th>
      <th>min_cloud_cover_8</th>
      <th>max_cloud_cover_10</th>
      <th>avg_hourly_cloud_cover_10</th>
      <th>avg_cloud_cover_10</th>
      <th>min_cloud_cover_10</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2022-12-31</td>
      <td>7.2</td>
      <td>5.94</td>
      <td>5.25</td>
      <td>3.3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>100</td>
      <td>99.6</td>
      <td>98.5</td>
      <td>...</td>
      <td>7.3</td>
      <td>6.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2022-12-30</td>
      <td>8.6</td>
      <td>6.32</td>
      <td>6.25</td>
      <td>3.9</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>96</td>
      <td>86.7</td>
      <td>88.0</td>
      <td>...</td>
      <td>8.0</td>
      <td>8.0</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2022-12-29</td>
      <td>6.3</td>
      <td>1.17</td>
      <td>0.64</td>
      <td>-5.0</td>
      <td>NaN</td>
      <td>-8.0</td>
      <td>94</td>
      <td>83.1</td>
      <td>80.5</td>
      <td>...</td>
      <td>7.8</td>
      <td>6.5</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2022-12-28</td>
      <td>0.0</td>
      <td>-2.04</td>
      <td>-2.00</td>
      <td>-4.0</td>
      <td>NaN</td>
      <td>-10.0</td>
      <td>94</td>
      <td>87.8</td>
      <td>87.0</td>
      <td>...</td>
      <td>7.5</td>
      <td>6.0</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2022-12-27</td>
      <td>-3.4</td>
      <td>-6.22</td>
      <td>-6.65</td>
      <td>-9.9</td>
      <td>NaN</td>
      <td>-16.0</td>
      <td>87</td>
      <td>77.1</td>
      <td>77.0</td>
      <td>...</td>
      <td>7.8</td>
      <td>6.5</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022</td>
      <td>12</td>
      <td>27</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 75 columns</p>
</div>



**Merge Data sets**

Merge the two datasets based on the 'Year', 'Month', and 'Day' columns


```python
# Assuming dfBIXI and dfTEMP are your datasets
# Replace 'TEMPyear', 'TEMPmonth', 'TEMPday' with the actual columns names you want to merge on

# Merge the two datasets on the specified columns
merged_df = pd.merge(dfBIXI, dfTEMP[['year', 'month', 'day', 'avg_temperature', 'avg_wind_speed', 'avg_dew_point', 'rain', 'snow', 'snow_on_ground']], 
                     how='left', on=['year', 'month', 'day'])

# Display the merged DataFrame
print(merged_df.head())
```

                STARTSTATIONNAME                STARTSTATIONARRONDISSEMENT  \
    0  St-Urbain / René-Lévesque                               Ville-Marie   
    1           Roy / St-Laurent                     Le Plateau-Mont-Royal   
    2      Lajeunesse / Villeray  Villeray - Saint-Michel - Parc-Extension   
    3                 Parc Plage                               Ville-Marie   
    4   Marie-Anne / de la Roche                     Le Plateau-Mont-Royal   
    
       STARTSTATIONLATITUDE  STARTSTATIONLONGITUDE  \
    0             45.507838             -73.563136   
    1             45.515616             -73.575808   
    2             45.542119             -73.622547   
    3             45.502828             -73.527793   
    4             45.527758             -73.576185   
    
                        ENDSTATIONNAME                  ENDSTATIONARRONDISSEMENT  \
    0        Mansfield / Ste-Catherine                               Ville-Marie   
    1                  Dorion / Rachel                     Le Plateau-Mont-Royal   
    2         Leman / de Chateaubriand  Villeray - Saint-Michel - Parc-Extension   
    3             de la Commune / King                               Ville-Marie   
    4  Métro Laurier (Bibaud / Rivard)                     Le Plateau-Mont-Royal   
    
       ENDSTATIONLATITUDE  ENDSTATIONLONGITUDE    STARTTIMEMS     ENDTIMEMS  year  \
    0           45.501399           -73.571786  1653343831220  1.653344e+12  2022   
    1           45.531634           -73.568246  1653343831410  1.653345e+12  2022   
    2           45.547218           -73.631103  1653343832935  1.653344e+12  2022   
    3           45.497515           -73.552571  1653343837732  1.653347e+12  2022   
    4           45.527839           -73.589575  1653343832286  1.653344e+12  2022   
    
       month  day  hour  avg_temperature  avg_wind_speed  avg_dew_point  rain  \
    0      5   23    22             11.3            11.5            2.8   0.0   
    1      5   23    22             11.3            11.5            2.8   0.0   
    2      5   23    22             11.3            11.5            2.8   0.0   
    3      5   23    22             11.3            11.5            2.8   0.0   
    4      5   23    22             11.3            11.5            2.8   0.0   
    
       snow  snow_on_ground  
    0   0.0             NaN  
    1   0.0             NaN  
    2   0.0             NaN  
    3   0.0             NaN  
    4   0.0             NaN  
    


```python
merged_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STARTSTATIONNAME</th>
      <th>STARTSTATIONARRONDISSEMENT</th>
      <th>STARTSTATIONLATITUDE</th>
      <th>STARTSTATIONLONGITUDE</th>
      <th>ENDSTATIONNAME</th>
      <th>ENDSTATIONARRONDISSEMENT</th>
      <th>ENDSTATIONLATITUDE</th>
      <th>ENDSTATIONLONGITUDE</th>
      <th>STARTTIMEMS</th>
      <th>ENDTIMEMS</th>
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>avg_temperature</th>
      <th>avg_wind_speed</th>
      <th>avg_dew_point</th>
      <th>rain</th>
      <th>snow</th>
      <th>snow_on_ground</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St-Urbain / René-Lévesque</td>
      <td>Ville-Marie</td>
      <td>45.507838</td>
      <td>-73.563136</td>
      <td>Mansfield / Ste-Catherine</td>
      <td>Ville-Marie</td>
      <td>45.501399</td>
      <td>-73.571786</td>
      <td>1653343831220</td>
      <td>1.653344e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Roy / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.515616</td>
      <td>-73.575808</td>
      <td>Dorion / Rachel</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.531634</td>
      <td>-73.568246</td>
      <td>1653343831410</td>
      <td>1.653345e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lajeunesse / Villeray</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.542119</td>
      <td>-73.622547</td>
      <td>Leman / de Chateaubriand</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.547218</td>
      <td>-73.631103</td>
      <td>1653343832935</td>
      <td>1.653344e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Parc Plage</td>
      <td>Ville-Marie</td>
      <td>45.502828</td>
      <td>-73.527793</td>
      <td>de la Commune / King</td>
      <td>Ville-Marie</td>
      <td>45.497515</td>
      <td>-73.552571</td>
      <td>1653343837732</td>
      <td>1.653347e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Marie-Anne / de la Roche</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527758</td>
      <td>-73.576185</td>
      <td>Métro Laurier (Bibaud / Rivard)</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527839</td>
      <td>-73.589575</td>
      <td>1653343832286</td>
      <td>1.653344e+12</td>
      <td>2022</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
num_rows = merged_df.shape[0]
print(f"The DataFrame has {num_rows} rows.")
```

    The DataFrame has 8967927 rows.
    


```python
df = merged_df
```


```python
# Assuming df is your DataFrame
df['TRIPDURATION'] = (df['ENDTIMEMS'] - df['STARTTIMEMS']) / 1000  # Convert milliseconds to seconds

# Display the updated DataFrame
print(df.head())
```

                STARTSTATIONNAME                STARTSTATIONARRONDISSEMENT  \
    0  St-Urbain / René-Lévesque                               Ville-Marie   
    1           Roy / St-Laurent                     Le Plateau-Mont-Royal   
    2      Lajeunesse / Villeray  Villeray - Saint-Michel - Parc-Extension   
    3                 Parc Plage                               Ville-Marie   
    4   Marie-Anne / de la Roche                     Le Plateau-Mont-Royal   
    
       STARTSTATIONLATITUDE  STARTSTATIONLONGITUDE  \
    0             45.507838             -73.563136   
    1             45.515616             -73.575808   
    2             45.542119             -73.622547   
    3             45.502828             -73.527793   
    4             45.527758             -73.576185   
    
                        ENDSTATIONNAME                  ENDSTATIONARRONDISSEMENT  \
    0        Mansfield / Ste-Catherine                               Ville-Marie   
    1                  Dorion / Rachel                     Le Plateau-Mont-Royal   
    2         Leman / de Chateaubriand  Villeray - Saint-Michel - Parc-Extension   
    3             de la Commune / King                               Ville-Marie   
    4  Métro Laurier (Bibaud / Rivard)                     Le Plateau-Mont-Royal   
    
       ENDSTATIONLATITUDE  ENDSTATIONLONGITUDE    STARTTIMEMS     ENDTIMEMS  ...  \
    0           45.501399           -73.571786  1653343831220  1.653344e+12  ...   
    1           45.531634           -73.568246  1653343831410  1.653345e+12  ...   
    2           45.547218           -73.631103  1653343832935  1.653344e+12  ...   
    3           45.497515           -73.552571  1653343837732  1.653347e+12  ...   
    4           45.527839           -73.589575  1653343832286  1.653344e+12  ...   
    
       month  day  hour  avg_temperature  avg_wind_speed  avg_dew_point  rain  \
    0      5   23    22             11.3            11.5            2.8   0.0   
    1      5   23    22             11.3            11.5            2.8   0.0   
    2      5   23    22             11.3            11.5            2.8   0.0   
    3      5   23    22             11.3            11.5            2.8   0.0   
    4      5   23    22             11.3            11.5            2.8   0.0   
    
       snow  snow_on_ground  TRIPDURATION  
    0   0.0             NaN       382.483  
    1   0.0             NaN      1137.948  
    2   0.0             NaN       268.894  
    3   0.0             NaN      3360.184  
    4   0.0             NaN       308.446  
    
    [5 rows x 21 columns]
    

<h3> <font color= black>3.5.</font> Greet the Data
    <h4> Import the Data


```python
# read data set
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>STARTSTATIONNAME</th>
      <th>STARTSTATIONARRONDISSEMENT</th>
      <th>STARTSTATIONLATITUDE</th>
      <th>STARTSTATIONLONGITUDE</th>
      <th>ENDSTATIONNAME</th>
      <th>ENDSTATIONARRONDISSEMENT</th>
      <th>ENDSTATIONLATITUDE</th>
      <th>ENDSTATIONLONGITUDE</th>
      <th>STARTTIMEMS</th>
      <th>ENDTIMEMS</th>
      <th>...</th>
      <th>month</th>
      <th>day</th>
      <th>hour</th>
      <th>avg_temperature</th>
      <th>avg_wind_speed</th>
      <th>avg_dew_point</th>
      <th>rain</th>
      <th>snow</th>
      <th>snow_on_ground</th>
      <th>TRIPDURATION</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>St-Urbain / René-Lévesque</td>
      <td>Ville-Marie</td>
      <td>45.507838</td>
      <td>-73.563136</td>
      <td>Mansfield / Ste-Catherine</td>
      <td>Ville-Marie</td>
      <td>45.501399</td>
      <td>-73.571786</td>
      <td>1653343831220</td>
      <td>1.653344e+12</td>
      <td>...</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>382.483</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Roy / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.515616</td>
      <td>-73.575808</td>
      <td>Dorion / Rachel</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.531634</td>
      <td>-73.568246</td>
      <td>1653343831410</td>
      <td>1.653345e+12</td>
      <td>...</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1137.948</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Lajeunesse / Villeray</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.542119</td>
      <td>-73.622547</td>
      <td>Leman / de Chateaubriand</td>
      <td>Villeray - Saint-Michel - Parc-Extension</td>
      <td>45.547218</td>
      <td>-73.631103</td>
      <td>1653343832935</td>
      <td>1.653344e+12</td>
      <td>...</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>268.894</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Parc Plage</td>
      <td>Ville-Marie</td>
      <td>45.502828</td>
      <td>-73.527793</td>
      <td>de la Commune / King</td>
      <td>Ville-Marie</td>
      <td>45.497515</td>
      <td>-73.552571</td>
      <td>1653343837732</td>
      <td>1.653347e+12</td>
      <td>...</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>3360.184</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Marie-Anne / de la Roche</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527758</td>
      <td>-73.576185</td>
      <td>Métro Laurier (Bibaud / Rivard)</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.527839</td>
      <td>-73.589575</td>
      <td>1653343832286</td>
      <td>1.653344e+12</td>
      <td>...</td>
      <td>5</td>
      <td>23</td>
      <td>22</td>
      <td>11.3</td>
      <td>11.5</td>
      <td>2.8</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>308.446</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>8967922</th>
      <td>St-Charles / Thomas-Keefer</td>
      <td>Le Sud-Ouest</td>
      <td>45.477605</td>
      <td>-73.573775</td>
      <td>de la Commune / St-Sulpice</td>
      <td>Ville-Marie</td>
      <td>45.504242</td>
      <td>-73.553470</td>
      <td>1661014205935</td>
      <td>1.661016e+12</td>
      <td>...</td>
      <td>8</td>
      <td>20</td>
      <td>16</td>
      <td>24.2</td>
      <td>8.5</td>
      <td>15.6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1829.385</td>
    </tr>
    <tr>
      <th>8967923</th>
      <td>de Lanaudière / Laurier</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.533314</td>
      <td>-73.583737</td>
      <td>Duluth / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.516876</td>
      <td>-73.579460</td>
      <td>1661014216698</td>
      <td>1.661015e+12</td>
      <td>...</td>
      <td>8</td>
      <td>20</td>
      <td>16</td>
      <td>24.2</td>
      <td>8.5</td>
      <td>15.6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>1149.723</td>
    </tr>
    <tr>
      <th>8967924</th>
      <td>de Bordeaux / Marie-Anne</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.533409</td>
      <td>-73.570657</td>
      <td>Gauthier / Papineau</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.529666</td>
      <td>-73.567336</td>
      <td>1661014214254</td>
      <td>1.661014e+12</td>
      <td>...</td>
      <td>8</td>
      <td>20</td>
      <td>16</td>
      <td>24.2</td>
      <td>8.5</td>
      <td>15.6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>178.542</td>
    </tr>
    <tr>
      <th>8967925</th>
      <td>Prince-Arthur / du Parc</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.510590</td>
      <td>-73.575470</td>
      <td>Vallières / St-Laurent</td>
      <td>Le Plateau-Mont-Royal</td>
      <td>45.518967</td>
      <td>-73.583616</td>
      <td>1661014213535</td>
      <td>1.661015e+12</td>
      <td>...</td>
      <td>8</td>
      <td>20</td>
      <td>16</td>
      <td>24.2</td>
      <td>8.5</td>
      <td>15.6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>312.281</td>
    </tr>
    <tr>
      <th>8967926</th>
      <td>U. Concordia - Campus Loyola (Sherbrooke / Wes...</td>
      <td>Côte-des-Neiges - Notre-Dame-de-Grâce</td>
      <td>45.457509</td>
      <td>-73.639485</td>
      <td>Parc de la Confédération (Fielding / West Hill)</td>
      <td>Côte-des-Neiges - Notre-Dame-de-Grâce</td>
      <td>45.471882</td>
      <td>-73.640022</td>
      <td>1661014219848</td>
      <td>1.661015e+12</td>
      <td>...</td>
      <td>8</td>
      <td>20</td>
      <td>16</td>
      <td>24.2</td>
      <td>8.5</td>
      <td>15.6</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>498.504</td>
    </tr>
  </tbody>
</table>
<p>8967927 rows × 21 columns</p>
</div>



**Preview the Data**


```python
# get a peek at the top 5 rows of the data set
print(df.head())
```

                STARTSTATIONNAME                STARTSTATIONARRONDISSEMENT  \
    0  St-Urbain / René-Lévesque                               Ville-Marie   
    1           Roy / St-Laurent                     Le Plateau-Mont-Royal   
    2      Lajeunesse / Villeray  Villeray - Saint-Michel - Parc-Extension   
    3                 Parc Plage                               Ville-Marie   
    4   Marie-Anne / de la Roche                     Le Plateau-Mont-Royal   
    
       STARTSTATIONLATITUDE  STARTSTATIONLONGITUDE  \
    0             45.507838             -73.563136   
    1             45.515616             -73.575808   
    2             45.542119             -73.622547   
    3             45.502828             -73.527793   
    4             45.527758             -73.576185   
    
                        ENDSTATIONNAME                  ENDSTATIONARRONDISSEMENT  \
    0        Mansfield / Ste-Catherine                               Ville-Marie   
    1                  Dorion / Rachel                     Le Plateau-Mont-Royal   
    2         Leman / de Chateaubriand  Villeray - Saint-Michel - Parc-Extension   
    3             de la Commune / King                               Ville-Marie   
    4  Métro Laurier (Bibaud / Rivard)                     Le Plateau-Mont-Royal   
    
       ENDSTATIONLATITUDE  ENDSTATIONLONGITUDE    STARTTIMEMS     ENDTIMEMS  ...  \
    0           45.501399           -73.571786  1653343831220  1.653344e+12  ...   
    1           45.531634           -73.568246  1653343831410  1.653345e+12  ...   
    2           45.547218           -73.631103  1653343832935  1.653344e+12  ...   
    3           45.497515           -73.552571  1653343837732  1.653347e+12  ...   
    4           45.527839           -73.589575  1653343832286  1.653344e+12  ...   
    
       month  day  hour  avg_temperature  avg_wind_speed  avg_dew_point  rain  \
    0      5   23    22             11.3            11.5            2.8   0.0   
    1      5   23    22             11.3            11.5            2.8   0.0   
    2      5   23    22             11.3            11.5            2.8   0.0   
    3      5   23    22             11.3            11.5            2.8   0.0   
    4      5   23    22             11.3            11.5            2.8   0.0   
    
       snow  snow_on_ground  TRIPDURATION  
    0   0.0             NaN       382.483  
    1   0.0             NaN      1137.948  
    2   0.0             NaN       268.894  
    3   0.0             NaN      3360.184  
    4   0.0             NaN       308.446  
    
    [5 rows x 21 columns]
    

**Date column types and count**


```python
# understand the type of each column
print(df.info())
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 8967927 entries, 0 to 8967926
    Data columns (total 21 columns):
     #   Column                      Dtype  
    ---  ------                      -----  
     0   STARTSTATIONNAME            object 
     1   STARTSTATIONARRONDISSEMENT  object 
     2   STARTSTATIONLATITUDE        float64
     3   STARTSTATIONLONGITUDE       float64
     4   ENDSTATIONNAME              object 
     5   ENDSTATIONARRONDISSEMENT    object 
     6   ENDSTATIONLATITUDE          float64
     7   ENDSTATIONLONGITUDE         float64
     8   STARTTIMEMS                 int64  
     9   ENDTIMEMS                   float64
     10  year                        int64  
     11  month                       int64  
     12  day                         int64  
     13  hour                        int64  
     14  avg_temperature             float64
     15  avg_wind_speed              float64
     16  avg_dew_point               float64
     17  rain                        float64
     18  snow                        float64
     19  snow_on_ground              float64
     20  TRIPDURATION                float64
    dtypes: float64(12), int64(5), object(4)
    memory usage: 1.5+ GB
    None
    

**Summarize the central tendency, dispersion and shape**


```python
# get information on the numerical columns for the data set
with pd.option_context('display.max_columns', len(df.columns)):
    print(df.describe(include='all'))
```

                                     STARTSTATIONNAME STARTSTATIONARRONDISSEMENT  \
    count                                     8952910                    8952910   
    unique                                        867                         22   
    top     Métro Mont-Royal (Rivard / du Mont-Royal)      Le Plateau-Mont-Royal   
    freq                                        86315                    3040985   
    mean                                          NaN                        NaN   
    std                                           NaN                        NaN   
    min                                           NaN                        NaN   
    25%                                           NaN                        NaN   
    50%                                           NaN                        NaN   
    75%                                           NaN                        NaN   
    max                                           NaN                        NaN   
    
            STARTSTATIONLATITUDE  STARTSTATIONLONGITUDE  \
    count           8.952910e+06           8.952910e+06   
    unique                   NaN                    NaN   
    top                      NaN                    NaN   
    freq                     NaN                    NaN   
    mean            4.539549e+01          -7.339111e+01   
    std             2.383190e+00           3.718387e+00   
    min            -1.000000e+00          -7.375823e+01   
    25%             4.550367e+01          -7.359322e+01   
    50%             4.552018e+01          -7.357718e+01   
    75%             4.553331e+01          -7.356626e+01   
    max             4.565141e+01          -1.000000e+00   
    
                                       ENDSTATIONNAME ENDSTATIONARRONDISSEMENT  \
    count                                     8907728                  8907728   
    unique                                        867                       22   
    top     Métro Mont-Royal (Rivard / du Mont-Royal)    Le Plateau-Mont-Royal   
    freq                                        72938                  2707105   
    mean                                          NaN                      NaN   
    std                                           NaN                      NaN   
    min                                           NaN                      NaN   
    25%                                           NaN                      NaN   
    50%                                           NaN                      NaN   
    75%                                           NaN                      NaN   
    max                                           NaN                      NaN   
    
            ENDSTATIONLATITUDE  ENDSTATIONLONGITUDE   STARTTIMEMS     ENDTIMEMS  \
    count         8.907728e+06         8.907728e+06  8.967927e+06  8.927404e+06   
    unique                 NaN                  NaN           NaN           NaN   
    top                    NaN                  NaN           NaN           NaN   
    freq                   NaN                  NaN           NaN           NaN   
    mean          4.537697e+01        -7.336199e+01  1.659274e+12  1.659271e+12   
    std           2.550592e+00         3.979576e+00  4.897347e+09  4.896699e+09   
    min          -1.000000e+00        -7.375823e+01  1.647457e+12  1.647457e+12   
    25%           4.550231e+01        -7.359214e+01  1.655167e+12  1.655167e+12   
    50%           4.551941e+01        -7.357602e+01  1.659219e+12  1.659217e+12   
    75%           4.553331e+01        -7.356391e+01  1.663190e+12  1.663189e+12   
    max           4.565141e+01        -1.000000e+00  1.671742e+12  1.688223e+12   
    
                 year         month           day          hour  avg_temperature  \
    count   8967927.0  8.967927e+06  8.967927e+06  8.967927e+06     8.967927e+06   
    unique        NaN           NaN           NaN           NaN              NaN   
    top           NaN           NaN           NaN           NaN              NaN   
    freq          NaN           NaN           NaN           NaN              NaN   
    mean       2022.0  7.490512e+00  1.554420e+01  1.425616e+01     1.725593e+01   
    std           0.0  1.878164e+00  8.948792e+00  7.415318e+00     5.656463e+00   
    min        2022.0  3.000000e+00  1.000000e+00  0.000000e+00    -5.750000e+00   
    25%        2022.0  6.000000e+00  8.000000e+00  1.100000e+01     1.330000e+01   
    50%        2022.0  7.000000e+00  1.500000e+01  1.700000e+01     1.860000e+01   
    75%        2022.0  9.000000e+00  2.300000e+01  2.000000e+01     2.165000e+01   
    max        2022.0  1.200000e+01  3.100000e+01  2.300000e+01     2.735000e+01   
    
            avg_wind_speed  avg_dew_point          rain          snow  \
    count     8.967927e+06   8.967927e+06  8.967927e+06  8.967927e+06   
    unique             NaN            NaN           NaN           NaN   
    top                NaN            NaN           NaN           NaN   
    freq               NaN            NaN           NaN           NaN   
    mean      1.526840e+01   1.032674e+01  2.488377e+00  1.830983e-02   
    std       5.246989e+00   6.454101e+00  6.777994e+00  5.457824e-01   
    min       5.500000e+00  -1.130000e+01  0.000000e+00  0.000000e+00   
    25%       1.150000e+01   6.200000e+00  0.000000e+00  0.000000e+00   
    50%       1.500000e+01   1.180000e+01  0.000000e+00  0.000000e+00   
    75%       1.900000e+01   1.490000e+01  8.000000e-01  0.000000e+00   
    max       3.250000e+01   2.020000e+01  3.960000e+01  1.940000e+01   
    
            snow_on_ground  TRIPDURATION  
    count      25417.00000  8.927404e+06  
    unique             NaN           NaN  
    top                NaN           NaN  
    freq               NaN           NaN  
    mean           1.30098  1.106366e+03  
    std            2.08772  4.535348e+04  
    min            0.00000  2.390000e-01  
    25%            0.00000  3.644170e+02  
    50%            0.00000  6.380750e+02  
    75%            1.00000  1.088062e+03  
    max           21.00000  3.660956e+07  
    

<h2> 4. Data Cleaning

The data is cleaned in 2 steps:
1. Correcting outliers
2. Completing null or missing data

<h3> 4.1. Correcting outliers

There aren't any noticable outliers.

<h3>4.2. Completing null or missing data

The columns containing null values need to be identified.
<br>**Training data**


```python
# find number of null values in each column
print('Number of null values per column:\n', df.isnull().sum())
```

    Number of null values per column:
     STARTSTATIONNAME                15017
    STARTSTATIONARRONDISSEMENT      15017
    STARTSTATIONLATITUDE            15017
    STARTSTATIONLONGITUDE           15017
    ENDSTATIONNAME                  60199
    ENDSTATIONARRONDISSEMENT        60199
    ENDSTATIONLATITUDE              60199
    ENDSTATIONLONGITUDE             60199
    STARTTIMEMS                         0
    ENDTIMEMS                       40523
    year                                0
    month                               0
    day                                 0
    hour                                0
    avg_temperature                     0
    avg_wind_speed                      0
    avg_dew_point                       0
    rain                                0
    snow                                0
    snow_on_ground                8942510
    TRIPDURATION                    40523
    dtype: int64
    

**Dropping Rows or Columns:**
<br> There aren null values. so I choose to drop rows or columns containing null values:


```python

```


```python
# find number of null values in each column
print('Number of null values per column:\n', df.isnull().sum())
```

    Number of null values per column:
     STARTSTATIONNAME                15017
    STARTSTATIONARRONDISSEMENT      15017
    STARTSTATIONLATITUDE            15017
    STARTSTATIONLONGITUDE           15017
    ENDSTATIONNAME                  60199
    ENDSTATIONARRONDISSEMENT        60199
    ENDSTATIONLATITUDE              60199
    ENDSTATIONLONGITUDE             60199
    STARTTIMEMS                         0
    ENDTIMEMS                       40523
    year                                0
    month                               0
    day                                 0
    hour                                0
    avg_temperature                     0
    avg_wind_speed                      0
    avg_dew_point                       0
    rain                                0
    snow                                0
    snow_on_ground                8942510
    TRIPDURATION                    40523
    dtype: int64
    

<h3>4.3. Normalizing Data

Let's start by looking at the skewness of each column to determine which ones need to be normalized.


```python
# find which columns need to be normalized

print('STARTSTATIONLATITUDE skewness: ', df.STARTSTATIONLATITUDE.skew())
print('STARTSTATIONLONGITUDE skewness ', df.STARTSTATIONLONGITUDE.skew())
print('ENDSTATIONLATITUDE skewness: ', df.ENDSTATIONLATITUDE.skew())
print('ENDSTATIONLONGITUDE skewness: ', df.ENDSTATIONLONGITUDE.skew())
print('STARTTIMEMS skewness: ', df.STARTTIMEMS.skew())
print('ENDTIMEMS skewness: ', df.ENDTIMEMS.skew())
print('avg_temperature skewness: ', df.avg_temperature.skew())
print('avg_wind_speed skewness: ', df.avg_wind_speed.skew())
print('avg_dew_point skewness: ', df.avg_dew_point.skew())
print('rain skewness: ', df.rain.skew())
print('avg_dew_point skewness: ', df.avg_dew_point.skew())
print('TRIPDURATION skewness: ', df.TRIPDURATION.skew())
```

    STARTSTATIONLATITUDE skewness:  -19.414318305070072
    STARTSTATIONLONGITUDE skewness  19.416157670057096
    ENDSTATIONLATITUDE skewness:  -18.12603074435913
    ENDSTATIONLONGITUDE skewness:  18.127583015530444
    STARTTIMEMS skewness:  0.040776290965860496
    ENDTIMEMS skewness:  0.04242292711139503
    avg_temperature skewness:  -0.6238090896651064
    avg_wind_speed skewness:  0.49574795470276817
    avg_dew_point skewness:  -0.8177896582826159
    rain skewness:  3.7598777163958363
    avg_dew_point skewness:  -0.8177896582826159
    TRIPDURATION skewness:  402.29321514009956
    

<br>Based on the skewness values, it appears that some of the columns have significant skewness. Skewness measures the asymmetry of a distribution. Here are some general recommendations based on the skewness values:

**4.3.1. High Positive Skewness (> 1):**
<br>For columns with high positive skewness (e.g., 'TRIPDURATION'), consider applying a transformation such as the logarithm to reduce the impact of extreme values.


```python
import numpy as np

# Assuming df is your DataFrame
df['STARTSTATIONLONGITUDE_log'] = np.log1p(df['STARTSTATIONLONGITUDE'])
df['ENDSTATIONLONGITUDE_log'] = np.log1p(df['ENDSTATIONLONGITUDE'])
df['STARTTIMEMS_log'] = np.log1p(df['STARTTIMEMS'])
df['ENDTIMEMS_log'] = np.log1p(df['ENDTIMEMS'])
df['avg_dew_point_log'] = np.log1p(df['avg_dew_point'])
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION'])
```

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\arraylike.py:358: RuntimeWarning: divide by zero encountered in log1p
      result = getattr(ufunc, method)(*inputs, **kwargs)
    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\arraylike.py:358: RuntimeWarning: invalid value encountered in log1p
      result = getattr(ufunc, method)(*inputs, **kwargs)
    


```python
print('STARTSTATIONLONGITUDE_log skewness', df.TRIPDURATION_log.skew())
print('ENDSTATIONLONGITUDE_log skewness', df.TRIPDURATION_log.skew())
print('STARTTIMEMS_log skewness', df.TRIPDURATION_log.skew())
print('ENDTIMEMS_log skewness', df.TRIPDURATION_log.skew())
print('avg_dew_point_log skewness', df.TRIPDURATION_log.skew())
print('TRIPDURATION_log skewness', df.TRIPDURATION_log.skew())
```

    STARTSTATIONLONGITUDE_log skewness -0.6082987689819698
    ENDSTATIONLONGITUDE_log skewness -0.6082987689819698
    STARTTIMEMS_log skewness -0.6082987689819698
    ENDTIMEMS_log skewness -0.6082987689819698
    avg_dew_point_log skewness -0.6082987689819698
    TRIPDURATION_log skewness -0.6082987689819698
    

**4.3.2. High Negative Skewness (< -1):**

For columns with high negative skewness (e.g., 'avg_wind_speed'), consider applying a transformation such as the square root to make the distribution more symmetric.


```python
# Assuming df is your DataFrame

df['STARTSTATIONLATITUDE_sqrt'] = np.sqrt(df['STARTSTATIONLATITUDE'])
df['ENDSTATIONLATITUDE_sqrt'] = np.sqrt(df['ENDSTATIONLATITUDE'])

```

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\arraylike.py:358: RuntimeWarning: invalid value encountered in sqrt
      result = getattr(ufunc, method)(*inputs, **kwargs)
    


```python
print('STARTSTATIONLATITUDE_sqrt skewness', df.STARTSTATIONLATITUDE_sqrt.skew())
print('ENDSTATIONLATITUDE_sqrt skewness', df.ENDSTATIONLATITUDE_sqrt.skew())

```

    STARTSTATIONLATITUDE_sqrt skewness -0.389345432915166
    ENDSTATIONLATITUDE_sqrt skewness -0.3324706108373027
    


```python

```


```python

```


```python

```


```python

```


```python


```


```python

```

<h2> 5. Data Exploration

Let's look at the distribution for each column based on the number of rides.


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame and 'STARTTIMEMS' is the column containing the start time of rides
# Convert milliseconds to datetime
df['STARTTIMEDT'] = pd.to_datetime(df['STARTTIMEMS'], unit='ms')

# Extract month from datetime
df['month'] = df['STARTTIMEDT'].dt.month

# Count the number of rides for each month
ride_counts = df['month'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=ride_counts.index, y=ride_counts.values, color='skyblue')
plt.title('Distribution of BIXI Rides by Month')
plt.xlabel('Month')
plt.ylabel('Number of Rides')
plt.show()
```


    
![png](output_74_0.png)
    



```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame and 'STARTTIMEMS' is the column containing the start time of rides
# Convert milliseconds to datetime
df['STARTTIMEDT'] = pd.to_datetime(df['STARTTIMEMS'], unit='ms')

# Extract month from datetime
df['month'] = df['STARTTIMEDT'].dt.month

# Count the number of rides for each month
ride_counts = df['month'].value_counts().sort_index()

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(ride_counts.to_frame().T, cmap='Blues', annot=True, fmt='d', cbar_kws={'label': 'Number of Rides'})
plt.title('Distribution of BIXI Rides by Month')
plt.xlabel('Month')
plt.ylabel('Number of Rides')
plt.xticks(ticks=range(0, 12), labels=[str(i) for i in range(1, 13)])
plt.yticks(rotation=0)
plt.show()

```


    
![png](output_75_0.png)
    



```python
print('month:\n', df.month.value_counts(sort=False))
```

    month:
     3           5
    4      342981
    5     1278593
    6     1385291
    7     1534730
    8     1504159
    9     1352126
    10    1118271
    11     451764
    12          7
    Name: month, dtype: int64
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame and 'STARTTIMEMS' is the column containing the start time of rides
# Convert milliseconds to datetime
df['STARTTIMEDT'] = pd.to_datetime(df['STARTTIMEMS'], unit='ms')

# Extract month from datetime
df['month'] = df['STARTTIMEDT'].dt.month

# Count the number of rides for each month
ride_counts = df['month'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=ride_counts.index, y=ride_counts.values, color='skyblue')
plt.title('Distribution of BIXI Rides by Month')
plt.xlabel('Month')
plt.ylabel('Number of Rides')
plt.xticks(ticks=range(1, 13), labels=[str(i) for i in range(1, 13)])
plt.show()

```


    
![png](output_77_0.png)
    



```python
print('day:\n', df.day.value_counts(sort=False))
```

    day:
     1     308147
    2     307373
    3     323122
    4     314783
    5     313761
    6     312522
    7     309537
    8     284490
    9     274085
    10    311699
    11    324172
    12    289074
    13    283450
    14    321807
    15    332362
    16    276009
    17    274970
    18    229537
    19    239413
    20    280284
    21    273634
    22    289040
    23    264207
    24    290240
    25    302646
    26    289243
    27    254177
    28    298057
    29    311635
    30    307682
    31    176769
    Name: day, dtype: int64
    


```python
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'day' is the column you want to visualize
day_counts = df['day'].value_counts(sort=False)

# Plotting
plt.figure(figsize=(10, 6))
day_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of BIXI Rides by Day')
plt.xlabel('Day')
plt.ylabel('Number of Rides')
plt.show()

```


    
![png](output_79_0.png)
    



```python
print('hour:\n', df.hour.value_counts(sort=False))
```

    hour:
     0     492375
    1     403128
    2     348584
    3     291502
    4     204815
    5     143172
    6     101018
    7      80826
    8      39020
    9      38739
    10     93191
    11    252582
    12    455746
    13    338841
    14    319413
    15    394142
    16    479101
    17    496790
    18    514920
    19    580439
    20    706606
    21    849925
    22    741224
    23    601828
    Name: hour, dtype: int64
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame and 'STARTTIMEMS' is the column containing the start time of rides
# Convert milliseconds to datetime
df['STARTTIMEDT'] = pd.to_datetime(df['STARTTIMEMS'], unit='ms')

# Extract hour from datetime
df['hour'] = df['STARTTIMEDT'].dt.hour

# Count the number of rides for each hour
hourly_ride_counts = df['hour'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(x=hourly_ride_counts.index, y=hourly_ride_counts.values, color='skyblue')
plt.title('Distribution of BIXI Rides by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Rides')
plt.xticks(rotation=45)
plt.show()

```


    
![png](output_81_0.png)
    



```python
print('Temp (°C):\n', df.avg_temperature.value_counts())
```

    Temp (°C):
      19.14    190816
     20.85    164508
     20.05    153979
     20.39    148416
     19.10    136544
               ...  
     9.15       3031
    -3.90          6
     0.89          5
     6.85          2
    -5.75          1
    Name: avg_temperature, Length: 178, dtype: int64
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame
# Set the size of the temperature bins based on your data distribution
temp_bins = pd.cut(df['avg_temperature'], bins=range(-10, 40, 5), right=False)

# Create a DataFrame with the counts for each temperature bin
temp_counts = pd.crosstab(index=temp_bins, columns='count')

# Create a heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(temp_counts.T, cmap='YlGnBu', annot=True, fmt='d', cbar_kws={'label': 'Number of Rides'})
plt.title('Distribution of BIXI Rides by Average Temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Number of Rides')
plt.xticks(rotation=45)
plt.show()

```


    
![png](output_83_0.png)
    



```python
print('start_station_code:\n', df.ENDSTATIONNAME.value_counts())
```

    start_station_code:
     Métro Mont-Royal (Rivard / du Mont-Royal)          72938
    de la Commune / Place Jacques-Cartier              65913
    Marquette / du Mont-Royal                          55967
    de la Commune / St-Sulpice                         52200
    du Mont-Royal / Clark                              49583
                                                       ...  
    Grenet / Poirier                                       8
    Quentin Gouvier (Duluth  / St-Denis)                   8
    Square Nelligan (des Appalaches / Alexis-Nihon)        6
    Gare Lachine (Sir George Simpson / 48e avenue)         3
    Dixie / 53e avenue                                     2
    Name: ENDSTATIONNAME, Length: 867, dtype: int64
    


```python

```


```python
print('duration_sec:\n', df.TRIPDURATION.value_counts())
```

    duration_sec:
     385.607     26
    447.114     26
    369.707     24
    313.735     24
    580.941     24
                ..
    4994.008     1
    2248.483     1
    5570.518     1
    2160.246     1
    2873.591     1
    Name: TRIPDURATION, Length: 2302474, dtype: int64
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='avg_temperature', y='TRIPDURATION', hue='avg_temperature', size='avg_temperature', palette='viridis', sizes=(20, 200))
plt.title('Scatterplot of TRIPDURATION vs. avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Trip Duration (seconds)')
plt.legend(title='Average Temperature (°C)', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()

```


    
![png](output_87_0.png)
    



```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='avg_temperature', y='TRIPDURATION_minutes', hue='avg_temperature', size='avg_temperature', palette='viridis', sizes=(20, 200))
plt.title('Scatterplot of TRIPDURATION vs. avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Trip Duration (minutes)')
plt.legend(title='Average Temperature (°C)', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()

```


    
![png](output_88_0.png)
    


<h2> 6. Feature Engineering


```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60

# Create a new column with log-transformed trip duration
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION_minutes'])

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='avg_temperature', y='TRIPDURATION_log', hue='avg_temperature', size='avg_temperature', palette='viridis', sizes=(20, 200))
plt.title('Scatterplot of log(TRIPDURATION) vs. avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Log(Trip Duration) (minutes)')
plt.legend(title='Average Temperature (°C)', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()

```


    
![png](output_90_0.png)
    



```python
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60

# Create a new column with log-transformed trip duration
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION_minutes'])

plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='avg_temperature', y='TRIPDURATION_log', hue='avg_temperature', palette='viridis', s=100, alpha=0.7)
plt.title('Comparison of log(TRIPDURATION) and avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Log(Trip Duration) (minutes)')
plt.legend(title='Average Temperature (°C)', bbox_to_anchor=(1, 1), loc='upper left')
plt.show()

```


    
![png](output_91_0.png)
    



```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60

# Create a new column with log-transformed trip duration
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION_minutes'])

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Create a scatterplot-like heatmap
sns.scatterplot(data=df, x='avg_temperature', y='TRIPDURATION_log', hue='TRIPDURATION_minutes', palette='viridis', size='TRIPDURATION_minutes', sizes=(20, 200))

# Set the title and labels
plt.title('Scatterplot-like Heatmap of TRIPDURATION_log and avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Log(Trip Duration) (minutes)')

# Show the colorbar
plt.colorbar(label='Trip Duration (minutes)')

# Show the plot
plt.show()

```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-57-70066c53ce58> in <module>
         23 
         24 # Show the colorbar
    ---> 25 plt.colorbar(label='Trip Duration (minutes)')
         26 
         27 # Show the plot
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\matplotlib\pyplot.py in colorbar(mappable, cax, ax, **kw)
       2350         mappable = gci()
       2351         if mappable is None:
    -> 2352             raise RuntimeError('No mappable was found to use for colorbar '
       2353                                'creation. First define a mappable such as '
       2354                                'an image (with imshow) or a contour set ('
    

    RuntimeError: No mappable was found to use for colorbar creation. First define a mappable such as an image (with imshow) or a contour set (with contourf).


    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\IPython\core\pylabtools.py:132: UserWarning: Creating legend with loc="best" can be slow with large amounts of data.
      fig.canvas.print_figure(bytes_io, **kw)
    


    
![png](output_92_2.png)
    



```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60

# Create a new column with log-transformed trip duration
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION_minutes'])

# Set up the matplotlib figure
plt.figure(figsize=(10, 8))

# Create a scatterplot with a regression line
sns.regplot(data=df, x='avg_temperature', y='TRIPDURATION_log', scatter_kws={'s': 20, 'alpha': 0.5}, line_kws={'color': 'red'})

# Set the title and labels
plt.title('Relationship between TRIPDURATION_log and avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Log(Trip Duration) (minutes)')

# Show the plot
plt.show()

```


    
![png](output_93_0.png)
    



```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60

# Create a new column with log-transformed trip duration
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION_minutes'])

# Set up the matplotlib figure
plt.figure(figsize=(10, 6))

# Create a scatterplot with a regression line
sns.set_theme(style="whitegrid")
sns.regplot(data=df, x='avg_temperature', y='TRIPDURATION_log', scatter_kws={'s': 30, 'alpha': 0.5}, line_kws={'color': 'red'})

# Set the title and labels
plt.title('Scatterplot with Regression Line of TRIPDURATION_log and avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Log(Trip Duration) (minutes)')

# Show the plot
plt.show()

```


    
![png](output_94_0.png)
    



```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Assuming df is your DataFrame
# Convert TRIPDURATION from seconds to minutes
df['TRIPDURATION_minutes'] = df['TRIPDURATION'] / 60



# Set up the matplotlib figure
plt.figure(figsize=(10, 6))

# Create a scatterplot with a regression line
sns.set_theme(style="whitegrid")
sns.regplot(data=df, x='avg_temperature', y='TRIPDURATION', scatter_kws={'s': 30, 'alpha': 0.5}, line_kws={'color': 'red'})

# Set the title and labels
plt.title('Scatterplot with Regression Line of TRIPDURATION and avg_temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Log(Trip Duration) (minutes)')

# Show the plot
plt.show()

```


    
![png](output_95_0.png)
    



```python
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming df is your DataFrame
# Create a bar plot
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='avg_temperature', bins=20, kde=False, color='skyblue', edgecolor='black')

# Set the title and labels
plt.title('Distribution of Trips by Average Temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Number of Trips')

# Show the plot
plt.show()

```


    
![png](output_96_0.png)
    



```python
fig, axs = plt.subplots(figsize=(13, 8), ncols=1)
sns.histplot(df["number_of_rides"], bins=50, color="#00ce96")
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       3079             try:
    -> 3080                 return self._engine.get_loc(casted_key)
       3081             except KeyError as err:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'number_of_rides'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-34-b8a428d4a7dc> in <module>
          1 fig, axs = plt.subplots(figsize=(13, 8), ncols=1)
    ----> 2 sns.histplot(df["number_of_rides"], bins=50, color="#00ce96")
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
       3022             if self.columns.nlevels > 1:
       3023                 return self._getitem_multilevel(key)
    -> 3024             indexer = self.columns.get_loc(key)
       3025             if is_integer(indexer):
       3026                 indexer = [indexer]
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       3080                 return self._engine.get_loc(casted_key)
       3081             except KeyError as err:
    -> 3082                 raise KeyError(key) from err
       3083 
       3084         if tolerance is not None:
    

    KeyError: 'number_of_rides'



    
![png](output_97_1.png)
    


<h2> 6. SOME EXPERIMENT 

Converting date columns to date-time format.
<br> Creating new columns year, month, day_of_the_week and hour.


```python
# get dates of the holidays
holiday_list = []
for holiday in holidays.USA(years=[2020, 2021, 2022]).items():
    holiday_list.append(holiday[0])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-cd0f46941726> in <module>
          1 # get dates of the holidays
          2 holiday_list = []
    ----> 3 for holiday in holidays.USA(years=[2020, 2021, 2022]).items():
          4     holiday_list.append(holiday[0])
    

    NameError: name 'holidays' is not defined



```python
season_dict = {1: 1,
               2: 1,
               3: 2,
               4: 2,
               5: 2,
               6: 3,
               7: 3,
               8: 3,
               9: 4,
               10: 4,
               11: 4,
               12: 1}
```


```python
def create_time_features(df_, date_col='start_date'):
    df_[date_col] = pd.to_datetime(df_[date_col])

    df_['year'] = df_[date_col].dt.year
    df_['month'] = df_[date_col].dt.month
    df_['season'] = df_['month'].apply(lambda x: season_dict[x])
    df_['day'] = df_[date_col].dt.day
    df_['hour'] = df_[date_col].dt.hour
    df_['week_day'] = df_[date_col].dt.day_name()
    df_['is_weekend'] = np.where(
        (df_['week_day'] == "Saturday") | (df_['week_day'] == "Sunday"), 1, 0)

    df_['is_holiday'] = np.where(
        df_[date_col].dt.date.isin(holiday_list), 1, 0)
    return df
```


```python
df = create_time_features(df, 'start_date')
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>start_date</th>
      <th>start_station_code</th>
      <th>end_date</th>
      <th>end_station_code</th>
      <th>duration_sec</th>
      <th>is_member</th>
      <th>year</th>
      <th>month</th>
      <th>season</th>
      <th>day</th>
      <th>hour</th>
      <th>week_day</th>
      <th>is_weekend</th>
      <th>is_holiday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2017-04-15 00:00:00</td>
      <td>7060</td>
      <td>4/15/2017 0:31</td>
      <td>7060</td>
      <td>1841</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2017-04-15 00:01:00</td>
      <td>6173</td>
      <td>4/15/2017 0:10</td>
      <td>6173</td>
      <td>553</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2017-04-15 00:01:00</td>
      <td>6203</td>
      <td>4/15/2017 0:04</td>
      <td>6204</td>
      <td>195</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2017-04-15 00:01:00</td>
      <td>6104</td>
      <td>4/15/2017 0:06</td>
      <td>6114</td>
      <td>285</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2017-04-15 00:01:00</td>
      <td>6174</td>
      <td>4/15/2017 0:11</td>
      <td>6174</td>
      <td>569</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1048570</th>
      <td>1048570</td>
      <td>2017-06-11 23:49:00</td>
      <td>6137</td>
      <td>6/12/2017 0:12</td>
      <td>7025</td>
      <td>1400</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048571</th>
      <td>1048571</td>
      <td>2017-06-11 23:49:00</td>
      <td>6199</td>
      <td>6/11/2017 23:54</td>
      <td>6182</td>
      <td>265</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048572</th>
      <td>1048572</td>
      <td>2017-06-11 23:49:00</td>
      <td>6214</td>
      <td>6/12/2017 0:06</td>
      <td>6198</td>
      <td>983</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048573</th>
      <td>1048573</td>
      <td>2017-06-11 23:49:00</td>
      <td>6407</td>
      <td>6/12/2017 0:01</td>
      <td>6092</td>
      <td>686</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048574</th>
      <td>1048574</td>
      <td>2017-06-11 23:50:00</td>
      <td>6085</td>
      <td>6/12/2017 0:17</td>
      <td>6131</td>
      <td>1617</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1048575 rows × 15 columns</p>
</div>



**Creating** a new columns trip_duration, ride_length.


```python
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    r = 6371
    return c * r
```


```python

```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-69-df445235ba78> in <module>
    ----> 1 df['end_date'] = pd.to_datetime(df_trips['end_date'])
          2 
          3 df['duration_sec'] = df.apply(lambda x: (
          4     x['end_date'] - x['start_date']).total_seconds(), axis=1)
          5 df['ride_length'] = df.apply(lambda x: haversine(
    

    NameError: name 'df_trips' is not defined



```python
def create_time_features(df_, date_col='end_date'):
    df_[date_col] = pd.to_datetime(df_[date_col])

    df_['endyear'] = df_[date_col].dt.year
    df_['endmonth'] = df_[date_col].dt.month
    df_['endseason'] = df_['endmonth'].apply(lambda x: season_dict[x])
    df_['endday'] = df_[date_col].dt.day
    df_['endhour'] = df_[date_col].dt.hour
    df_['endweek_day'] = df_[date_col].dt.day_name()
    df_['endis_weekend'] = np.where(
        (df_['endweek_day'] == "Saturday") | (df_['endweek_day'] == "Sunday"), 1, 0)

    df_['endis_holiday'] = np.where(
        df_[date_col].dt.date.isin(holiday_list), 1, 0)
    return df
```


```python
df = create_time_features(df, 'end_date')
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>start_date</th>
      <th>start_station_code</th>
      <th>end_date</th>
      <th>end_station_code</th>
      <th>duration_sec</th>
      <th>is_member</th>
      <th>year</th>
      <th>month</th>
      <th>season</th>
      <th>day</th>
      <th>hour</th>
      <th>week_day</th>
      <th>is_weekend</th>
      <th>is_holiday</th>
      <th>endyear</th>
      <th>endmonth</th>
      <th>endseason</th>
      <th>endday</th>
      <th>endhour</th>
      <th>endweek_day</th>
      <th>endis_weekend</th>
      <th>endis_holiday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>2017-04-15 00:00:00</td>
      <td>7060</td>
      <td>2017-04-15 00:31:00</td>
      <td>7060</td>
      <td>1841</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2017-04-15 00:01:00</td>
      <td>6173</td>
      <td>2017-04-15 00:10:00</td>
      <td>6173</td>
      <td>553</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>2017-04-15 00:01:00</td>
      <td>6203</td>
      <td>2017-04-15 00:04:00</td>
      <td>6204</td>
      <td>195</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>2017-04-15 00:01:00</td>
      <td>6104</td>
      <td>2017-04-15 00:06:00</td>
      <td>6114</td>
      <td>285</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>2017-04-15 00:01:00</td>
      <td>6174</td>
      <td>2017-04-15 00:11:00</td>
      <td>6174</td>
      <td>569</td>
      <td>1</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>4</td>
      <td>2</td>
      <td>15</td>
      <td>0</td>
      <td>Saturday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1048570</th>
      <td>1048570</td>
      <td>2017-06-11 23:49:00</td>
      <td>6137</td>
      <td>2017-06-12 00:12:00</td>
      <td>7025</td>
      <td>1400</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>Monday</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048571</th>
      <td>1048571</td>
      <td>2017-06-11 23:49:00</td>
      <td>6199</td>
      <td>2017-06-11 23:54:00</td>
      <td>6182</td>
      <td>265</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048572</th>
      <td>1048572</td>
      <td>2017-06-11 23:49:00</td>
      <td>6214</td>
      <td>2017-06-12 00:06:00</td>
      <td>6198</td>
      <td>983</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>Monday</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048573</th>
      <td>1048573</td>
      <td>2017-06-11 23:49:00</td>
      <td>6407</td>
      <td>2017-06-12 00:01:00</td>
      <td>6092</td>
      <td>686</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>Monday</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1048574</th>
      <td>1048574</td>
      <td>2017-06-11 23:50:00</td>
      <td>6085</td>
      <td>2017-06-12 00:17:00</td>
      <td>6131</td>
      <td>1617</td>
      <td>1</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>23</td>
      <td>Sunday</td>
      <td>1</td>
      <td>0</td>
      <td>2017</td>
      <td>6</td>
      <td>3</td>
      <td>12</td>
      <td>0</td>
      <td>Monday</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1048575 rows × 23 columns</p>
</div>




```python
df['end_date'] = pd.to_datetime(df['end_date'])

df['duration_sec'] = df.apply(lambda x: (
    x['end_date'] - x['start_date']).total_seconds(), axis=1)
df['ride_length'] = df.apply(lambda x: haversine(
    x['start_lat'], x['start_lng'], x['end_lat'], x['end_lng']), axis=1)

df.drop(['start_date', 'end_date'], inplace=True, axis=1)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       3079             try:
    -> 3080                 return self._engine.get_loc(casted_key)
       3081             except KeyError as err:
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'start_lat'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-76-25fe12d1e053> in <module>
          4     x['end_date'] - x['start_date']).total_seconds(), axis=1)
          5 df['ride_length'] = df.apply(lambda x: haversine(
    ----> 6     x['start_lat'], x['start_lng'], x['end_lat'], x['end_lng']), axis=1)
          7 
          8 df.drop(['start_date', 'end_date'], inplace=True, axis=1)
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\frame.py in apply(self, func, axis, raw, result_type, args, **kwds)
       7766             kwds=kwds,
       7767         )
    -> 7768         return op.get_result()
       7769 
       7770     def applymap(self, func, na_action: Optional[str] = None) -> DataFrame:
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\apply.py in get_result(self)
        183             return self.apply_raw()
        184 
    --> 185         return self.apply_standard()
        186 
        187     def apply_empty_result(self):
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\apply.py in apply_standard(self)
        274 
        275     def apply_standard(self):
    --> 276         results, res_index = self.apply_series_generator()
        277 
        278         # wrap results
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\apply.py in apply_series_generator(self)
        288             for i, v in enumerate(series_gen):
        289                 # ignore SettingWithCopy here in case the user mutates
    --> 290                 results[i] = self.f(v)
        291                 if isinstance(results[i], ABCSeries):
        292                     # If we have a view on v, we need to make a copy because
    

    <ipython-input-76-25fe12d1e053> in <lambda>(x)
          4     x['end_date'] - x['start_date']).total_seconds(), axis=1)
          5 df['ride_length'] = df.apply(lambda x: haversine(
    ----> 6     x['start_lat'], x['start_lng'], x['end_lat'], x['end_lng']), axis=1)
          7 
          8 df.drop(['start_date', 'end_date'], inplace=True, axis=1)
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\series.py in __getitem__(self, key)
        851 
        852         elif key_is_scalar:
    --> 853             return self._get_value(key)
        854 
        855         if is_hashable(key):
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\series.py in _get_value(self, label, takeable)
        959 
        960         # Similar to Index.get_value, but we do not fall back to positional
    --> 961         loc = self.index.get_loc(label)
        962         return self.index._get_values_for_loc(self, loc, label)
        963 
    

    C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
       3080                 return self._engine.get_loc(casted_key)
       3081             except KeyError as err:
    -> 3082                 raise KeyError(key) from err
       3083 
       3084         if tolerance is not None:
    

    KeyError: 'start_lat'



```python
# Assuming df is your DataFrame
df.to_csv('modified_dataset.csv', index=False)

```


```python

```
