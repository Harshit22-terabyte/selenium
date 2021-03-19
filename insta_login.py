
def instalogin():
    from selenium import webdriver
    import time

    driver= webdriver.Chrome(executable_path ='chromedriver_win32/chromedriver')
    #driver.get("https://www.instagram.com/accounts/login/")
    driver.implicitly_wait(10)   #To add wait time so that browser is properly loaded
    driver.get("https://www.google.co.in")   #To search goggle.com
    driver.maximize_window()                 #To maximize browser window
    goggle=driver.find_element_by_name("q")
    goggle.click()
    goggle.clear()
    goggle.send_keys("insta login")
    goggle.submit()
    insta_page=driver.find_element_by_xpath("//div[@class='TbwUpd NJjxre']")
    insta_page.click()
    username=driver.find_element_by_name("username")
    username.click()
    username.clear()
    username.send_keys('Type username here')
    password=driver.find_element_by_name("password")
    password.click()
    password.clear()
    password.send_keys('Type password here')
    signin=driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
    signin.submit()
    home=driver.find_element_by_class_name('cq2ai')
    home.click()
    alert=driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
    alert.click()

    time.sleep(1)  # Allow 1 seconds for the web page to open
    scroll_pause_time = 1 # You can set your own pause time. So that the scroll may load pages
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        scroll=int(input("To stop : Press '1' , To Continue : Press'2' "))
        if (scroll==1):
            break
        else:
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            # Break the loop when the height we need to scroll is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break

instalogin()
