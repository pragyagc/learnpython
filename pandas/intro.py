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






