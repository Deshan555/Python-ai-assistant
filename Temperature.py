
import mysql.connector

import Speak

import Config


class event:

    def __init__(self):

        sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD, database=Config.DATABASE_NAME)

        connection = sql_connection.cursor()

        SQL = "SELECT temperature from real_time_box_1;"

        print(SQL)

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            Speak.Speak("Current Temperature in Green House " + str(x) + 'in kelvin')

        sql_connection.close()
