import tkinter as tk
import os
from tkinter import BOTH, HORIZONTAL, CURRENT, END, TRUE, IntVar
import sys
import requests

os.chdir(os.path.dirname(os.path.abspath(__file__)))

TK_SILENCE_DEPRECATION=1
root = tk.Tk()
root.title("Weather App 2.0")
root.geometry("400x400")
root.resizable(0,0)

def search():
	global response
	url = 'https://api.openweathermap.org/data/2.5/weather'
	# Add your newly generated OpenWeatherMap API key below.
	api_key = "YOUR API KEY"
	city = city_entry.get().strip()

	if not city:
		from tkinter import messagebox
		messagebox.showwarning("Missing Input", "Please enter a city name.")
		return

	querystring = {"q": city, 'appid': api_key, 'units': 'imperial'}

	try:
		api_response = requests.get(url, params=querystring, timeout=10)
		response = api_response.json()

		if api_response.status_code != 200:
			from tkinter import messagebox
			messagebox.showerror("Weather Search Failed",
				response.get("message", "Unable to find this city."))
			return

		get_weather()

	except requests.exceptions.RequestException as error:
		from tkinter import messagebox
		messagebox.showerror("Connection Error",
			f"Could not connect to the weather service.\\n{error}")

def get_weather():
	city_name = response['name']
	city_lat = str(response['coord']['lat'])
	city_lon = str(response['coord']['lon'])

	main_weather = response['weather'][0]['main']
	description = response['weather'][0]['description']

	temp = str(response['main']['temp'])
	feels_like = str(response['main']['feels_like'])
	temp_min = str(response['main']['temp_min'])
	temp_max = str(response['main']['temp_max'])
	temp = str(response['main']['temp'])
	humidity = str(response['main']['humidity'])

	city_info.config(text=city_name + "(" + city_lat + "," + city_lon + ")", font=large_font, bg=output_color)
	weather_label.config(text="Weather: " + main_weather + ", "  + description, font=small_font, bg=output_color)
	temp_label.config(text= "Temperature: " + temp +  "F", font=small_font, bg=output_color)
	feels_label.config(text="feels like: " + feels_like + "F", font=small_font, bg=output_color)
	temp_min_label.config(text= "Min Temperature: " + temp_min + "F", font=small_font, bg=output_color)
	temp_max_label.config(text="Max Temperature: " + temp_max + "F", font=small_font, bg=output_color)
	humidity_label.config(text ="Humidity: " + humidity, font=small_font, bg=output_color)

	city_info.pack(pady=3)
	weather_label.pack(pady=3)
	temp_label.pack(pady=3)
	feels_label.pack(pady=3)
	temp_min_label.pack(pady=3)
	temp_max_label.pack(pady=3)
	humidity_label.pack(pady=3)
	

sky_color = "#ADDCFF"
grass_color = "#ADDCFF"
output_color = "#DDF0FF"
input_color = "#DDF0FF"
text_colour = "#003A66"
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)


skyframe = tk.Frame(root, bg=sky_color, height=250)
grass_frame = tk.Frame(root, bg=grass_color)


skyframe.pack(fill=BOTH, expand=TRUE)
grass_frame.pack(fill=BOTH, expand=TRUE)

outputframe = tk.LabelFrame(skyframe, bg=output_color, width=325, height=225)
input_frame = tk.LabelFrame(grass_frame, bg=input_color, width=325)


outputframe.pack(pady=30)
outputframe.pack_propagate(0)
input_frame.pack(pady=15)


city_info = tk.Label(outputframe, bg=output_color, fg=text_colour, text="TESTING")
weather_label = tk.Label(outputframe, bg=output_color ,fg=text_colour,text="TESTING")
temp_label = tk.Label(outputframe, bg=output_color, fg=text_colour,text="TESTING")
feels_label = tk.Label(outputframe, bg=output_color,fg=text_colour, text="TESTING")
temp_min_label = tk.Label(outputframe, bg=output_color, fg=text_colour, text="TESTING")
temp_max_label = tk.Label(outputframe, bg=output_color,fg=text_colour, text="TESTING")
humidity_label = tk.Label(outputframe, bg=output_color, fg=text_colour, text="TESTING")




blue = "#76c3ef"
city_entry = tk.Entry(input_frame, width=20, bg='white', fg='black', font=large_font)
submit_button_1 = tk.Button(input_frame, text="Submit", font=large_font, bg=input_color, command=search)
search_method = IntVar()
search_method.set(1)
search_city = tk.Label(input_frame, text="Search By City Name", font=small_font, bg=input_color, fg=text_colour)

city_entry.grid(row=0, column=0, padx=10, pady=(10,10))
submit_button_1.grid(row=0, column=1, padx=10)
search_city.grid(row=1, column=0, columnspan=2, pady=2)
city_entry.focus_set()






root.mainloop()