sed 's/^/&0 /g' no_trip.txt > trip_place_temp1

sed 's/&:1 /g' no_trip_temp1 > trip_place_temp2

sed 's/& 249/g' no_trip_temp2 > trip_place_temp1

paste -d : trip_place_temp1 dmite > trip_place_temp2

sed 's/& 250/g' trip_place_temp2 > trip_place_temp1

paste -d : trip_place_temp1 latitude > trip_place_temp2

sed 's/& 251/g' trip_place_temp2 > trip_place_temp1

paste -d : trip_plave_tmep1 longitude > trip_place_temp2

cp trip_place_temp2 rel.trip
 
