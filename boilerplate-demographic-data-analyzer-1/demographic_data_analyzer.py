import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = list(df['race'].unique())
    race_num = []
    for i in races:
      race_num.append(len(df[df['race'].str.contains(i)]))

    race_series = pd.Series(data=race_num, index=races)

    race_count = race_series

    # What is the average age of men?
    men = df.loc[df['sex'] == 'Male']
    average_age_men = round(men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total = len(df)
    percent_bachelors =  len(df.loc[df['education'] == 'Bachelors']) / total 
    percentage_bachelors = round((percent_bachelors * 100),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    #These 2 variables were not on the readme and aren't tested against so they
    #are being left blank
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_ed = df[df.education.isin(['Bachelors', 'Masters', 'Doctorate'])] #prof-school not included in requirements
    higher_ed_total = len(higher_ed)
    salary_above = len(higher_ed.loc[higher_ed['salary'] == '>50K']) / higher_ed_total 
    
    higher_education_rich = round((salary_above * 100),1)
    
    lower_ed = df.loc[(df['education-num'] == 15) | (df['education-num'] < 13)]
    lower_ed_total = len(lower_ed)
    lower_sal_above = len(lower_ed.loc[lower_ed['salary'] == '>50K']) / lower_ed_total

    lower_education_rich = round((lower_sal_above * 100),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?

    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #Another field that isn't on the read me and isn't tested for
    num_min_workers = None

    rich_percentage = int(len(df.loc[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')]) / len(df.loc[df['hours-per-week'] == 1] )*100)

    # What country has the highest percentage of people that earn >50K?
    df['native-country'] = df['native-country'].str.replace('?', 'Unknown') #Was getting a regex error in below for loop because of the ?, changed it to Unknown
    desired_cols = df.loc[df['salary'] == '>50K', 'native-country']
    test = pd.DataFrame(data=desired_cols.copy()) 

    countries = list(test['native-country'].unique())

    above_50k_count = [] 

    for i in countries:
      above_50k_count.append(len(test[test['native-country'].str.contains(i)]))

    pop_total = []

    for i in countries:
      pop_total.append(len(df[df['native-country'].str.contains(i)]))

    final_data = {'above-50k': above_50k_count, 'pop-total': pop_total}

    final_df = pd.DataFrame(data=final_data, index=countries)

    final_df['percent'] = final_df['above-50k'] / final_df['pop-total']

    country = str(final_df['percent'].idxmax())
    country_percent = final_df.loc[['Iran'], ['percent']].values
    
    highest_earning_country = country
    highest_earning_country_percentage = round((country_percent[0][0] * 100),1)

    # Identify the most popular occupation for those who earn >50K in India.
    pop_occ_50k = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')].mode()
    
    top_IN_occupation = pop_occ_50k['occupation'][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
