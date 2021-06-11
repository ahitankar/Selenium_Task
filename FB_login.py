from openpyxl import load_workbook
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

filepath="login_details.xlsx"
wb = load_workbook(filepath)
sheet=wb.active
b1=sheet['A1']
b2=sheet['B1']
usrname=b1.value
password=b2.value
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
sleep(1)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usrname)

sleep(1)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(password)

login_box = driver.find_element_by_name('login')
login_box.click()
input('You can type quit to exist')
driver.quit()