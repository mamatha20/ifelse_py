day=input('enter any day')
size=input('enter any size')
if day=='sunday':
	if size=='large':
		print('piza with free brounick')
	elif size=='medium':
		print('piza with free garlick stick')
	else:
		print('free coca')
elif day=='monday' or day=='tuesday':
	if size=='large':
		print('pizza with 10%discount')
	elif size=='medium':
		print('pizza with 20%discount')
	else:
		print('pizza without discount')
elif day=='wednseday' or day=='Thursday':
	if size=='large'or size=='medium' or size =='small':
		print('pizza with garlic stick and coce free')
elif day=='friday' or day=='saturday':
	if size=='large':
		print('pizza only')
else:
	print('invalid day')