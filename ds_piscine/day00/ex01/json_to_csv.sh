#!/bin/sh
jq -f -s --raw-output  ./filter.jq '../ex00/hh.json' > hh.csv


