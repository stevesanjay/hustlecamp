# Calculating Future Date:

import datetime

current_datetime = datetime.datetime.now()
days_to_add = 7
future_date = current_datetime + datetime.timedelta(days=days_to_add)
print("Future Date (after 7 days):", future_date)
