
times = [_ for _ in range(9, 17)]
print(times)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(days)
timetable_list = [f'{day} {time}' for day in days for time in times]
print(timetable_list)
timetable = dict((k, False) for k in timetable_list)
print(timetable)