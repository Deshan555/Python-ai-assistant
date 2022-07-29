
import mysql.connector

import Config

import Speak


class get_WaterLv:

    def __init__(self):

        sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD,database=Config.DATABASE_NAME)

        connection = sql_connection.cursor()

        SQL = "SELECT Water_Level from real_time_box_2;"

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            data_get = (int(x[0])/470)*100

            print("Current Water Level In Hydroponics Area " + str(round(data_get)) + ' percentage')

            Speak.Speak("Current Water Level In Hydroponics Area " + str(round(data_get)) + 'percentage')

        sql_connection.close()
