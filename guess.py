import random
r = random.randint(1, 100)
count = 0
while True:
	count = count+1
	guess = input('猜猜是多少：')
	guess = int(guess)
	if guess == r:
		print('你猜對了！')
		print('已經猜', count, '次了')
		break
	elif guess > r:
		print('太大了')
	elif guess < r:
		print('太小了')
	print('已經猜', count, '次了')