
import mysql.connector

import Config

import Speak


class get_SoilMoist:

    def __init__(self):

        sql_connection = mysql.connector.connect(host=Config.HOST_NAME, user=Config.USER_NAME, password=Config.PASSWORD,database=Config.DATABASE_NAME)

        connection = sql_connection.cursor()

        SQL = "SELECT Soil_Moisture from real_time_box_2;"

        connection.execute(SQL)

        result = connection.fetchall()

        for x in result:

            print("Current Soil Moisture Level In Indoor Growing Room like " + str(x[0]) + ' percentage')

            Speak.Speak("Current Soil Moisture Level In Indoor Growing Room like " + str(x[0]) + 'percentage')

        sql_connection.close()
