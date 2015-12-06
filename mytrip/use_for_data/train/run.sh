#!/bin/bash

sed -e '1d' trip_id > trip_id_temp

python trip_id2no.py

python random_likes.py

paste trip2no trip_id_temp > no_match_trip


sed -e '1d' idnum > user_id_temp

python user_id2no.py

paste user2no user_id_temp > no_match_user


cp likes target-train
