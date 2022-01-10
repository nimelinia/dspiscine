def tocsv:
    (map("id", "created_at", "name", "has_test", "alternate_url")
    ) as $cols
    |map(.items[] as $row
        |$cols
        |map($row[.]|tostring)
    ) as $rows
    |$cols,$rows[]
    | @csv;

tocsv