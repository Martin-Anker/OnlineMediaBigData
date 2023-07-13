import time
import mechanicalsoup
import threading

#Constantes

#Krone online
kroneMainPage = "https://www.krone.at/"

browser = mechanicalsoup.StatefulBrowser()

def printCol(color: str, bold: bool, colText: str, *moreText: str):

    color_code = ""

    if color == "red":
        color_code = "\033[91m"
    elif color == "green":
        color_code = "\033[92m"
    elif color == "blue":
        color_code = "\033[94m"
    elif color == "yellow":
        color_code = "\033[93m"
    elif color == "purple":
        color_code = "\033[95m"
    elif color == "cyan":
        color_code = "\033[96m"
    elif color == "white":
        color_code = "\033[97m"

    if bold:
        color_code += "\033[1m"

    print(color_code + colText + "\033[0m", end=" ")
    for text in moreText:
        print(text, end=" ")
    print()

def checkForAllArticles():
    checkForNewKroneArticles()

    print("Checked for all articles from all the medias online")

def processKroneArticle(urlToArticle):
    browser.open(urlToArticle)

    articlePage = browser.page

    #Extract main section
    main_section = articlePage.find(class_=["kmm-article-box"])
    
def checkForNewKroneArticles():
    # Create a MechanicalSoup browser object
    
    browser.open(kroneMainPage)

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

                printCol("blue", True, "Processing article with the title:", name)
                processKroneArticle(link)
                print("-----------------")

            else:
                print("No top-most div element found with the provided classes.")

#should be set to false, because the server should be running permanently
running = True

main_thread = threading.Thread(target=checkForAllArticles)

while running:
    if main_thread.is_alive():
        print("The server is still processing after 5 minutes! Timeout, exiting program")
        main_thread.stop()
        exit()

    main_thread.start()
    
    #Check all 5 Minutes of new articles are avalible
    time.sleep(5000)
