#!/usr/bin/env python3
"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
import psycopg2


def connect_to_database():
    """Connects to the news database and return a database cursor."""
    database = psycopg2.connect("dbname=news")
    cursor = database.cursor()

    return cursor


def most_popular_three_articles(db_cursor):
    """Query and print out the 3 most popular articles."""
    query = """
            SELECT articles.title,
                   count(*)
            FROM   log,
                   articles
            WHERE  log.path like '%' || articles.slug || '%'
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('')
    print('Three most popular articles of all time')
    print('=======================================')

    for result in results:
        print('"{title}" — {count} views'.format(title=result[0],
                                                 count=result[1]))

    print('')
    return


def most_popular_authors(db_cursor):
    """Query and print out the most popular authors."""
    query = """
            SELECT authors.name,
                   count(*)
            FROM   log,
                   articles,
                   authors
            WHERE  log.path LIKE '%' || articles.slug || '%'
              AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY count(*) DESC;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('')
    print('Most popular authors of all time')
    print('================================')

    for result in results:
        print('{author} — {count} views'.format(author=result[0],
                                                count=result[1]))

    print('')
    return


if __name__ == "__main__":
    CURSOR = connect_to_database()
    most_popular_three_articles(CURSOR)
    most_popular_authors(CURSOR)
    CURSOR.close()
