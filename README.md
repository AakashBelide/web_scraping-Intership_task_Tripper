# web_scraping-Intership_task_Tripper

Extracted various fields of information from travel website using web scraping. As the website requires searching a particular word, redirecting to another url and many other tasks, [Selenium](https://selenium-python.readthedocs.io/) is used in order to facilitate these tasks. When we try to get the place names directly, we get the numerical before it as well. In order to get only the place name, the remdig function removes the digits from the names and then returns the place name. As the places are distributed in various pages, we first store the redirect url links of each page in a list in order to traverse in it to go to the next page later.

> ## Python libraries used:
> * [Selenium](https://selenium-python.readthedocs.io/)
> * [Pandas](https://pandas.pydata.org/)


> ## Requirements:
> * [Google Chrome](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwyo36BRAXEiwA24CwGX-VodFH-_NIx7AhJWESiWlB22zR6GlO1Alc5ruvDkacNNaW7uriohoC1B8QAvD_BwE&gclsrc=aw.ds)
> * [ChromeDriver](https://chromedriver.chromium.org/)

> ## Directions to use:
> * This is designed for only holidify. You can change the place name you want to search to get the different data.
> * Make sure you have good internet connection and keep the system on while the process takes place.
> * You will get various pieces of information from the website like Place Names and Descriptions.
> * Rename the csv file you want to save according to your needs.