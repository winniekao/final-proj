import random
g = open("gender",'w')

with open("user_id") as f:
	for line in f:
		likes = random.randint(0, 1)
		g.write(str(likes))
		g.write('\n')
g.close()

