#!/bin/sh

COUNTER_J=0
COUNTER_M=0
COUNTER_S=0

while IFS=, read -r id created_at name has_test alternate_url
do
    case "$name" in
       *[Ss]enior*) ((COUNTER_S=$COUNTER_S+1));;
    esac
    case "$name" in
       *[Mm]iddle*) ((COUNTER_M=$COUNTER_M+1));;
    esac
    case "$name" in
       *[Jj]unior*) ((COUNTER_J=$COUNTER_J+1));;
    esac
done < '../ex03/hh_positions.csv'
echo "\"name\"," "\"count\"" >> hh_uniq_positions.csv
echo "\"Junior\"," $COUNTER_J >> hh_uniq_positions.csv
echo "\"Middle\"," $COUNTER_M >> hh_uniq_positions.csv
echo "\"Senior\"," $COUNTER_S >> hh_uniq_positions.csv
