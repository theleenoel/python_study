# 💻Python Project - calculating machine💻

random calculating machine

# Language
python

# Description

단계별로 다른 난수 계산기를 생성한다.<br>
단계는 다음과 같다.<br>

-0단계 - 음수 없는 빼기<br>
-1단계 - 음수 있는 빼기<br>
-2단계 - 빼기 더하기 랜덤<br>
-3단계 - 빼기, 더하기, 나누기, 곱하기 랜덤<br>


	import random  


	round = int(input("단계를 선택하세요(0,1,2,3):"))
	# round에서 단계를 선택한다
	count = int(input("몇 개의 문제를 풀까요?(1~5):"))
	# count에서 몇 문제를 풀지 선택한다
	score = 0
	# score는 정답의 갯수를 출력한다


	for i in range(count):
	#for 반복문으로 문제의 갯수만큼 반복한다.

		x = random.randint(1,100)
		y = random.randint(1,100)
		xy_m = x-y #빼기
		xy_p = x+y #더하기
		xy_mp = x*y #곱하기
		xy_d = x//y #나누기
		xy_list = [xy_m,xy_p,xy_mp,xy_d] #변수를 담은 리스트 


		if round == 0: #0단계 - 음수 없는 빼기
			if x>=y:
				print("{}-{}=".format(x,y))
			else:
				xy_m = y-x
				print("{}-{}=".format(y,x))
		elif round == 1: #1단계 - 음수 있는 빼기
			print("{}-{}=".format(x,y))
		elif round == 2: #2단계 - 빼기 더하기 랜덤
			xy_list = random.choice([xy_m,xy_p])
			if xy_list == xy_m:
				print("{}-{}=".format(x,y))
			elif xy_list == xy_p:
				print("{}+{}=".format(x,y))
		else: #3단계 - 빼기, 더하기, 나누기, 곱하기 랜덤
			xy_list = random.choice([xy_m,xy_p,xy_mp,xy_d])
			if xy_list == xy_m:
				print("{}-{}=".format(x,y))
			elif xy_list == xy_p:
				print("{}+{}=".format(x,y))
			elif xy_list == xy_mp:
				print("{}*{}=".format(x,y))
			elif xy_list == xy_d:
				print("{}//{}=".format(x,y))


		answer = int(input("정답은:")) #정답은 직접 입력한다

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
			
	#학점을 계산한다 		
	if score == count: # 다 맞았으면 A학점
	print("A학점 입니다")
	elif score >= count/2: #문제 중에 반 넘게 맞았으면 B학점
		print("B학점 입니다")
	elif score < count/2 and score != 0: #문제 중에 반 넘게 틀렸으면 C학점
		print("C학점 입니다")
	else: #모두 틀렸으면 F학점 
		print("F학점 입니다")	

	print(score,'개 맞았습니다')
