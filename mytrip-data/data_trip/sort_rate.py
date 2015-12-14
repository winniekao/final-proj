g = open ("rate_sort20",'w')

d = {}
e = {}
a = ""
b = ""
i=0
with open("rate_trip_user") as f:
	for line in f:
		(user, trip, rate) = line.split()
		b = user
		if(b != a and a!=""):
			for key, value in sorted(user_no.iteritems(),key = lambda (k,v): (v,k), reverse =True):
					i = i+1
					if i==21:break
					print "%s %s %s" % (a,key,value) 
#		print trip
#		print rate
#		print user
		d[trip] = rate

		a = user
		user_no = user
		user_no = {}
		user_no.update(d)
#		print user

g.close()
