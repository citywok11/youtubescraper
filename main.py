# time is library that you need to import, it allows you to use the function time.sleep
# webdriver is the other library that you need , it contains selenium
# you will need to right click the words and select import library to actually import the files to your directory
import time
from selenium import webdriver

# this selects the webdriver you will be using. I chose chrome
driver = webdriver.Chrome()
# this opens the browser on this selected URL , insert whichever URL you'd like to open
driver.get("https://www.youtube.com/user/Moeinfard/channels")
# sleeps the program for 2 seconds
# basically allows the browser to load before running any code, might need a longer sleep depending on ur computer
time.sleep(2)

scroll_pause_time = 1
# this actually runs some javascriot to find the size of your web browser window
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
# this value i stands for index it starts the loop at value 1 , each loop ads one to i , see i += 1
i = 1

# this is the start of your loop , while True , honestly not sure entirely how it works idk python
while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.documentElement.scrollHeight;")
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

# this is where we are when we've broken the loop , bottom of the web page , now we can process the data
# this finds all the titles on the web page and adds them to this array called channel_title
channel_title = driver.find_elements_by_xpath('//*[@id="title"]')
# this finds the hyperlinks on the web page for the channels and add them to this array called channel_link
channel_link = driver.find_elements_by_xpath('//*[@id="channel-info"]')
# we declare an empty array here, we are about to add all the information to it
listTitle = []
# we need a loop to populate our array listTItle. (arrays are declared example[] )
# it means for each item in the channel_title array, do something ¬
# the something we are doing is appending our title from the html
for i in channel_title:
    listTitle.append(i.get_attribute('innerHTML'))
# we just do the same thing here but for the URL
# you can write code here console.log(listTitle) and it will output the contents of ListTitle to your console to see
# the contents
listLink = []
for i in channel_link:
    listLink.append(i.get_attribute('href'))
# At this point I got a bit stuck . We have two different Arrays. I decided to create a dictionary object with it
# a dictionary object is like an array with 2 values on each index
res = dict(zip(listTitle, listLink))
# im printing the dictionary object below
print(res)
# useful things you can do now to figure stuff out :
# print(listLink)
# print(listTitle)
# THIS CODE BELOW OUTPUTS TO TXTFILE : https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
# with open("output.txt", "a") as f:
#    print("Hello stackoverflow!", file=f)
#    print("I have a question.", file=f)
