#!/usr/bin/env bash

# get logs from repo
(
cd ~/sm10work
# -p for printing the project names
# --date=iso for printing user friendly dates
# --stat for printing the file changes
./repo forall \
-p \
-c git log --since="2017-1-1" --until="2017-2-6" \
--stat \
--date=iso  # print excel friendly date format
) | ./pars.py

