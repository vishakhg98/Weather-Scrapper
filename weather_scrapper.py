# importing modules
import tkinter as tk
from tkinter import messagebox 

from bs4 import BeautifulSoup
import requests


class WeatherWindow:
    def __init__(self, master):
        self.master = master
        # Adding title icon
        master.iconbitmap('./images/weather_titleicon.ico')
        # Adding title name
        master.title("Weather Scrapper")
        # Setting geometry size
        master.geometry('500x600') # Width x Height
        # Disabling resize of window
        master.resizable(0,0)
        
        # Background Main Canvas
        bg_canvas = tk.Canvas(master, width=500, height=600)
        bg_canvas.pack()
        # Canvas / Program background wall
        self.background_image = tk.PhotoImage(file='./images/canvas_background.png')
        background_label = tk.Label(master, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        # ============ Search Box and Button ==================================#
        
        # Search Entry and Button
        self.search_box = tk.Entry(background_label, font=("Arial 18"),
                                   bd=0, justify='center')
        self.search_box.place(x=90, y=100)

        self.search_btn_img = tk.PhotoImage(file='./images/search_button.png')
        self.search_btn = tk.Button(background_label, image=self.search_btn_img,
                                 bd=0, bg='#94c5e3', activebackground='#a7c8d9',
                                 command=lambda : self.fetch_weather())
        self.search_btn.place(x=375, y=103)
        

        # ================ Data Frame =========================================#

        data_frame = tk.Frame(master, bg='white')
        data_frame.place(relx=0.5, rely=0.3,
                         relwidth=0.8, relheight=0.6, anchor='n')

        # Location Label
        self.loc_label = tk.Label(data_frame, font="Arial 12 bold",
                    bg='white', fg="#444")
        self.loc_label.place(x=30, y=25)

        # Status/ Condition Label
        self.status_label = tk.Label(data_frame, font="Arial 15 bold",
                                 bg='white', fg="#444")
        self.status_label.place(x=30, y=65)
        
        # Conditon Image
        self.condition_label = tk.Label(data_frame, bg='white')
        self.condition_label.place(x=50, y=110)
        
        # Temperature Label
        self.temp_label = tk.Label(data_frame, font="Consolas 30",
                             bg='white', fg="#444")
        self.temp_label.place(x=25, y=180)

        # Celsius / Fahrenhite Degree Changer Button
        self.degree_btn = tk.Button(data_frame, text='|°F', font=("Consolas 12 bold"),
                                    bd=0, bg='#fff', activebackground='#fff',
                                    fg='#68add7', activeforeground='#68add7',
                                    command=lambda : self.degree_changer())
        self.degree_btn.place(x=135, y=190)

        # Precipitation Label
        self.precipitation_label = tk.Label(data_frame, font="Consolas 11",
                             bg='white', fg="#444")
        self.precipitation_label.place(x=30, y=255)

        # Humidity Label
        self.humidity_label = tk.Label(data_frame, font="Consolas 11",
                             bg='white', fg="#444")
        self.humidity_label.place(x=30, y=285)

        # Wind Label
        self.wind_label = tk.Label(data_frame, font="Consolas 11",
                             bg='white', fg="#444")
        self.wind_label.place(x=30, y=315)

        # Next Days Predictions

        # Day 0 == Current Day
        self.name_day0 = tk.Label(data_frame, font="Arial 12 bold",
                            bg='white', fg="#444")
        self.name_day0.place(x=205, y=105)
        self.min_temp0 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp0.place(x=185, y=135)
        self.max_temp0 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp0.place(x=230, y=135)

        # Day : 1 == Next Day
        self.name_day1 = tk.Label(data_frame, font="Arial 12 bold",
                            bg='white', fg="#444")
        self.name_day1.place(x=315, y=105)
        self.min_temp1 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp1.place(x=295, y=135)
        self.max_temp1 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp1.place(x=340, y=135)

        # Day : 2
        self.name_day2 = tk.Label(data_frame, font="Arial 12 bold",
                             bg='white', fg="#444")
        self.name_day2.place(x=205, y=165)
        self.min_temp2 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp2.place(x=185, y=195)
        self.max_temp2 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp2.place(x=230, y=195)

        # Day : 3
        self.name_day3 = tk.Label(data_frame, font="Arial 12 bold",
                             bg='white', fg="#444")
        self.name_day3.place(x=315, y=165)
        self.min_temp3 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp3.place(x=295, y=195)
        self.max_temp3 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp3.place(x=340, y=195)

        # Day : 4
        self.name_day4 = tk.Label(data_frame, font="Arial 12 bold",
                             bg='white', fg="#444")
        self.name_day4.place(x=205, y=225)
        self.min_temp4 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp4.place(x=185, y=255)
        self.max_temp4 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp4.place(x=230, y=255)

        # Day : 5
        self.name_day5 = tk.Label(data_frame, font="Arial 12 bold",
                             bg='white', fg="#444")
        self.name_day5.place(x=315, y=225)
        self.min_temp5 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp5.place(x=295, y=255)
        self.max_temp5 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp5.place(x=340, y=255)

        # Day : 6
        self.name_day6 = tk.Label(data_frame, font="Arial 12 bold",
                            bg='white', fg="#444")
        self.name_day6.place(x=205, y=285)
        self.min_temp6 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp6.place(x=185, y=315)
        self.max_temp6 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp6.place(x=230, y=315)

        # Day : 7 == Next weeks current day
        self.name_day7 = tk.Label(data_frame, font="Arial 12 bold",
                            bg='white', fg="#444")
        self.name_day7.place(x=315, y=285)
        self.min_temp7 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.min_temp7.place(x=295, y=315)
        self.max_temp7 = tk.Label(data_frame, font="Arial 10",
                             bg='white', fg="#444")
        self.max_temp7.place(x=340, y=315)


        # Fetching weather info of current location at startup
        self.fetch_weather()



    def degree_changer(self):
        if self.degree_btn['text'] == '|°F':
            self.degree_btn.config(text='|°C')
        else:
            self.degree_btn.config(text='|°F')
        self.degree_btn.config(state='disabled')
        self.fetch_weather()
        self.degree_btn.config(state='normal')


    def fetch_weather(self):
        # Disabling search button to prevent multiple-clicks when searching
        self.search_btn.config(state='disabled')

        # user agent and language is used as a loophole to fetch data from google
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE

        # Searching in Google
        city = self.search_box.get()
        url = "https://www.google.com/search?q=Weather+" + city
        # print(url)
        
        response = session.get(url)
        # Fetching Values from Google Weather Card
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup)
        try:
            # Current Temperature in Celsius
            ctemp = soup.find("span", attrs={"id": "wob_tm"}).text

            # Current Temperature in Fahrenheit
            ftemp = soup.find("span", attrs={"id": "wob_ttm"}).text
            
            # Location : State
            loc = soup.find("div", attrs={"id": "wob_loc"}).text
            
            # Day and Time of update of weather information
            dayhr = soup.find("div", attrs={"id": "wob_dts"}).text
            
            # Status of current weather
            sky_condition = soup.find("span", attrs={"id": "wob_dc"}).text
            
            # Precipitation Chances
            rainfall = soup.find("span", attrs={"id": "wob_pp"}).text
            
            # Humidity Percentage
            humidity = soup.find("span", attrs={"id": "wob_hm"}).text
            
            # Wind Speed
            wind = soup.find("span", attrs={"id": "wob_ws"}).text
            
            
            # Fetching next 7 day's predictions 
            next_days = []
            days = soup.find("div", attrs={"id": "wob_dp"})
            for day in days.findAll("div", attrs={"class": "wob_df"}):
                # print(day)
                # extract the name of the day
                day_name = day.find("div",
                                    attrs={"class": "QrNVmd",
                                    "class": "QrNVmd Z1VzSb"}).text #.attrs['aria-label']

                # get weather status for that day
                weather = day.find("img").attrs["alt"]
                # print(weather)
                predict_temp = day.findAll("span", {"class": "wob_t"})
                # Maximum temp in Celsius, use temp[1].text if you want fahrenheit
                max_ctemp = predict_temp[0].text
                max_ftemp = predict_temp[1].text
                # Minimum temp in Celsius, use temp[3].text if you want fahrenheit
                min_ctemp = predict_temp[2].text
                min_ftemp = predict_temp[3].text

                next_days.append({"name": day_name,
                                 "weather": weather,
                                  "max_ctemp": max_ctemp,
                                   "max_ftemp": max_ftemp,
                                    "min_ctemp": min_ctemp,
                                     "min_ftemp": min_ftemp})
            print(next_days)       


            #============= Inserting Values to data frame   ====================
            
            # Inserting Location data
            self.loc_label.config(text = loc)
            
            # Inserting Condition / Description
            self.status_label.config(text = sky_condition)

            # Fetching button value : °C or °F and setting values accordingly
            if self.degree_btn['text'] == '|°F':
                deg = '°C'
                temp = ctemp + deg
                min = 'min_ctemp'
                max = 'max_ctemp'
                
            else:
                deg = '°F'
                temp = ftemp + deg
                min = 'min_ftemp'
                max = 'max_ftemp'

            # Inserting Temperature value
            self.temp_label.config(text = temp)

            # Inserting Precipitation/ Rainfall Chances %
            self.precipitation_label.config(text="Rainfall : "+ rainfall)

            # Inserting Humidity Level %
            self.humidity_label.config(text="Humidity : "+ humidity)

            # Inserting Wind Speed
            self.wind_label.config(text="Wind : " + wind)

            # Inserting Next days predictions Min and Max values
            # 8days starting from current day to next week's current day
            for index, dayweather in enumerate(next_days):
                day_name = dayweather['name']
                min_temp = dayweather[min] + deg
                max_temp = dayweather[max] + deg

                exec("self.name_day{}.config(text='{}')".format(index, day_name))
                exec("self.min_temp{}.config(text='{}')".format(index, min_temp))
                exec("self.max_temp{}.config(text='{}')".format(index, max_temp))
    
            # Inserting Weather Icon
            try:
                # Different Conditions has same image/ icons
                if sky_condition.lower() in ['haze', 'fog', 'hazy', 'smoke']:
                    sky_condition = 'haze'
                elif sky_condition.lower() in ['scattered thunderstorms', 'storm']:
                    sky_condition = 'scattered thunderstorms'
                elif sky_condition.lower() in ['partly cloud', 'partly sunny']:
                    sky_condition = 'partly cloudy'
                elif sky_condition.lower() in ['sunny', 'clear']:
                    sky_condition = 'sunny'
                elif sky_condition.lower() in ['partly cloudy', 'partly sunny']:
                    sky_condition = 'partly cloudy'
                
                
                # Inserting Condition/description image
                # Deleting old weather image
                self.condition_label.config(image='')
                # Item will be added only if condition icon is present in the icons folder
                self.condition_image = tk.PhotoImage(file='./images/weather icons/{}.png'.format(sky_condition))
                self.condition_label.config(image=self.condition_image)
            except:
                # Deleting old weather image
                self.condition_label.config(image='')
                
                # Enter missing condition icons with link in missing_icons.txt,
                # Missing icons can be looked from the txt file and fixed in later versions
                icon_link = soup.find("img", attrs={'alt': sky_condition})
                icon_link = str(icon_link)
                print(icon_link)
                with open('./images/weather icons/missing_icons.txt', "a") as f:            
                    f.write(icon_link+"\n")

            
            # # Calling print function
            # self.print_weather(ctemp, ftemp, loc, dayhr, sky_condition,
            #             rainfall, humidity, wind, next_days)

            # Enabling search button after search is completed
            self.search_btn.config(state='normal')

        except Exception as e:
            # print(e)
            # Showing error message
            messagebox.showerror("showerror",
                             "There was a problem retrieving that information\nRecheck the location entered or Try different location")

            # Deleting Entry of Search-box
            self.search_box.delete(0, 'end')
            # Enabling search button 
            self.search_btn.config(state='normal')

    def print_weather(self, ctemp, ftemp, loc, dayhr, sky_condition,
                        rainfall, humidity, wind, next_days):
        """ Prints Fetched weather info to Terminal"""
        print("Temperature in °C       : " + ctemp+ "°C")
        print("Temperature in °F       : " + ftemp+ "°C")
        print("Location      :", loc)
        print("Day & Hour of Update :", dayhr)
        print("Status        :", sky_condition)
        print("Precipitation :", rainfall)
        print("Humidity      :", humidity)
        print("Wind Speed    :", wind)

        # Printing next days 
        print("\n")
        print("="*85)
        print("NEXT DAYS:")
        for dayweather in next_days:
            print("="*40, dayweather["name"], "="*40)
            print("Description:", dayweather["weather"])
            print(f"Max temp °C: {dayweather['max_ctemp']}°C")
            print(f"Max temp °F: {dayweather['max_ftemp']}°F")
            print(f"Min temp °C: {dayweather['min_ctemp']}°C")
            print(f"Min temp °F: {dayweather['min_ftemp']}°F")



if __name__ == '__main__':
    # Constant Variables
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    master = tk.Tk()
    app = WeatherWindow(master)
    master.mainloop()