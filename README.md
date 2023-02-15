# PostgreSQL Test

Following CI Walkthrough Tutorial

## Examples

Create CSV File using data extracted from Chinook Database: 
`\copy (SELECT * FROM "Track" WHERE "Composer" = 'Queen') TO 'test.csv' WITH CSV DELIMITER ',' HEADER;
`