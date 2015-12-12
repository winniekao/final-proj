
sed 's/^/&0 /g' user_id2no > user_id_temp1
sed 's/$/&:1 199/g' user_id_temp1 >user_id_temp2

paste -d : user_id_temp2 gender > user_id_temp1

cp user_id_temp1 rel.user
