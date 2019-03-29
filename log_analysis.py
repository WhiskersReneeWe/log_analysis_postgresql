#!/usr/bin/python
import psycopg2
import datetime

print('Hi, this is my LOG ANALYSIS project!')
print('Thanks for reviewing it!')


def connect_db():

    DBNAME = "news"
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect!")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)
    else:
        print("Connected!")
        return db

def get_top3_articles():
    """fetch the top 3 most popular articles in the database"""
    
    
    query1 = "select path, count(*) as total_views from log \
    group by path order by total_views DESC \
    limit 4;"

    cursor = db.cursor()
    cursor.execute(query1)
    top_arts = cursor.fetchall()
    # formatting the result
    top_3 = top_arts[1:]
    for i in range(len(top_3)):
        name = top_3[i][0].split('/', 2)[-1]
        print("Top {} article: {} with {} viewed in total"
              .format((i+1), name, top_3[i][1]))


def get_top3_authors():
     """fetch the top 3 most popular authors in the database"""

        
    query2 = "select name, SUM(temp_tbl.num_viewed) as all_views \
    FROM temp_tbl \
    GROUP BY name \
    ORDER BY all_views DESC;"
    
    cursor = db.cursor()
    cursor.execute(query2)
    popular_authors = cursor.fetchall()

    # formatting the result
    authors_pop = []
    for i in range(len(popular_authors)):
        name = popular_authors[i][0]
        views = popular_authors[i][1]
        temp = name + "---" + str(views) + " views."
        authors_pop.append(temp)

    print(authors_pop)


def find_error_date():
    """Get the date that has Request error rate that is higher than 1%"""

    query3 = "select time, error_rate from (select time, num_errors \
    / CAST(num_total AS float) as error_rate \
    from error_tbl) as error_rate_tbl \
    where error_rate > 0.01 \
    ORDER BY error_rate DESC;"
    
    cursor = db.cursor()
    cursor.execute(query3)
    dates_errors = cursor.fetchall()

    # formatting dates and time

    for i in range(len(dates_errors)):
        day = dates_errors[i][0].strftime('%b %d, %Y')
        err_pct = str(float(round(dates_errors[i][1] * 100, 1))) + "%"
        temp = day + "---" + err_pct
        print(temp + '\n')

if __name__ == "__main__":
    print('Top 3 popular articles:' + '\n')
    db = connect_db()
    answer_q1()
    print('\n')
    print('Top 3 popular authors:' + '\n')
    answer_q2()
    print('\n')
    print('More than 1 percent request errors on this day:' + '\n')
    answer_q3()
    db.close()
    print('Thank you again for your patience!')
