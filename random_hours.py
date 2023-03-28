import datetime
import os
import random

# Set the base path
base_path = '/net/corpora/twitter2/Tweets/'

# Set the start and end dates (inclusive)
start_date = datetime.date(2013, 1, 1)
end_date = datetime.date(2023, 3, 28)

# Define a function to generate a random hour
def random_hour():
    return '{:02d}'.format(random.randint(0, 23))

# Loop over each date
current_date = start_date
while current_date <= end_date:
    # Create the file path with a random hour
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    day = current_date.strftime('%d')
    hour = random_hour()
    file_path = os.path.join(base_path, year, month, year + month + day + ':' + hour + '.out.gz' + " " + '\\')
    
    # Do something with the file path
    print(file_path)
    
    # Increment the date
    current_date += datetime.timedelta(days=1)
