from datetime import datetime

def separate_time_hour(time) :
	day = str(time.date())
	hour = int(time.strftime('%H'))
	return {'day':day, 'hour':hour}

def separate_time_hour_minute(time) :
	day = str(time.date())
	hour = int(time.strftime('%H'))
	minute = int(time.strftime('%M'))
	return {'day':day, 'hour':hour, 'minute':minute}

def get_time_from_hour(time) :
	time_list = time['day'].split('-')
	return datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]),int(time['hour']),0)

def get_time_from_hour_minute(time) :
	time_list = time['day'].split('-')
	return datetime(int(time_list[0]),int(time_list[1]),int(time_list[2]),int(time['hour']),int(time['minute']))