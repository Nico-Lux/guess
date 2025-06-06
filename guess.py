import random
r = random.randint(1, 100)
while True:
	guess = input('猜猜是多少：')
	guess = int(guess)
	if guess == r:
		print('你猜對了！')
		break
	elif guess > r:
		print('太大了')
	elif guess < r:
		print('太小了')