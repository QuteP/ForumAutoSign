import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import urllib.request
from selenium.webdriver.common.keys import Keys
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data_path=input('請輸入chrome user data的絕對路徑')
driver_path=input('請輸入chromedriver的絕對路徑')

def fourgamer():
    options = Options()
    mobile_emulation = { "deviceName": "iPhone SE" }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    # options.add_argument('--window-size=960x540')
    options.add_argument("user-data-dir="+ data_path)
    browser = webdriver.Chrome(executable_path=driver_path, options=options)
    family_url=r'https://www.4gamers.com.tw/gamily'
    news_url=r'https://www.4gamers.com.tw/news/detail/' #後面要加變數，前4碼是天，後1碼是篇
    gacha_url=r'https://www.4gamers.com.tw/gacha/detail/wdpjo92r'
    mission_url=r'https://www.4gamers.com.tw/r/member/quest'
    browser.get(family_url)
    time.sleep(3)
    family_arr=browser.find_elements_by_xpath('//div[@class="aroma-col mDb-2 mDb-lg-3 col"]/a[@class="text-dark d-lg-none"]')
    for i in range(len(family_arr)):
        family_arr[i]=family_arr[i].get_attribute("href")
    for i in range(10):
        browser.get(family_arr[i])
        time.sleep(3)
        try:
            emo_btn=browser.find_elements_by_xpath('//a[@class="expression-emoji-button position-relative rounded-circle d-inline-flex align-items-center justify-content-center"]/img')[0]
            # browser.execute_script("window.scrollTo(0, 3*(document.body.scrollHeight)/8);")
            emo_btn = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(emo_btn))
            browser.execute_script('arguments[0].click()',emo_btn)
            time.sleep(0.5)
        except Exception as e:
            print(e)
        if i==9:
            try:
                donate_btn=browser.find_element(By.XPATH,"//a[@class='donate-button d-inline-flex align-items-center text-white text-base font-bold p-1 pr-3 mDl-1']")
                browser.execute_script('arguments[0].click()',donate_btn)
                time.sleep(2)
                submit_btn=browser.find_element_by_xpath('//form/button')
                browser.execute_script('arguments[0].click()',submit_btn)
                time.sleep(2)
                share_btn=browser.find_element(By.XPATH,"//span[@class='share-button ml-1']")
                browser.execute_script('arguments[0].click()',share_btn)
                time.sleep(2)
                fb_btn=browser.find_element(By.XPATH,"//div/a/div[@class='share-button fb-button d-flex align-items-center justify-content-center rounded-circle text-white mb-1']")
                browser.execute_script('arguments[0].click()',fb_btn)
                time.sleep(2)
            except Exception as e:
                print(e)
    browser.get(gacha_url)
    time.sleep(3)
    # browser.execute_script("window.scrollTo(0, 3*(document.body.scrollHeight)/16);")
    time.sleep(3)
    gacha_btn=browser.find_element(By.XPATH,"//body/div[@class='taiwan-edition']/div[@class='d-flex flex-column px-0 full-layout justify-content-between container-fluid']/div[@class='flex-grow-1 pDb-lg-0 pDb-6']/div/div[@class='aroma-container pDy-2 pDy-lg-3 container']/div[@class='row no-gutters']/div[@class='member-wallet-two-column-layout-main mr-lg-auto col-lg col-12']/div[@class='row mDb-3 mDb-lg-0 no-gutters']/div/section[@class='d-flex justify-content-between justify-content-sm-center mDb-3 mDb-lg-4']/button[1]")
    browser.execute_script('arguments[0].click()',gacha_btn)
    time.sleep(3)
    back='-1'
    try:
        with open('news_num.txt', 'r') as fp:
            back=int(fp.readlines()[0])
            fp.close()
    except Exception as e:
        print(e)
    browser.get(mission_url)
    time.sleep(5)
    news_num_div=browser.find_element(By.XPATH,"//div[./img[@src='https://img.4gamers.com.tw/quest-image/2067a7b2-6013-4575-bbe6-a5627a0e01fb.png']]/div[@class='flex-shrink-0 d-flex flex-column justify-content-center position-relative']/p")
    news_num=int((news_num_div.text.split('/'))[0])
    while news_num<10:
        i=news_num
        while i<10:
            browser.get(news_url+str(back))
            time.sleep(10)
            try:
                none_bg=browser.find_element(By.XPATH,"//img[@class='d-none d-xl-block']")
                back=(back//10+1)*10
                continue
            except Exception as e:
                print(e)
            share_btn=browser.find_element(By.XPATH,"//div[@class='aroma-news-detail-page pb-0 pDb-lg-0 mx-auto pt-3 pDt-lg-3']//a[@class='share-button d-inline-flex align-items-center text-gray-500']")
            browser.execute_script('arguments[0].click()',share_btn)
            time.sleep(2)
            fb_btn=browser.find_element(By.XPATH,"//div/a/div[@class='share-button fb-button d-flex align-items-center justify-content-center rounded-circle text-white mb-1']")
            browser.execute_script('arguments[0].click()',fb_btn)
            time.sleep(2)
            back=back+1
            i=i+1
        browser.get(mission_url)
        time.sleep(3)
        news_num_div=browser.find_element(By.XPATH,"//div[./img[@src='https://img.4gamers.com.tw/quest-image/2067a7b2-6013-4575-bbe6-a5627a0e01fb.png']]/div[@class='flex-shrink-0 d-flex flex-column justify-content-center position-relative']/p")
        news_num=int((news_num_div.text.split('/'))[0])
    try:
        with open('news_num.txt', 'w') as fp:
            fp.write(str(back))
            fp.close()
    except Exception as e:
        print(e)
    browser.get(mission_url)
    time.sleep(5)
    btn_lt=browser.find_elements(By.XPATH,"//button[@class='btn gradient-button text-nowrap py-1 btn-secondary warning fixed-width px-0']")
    for btn in btn_lt:
        browser.execute_script('arguments[0].click()',btn)
    browser.refresh()
    time.sleep(5)
    btn_lt=browser.find_elements(By.XPATH,"//button[@class='btn gradient-button text-nowrap py-1 btn-secondary warning fixed-width px-0']")
    for btn in btn_lt:
        browser.execute_script('arguments[0].click()',btn)
    time.sleep(2)
    browser.quit()
def buifire():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument(r"user-data-dir="+data_path)
    browser = webdriver.Chrome(executable_path=driver_path, options=options)
    fire_url=r'https://www.byzhihuo.com/plugin.php?id=dsu_paulsign:sign'
    browser.get(fire_url)
    time.sleep(3)
    try:
        face=browser.find_element(By.XPATH,"//li[@id='kx']")
        face.click()
        btn=browser.find_element(By.XPATH,"//td[@class='tr3 tac']/div//img")
        btn.click()
        time.sleep(3)
    except Exception as e:
        print(e)
    browser.quit()
def baha():
    options = Options()
    mobile_emulation = { "deviceName": "iPhone SE" }
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    # options.add_argument('--start-maximized')
    options.add_argument(r"user-data-dir="+data_path)
    browser = webdriver.Chrome(executable_path=driver_path, options=options)
    login_url=r'https://m.gamer.com.tw/?t=GNN&page=1#drawer'
    browser.get(login_url)
    time.sleep(3)
    try:
        login_btn=browser.find_elements(By.XPATH,"//ul[@class='SubMenu_more SubMenu_moreA']/li/a[@class='gtm-nav-menu']")[2]
        browser.execute_script('arguments[0].click()',login_btn)
        time.sleep(1)
        double_btn=browser.find_element(By.XPATH,"//a[contains(text(),'觀看廣告領取雙倍巴幣')]")
        browser.execute_script('arguments[0].click()',double_btn)
        time.sleep(10)
        yes_btn=browser.find_element(By.XPATH,"//button[@class='btn btn-insert btn-primary']")
        browser.execute_script('arguments[0].click()',yes_btn)
        WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//ins/div/iframe"))) #這行可能會有問題，下面的也是
        try:
            close_btn=browser.find_element(By.XPATH,"//div[@id='dismiss-button']")
            time.sleep(10)
            browser.execute_script('arguments[0].click()',close_btn)
        except Exception as e:
            print("")
            close_btn=browser.find_element(By.XPATH,"//div[7]//div[1]//div[3]//div[2]")#這竟然可以用
            browser.execute_script('arguments[0].click()',close_btn)
            close_btn=browser.find_elements(By.XPATH,"//div[@class='ad-video']/img")[2]
            time.sleep(10)
            browser.execute_script('arguments[0].click()',close_btn)
    except Exception as e:
        print("沒第二或沒雙倍")
        print(e)
    baha_url=r'https://fuli.gamer.com.tw/shop.php'
    browser.get(baha_url)
    time.sleep(3)
    link_arr=[]
    try:
        prize_arr=browser.find_elements(By.XPATH,"//a[./div/div/div/span[text()='抽抽樂']]")
        for prize in prize_arr:
            link_arr.append(prize.get_attribute('href'))
    except Exception as e:
        print("沒抽抽樂")
        print(e)
    for link in link_arr:
        browser.get(link)
        time.sleep(3)
        i=0
        while i<10:
            # browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(5)
                first_btn=browser.find_element(By.XPATH,"//a[@class='btn-base c-accent-o ']")
                # browser.execute_script('arguments[0].click()',first_btn)
                first_btn.click()
            except Exception as e:
                print("抽完了")
                print(e)
                i=10
                continue
            time.sleep(10)
            try:
                second_btn=browser.find_element(By.XPATH,"//button[@class='btn btn-insert btn-primary']")
                # browser.execute_script('arguments[0].click()',second_btn)
                second_btn.click()
            except Exception as e:
                print("沒廣告跑出來")
                print(e)
                danger_btn=browser.find_element(By.XPATH,"//button[@class='btn btn-insert btn-danger']")
                browser.execute_script('arguments[0].click()',danger_btn)
                browser.refresh()
                continue
            time.sleep(5)
            WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//ins/div/iframe")))
            # c=input()
            # iframe=browser.find_element(By.XPATH,"//ins/div/iframe")
            # browser.switch_to.frame(iframe)
            # time.sleep(5)
            try:
                #定位不到google的按鈕，需檢查
                close_btn=browser.find_element(By.XPATH,"//div[@id='dismiss-button']")
                time.sleep(10)
                browser.execute_script('arguments[0].click()',close_btn)
                time.sleep(5)
                # browser.execute_script("window.scrollTo(0, 7*(document.body.scrollHeight)/8);")
                check_box=browser.find_element(By.XPATH,"//input[@id='agree-confirm']")
                check_box = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(check_box))
                browser.execute_script('arguments[0].click()',check_box)
                # check_box.click()
                third_btn=browser.find_element(By.XPATH,"//a[@class='btn-base c-primary']")
                browser.execute_script('arguments[0].click()',third_btn)
                time.sleep(0.5)
                fourth_btn=browser.find_element(By.XPATH,"//button[@class='btn btn-insert btn-primary']")
                browser.execute_script('arguments[0].click()',fourth_btn)
                time.sleep(5)
                fifth_btn=browser.find_element(By.XPATH,"//button[@class='btn btn--primary']")
                browser.execute_script('arguments[0].click()',fifth_btn)
                time.sleep(5)
                i=i+1
            except Exception as e:
                print("沒google")
                print(e)
                try:
                    close_btn=browser.find_element(By.XPATH,"//div[7]//div[1]//div[3]//div[2]")#這不能用了
                    browser.execute_script('arguments[0].click()',close_btn)
                    close_btn=browser.find_elements(By.XPATH,"//div[@class='ad-video']/img")[2]
                    time.sleep(10)
                    browser.execute_script('arguments[0].click()',close_btn)
                    time.sleep(5)
                    try:
                        temp_btn=browser.find_element(By.XPATH,"//div[7]//div[1]//div[3]//div[2]")
                        browser.refresh()
                        continue
                    except Exception as f:
                        print("第二正常")
                        print(f)
                    check_box=browser.find_element(By.XPATH,"//input[@id='agree-confirm']")
                    check_box = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(check_box))
                    browser.execute_script('arguments[0].click()',check_box)                    
                    third_btn=browser.find_element(By.XPATH,"//a[@class='btn-base c-primary']")
                    browser.execute_script('arguments[0].click()',third_btn)
                    time.sleep(0.5)
                    fourth_btn=browser.find_element(By.XPATH,"//button[@class='btn btn-insert btn-primary']")
                    browser.execute_script('arguments[0].click()',fourth_btn)
                    time.sleep(5)
                    fifth_btn=browser.find_element(By.XPATH,"//button[@class='btn btn--primary']")
                    browser.execute_script('arguments[0].click()',fifth_btn)
                    time.sleep(5)
                    i=i+1
                except Exception as g:
                    print("沒第二和google")
                    print(g)
                    try:
                        close_btn=browser.find_element(By.XPATH,"//div[@id='close_button']")
                        time.sleep(30)
                        browser.execute_script('arguments[0].click()',close_btn)
                        time.sleep(5)
                        check_box=browser.find_element(By.XPATH,"//input[@id='agree-confirm']")
                        check_box = WebDriverWait(browser, 20).until(EC.element_to_be_clickable(check_box))
                        browser.execute_script('arguments[0].click()',check_box)                    
                        third_btn=browser.find_element(By.XPATH,"//a[@class='btn-base c-primary']")
                        browser.execute_script('arguments[0].click()',third_btn)
                        time.sleep(0.5)
                        fourth_btn=browser.find_element(By.XPATH,"//button[@class='btn btn-insert btn-primary']")
                        browser.execute_script('arguments[0].click()',fourth_btn)
                        time.sleep(5)
                        fifth_btn=browser.find_element(By.XPATH,"//button[@class='btn btn--primary']")
                        browser.execute_script('arguments[0].click()',fifth_btn)
                        time.sleep(5)
                        i=i+1
                    except Exception as h:
                        print("沒第三")
                        print(h)
                        i=10

buifire()
fourgamer()
baha()


