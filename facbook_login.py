from selenium import webdriver 

options = webdriver.ChromeOptions()
options.binary_location = r"Browser_location"
chromedriver = "chromedriver_location"
driver = webdriver.Chrome(chromedriver,chrome_options=options) 
driver.get('https://www.facebook.com/') 
  
username_box = driver.find_element_by_id('email') 
username_box.send_keys('Username') 
 
password_box = driver.find_element_by_id('pass') 
password_box.send_keys('password') 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

driver.quit() 
print("Login Succesfull")