import pickle

d = {}
c = {}

mydict = {}
a= ""
b=""

with open("final")as f:
	for line in f:
		(user_id, trip_id, photo) = line.split()
		b = user_id
		if(b!=a and a!=""):
			mydict.update(c)
		d[trip_id] = photo
		
		a = user_id
		user_no = user_id
		c[user_id] = d
		c.update(d)
#		print user_no
#		mydict.update(user_no)
print mydict
output = open('myfile.pkl','wb')
pickle.dump(mydict, output)

output.close()		


pkl_file = open('myfile.pkl','rb')
mydict2 = pickle.load(pkl_file)
pkl_file.close()

#print mydict2

