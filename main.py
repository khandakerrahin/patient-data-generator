# imports
import json
import random
import datetime


# functions
def get_condition(name):
    # print(name)
    return name


def get_random_int(x, y):
    return random.randint(x, y)


def get_leading_zero_string(x, n):
    # Convert `x` to a string
    number_str = str(x)

    # Pad `number_str` with zeros to 'n' digits
    zero_filled_number = number_str.zfill(n)

    return zero_filled_number


def new_condition_entry(cond_id):
    condition_string = '{}'

    cond_json = json.loads(condition_string)

    dates = get_random_dates()

    cond_json['id'] = cond_id
    cond_json['diagnosed'] = dates[0]
    cond_json['cured'] = dates[1]
    cond_json['kind'] = "cond" + get_leading_zero_string(get_random_int(1, 668), 5) # total conditions = 668

    return cond_json


def get_random_dates():
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2021, 12, 20)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    # print(random_number_of_days)

    random_date_start = start_date + datetime.timedelta(days=random_number_of_days)
    random_date_end = random_date_start + datetime.timedelta(days=get_random_int(0, 10))

    # print(random_date_start.strftime("%Y%m%d"))
    # print(random_date_end.strftime("%Y%m%d"))

    return [random_date_start.strftime("%Y%m%d"), random_date_end.strftime("%Y%m%d")]


# main
# read JSON file
with open('patients_basic.json', encoding="utf8") as f:
    data = json.load(f)

# loop through JSON file
for patient in data:
    # print(patient['name'])
    conditionCount = get_random_int(1, 5)
    trialCount = get_random_int(1, 10)

    conditionCount = get_random_int(0, 5)
    trialCount = get_random_int(0, 10)

    patient['condition'] = []
    patient['trials'] = []

    for x in range(conditionCount):
        # Add new Conditions to patients
        patient['condition'].append(new_condition_entry('pc'+get_leading_zero_string(x+1, 5)))

    for x in range(trialCount):
        # Add new Trials to patients
        patient['condition'].append(new_condition_entry('pc'+get_leading_zero_string(x+1, 5)))

# data.append(new_condition_entry('cond2441139'))


# dump new JSON file
with open('patients.json', 'w') as f:
    json.dump(data, f, indent=4)
