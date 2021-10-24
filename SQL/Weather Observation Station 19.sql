/*
MS SQL Server Syntax
*/
SELECT cast(round(SQRT(square(max(lat_n)-MIN(lat_N)) + square(MAX(long_w)-MIN(Long_w))),4) as numeric(18,4)) FROM STATION 
