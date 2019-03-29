# Log Analysis Project with PostgreSQL
## Project No.1 from Udacity's Fullstack Nanodegree

## Python Packages
* psycopg2
* datetime

## File Descriptions
There are only two files in this repository,

1. log_analysis.py (Source code for SQL queries and other related "dirty" work when interacting with the database)
2. p1_out.txt (expected output in .txt format)

## Guided Usage
You will only need to use the first .py file when interacting with the database in front of you. <br/> 
In the context of this project, I assume that you have a database named 'news' that is populated <br/>
and ready to be connected. <br/>

You can follow the steps listed below to get all 3 answers from this project in one go.

0. Download the database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Fire up a termnial (I used Git Bash)
2. Change your working directory, if you haven't done so, to where the database files are
3. Unzip the file you downloaded from step 0 into the current working directory
4. run `psql -d news -f newsdata.sql` in your command line
5. Once everything looks good, then run `python log_analysis.py > your_output.txt`

## Result

You should be able to read through the log analysis when you open the your_output.txt file by <br/>
following the above steps.

## Views Statement and code

The source code relies on a couple of views I created on the database when querying through the database. I will list <br/>
the names of all the views to be created and their code below,

1. log_art_match (a relation that joins log table and articles table)

 `view1 = "create view log_art_match as SELECT log.path, log.id, articles.slug, articles.author 
            from log, articles 
            WHERE log.path = '/article/' || articles.slug;"`

2. author_views (a relation that shows the name of each author and the number of views of each article from this author)

  `view2 = "create view author_views as 
            select log_art_match.id, log_art_match.slug, authors.name FROM 
            log_art_match JOIN authors ON log_art_match.author = authors.id;"`

3. temp_tbl:

  `view3 = "create view temp_tbl as 
            select name, count(*) num_viewed from author_views 
            GROUP BY name, slug 
            ORDER BY num_viewed DESC;"`

4. date_error (a relation describes the number of Error Responses, i.e., the number of "404 NOT FOUND" on each day)
  
  
  `view4 = "create view date_error as 
	    SELECT time, COUNT(*) AS num_errors from (SELECT CAST(time AS DATE), status FROM log) as date_status 
            WHERE status = '404 NOT FOUND' 
            GROUP BY time;"`
              
5. date_status (a relation describes the total number of Ruquest status on each day)

  `view5 = "create view date_status as
            SELECT time, COUNT(*) AS num_total from (SELECT CAST(time AS DATE), status FROM log) as date_status
            GROUP BY time;"`

6. error_tbl:
  * a relation describes the number of Error responses and total number of request status on each day
  * This is the final relation I used to query for Question 3
  
  
  `view6 = "create view error_tbl AS SELECT date_error.time, date_error.num_errors, date_status.num_total 
            FROM date_error join date_status 
            on date_error.time = date_status.time;"`
  
## Acknowledgement

I sincerely thank the amazing Udacity community for my adventure with Python and SQL!





