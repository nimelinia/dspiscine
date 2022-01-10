#!/bin/sh

while IFS=, read -r id created_at name has_test alternate_url
do
    case "$created_at" in
      *created_at*) COLUMN="\"id\", \"created_at\", \"name\", \"has_test\", \"alternate_url\"";;
      *[1-9]*)
        if test -e "${created_at:0:12}".csv;
        then
          echo "${id}," "${created_at}," "${name}," "${has_test}," "${alternate_url}" >> "${created_at:0:12}".csv
        else
          echo "${COLUMN}" >> "${created_at:0:12}".csv
          echo "${id}," "${created_at}," "${name}," "${has_test}," "${alternate_url}" >> "${created_at:0:12}".csv
        fi;;
    esac
done < '../ex03/hh_positions.csv'
