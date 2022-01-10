#!/bin/sh

#cat '../ex01/hh.csv' | sort -t ',' -k2.4n -k2.7 -k2.10 -k2.12 -k2 -k1.2 > hh_sorted.csv
cat '../ex01/hh.csv' | sort -t ',' -k2,2 -k1,1 > hh_sorted.csv