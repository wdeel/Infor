list.py includes the first problem presented during the interview.  It 
iterates through a list and adds the number (key), as well as its number 
of occurences (value) to a dictionary.  

Ran with Python version 3.6.9 

The SQL folder contains files dealing with the second problem presented
during the interview.  CreateEvents.sql is code that creates the Events
table with 5 fields, one of which is the primary key (EventId).  

PopulateEvents.sql has 4 Insertions into the database, populating the
Events table with the information provided during the coding challenge.

Finally, Query.sql contains the query to the Events table that shows
all EventIds in the Events table that have the same resourceId, as well
as overlapping times.  I did not receive the expected output of only one
row of results however, received the following which I believe to be a 
duplicate.  I attempted to use DISTINCT and GROUP BY in my query to only
return one result, but it did not work.  See below

Event1Id    Event2Id
  100         101
  101         100


DropEvents.sql will remove the Events table from the database

To run the files, I logged into a Clemson University lab machine
remotely and utilized a mysql server that I created during a 
summer class.  Once I logged into the mysql server, i would type
SOURCE <filename>; and the code of the file would run.  For example:
SOURCE CreateEvents.sql; would create the Events table in the database.

MYSQL Version used: 
mysql  Ver 8.0.22-0ubuntu0.20.04.3 for Linux on x86_64 ((Ubuntu))
