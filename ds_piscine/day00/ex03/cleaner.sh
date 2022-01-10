#!/bin/sh

while IFS=, read -r id created_at name has_test alternate_url
do
    case "$name" in
       *[Jj]unior*[Mm]iddle*[Ss]enior*|*[Jj]unior*[Ss]enior*[Mm]iddle*|*[Mm]iddle*[Jj]unior*[Ss]enior*|*[Mm]iddle*[Ss]enior*[Jj]unior*|*[Ss]enior*[Mm]iddle*[Jj]unior*|*[Ss]enior*[Jj]unior*[Mm]iddle*) echo "${id}," "${created_at}," "${name/*/\"Junior/Middle/Senior\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *[Ss]enior*[Mm]iddle*|*[Mm]iddle*[Ss]enior*) echo "${id}," "${created_at}," "${name/*/\"----Middle/Senior----\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *[Ss]enior*[Jj]unior*|*[Jj]unior*[Ss]enior*) echo "${id}," "${created_at}," "${name/*/\"----Middle/Senior----\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *[Jj]unior*[Mm]iddle*|*[Mm]iddle*[Jj]unior*) echo "${id}," "${created_at}," "${name/*/\"----Middle/Senior----\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *[Ss]enior*) echo "${id}," "${created_at}," "${name/*/\"--------Senior-------\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *[Mm]iddle*) echo "${id}," "${created_at}," "${name/*/\"--------Middle-------\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *[Jj]unior*) echo "${id}," "${created_at}," "${name/*/\"--------Junior-------\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
        \"name\") echo "${id}," "${created_at}," "${name}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
       *) echo "${id}," "${created_at}," "${name/*/\"---------------------\"}," "${has_test}," "${alternate_url}" >> hh_positions.csv;;
    esac
done < '../ex02/hh_sorted.csv'