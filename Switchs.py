
import Request_web

import Speak


def Water_on():

    Speak.Speak('Water Pump Will turn on')

    Request_web.web_requests('http://192.168.43.178/1/on', 'Water Pump turn on successfully')


def Water_off():

    Speak.Speak('Water Pump Will turn off')

    Request_web.web_requests('http://192.168.43.178/1/off', 'Water Pump turn off successfully')


def sprinkler_on():

    Speak.Speak('sprinkler Will turn on')

    Request_web.web_requests('http://192.168.43.178/2/on', 'sprinkler turn on successfully')


def sprinkler_off():

    Speak.Speak('sprinkler Will turn off')

    Request_web.web_requests('http://192.168.43.178/2/off', 'sprinkler turn off successfully')
