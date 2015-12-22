g = open ("rate_sort20",'w')

d = {}
e = {}
a = ""
b = ""
with open("rate_trip_user") as f:
	for line in f:
		(user, trip, rate) = line.split()
		b = user
		if(b != a and a!=""):
			i = 0
			for key, value in sorted(user_no.iteritems(),key = lambda (k,v): (v,k), reverse =True):
					i = i+1
					print "%s %s %s" % (a,key,value)
					g.write(a)
					g.write('\t')
					g.write(key)
					g.write('\t')
					g.write(value)
					g.write('\n')
					
					if i == 20:break
#		print trip
#		print rate
#		print user
		d[trip] = rate

		a = user
		user_no = user
		user_no = {}
		user_no.update(d)
print user_no

g.close()
