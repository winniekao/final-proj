cut -f 1 trip_place  > trip_id
sed -i '1d' trip_id 
cut -f 2 trip_place  > dtime
sed -i '1d' dtime 
sed -i 's/NULL/0/g' dtime
sed -i 's/-//g' dtime
sed -i 's/://g' dtime
sed -i 's/ //g' dtime

cut -f 3 trip_place  > longitude
sed -i '1d' longitude 
sed -i 's/NULL/0/g' longitude

cut -f 4 trip_place  > latitude
sed -i '1d' latitude
sed -i 's/NULL/0/g' latitude

python trip2no.py

sed 's/^/&0 /g' tripinno > trip_id_temp1
sed 's/$/&:1 249/g' trip_id_temp1 > trip_id_temp2

paste -d : trip_id_temp2 dtime > trip_id_temp1

sed 's/$/& 250/g' trip_id_temp1 > trip_id_temp2

paste -d : trip_id_temp2 longitude > trip_id_temp1


sed 's/$/& 251/g' trip_id_temp1 > trip_id_temp2

paste -d : trip_id_temp2 latitude > trip_id_temp1

cp trip_id_temp1 rel.trip



