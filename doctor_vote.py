import sys, os
import pandas as pd
import random,time
from selenium import webdriver  # 從library中引入webdriver
# from selenium.webdriver.common.by import By
from fake_useragent import UserAgent # !pip install fake-useragent
from selenium.webdriver.chrome.options import Options
import urllib
import multiprocessing as mp
# import argparse
# pd.set_option('display.max_rows', 250)

# 針對第一間診所投票
def vote():
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.random
    options = Options()
    options.add_argument("window-size=800,800")
    options.add_argument(f'user-agent={user_agent}')
    print(user_agent)

    browser = webdriver.Chrome('./chromedriver', options=options)
#     browser = webdriver.Chrome('./chromedriver')
    
    browser.get('https://health.businessweekly.com.tw/event/2020/pediatrics/search.html?keywords=張虔熙')

    try:
        agree_button = browser.find_element_by_xpath('//*[@id="gdrp"]')
        agree_button.click() 
        time.sleep(7)
#         scroll_down="var q=document.documentElement.scrollTop=1000"  
#         browser.execute_script(scroll_down)  
        
        vote_button = browser.find_element_by_xpath('//*[@id="search"]/section[3]/div[2]/div[1]/div[2]/a/picture/img')
        time.sleep(random.randint(2,3))
        vote_button.click()
        #time.sleep(random.randint(1,3))
#         //*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label
#         //*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label
        time.sleep(random.randint(3,5))
        check_box_pro = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label')
        time.sleep(1)
        check_box_pro.click()
#         time.sleep(random.randint(1,2))
        submit_button = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[3]/a[1]')
        time.sleep(1)
        submit_button.click()
        time.sleep(1)
    except:
        browser.quit()
        return vote()

#     check_box_nice = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label')
#     check_box_nice.click()
#     check_box_detail = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[3]/label')
#     chekc_box_detail.click()
#     check_box_med = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[4]/label')
#     check_box_med.click()

#     check_box_pro = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label')
#     check_box_nice = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label')
#     check_box_detail = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[3]/label')
#     check_box_med = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[4]/label')

#     checkbox_list = [check_box_pro, check_box_nice, check_box_detail, check_box_med]

#     pick = random.randint(1,4)
#     chosen_checkbox = random.choices(checkbox_list, k=pick)

#     for val in chosen_checkbox:
#         val.click()
    browser.quit()
        
    return

# 對第二間診所投票
def vote1():
    ua = UserAgent(verify_ssl=False)
    user_agent = ua.random
    options = Options()
    options.add_argument("window-size=800,800")
    options.add_argument(f'user-agent={user_agent}')
    print(user_agent)

    browser = webdriver.Chrome('./chromedriver', options=options)
#     browser = webdriver.Chrome('./chromedriver')
    
    browser.get('https://health.businessweekly.com.tw/event/2020/pediatrics/search.html?keywords=張虔熙&zipcode=0&page=1')

    try:
        agree_button = browser.find_element_by_xpath('//*[@id="gdrp"]')
        agree_button.click() 
        time.sleep(1)
#         scroll_down="var q=document.documentElement.scrollTop=1000"  
#         browser.execute_script(scroll_down)  

        vote_button = browser.find_element_by_xpath('//*[@id="search"]/section[3]/div[1]/div[1]/div[2]/a/picture/img')
        time.sleep(random.randint(2,3))
        vote_button.click()
        #time.sleep(random.randint(1,3))
#         //*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label
#         //*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label
        time.sleep(random.randint(2,3))
        check_box_pro = browser.find_element_by_xpath('//*[@id="doctor-49ef4f5a-b2dd-43f7-9147-526ae7424cb8"]/div[2]/div[1]/label')
        time.sleep(1)
        check_box_pro.click()
#         time.sleep(random.randint(1,2))
        submit_button = browser.find_element_by_xpath('//*[@id="doctor-49ef4f5a-b2dd-43f7-9147-526ae7424cb8"]/div[3]/a[1]')
        time.sleep(1)
        submit_button.click()
        time.sleep(1)
    except:
        browser.quit()
        return vote()

#     check_box_nice = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label')
#     check_box_nice.click()
#     check_box_detail = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[3]/label')
#     chekc_box_detail.click()
#     check_box_med = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[4]/label')
#     check_box_med.click()

#     check_box_pro = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[1]/label')
#     check_box_nice = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[2]/label')
#     check_box_detail = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[3]/label')
#     check_box_med = browser.find_element_by_xpath('//*[@id="doctor-141d027a-a272-4361-b095-fa8b47c6b3cd"]/div[2]/div[4]/label')

#     checkbox_list = [check_box_pro, check_box_nice, check_box_detail, check_box_med]

#     pick = random.randint(1,4)
#     chosen_checkbox = random.choices(checkbox_list, k=pick)

#     for val in chosen_checkbox:
#         val.click()
    browser.quit()
        
    return

def loopvote(n):
    time.sleep(1)
    while n>0:
        print('remained '+str(n))
        try:
            vote()
            n = n-1
        except:
            time.sleep(5)
            return loopvote(n)  
    return


if __name__ == '__main__':
    # jobs = []
    # 平行處理開影分身～
    for i in range(10): # 看要一次開幾個？先開 10 個
        # p = mp.Process(target=loopvote)
        p = mp.Process(target=loopvote, args=(1,))
        # jobs.append(p)
        p.start()


