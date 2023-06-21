import datetime
from dateutil.relativedelta import relativedelta


def get_list_of_months():
    today = datetime.date.today()
    first_date_of_year = datetime.date(today.year, 1, 1)
    return [(first_date_of_year + relativedelta(months=i)).strftime('%B') for i in range(12)]


def get_month_options_tuple():
    months = get_list_of_months()
    month_options = []
    for i in range(len(months)):
        option_tuple = (i + 1, months[i])
        month_options.append(option_tuple)
    return tuple(month_options)


def get_name_of_current_month():
    return datetime.date.today().strftime('%B')


