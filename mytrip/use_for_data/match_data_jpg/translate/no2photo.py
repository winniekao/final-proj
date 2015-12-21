g = open("final_photo",'w')

d ={}

h = {}

with open("id_no") as f:
	for line in f:
		(trip_id, no) = line.split()
		d[trip_id] = no

with open("no_photo") as i:
	for line in i:
		(no, photo) = line.split()
		h[no] = photo


with open("final_trip_id") as j:
	for line in j:
		a = line.split()
		b = a[0]
#		print b
		trip4no = d[b]
		print trip4no
		if(trip4no == 'NULL'):
			g.write('/No.jpg')
			g.write('\n')

		else:
			no4photo = h[trip4no]
			if(no4photo == '/No'):
				g.write('/No.jpg')
				g.write('\n')

			else:
				g.write(no4photo)
				g.write('\n')

g.close()		 


