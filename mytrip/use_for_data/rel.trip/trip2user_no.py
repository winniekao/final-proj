g = open("no_trip",'w')

d ={}

with open("no_match_trip") as f:
	for line in f:
		(val, key) = line.split()
		d[int(key)] = val
with open("trip_id_temp") as h:
	for line in h:
		a = line.split()
		b = a[0]
		print b
		no = d[int(b)]
		g.write(no)
		g.write('\n')

g.close()		 


