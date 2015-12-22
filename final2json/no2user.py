import json
g = open("data.json",'w')

d ={}
a = ""
b = ""
c = ""
g.write('{')
i = 0

with open("final") as f:
	for line in f:
		line = line.replace("\n","")
		(user_id, idnum, trip_id, rate, photo,trip_name) = line.split('\t')
		i = i+1
		b = user_id
		print b
		print a
		if(b != a):
			g.write("\"")
			g.write(user_id)
			g.write("\"")
			g.write(":")
			g.write("{")
		g.write("\"")
		g.write(trip_id)
		g.write("\"")
		g.write(":")
		g.write("[")
		g.write("\"")
		g.write(photo)
		g.write("\"")
		g.write(",")
		g.write("\"")
		g.write(trip_name)
		g.write("\"")
		g.write("]")
#		a = user_id
		if( i % 20 == 0):
			g.write("}")
			g.write(",")
			g.write("\n")
		else:
			g.write(",")
#		i = i+1
		a = user_id		 
		print i
#with open("rel.user.test") as h:
#	for line in h:
#		a = line.split()
#		b = a[0]
#		print b
#		no = d[int(b)]
#		g.write(no)
#		g.write('\n')

g.close()		 


