from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Installs Chrome driver if latest version is not available
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

#Url on which web scraping has to be done
url = "https://www.holidify.com/"
driver.get(url)

#Place name and description lists
p_name = []
desc = []

#Function to remove the digits in the place names
def remdig(s):
            a = s.split()
            b = " ".join(a[1:])
            return b

#Locating the search bar and then type Delhi
try:
    ser = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header-autocomplete"]')))
    ser.send_keys("delhi")
    ser.click()
except:
    print("Search bar not located.")

#Selecting the Place to Visit from dropdown
try:
    dd_select = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "tt-suggestion")))
    dd_select[1].click()
except:
    print("Desired dropdown not located.")

#Find the place names along with description in each page and then appending them to the lists
try:
    pages = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "page-link")))
    links = []
    #Getting the href attribute for each page and storing them to navigate to other pages later
    for j in range(len(pages)):
        l = pages[j].get_attribute('href')
        links.append(l)
    #Finding places names along with description in the current page and use remdig function to remove the starting digits from the place names, then append to their respective lists
    for k in range(2, len(links)):
        cards = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "col-12.col-md-6.pr-md-3")))
        for i in range(len(cards)):
            names = cards[i].find_element_by_class_name("card-heading")
            descriptions = cards[i].find_element_by_class_name("card-text")
            na = names.text
            dr = remdig(na)
            p_name.append(dr)
            desc.append(descriptions.text)
        #If the current page is the final page, then quit. Else, go to next page
        if (k == (len(links) - 1)):
            driver.quit()
        else:
            driver.get(links[k])  
except:
    print("Place names and descriptions not located")

#Creating a pandas dataframe and assigning respective headers and then assign the lists respectively
df = pd.DataFrame(list(zip(p_name, desc)), columns = ['Place Name', 'Description'])
#Converting pandas dataframes to csv file
holidify = df.to_csv('hello_tripper_internship.csv', index=False)
