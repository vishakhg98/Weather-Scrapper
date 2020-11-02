# Weather Scrapper
Weather Scrapper is a GUI application to scrap/fetch weather data from google cards and display it on your GUI app.

## Features
* Fahrenhite and Celsius Switch.
* Next 7 days predictions.
* Static google-weather icons.
* Missing weather icons name and link to download gets added to the missing_icons.txt in .\images\weather icons\missing_icons.txt


## Technologies
Project is created with:
* Python 3.9
* OOPS Concept.
* Tkinter(tk) module for GUI.
* Beautifulsoup4 and Requests external modules for Fetching/Scrapping data from google.


## Installation
1. Download the project to your Device using one of the ways listed below
   1. Clone the repo:
git clone https://github.com/vishakhg98/Weather-Scrapper.git
   1. Download Zip using : [Download](https://github.com/vishakhg98/Weather-Scrapper/archive/master.zip)
	 
1. (Optional) If want to use virtual environment:
		
		venv\Scripts\activate

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to download the necessary modules using one of the ways listed below.
   1. To install all necessary modules

			pip install -r requirements.txt
   1. To install individually

			pip install beautifulsoup4==4.9.3
			pip install requests==2.24.0

## How To Run
(Optional) Use virtual Environment.

Run weather_scrapper.py file.

	venv\Scripts\activate
	python3 weather_scrapper.py
  

## Screenshots 📸
![Celsius](https://github.com/vishakhg98/Weather-Scrapper/blob/master/screenshots/Celsius.png)
![Fahrenhite](https://github.com/vishakhg98/Weather-Scrapper/blob/master/screenshots/Fahrenhite.png)

for more screenshots visit [Screenshots](https://github.com/vishakhg98/Weather-Scrapper/tree/master/screenshots) folder in the main branch.


## Bugs
Some icons missing for some uncommon weather events.
Weather condition name and link of icon automatically gets added to the missing_icons.txt in .\images\weather icons\missing_icons.txt
So please open an issue uploading missing_icons.txt file to fix those icons in future updates.
You can manually add that icons to ./images/weather icons folder yourself too to fix this bug.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
