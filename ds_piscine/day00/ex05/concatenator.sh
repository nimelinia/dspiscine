#!/bin/sh

awk '!a[$0]++' *.csv > hh_positions.csv