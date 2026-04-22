from dateutil import parser
start = '9/30/2021 1:35 PM'
end = '9/30/2021 1:50 PM'
start_date= parser.parse(start)
end_date= parser.parse(end)
type(start_date)
print((end_date-start_date).total_seconds())