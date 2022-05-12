from datetime import date

import mysql.connector

import Speak


class event:

    def __init__(self):

        sql_connection = mysql.connector.connect(host="localhost", user="root", password="", database="data_store")

        count: int = 0

        event_list: list = []

        connection = sql_connection.cursor()

        today = date.today()

        SQL = "SELECT activity from to_do where task_date = '" + str(today) + "';"

        print(SQL)

        connection.execute(SQL)

        result = connection.fetchall()

        length = (len(result))

        count: int = 0

        if length == 0:

            Speak.Speak('Sir No Events scheduled today')

        else:

            for x in result:

                event_number = count + 1

                event_info = result[count]

                Speak.Speak('Event Number ' + str(event_number))

                Speak.Speak('Event Info ' + str(event_info))

                count = count + 1

        sql_connection.close()
