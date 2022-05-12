from datetime import date

import mysql.connector

import Speak


class event:

    def __init__(self):

        sql_connection = mysql.connector.connect(host="localhost", user="root", password="", database="data_store")

        count: int = 1

        connection = sql_connection.cursor()

        today = date.today()

        SQL = "SELECT activity from to_do where task_date = '" + str(today) + "';"

        print(SQL)

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            Speak.Speak(x)

            count = count + 1

        sql_connection.close()