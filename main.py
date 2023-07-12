import requests
import time
import mechanicalsoup

#Constantes

#Krone online
kroneMainPage = "https://www.krone.at/"
kroneNewArticlesContainerId = "swiper-wrapper-1ed865ae5326a75d"

browser = mechanicalsoup.StatefulBrowser()

def checkForAllArticles():
    checkForNewKroneArticles()

    print("Checked for all articles from all the medias online")
    
def checkForNewKroneArticles():
    # Create a MechanicalSoup browser object
    
    response = browser.open(kroneMainPage)

    # Find all elements with both classes "swiper-slide" and "c_anmod"

    newArticlesContainer = browser.page.find(class_=["c_newsticker"])

    newArticles = newArticlesContainer.find_all(class_=["swiper-slide", "c_anmod"])

    if newArticles:
        # Print the tag name of each element
        for articleDiv in newArticles:
            if articleDiv:
                # Extract the link to the article
                link = articleDiv.select_one('a')['href']
                
                # Extract the name of the article
                name = articleDiv.select_one('.a__title').text

                print("Link: ", link)
                print("Name: ", name)
                print("-----------------")
            else:
                print("No top-most div element found with the provided classes.")

#should be set to false, because the server should be running permanently
running = True

while running:
    checkForAllArticles()
    
    #Check all 5 Minutes of new articles are avalible
    time.sleep(5000)
