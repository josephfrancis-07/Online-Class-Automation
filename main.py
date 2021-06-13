from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime
from datetime import datetime, timedelta
import time
# from threading import Thread

# Defining subjects' x_Path
VLSI='//*[@id="yDmH0d"]/div[4]/div[1]/div[2]/div/ol/li[1]/div[1]/div[3]/h2/a[1]/div[1]'
OOP='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]'
MCLAB='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]'
DIP='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[4]/div[1]/div[3]/h2/a[1]/div[1]'
COMLAB='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[5]/div[1]/div[3]/h2/a[1]/div[1]'
DC='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[7]/div[1]/div[3]/h2/a[1]/div[1]'
ES='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[8]/div[1]/div[3]/h2/a[1]/div[1]'
AWP='//*[@id="yDmH0d"]/div[4]/div/div[2]/div/ol/li[9]/div[1]/div[3]/h2/a[1]/div[1]'
COMPEXAM='//*[@id="yDmH0d"]/div[4]/div[1]/div[2]/div/ol/li[6]/div[1]/div[3]/h2/a[1]/div[1]'
FREE="free"

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

#Defining Timetable
timetable={"Monday":[OOP,ES,VLSI,DC,COMPEXAM],
           "Tuesday":[VLSI,DC,ES,AWP,COMPEXAM],
           "Wednesday":[ES,FREE,DIP,MCLAB,DIP],
           "Thursday":[DC,VLSI,AWP,OOP,FREE],
           "Friday":[AWP,OOP,DIP,COMLAB,FREE]}

Username="RIT Mail"
Password="Password"

def Join(x_subject):
      if x_subject=="free":
            print("This hour is free")
            time.sleep(3300) 
      else:       
            chromedriver_path ="/home/zeca/Projects/Python/Projects including Virtual enironments/Skippon/chromedriver"

            opt = Options()
            opt.add_argument("--disable-infobars")
            opt.add_argument("start-maximized")
            opt.add_argument("--disable-extensions")

            # Pass the argument 1 to allow and 2 to block

            opt.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2, 
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.geolocation": 2, 
            "profile.default_content_setting_values.notifications": 2, 
            })

            driver = webdriver.Chrome(chrome_options=opt,executable_path=chromedriver_path)
            
            driver.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

            username=driver.find_element_by_xpath('//*[@id="identifierId"]')
            username.click()
            username.send_keys(Username)

            next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
            next.click()

            time.sleep(2)

            password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
            password.click()
            password.send_keys(Password)

            next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
            next.click()

            time.sleep(15)

            subject=driver.find_element_by_xpath(x_subject)
            subject.click()

            time.sleep(8)

            x_link='//*[@id="yDmH0d"]/div[4]/div[2]/div/div[1]/div/div[2]/div[2]/div/span/a/div'

            link=driver.find_element_by_xpath(x_link)
            link.click()

            time.sleep(3)

            to_switch_tab=driver.window_handles[1]
            driver.switch_to_window(to_switch_tab)

            time.sleep(3)

            # dismiss=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/span/span')
            # dismiss.click()

            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            
            time.sleep(8)

            join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
            join.click()
            
            print("Successfully Attended")

            time.sleep(3300)
            
            driver.quit()


def Periods(cls_hrs , current_time):
      while current_time.hour<=14:
            current_time=datetime.now()
            if current_time.hour==8 and current_time.minute>28:
                  Join(cls_hrs[0])
            elif current_time.hour==9 and current_time.minute>28 :
                  Join(cls_hrs[1])
            elif current_time.hour==10 and current_time.minute>38 :
                  Join(cls_hrs[2])
            elif current_time.hour==11 and current_time.minute>38:
                  Join(cls_hrs[3])
            elif current_time.hour==12 and current_time.minute>38:
                  Join(cls_hrs[4])
            else:
                  continue

cls_hrs=[]  
while 1>0:
      current_time=datetime.now()
      if current_time.hour>=8:
            thisDay=datetime.today().weekday()
            thisDayAsString = weekDays[thisDay]
            if thisDayAsString != "Sunday" and thisDayAsString != "Saturday":
                  cls_hrs=timetable[thisDayAsString]  
                  Periods(cls_hrs,current_time)
            else :
                  time.sleep(10800) #Sleeping for 3hours
                  continue 
      else:
            time.sleep(360)
            continue

            
# if __name__ == '__main__':
#     Thread(target = Join("RIT Mail","Password")).start()
