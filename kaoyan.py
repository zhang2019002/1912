# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:code4
# File_name:kaoyan.py
# Author: ling
# Time:2020年07月15日

# 从appium模块中调用webdriver
from  appium import webdriver
import random

# 加入一个时间模块

desird_cap={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset":False
}


# 启动服务器的              服务器地址：appium端口号  服务器的启动路径
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desird_cap)
# 隐性等待20秒
driver.implicitly_wait(20)

def skip():
  '''点击跳过'''
  # id 定位  click()点击

  # 如果没有找到跳过ID，直接打印print（），如果找到直接点击。
  try:
    skip = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
  except:
    print('no skip element')
  else:
    skip.click()

skip()


def agreement():
  '''同意条约'''

  # 如果没有找到跳过ID，直接打印print（），如果找到直接点击。
  try:
    no_agree = driver.find_element_by_id('com.tal.kaoyan:id/tip_commit')
  except:
    print('click no_agree')
  else:
    no_agree.click()

agreement()

def login():
  '''点击注册'''
  driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
login()

def photo():
  '''头像'''
  driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.View/android.widget.RelativeLayout[3]/android.widget.ImageView').click()
  driver.find_element_by_id('com.tal.kaoyan:id/picture_tv_ok').click()
  driver.find_element_by_id('com.tal.kaoyan:id/menu_crop').click()

photo()

def product_name():
  '''随机产生账户'''

  username = 'zhang1298'+'zxl'+str(random.randint(1,200))
  return username
name = product_name()

def product_passwd():
  '''随机密码'''
  userpasswd = 'bowen123'+str(random.randint(1,200))
  return userpasswd
passwd = product_passwd()


def email_aa():
    '''随机邮箱'''
    useremail = 'zhang1583'+str(random.randint(1,2000))+'@163.com'
    return useremail
email = email_aa()

driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys(name)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys(passwd)
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys(email)

def login():
    # 点击立即注册

  driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
login()

def time_school():
  '''选择2020届'''
  driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_time').click()
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[5]').click()
time_school()

def zhuanye():
  '''选择专业'''
  driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView').click()

  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.widget.TextView').click()

zhuanye()


def school():
    # 选择学校
  driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_school').click()
  driver.find_element_by_class_name('android.widget.LinearLayout')
  driver.tap([(128,1066),(127,1096)],200)
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[2]/android.widget.TextView[1]').click()
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ExpandableListView/android.widget.LinearLayout[3]/android.widget.TextView').click()
  driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/android.widget.LinearLayout')
  driver.tap([(658,955),(677,955)],200)

school()

def login_0():
    # 保存资料
  driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_goBtn').click()

login_0()






