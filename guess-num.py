import random
r = random.randint(1, 100)
i = 1
while i > 0:
	x = input('請輸入一個1~100之間的整數: ')
	x = int(x)
	print('一共猜了', i,'次!')
	i = i + 1
	if x == r:
		print('終於答對了!')
		break
	elif x > r:
		print('比答案大!')
	else:
		print('比答案小!')