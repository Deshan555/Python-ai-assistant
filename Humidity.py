
import mysql.connector

import Config

import Speak


class get_humidity:

    def __init__(self):

        sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD,database=Config.DATABASE_NAME)

        connection = sql_connection.cursor()

        SQL = "SELECT humidity from real_time_box_1;"

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            Speak.Speak("Current Humidity In Green House " + str(x[0]) + ' percentage')

            print("Current Humidity In Green House " + str(x[0]) + ' percentage')

        sql_connection.close()
