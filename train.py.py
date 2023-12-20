#!/usr/bin/env python
# coding: utf-8

# <h1>EDA Notebook - 1

# <h2>Preparing the Data

# <h3>Import Libraries

# The following code is written in Python 3.7. Below is the list of libraries used.

# In[7]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import sklearn
import itertools
import copy
import csv
import openpyxl


# <h3>Load Data Modeling Libraries

# These are the most common machine learning and data visualization libraries.

# In[2]:


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


#Common Model Helpers
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
from sklearn import metrics
from sklearn.metrics import accuracy_score, mean_absolute_error, r2_score


# <h3> Data Set Restructuring

# In[9]:


# read BIXI data set
dfBIXI = pd.read_csv('DonneesOuverte2022.csv')


# In[10]:


dfBIXI


# In[11]:


# read Temparature data set
dfTEMP = pd.read_csv('Montreal_weather-2022.csv')


# In[12]:


dfTEMP


# **Organazing BIXI Data**

# In[13]:


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


# **Organasing Montreal Temparature Data**

# 

# In[14]:


# Assuming TEMPdf is your DataFrame
# Convert the 'date' column to datetime format
dfTEMP['date'] = pd.to_datetime(dfTEMP['date'], format='%m/%d/%Y')

# Create new columns 'TEMPyear', 'TEMPmonth', 'TEMPday'
dfTEMP['year'] = dfTEMP['date'].dt.year
dfTEMP['month'] = dfTEMP['date'].dt.month
dfTEMP['day'] = dfTEMP['date'].dt.day

# Display the updated DataFrame
dfTEMP.head()


# **Merge Data sets**

# Merge the two datasets based on the 'Year', 'Month', and 'Day' columns

# In[15]:


# Assuming dfBIXI and dfTEMP are your datasets
# Replace 'TEMPyear', 'TEMPmonth', 'TEMPday' with the actual columns names you want to merge on

# Merge the two datasets on the specified columns
merged_df = pd.merge(dfBIXI, dfTEMP[['year', 'month', 'day', 'avg_temperature', 'avg_wind_speed', 'avg_dew_point', 'rain', 'snow', 'snow_on_ground']], 
                     how='left', on=['year', 'month', 'day'])

# Display the merged DataFrame
print(merged_df.head())


# In[16]:


merged_df.head()


# In[17]:


num_rows = merged_df.shape[0]
print(f"The DataFrame has {num_rows} rows.")


# In[18]:


df = merged_df


# In[19]:


# Assuming df is your DataFrame
df['TRIPDURATION'] = (df['ENDTIMEMS'] - df['STARTTIMEMS']) / 1000  # Convert milliseconds to seconds

# Display the updated DataFrame
print(df.head())


# <h3> <font color= black></font> Greet the Data
#     <h4> Import the Data

# In[20]:


# read data set
df


# **Preview the Data**

# In[21]:


# get a peek at the top 5 rows of the data set
print(df.head())


# **Date column types and count**

# In[22]:


# understand the type of each column
print(df.info())


# **Summarize the central tendency, dispersion and shape**

# In[23]:


# get information on the numerical columns for the data set
with pd.option_context('display.max_columns', len(df.columns)):
    print(df.describe(include='all'))


# <h2> Data Cleaning

# The data is cleaned in 2 steps:
# 1. Correcting outliers
# 2. Completing null or missing data

# <h3> Correcting outliers

# There aren't any noticable outliers.

# <h3>Completing null or missing data

# The columns containing null values need to be identified.
# <br>**Training data**

# In[24]:


# find number of null values in each column
print('Number of null values per column:\n', df.isnull().sum())


# **Dropping Rows or Columns:**
# <br> There aren null values. so I choose to drop rows or columns containing null values:

# In[ ]:





# In[25]:


# find number of null values in each column
print('Number of null values per column:\n', df.isnull().sum())


# <h3>Normalizing Data

# Let's start by looking at the skewness of each column to determine which ones need to be normalized.

# In[26]:


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


# <br>Based on the skewness values, it appears that some of the columns have significant skewness. Skewness measures the asymmetry of a distribution. Here are some general recommendations based on the skewness values:

# **High Positive Skewness (> 1):**
# <br>For columns with high positive skewness (e.g., 'TRIPDURATION'), consider applying a transformation such as the logarithm to reduce the impact of extreme values.

# In[27]:


import numpy as np

# Assuming df is your DataFrame
df['STARTSTATIONLONGITUDE_log'] = np.log1p(df['STARTSTATIONLONGITUDE'])
df['ENDSTATIONLONGITUDE_log'] = np.log1p(df['ENDSTATIONLONGITUDE'])
df['STARTTIMEMS_log'] = np.log1p(df['STARTTIMEMS'])
df['ENDTIMEMS_log'] = np.log1p(df['ENDTIMEMS'])
df['avg_dew_point_log'] = np.log1p(df['avg_dew_point'])
df['TRIPDURATION_log'] = np.log1p(df['TRIPDURATION'])


# In[28]:


print('STARTSTATIONLONGITUDE_log skewness', df.TRIPDURATION_log.skew())
print('ENDSTATIONLONGITUDE_log skewness', df.TRIPDURATION_log.skew())
print('STARTTIMEMS_log skewness', df.TRIPDURATION_log.skew())
print('ENDTIMEMS_log skewness', df.TRIPDURATION_log.skew())
print('avg_dew_point_log skewness', df.TRIPDURATION_log.skew())
print('TRIPDURATION_log skewness', df.TRIPDURATION_log.skew())


# **High Negative Skewness (< -1):**
# 
# For columns with high negative skewness (e.g., 'avg_wind_speed'), consider applying a transformation such as the square root to make the distribution more symmetric.

# In[29]:


# Assuming df is your DataFrame

df['STARTSTATIONLATITUDE_sqrt'] = np.sqrt(df['STARTSTATIONLATITUDE'])
df['ENDSTATIONLATITUDE_sqrt'] = np.sqrt(df['ENDSTATIONLATITUDE'])


# In[30]:


print('STARTSTATIONLATITUDE_sqrt skewness', df.STARTSTATIONLATITUDE_sqrt.skew())
print('ENDSTATIONLATITUDE_sqrt skewness', df.ENDSTATIONLATITUDE_sqrt.skew())


# <h2> Data Exploration

# Let's look at the distribution for each column based on the number of rides.

# In[31]:


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


# In[35]:


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


# In[25]:


print('month:\n', df.month.value_counts(sort=False))


# In[36]:


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


# In[26]:


print('day:\n', df.day.value_counts(sort=False))


# In[37]:


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


# In[27]:


print('hour:\n', df.hour.value_counts(sort=False))


# In[38]:


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


# In[28]:


print('Temp (°C):\n', df.avg_temperature.value_counts())


# In[48]:


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


# In[29]:


print('start_station_code:\n', df.ENDSTATIONNAME.value_counts())


# In[30]:


print('duration_sec:\n', df.TRIPDURATION.value_counts())


# In[51]:


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


# In[52]:


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


# <h2> 6. Feature Engineering

# In[53]:


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


# In[54]:


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


# In[57]:


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


# In[59]:


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


# In[60]:


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


# In[61]:


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


# In[33]:


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

