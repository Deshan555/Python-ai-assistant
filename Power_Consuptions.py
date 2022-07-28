import psutil

import Speak


def battery_data():

    battery = psutil.sensors_battery()

    battery_present = battery.percent

    if battery.power_plugged:

        Speak.Speak("System Power Percentage Like " + str(battery_present) + "% and Power Source Connected")

    else:

        Speak.Speak("System Power Percentage Like " + str(battery_present) + "% and Power Source disconnected")



