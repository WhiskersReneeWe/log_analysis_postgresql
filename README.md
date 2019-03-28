# Log Analysis Project with PostgreSQL
## Project No.1 from Udacity's Fullstack Nanodegree

## Python Packages
* psycopg2
* datetime

## File DescriptionS
There are only two files in this repository,

1. log_analysis.py (Source code for SQL queries and other related "dirty" work when interacting with the database)
2. p1_out.txt (expected output in .txt format)

## Guided Usage
You will only need to use the first .py file when interacting with the database in front of you. <br/> 
In the context of this project, I assume that you have a database named 'news' that is populated <br/>
and ready to be connected. <br/>

You can follow the steps listed below to get all 3 answers from this project in one go.

1. Fire up a termnial (I used Git Bash)
2. Change your working directory, if you haven't done so, to where the live database is running on your Virtual Machine
3. Download log_analysis.py into the current working directory
4. run `python log_analysis.py > your_output.txt`

## Result

You should be able to read through the log analysis when you open the your_output.txt file by <br/>
following the above steps.

## Important Note 

The source code replies on a couple of views I created when querying through the database. I will list <br/>
the names of all the views to be created and their descriptions below.

1. log_art_match
  * a relation that joins log table and articles table
2. author_views: 
  * a relation that shows the name of each author and the number of views of each article from this author
3. temp_tbl:
  * similar to author_views but simpler.
  * This is the final relation I used to query for Question 2
4. date_error:
  * a relation describes the number of Error Responses, i.e., the number of "404 NOT FOUND" on each day
5. date_status:
  * a relation describes the total number of Ruquest status on each day
6. error_tbl:
  * a relation describes the number of Error responses and total number of request status on each day
  * This is the final relation I used to query for Question 3
  
## Acknowledgement

I sincerely thank the amazing Udacity community for my adventure with Python and SQL!





