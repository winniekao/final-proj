g = open("rel.trip.test","w")

with open("user2no") as h:
	for line in h:
		with open("trip2no") as f:
			for line in f:
				trip = line.split()
				trip_no = trip[0] 
#				print trip_no
				g.write(trip_no)
				g.write('\n')
g.close

