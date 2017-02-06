#!/usr/bin/env bash

# get logs from repo
(
cd ~/sm10work
./repo forall \
-p \
-c git log --since="2017-1-1" --until="2017-2-6" \
--stat \
--date=iso  # print excel friendly date format
) | ./pars.py

