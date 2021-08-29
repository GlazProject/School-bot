# main
def lessons(today, text, time):
	if today == 9: g = 0
	elif (today>6): today = 0
	if('понедельник' in text): today = 0
	elif('вторник' in text): today = 1
	elif('сред' in text): today = 2
	elif('четверг' in text): today = 3
	elif('пятниц' in text): today = 4
	elif('суббот' in text): today = 5
	elif('воскресен' in text): today = 6
	elif('завтра' in text): 
		today += 1
		if (today>6): today = 0
	elif('вчера' in text): 
		today -= 1
		if(today<0): today = 6
	else:
		today=today
	if time == 0:
		return "day"+str(today)
	elif time == 1:
		return "tday"+str(today)
	elif time == 2:
		return "remake"+str(today)
	elif time == 3:
		return str(today)