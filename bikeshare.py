import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
            city = str(input('please choose City Name :chicago, new york city, washington : ').lower())
            if city == 'chicago':
                print(' You Choose Chicago City')

            if city == 'new york city':
                print(' You Choose New York City')

            if city == 'washington':
                print(' You Choose washington City')

                
            if city not in ('chicago','new york city','washington'):
                print('Invalid input. Please try again.')
                continue
            else:
                break
                
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('please choose a month (all, january, february, march, april,may, june): ').lower())
        if month not in ('all', 'january','february','march','april','may','june'):
            print('Please Enter Vaild month name ')
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('please choose a week day (all, monday, tuesday, wednesday,thursday,friday,Saturday,sunday): ').lower())
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print('Please Enter Vaild Week Day ')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    return df

def first_few_rows(df):
	# "Ask user if want to take a look at the first few rows of the chosen city data."
	ask_user= input('\nWould you like  to see raw data? Enter yes or no.\n')
	
	col=0
	row=5
	while True:
		if ask_user.lower() == 'yes':
			print(df.iloc[col:row])
			row+=5
			col+=5
			ask_user= input('\nWould you like  to see raw data? Enter yes or no.\n')
		else:
			break





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].value_counts().idxmax()
    print('Most common month: ', common_month)

    print('\n')
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week: ', common_day)

    print('\n')
  
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station:\n', df['Start Station'].mode(0))

    print('\n')

    # TO DO: display most commonly used end station
    print('Most commonly End Station station:\n',df['End Station'].mode(0))

    print('\n')

    # TO DO: display most frequent combination of start station and end station trip
    common_two_station = df['Start Station'] + df['End Station']
    print('Most Frequent Combination of Start Station and End Station Trip:\n',common_two_station.mode(0))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: ',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n',df['User Type'].value_counts())

    print('\n')

    # TO DO: Display counts of gender
    try:
    	print('Counts of Gender:\n', df['Gender'].value_counts())
    	print('\n')
    except:
    	print('There is no gender vaules in this source of data.\n')



    # TO DO: Display earliest, most recent, and most common year of birth
    try:
    	print('Earliest Year Of Birth',df['Birth Year'].min())
    	print('Most Recent Year Of Birth: ',df['Birth Year'].max())
    	print('Most common Year Of Birth: '+ str(df['Birth Year'].mode()[0]))
    except:
    	print('No brith data during this period of time.')

           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        first_few_rows(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
