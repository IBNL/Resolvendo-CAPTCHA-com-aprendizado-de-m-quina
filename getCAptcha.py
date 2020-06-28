### Script por Igor Balbino

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from Screenshot import Screenshot_Clipping
import time
from PIL import Image
from io import BytesIO
import pytesseract
import pickle
from selenium.webdriver.firefox.options import Options
import os


total = 1000
url = "https://rarbgprx.org/torrents.php?category=2;14;15;16;17;21;22;42;18;19;41;27;28;29;30;31;32;40;23;24;25;26;33;34;43;44;45;46;47;48;49;50;51;52"
option = Options()
option.headless = True 
#driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)
driver.find_element_by_link_text("Click here").click()

for count in range(total):
    #print("wait 10 for")
    time.sleep(25)
    imgCaptcha = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/img[1]")
    png = driver.get_screenshot_as_png() # saves screenshot of entire page

    location = imgCaptcha.location
    size = imgCaptcha.size

    #print(location)
    #print(size)

    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) # defines c
    time.sleep(1)

    im.save('/home/bluecase/Documentos/breakCaptchaRARBG/dataset/captcha.png') # saves new cropped image
            

    captachResolv = pytesseract.image_to_string( Image.open('/home/bluecase/Documentos/breakCaptchaRARBG/dataset/captcha.png') )  # Extract string to img

    print(captachResolv)
    os.rename("/home/bluecase/Documentos/breakCaptchaRARBG/dataset/"+'captcha.png', "/home/bluecase/Documentos/breakCaptchaRARBG/dataset/"+captachResolv)
    print('total de captchas extraidos: ' + str(count))
    time.sleep(15)
    driver.find_element_by_name( 'solve_string' ).send_keys('12345')
        
    submit_button = driver.find_elements_by_xpath('/html[1]/body[1]/form[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/button[1]')[0]
    submit_button.click()
    print('voltar')
print('finish') 
       