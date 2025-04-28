import pandas as pd

covid_df =pd.read_csv('italy-covid-daywise.csv')
print(covid_df)
print(covid_df.info())
print(covid_df.describe())
print(covid_df.columns)
print(covid_df.shape)


covid_data_dict = {
    'date':       ['2020-08-30', '2020-08-31', '2020-09-01', '2020-09-02', '2020-09-03'],
    'new_cases':  [1444, 1365, 996, 975, 1326],
    'new_deaths': [1, 4, 6, 8, 6],
    'new_tests': [53541, 42583, 54395, None, None]
}
print(covid_data_dict['new_cases'])

print(covid_df['new_cases'])

#
print(covid_df['new_cases'][246])
print(covid_df['new_tests'][240])

#or

print(covid_df.at[246, 'new_cases'])
print(covid_df.at[240, 'new_tests'])
#

print(covid_df.new_cases)

cases_df = covid_df[['date', 'new_cases']]
print(cases_df)

covid_df_copy = covid_df.copy()

print(covid_df.loc[243])
print(covid_df.head(5))
print(covid_df.tail(4))


print(covid_df.at[0, 'new_tests'])
print(covid_df.new_tests.first_valid_index())


print(covid_df.loc[108:113])


print(covid_df.sample(10))


#Analyzing data from data frames

#Q: What are the total number of reported cases and deaths related to Covid-19 in Italy?
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
print('The number of reported cases is {} and the number of reported deaths is {}.'.format(int(total_cases), int(total_deaths)))

#Q: What is the overall death rate (ratio of reported deaths to reported cases)?
death_rate = covid_df.new_deaths.sum() / covid_df.new_cases.sum()
print("The overall reported death rate in Italy is {:.2f} %.".format(death_rate*100))

#Q: What is the overall number of tests conducted? A total of 935310 tests were conducted before daily test numbers were reported.
initial_tests = 935310
total_tests = initial_tests + covid_df.new_tests.sum()
print("The overall number of tests conducted in Italy is {}.".format(int(total_tests)))

#Q: What fraction of tests returned a positive result?
positive_rate = total_cases / total_tests
print('{:.2f}% of tests in Italy led to a positive diagnosis.'.format(positive_rate*100))



# Querying and sorting rows
high_new_cases = covid_df.new_cases > 1000 #returns a series of boolean values
print(high_new_cases)

print(covid_df[high_new_cases]) #provides a data frame with all the rows where the condition is true

from IPython.display import display
with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000]) #displays all the rows with new cases > 1000

print(positive_rate)

high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate]
print(high_ratio_df)

covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests
a= covid_df['positive_rate']
print(a)


print(covid_df.drop(columns=['positive_rate'], inplace=True))

#sorting rows using column values
print(covid_df.sort_values('new_cases', ascending=False).head(10))

print(covid_df.sort_values('new_deaths', ascending=False).head(10))


print(covid_df.loc[169:175])

covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases'])/2
print(covid_df.at[172, 'new_cases'])


#working with dates
print(covid_df.date)
# or
covid_df['date'] = pd.to_datetime(covid_df.date)
print(covid_df['date'])



covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
print(covid_df)


# Query the rows for May
covid_df_may = covid_df[covid_df.month == 5]

# Extract the subset of columns to be aggregated
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Get the column-wise sum
covid_may_totals = covid_df_may_metrics.sum()

print(covid_may_totals)

b=covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
print(b)

#overall average of new cases
print(covid_df.new_cases.mean())


# Average for Sundays
print(covid_df[covid_df.weekday == 6].new_cases.mean())


#grouping  and aggregating data
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
print(covid_month_df)

covid_month_mean_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()
print(covid_month_mean_df)


covid_df['total_cases'] = covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests
print(covid_df)

#Merging data from multiple sources
locations_df = pd.read_csv('locations.csv')
print(locations_df)

print(locations_df[locations_df.location == "Italy"])

covid_df['location'] = "Italy"
print(covid_df)

merged_df = covid_df.merge(locations_df, on="location")
print(merged_df)    

merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population
print(merged_df)


#writing back to files

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

print(result_df.to_csv('results.csv', index=None))

#basic plotting with pandas
import matplotlib.pyplot as plot

result_df.set_index('date', inplace=True)
result_df.new_cases.plot()

print(result_df.loc['2020-09-01'])
result_df.new_cases.plot()
result_df.new_deaths.plot()
plot.show()

result_df.total_cases.plot()
result_df.total_deaths.plot()
plot.show()

death_rate = result_df.total_deaths / result_df.total_cases
death_rate.plot(title='Death Rate')
plot.show()

positive_rates = result_df.total_cases / result_df.total_tests
positive_rates.plot(title='Positive Rate')
plot.show()

covid_month_df.new_cases.plot(kind='bar')
plot.show()

covid_month_df.new_tests.plot(kind='bar')
plot.show()



