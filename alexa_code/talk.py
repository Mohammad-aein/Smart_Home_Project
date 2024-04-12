from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as choromesevise
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
import time
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome()



counter = 0
def speak(massage,l = 0):
        try:
            if l == 0:
                
                driver.get("https://aipaa.ir/demo/voice-analysis?tag=tts")
                

                
                time.sleep(0.2)
                googleSerchbox = driver.find_element (By.XPATH,'//*[@id="mat-input-0"]')
                for i in  range(0,25):
                    googleSerchbox.send_keys(Keys.BACK_SPACE)



                googleSerchbox.send_keys(massage)


                googleSerchbox2 = driver.find_element (By.XPATH,'/html/body/app-root/app-layout/div/mat-sidenav-container/mat-sidenav-content/div/div[2]/div')
                for i in  range(0,15):
                    googleSerchbox2.send_keys(Keys.ARROW_DOWN)



                googleSerchbox3 = driver.find_element (By.XPATH,'//*[@id="mat-tab-content-0-4"]/div/app-tts/div/div[3]/div/div[1]/div/button')
                googleSerchbox3.click()
                A = len(massage)* 0.01
                print(3+A)
                time.sleep(4+A)
               
                googleSerchbox4 = driver.find_element (By.XPATH,'//*[@id="mat-tab-content-0-4"]/div/app-tts/div/div[4]/div[3]/button/span')
                googleSerchbox4.click()

                
            # منتظر بمانید تا مرورگر کاملاً بارگذاری شود (می‌توانید بجای زمان ثابت، برای مثال بر اساس وقت بارگذاری صفحه منتظر بمانید)
            elif l == 3:
                buttons = []
                bord = []
                bord2 = []
                pin = []
                pin2 = []
                object_ = []
                dive = massage

                driver.get(r'https://aeintech.ir/ESP/esp-outputs.php')
                counter = 0
                while True:
                    counter = counter+1
                    try:
                        for i in range(int(counter /3)):
                            for i in range(13):
                                texts1= driver.find_element(By.XPATH, f'/html')
                                texts1.send_keys(Keys.ARROW_DOWN)
                        texts = driver.find_element(By.XPATH, f'/html/body/h3[{counter}]')
                        CREATED = texts.text.split(" - ")
                        
                        buttons.append(CREATED[0])
                        bord.append(CREATED[1])
                        pin.append(CREATED[2])
                        
                        object_.clear()
                        

                    except:
                        for i in bord:
                            bord2.append(i.split(" ")[1])
                        for i in pin:
                            pin2.append(i.split(" ")[1])
                        #print(bord2)
                        #print(buttons)
                        return buttons,bord2,pin2
            elif l == 4:
                dive = massage

                driver.get(r'https://aeintech.ir/ESP/esp-outputs.php') 
                try:
                    for i in range(int(dive /3)):
                            for i in range(13):
                                texts2= driver.find_element(By.XPATH, f'/html')
                                texts2.send_keys(Keys.ARROW_DOWN)
                    texts = driver.find_element(By.XPATH, f'/html/body/label[{dive}]/span')
                    texts.click()
                except:
                    print("EROOR ON/OFF")
            elif (l == 5):
                driver.get("https://www.google.com")
        except:
             print("EROOR")

