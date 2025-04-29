import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

# Read CSV files
covid_df = pd.read_csv('italy-covid-daywise.csv')
locations_df = pd.read_csv('locations.csv')

# Show basic information
print(covid_df)
print(covid_df.info())
print(covid_df.describe())
print(covid_df.columns)
print(covid_df.shape)

# Handle missing values
covid_df['new_tests'].fillna(method='ffill', inplace=True)

# Sample dictionary data
covid_data_dict = {
    'date': ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases': [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, np.nan, np.nan]
}
print(covid_data_dict['new_cases'])

# Access columns
print(covid_df['new_cases'])
print(covid_df['new_cases'][246])
print(covid_df['new_tests'][240])
print(covid_df.at[246, 'new_cases'])
print(covid_df.at[240, 'new_tests'])

# Another way
print(covid_df.new_cases)

# Create a smaller DataFrame
cases_df = covid_df[['date', 'new_cases']]
print(cases_df)

# Copy dataframe
covid_df_copy = covid_df.copy()

# Check specific rows
print(covid_df.loc[243])
print(covid_df.head(5))
print(covid_df.tail(4))

# Check first valid value in new_tests
print(covid_df.at[0, 'new_tests'])
print(covid_df.new_tests.first_valid_index())

# View specific range of rows
print(covid_df.loc[108:113])

# Random 10 samples
print(covid_df.sample(10))

# ---------------------------------------------
# Analyzing data
# ---------------------------------------------

# Total cases and deaths
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))

# Overall death rate
death_rate = total_deaths / total_cases
print("The overall reported death rate in Italy is {:.2f}%.".format(death_rate * 100))

# Overall number of tests conducted
initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()
print("The overall number of tests conducted in Italy is {}.".format(int(total_tests)))

# Positive rate
positive_rate = total_cases / total_tests
print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate * 100))

# ---------------------------------------------
# Querying and sorting
# ---------------------------------------------

# High new cases (>1000)
high_new_cases = covid_df.new_cases > 1000
print(high_new_cases)
print(covid_df[high_new_cases])

# Check rows where new_cases/new_tests > average positive_rate
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]
print(high_ratio_df)

# Add positive rate column temporarily
covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests
print(covid_df['positive_rate'])

# Drop positive_rate column
covid_df.drop(columns=['positive_rate'], inplace=True)

# Sort by new_cases and new_deaths
print(covid_df.sort_values('new_cases', ascending=False).head(10))
print(covid_df.sort_values('new_deaths', ascending=False).head(10))

# View specific range
print(covid_df.loc[169:175])

# Fix missing new_cases value
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases']) / 2
print(covid_df.at[172, 'new_cases'])

# ---------------------------------------------
# Working with dates
# ---------------------------------------------

# Convert to datetime
covid_df['date'] = pd.to_datetime(covid_df['date'])
print(covid_df['date'])

# Extract year, month, day, weekday
covid_df['year'] = covid_df.date.dt.year
covid_df['month'] = covid_df.date.dt.month
covid_df['day'] = covid_df.date.dt.day
covid_df['weekday'] = covid_df.date.dt.weekday
print(covid_df)

# ---------------------------------------------
# Aggregations
# ---------------------------------------------

# Data for May
covid_df_may = covid_df[covid_df.month == 5]
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]
covid_may_totals = covid_df_may_metrics.sum()
print(covid_may_totals)

# Overall average new cases
print(covid_df.new_cases.mean())

# Average new cases on Sundays
print(covid_df[covid_df.weekday == 6].new_cases.mean())

# Monthly sum
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
print(covid_month_df)

# Monthly average
covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()
print(covid_month_mean_df)

# ---------------------------------------------
# Cumulative sums
# ---------------------------------------------

covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests
print(covid_df)

# ---------------------------------------------
# Merging data
# ---------------------------------------------

print(locations_df)
print(locations_df[locations_df.location == "Italy"])

covid_df['location'] = "Italy"
print(covid_df)

merged_df = covid_df.merge(locations_df, on="location")
print(merged_df)

# Calculating per million metrics
merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population
print(merged_df)

# ---------------------------------------------
# Writing to CSV
# ---------------------------------------------

result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]

print(result_df)

result_df.to_csv('results.csv', index=False)
print('Results saved to results.csv.')

# ---------------------------------------------
# Plotting
# ---------------------------------------------

result_df.set_index('date', inplace=True)

# Plot new cases
result_df.new_cases.plot(title='New Cases Over Time')
plot.show()

# Plot new deaths
result_df.new_deaths.plot(title='New Deaths Over Time')
plot.show()

# Plot total cases and total deaths
result_df.total_cases.plot(title='Total Cases Over Time')
result_df.total_deaths.plot(title='Total Deaths Over Time')
plot.show()

# Death rate over time
death_rate = result_df.total_deaths / result_df.total_cases
death_rate.plot(title='Death Rate Over Time')
plot.show()

# Positive rates over time
positive_rates = result_df.total_cases / result_df.total_tests
positive_rates.plot(title='Positive Rate Over Time')
plot.show()

# Monthly new cases
covid_month_df.new_cases.plot(kind='bar', title='Monthly New Cases')
plot.show()

# Monthly new tests
covid_month_df.new_tests.plot(kind='bar', title='Monthly New Tests')
plot.show()