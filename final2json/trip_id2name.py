g = open("final_trip_name",'w')

d ={}

h = {}

with open("trip_id_name") as f:
	for line in f:
		line = line.replace("\n","")
		(tid, name) = line.split('\t')
		d[int(tid)] = name
print d	
#with open("no_photo") as i:
#	for line in i:
#		(no, photo) = line.split()
#		h[no] = photo


with open("final") as j:
	for line in j:
		a = line.split('\t')
		b = a[2]
		print b
		trip4no = d[int(b)]
		print trip4no
#		if(trip4no == 'NULL'):
#			g.write('/No.jpg')
#			g.write('\n')

#		else:
#			no4photo = h[trip4no]
#			if(no4photo == '/No'):
#				g.write('/No.jpg')
#				g.write('\n')

#			else:
		g.write(trip4no)
		g.write('\n')

g.close()		 


