g = open("no2tirp",'w')

d ={}

with open("no_match_trip") as f:
	for line in f:
		(val, key) = line.split()
		d[int(val)] = key
with open("rel.trip.test") as h:
	for line in h:
		a = line.split()
		b = a[0]
		print b
		no = d[int(b)]
		g.write(no)
		g.write('\n')

g.close()		 


