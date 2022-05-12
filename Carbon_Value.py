
import mysql.connector

import Speak


class event:

    def __init__(self):

        sql_connection = mysql.connector.connect(host="localhost", user="root", password="", database="data_store")

        connection = sql_connection.cursor()

        SQL = "SELECT gas_value from real_time_box_1;"

        print(SQL)

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            Speak.Speak("Current Carbon dioxide Percentage in Green House " + str(x) + 'parts per million')

        sql_connection.close()
