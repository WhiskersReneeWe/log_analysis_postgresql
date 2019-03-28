#!/usr/bin/python

import psycopg2
import datetime

print('Hi, this is my LOG ANALYSIS project!')
print('Thanks for reviewing it!')

print('\n')

def answer_q1():

    DBNAME = "news"
    query1 = "select path, count(*) as total_views from log \
    group by path order by total_views DESC \
    limit 4;"

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query1)
    top_arts = cursor.fetchall()
    db.close()

    # formatting the result
    top_3 = top_arts[1:]
    for i in range(len(top_3)):
        name = top_3[i][0].split('/',2)[-1] 
        print("Top {} article: {} with {} viewed in total".format((i+1), name, top_3[i][1]))


def answer_q2():
    DBNAME = "news"

    query20 ="create view log_art_match as SELECT log.path, log.id, articles.slug, articles.author \
    FROM log join articles ON log.path LIKE CONCAT('%', articles.slug, '%');"

    query21 = "create view author_views as \
              select log_art_match.id, log_art_match.slug, authors.name FROM \
              log_art_match JOIN authors ON log_art_match.author = authors.id;"

    query22 = "create view temp_tbl as \
    select name, count(*) num_viewed from author_views \
    GROUP BY name, slug \
    ORDER BY num_viewed DESC;"


    query2 = "select name, SUM(temp_tbl.num_viewed) as all_views \
    FROM temp_tbl \
    GROUP BY name \
    ORDER BY all_views DESC;"

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query20)
    cursor.execute(query21)
    cursor.execute(query22)
    cursor.execute(query2)

    popular_authors = cursor.fetchall()
    db.close()

    # formatting the result
    authors_pop = []
    for i in range(len(popular_authors)):
        name = popular_authors[i][0]
        views = popular_authors[i][1]
        temp = name + "---" + str(views) +" views."
        authors_pop.append(temp)

    print(authors_pop)


#On which days did more than 1% of requests lead to errors?

def answer_q3():

    DBNAME = "news"

    query0 = "create view date_error as \
	          SELECT time, COUNT(*) AS num_errors from (SELECT CAST(time AS DATE), status FROM log) as date_status \
              WHERE status = '404 NOT FOUND' \
              GROUP BY time;"

    query1 = "create view date_status as \
              SELECT time, COUNT(*) AS num_total from (SELECT CAST(time AS DATE), status FROM log) as date_status \
              GROUP BY time;"

    query2 = "create view error_tbl AS SELECT date_error.time, date_error.num_errors, date_status.num_total \
              FROM date_error join date_status \
              on date_error.time = date_status.time;"

    # the above queries create a table that is intuitive to see the errors and total number of responses on each day
    query3 = "select time, num_errors / CAST(num_total AS float) as error_rate \
    from error_tbl \
    where num_errors > 0.001 \
    ORDER BY num_errors DESC;"

    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query0)
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    dates_errors = cursor.fetchall()
    db.close()

    # formatting dates and time
 
    for i in range(len(dates_errors)):
        day = dates_errors[i][0].strftime('%b %d, %Y')
        err_pct = str(float(round(dates_errors[i][1] * 100, 1))) + "%" 
        temp = day + "---" + err_pct
        print(temp + '\n')
    

    







#######Testing#######
print('Answers to Question 1:' + '\n')
answer_q1()
print('\n')
print('Answers to Question 2:' + '\n')
answer_q2()
print('\n')
print('Answers to Question 3:' + '\n')
answer_q3()

print('Thank you again for your patience!')




