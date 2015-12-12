#!/bin/bash

../bin/convert --ifile target-train --ofilex target-train.x --ofiley target-train.y
../bin/convert --ifile target-test --ofilex target-test.x --ofiley target-test.y
../bin/convert --ifile rel.user --ofilex rel.user.x --ofiley rel.user.y
../bin/convert --ifile rel.trip --ofilex rel.trip.x --ofiley rel.trip.y

../bin/transpose --ifile target-train.x --ofile target-train.xt
../bin/transpose --ifile target-test.x --ofile target-test.xt
../bin/transpose --ifile rel.user.x --ofile rel.user.xt
../bin/transpose --ifile rel.trip.x --ofile rel.trip.xt

../bin/libFM -task r -train target-train -test target-test -dim ’1,1,8’ --relation rel.user,rel.trip -out out
