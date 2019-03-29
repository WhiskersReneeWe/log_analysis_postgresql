#!/usr/bin/python3

import psycopg2
import datetime

print('Hi, this is my LOG ANALYSIS project!')
print('Thanks for reviewing it!')

print('\n')

def connect_db():
    DBNAME = "news"
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print "Unable to connect!"
        print e.pgerror
        print e.diag.message_detail
        sys.exit(1)
    else:
        print "Connected!"
        return db

def answer_q1():

    query1 = "select path, count(*) as total_views from log \
    group by path order by total_views DESC \
    limit 4;"

    db = connect_db()

    # db = psycopg2.connect(database=DBNAME)
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

    query2 = "select name, SUM(temp_tbl.num_viewed) as all_views \
    FROM temp_tbl \
    GROUP BY name \
    ORDER BY all_views DESC;"

    db = connect_db()
    cursor = db.cursor()
    #cursor.execute(query20)
    #cursor.execute(query21)
    #cursor.execute(query22)
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


    # the above queries create a table that is intuitive to see the errors and total number of responses on each day
    query3 = "select time, error_rate from (select time, num_errors / CAST(num_total AS float) as error_rate \
    from error_tbl) as error_rate_tbl \
    where error_rate > 0.01 \
    ORDER BY error_rate DESC;"
    db = connect_db()
    cursor = db.cursor()
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




