WITH latests AS (
    SELECT DISTINCT ON (event_type) event_type, value, time
    FROM events
    ORDER BY event_type, time DESC
), second_latests AS (
    SELECT DISTINCT ON (event_type) event_type, value, time
    FROM (
        SELECT * FROM events
        EXCEPT
        SELECT * FROM latests
    ) AS non_latests
    ORDER BY event_type, time DESC
)
SELECT l.event_type, l.value - sl.value AS value
FROM latests l JOIN second_latests sl ON l.event_type = sl.event_type
ORDER BY l.event_type
