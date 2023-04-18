#!/bin/usr/env python3

#------------------------Libraries and Dictionaries

from configparser import ConfigParser
from tkinter import *
import requests
import json
from datetime import datetime

# ------------------------------ConfigParser for super secret api_key

# <---------------Please replace with exact file path where file is stored.
file = 'G:\Github\HotOrNot-Python-Extra-Credit\config.ini'
config = ConfigParser()
config.read(file)
api_key = config['secret']['api_key']

# --------------------------------GUI Pop up Box settings

gui = Tk()
gui.geometry("400x700")  # size of the window by default
gui.title("Is it Hot or Not: Pants or Shorts?")


# ----------------------Functions to fetch and display weather info
city_value = StringVar()

# ----------------------------------This is the section I least understood and also least changed


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()



# -----------------------------------This is the where the information is stored and held until called upon later to print in Pop up box


def showWeather():
    city_name = city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?' + '&units=imperial&' + \
        "appid=" + api_key + "&q=" + city_name

    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")
    if weather_info['cod'] == 200:
        temp = int(weather_info['main']['temp'])
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        if temp > 65:
            coat_or_shorts = 'Wear Shorts'
        else:
            coat_or_shorts = 'Wear a Coat'

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        weather = f"\nWeather of: {city_name}\nTemperature (Farenheit): {temp}°\nCoat or Shorts?: {coat_or_shorts}\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tNot Found on Planet Earth, Enter valid City Name !!"
    tfield.insert(INSERT, weather)
# -------------------------------------------------This is the settings for the GUI/cosmetic part of the APP


city_head = Label(gui, text='Enter City Name', font='Arial 20 bold').pack(
    pady=10)

inp_city = Entry(gui, textvariable=city_value,
                 width=24, font='Arial 20 bold').pack()

Button(gui, command=showWeather, text="Check Weather", font="Arial 16",
       bg='grey', fg='black', activebackground="red", padx=5, pady=5).pack(pady=20)

weather_now = Label(gui, text="The Weather is:",
                    font='arial 20 bold').pack(pady=10)

tfield = Text(gui, width=46, height=10)
tfield.pack()
# -------------------------------------closed in mainloop to run
gui.mainloop()
