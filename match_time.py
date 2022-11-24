#This part of the program asks for an input of a single line space separated input of 3 integer inputs
print("Enter the inputs of Num of teams, match time and wait time simultaneously in a single line")
Num,match_time,wait_time = input().split()
time = 0
Num = int(Num)
while(Num != 1):
	time = time + int(match_time)
	if (Num != 2):
		time = time + int(wait_time)
	Num = Num//2
print(time)
