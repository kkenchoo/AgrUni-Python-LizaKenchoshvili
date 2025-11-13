input_date = input('Enter date: ').split('T')

date_day = input_date[0].split('-')
date_day.reverse()
new_date_day = '-'.join(date_day)

date_time = input_date[1].split('.')
input_time = date_time[0].split(':')
hour = int(input_time[0])

if hour > 12:
    input_time[0] = str(hour - 12)
elif hour == 0:
    input_time[0] = '12'
time_12hr = ':'.join(input_time)

timezone = date_time[1]

if '+' in timezone:
    tz = timezone.split('+')
    new_tz = tz[1].split(':')
    time_12hr += ' +' + str(int(new_tz[0]))
elif '-' in timezone:
    tz = timezone.split('-')
    new_tz = tz[1].split(':')
    time_12hr += ' -' + str(int(new_tz[0]))

#input 2024-03-22T19:17:42.956376+00:00
#output 22-03-2024 7:17:42 +0

print(f'Output: {new_date_day} {time_12hr}')