import random
r = random.randint(1, 100)
while True:
	x = input('請輸入一個1~100之間的整數: ')
	x = int(x)
	if x == r:
		print('終於答對了!')
		break
	elif x > r:
		print('比答案大!')
	else:
		print('比答案小!')