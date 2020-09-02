'''난수 계산기 만들기'''

'''
0단계 - 음수 없는 빼기
1단계 - 음수 있는 빼기
2단계 - 빼기 더하기 랜덤
3단계 - 빼기, 더하기, 나누기, 곱하기 랜덤
'''

import random


round = int(input("단계를 선택하세요(0,1,2,3):"))
count = int(input("몇 개의 문제를 풀까요?(1~5):"))
score = 0
# score는 정답의 갯수를 출력한다


for i in range(count):
		
	x = random.randint(1,100)
	y = random.randint(1,100)
	xy_m = x-y
	xy_p = x+y
	xy_mp = x*y
	xy_d = x//y
	xy_list = [xy_m,xy_p,xy_mp,xy_d]
	

	if round == 0:
		if x>=y:
			print("{}-{}=".format(x,y))
		else:
			xy_m = y-x
			print("{}-{}=".format(y,x))
	elif round == 1:
		print("{}-{}=".format(x,y))
	elif round == 2:
		xy_list = random.choice([xy_m,xy_p])
		if xy_list == xy_m:
			print("{}-{}=".format(x,y))
		elif xy_list == xy_p:
			print("{}+{}=".format(x,y))
	else:
		xy_list = random.choice([xy_m,xy_p,xy_mp,xy_d])
		if xy_list == xy_m:
			print("{}-{}=".format(x,y))
		elif xy_list == xy_p:
			print("{}+{}=".format(x,y))
		elif xy_list == xy_mp:
			print("{}*{}=".format(x,y))
		elif xy_list == xy_d:
			print("{}//{}=".format(x,y))


	answer = int(input("정답은:"))

	if answer == xy_m:
		score = score+1
		print("맞았습니다")
	elif answer == xy_p:
		score = score+1
		print("맞았습니다")
	elif answer == xy_mp:
		score = score+1
		print("맞았습니다")
	elif answer == xy_d:
		score = score+1
		print("맞았습니다")
	else:
		print("틀렸습니다")
	
	
if score == count:
	print("A학점 입니다")
elif score >= count/2:
	print("B학점 입니다")
elif score < count/2 and score != 0:
	print("C학점 입니다")
else:
	print("F학점 입니다")	

print(score,'개 맞았습니다')