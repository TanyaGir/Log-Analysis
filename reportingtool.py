import psycopg2
from datetime import datetime


def connect(query):
    try:
        database = psycopg2.connect(database="news")
        c = database.cursor()
        c.execute(query)
        query_results = c.fetchall()
        database.close()
        return query_results
    except BaseException:
        print("Sorry, unable to fetch results from Database")


def print_results(query_results):
    for i in query_results:
        print('"' + str(i[0]) + '"' + ' -- ' + str(i[1]))
        print '\n'


def print_articles():
    print("Most popular articles")
    query1 = """
             select articles.title, count(*) as views
             from articles join log
             on articles.slug = substring(log.path,10)
             where path != '/'
             group by substring(log.path, 10),articles.title
             order by views desc
             limit 3
             """
    popular_articles = connect(query1)
    print_results(popular_articles)


def print_authors():
    print("Most popular authors")
    query2 = """
             select name, view from authors, logviews
             where authors.id = logviews.author
             order by view desc
             limit 4
             """
    popular_authors = connect(query2)
    print_results(popular_authors)


def print_err_result():
    print("The days on which more than 1% of the requests lead to errors")
    print '\n'
    query3 = """
             select day , error from lastview where (error > 1.0)
             """
    err_result = connect(query3)
    for i, j in err_result:
        mydate = i
        myerr = j
        print(mydate.strftime("%B %d, %Y") + ' -- ' + str(myerr))

if __name__ == "__main__":
    print_articles()
    print_authors()
    print_err_result()
