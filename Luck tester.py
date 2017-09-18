
# 100个人 每个人轮流随机给别人1元钱 循环N次之后的财富分布

import random

money = {}
number_people = 100
init_money = 500
cycle_times = 5000

def exchange_money (dict):
	for people in dict:
		dict[people] = dict[people] - 1
		lucky_person = random.randint(0,number_people-1)
		dict[lucky_person] = dict[lucky_person] + 1
		

for i in range(number_people):
	money[i] = init_money
	
for i in range(cycle_times):
	exchange_money (money)

	
max = float("-inf")
min = float("inf")
for i in range(number_people):
	if money[i] > max:
		max = money[i]
	if money[i] < min:
		min = money[i]
#print(money)
print('richest {} , poorest {}'.format(max, min))