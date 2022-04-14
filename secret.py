from datetime import datetime

def get_datetimenow():
	now = datetime.now()
	return now.strftime('%Y-%m-%d %H:%M')
 
def get_pass(pstr):
	# string przychodzacy z formularza
	custom_str = pstr[:3]
	# dowolnie modyfikowane stale wystepujace w hasle
	now = datetime.now()
	date_part1 = now.strftime('%d')
	date_part2 = now.strftime('%H')
	custom_salt = '*$*'
	cusom_password = date_part1+custom_salt+date_part2+custom_str	
	
	# hasło testowe
	custom_password = pstr[:2]+'123'
	
	return custom_password
