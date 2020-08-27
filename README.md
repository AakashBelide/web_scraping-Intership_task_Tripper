# web_scraping-Intership_task

Extracted various fields of information from housing website using web scraping. As the website requires redirecting to different url and scrolling and many other tasks, [Selenium](https://selenium-python.readthedocs.io/) is used in order to facilitate these tasks. There are 3 parameters required for the scroll function, they are driver, timeout (time to wait till next scroll) and number of times to scroll respectively. Set the number of times to scroll according to the number of data entries you require. Magicbricks loads 30 new houses everytime you scroll and reach the end of the website, so as I require information of 500 houses, I have set it as 18 (18 x30 = 540), and later I have kept 500 in the for loop for only information of 500 houses in the csv file.

## Python libraries used:
> * [Selenium](https://selenium-python.readthedocs.io/)
> * [Time](https://docs.python.org/3/library/time.html)
> * [Pandas](https://pandas.pydata.org/)


## Requirements:
> * [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwyo36BRAXEiwA24CwGX-VodFH-_NIx7AhJWESiWlB22zR6GlO1Alc5ruvDkacNNaW7uriohoC1B8QAvD_BwE&gclsrc=aw.ds)
> * [ChromeDriver](https://chromedriver.chromium.org/)

## Directions to use:
> * This is designed for only magicbricks. You can provide the searched url in a specific locality.
> * Make sure you have good internet connection and keep the system on while the process takes place.
> * You will get various pieces of information from the website like:
>> * Price
>> * Headline
>> * Address
>> * Owner
>> * Bedrooms
>> * Bathrooms
>> * Balconies
>> * Super area
>> * Price Per sqft
>> * Status
>> * Transaction type
>> * Floor
>> * Car parking
>> * Furnished
>> * Lifts
>> * Descrption
>> * Price breakup
>> * Address2
>> * Landmarks
>> * Age of Construction
>> * Price comparison
>> * Expected rent
>> * Monthly EMI