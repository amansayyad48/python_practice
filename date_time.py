from datetime import datetime, timedelta
# #
# # print(datetime.datetime.now()
#
# from time import gmtime, strftime
#
# print(strftime("%y-%d-%m %H:%M:%S", gmtime()))
# print(gmtime())
# print(strftime("%y-%d-%m %H:%M:%S"))

# date_string = "Jan 23 2023 1:30PM"
#
# date_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
# print(date_obj)

given_date = datetime(2023, 1, 23).date()
# day_sub = 7
# new_date = given_date - timedelta(days=day_sub)
new_date = datetime(2022, 12, 23).date()
diff = (given_date - new_date)
print(diff.days)
print(given_date)
