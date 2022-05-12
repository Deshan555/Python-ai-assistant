
import mysql.connector

import Speak


class event:

    def __init__(self):

        sql_connection = mysql.connector.connect(host="localhost", user="root", password="", database="data_store")

        connection = sql_connection.cursor()

        SQL = "SELECT humidity from real_time_box_1;"

        print(SQL)

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            Speak.Speak("Current Humidity In Green House " + str(x) + 'percentage')

        sql_connection.close()
