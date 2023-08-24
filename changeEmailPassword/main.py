from time import sleep
from autoRecognition import autoRecognition
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/92.0.4896.127 Safari/537.36"
    )


driver = webdriver.Chrome(options=options)
driver.maximize_window()

# driver.implicitly_wait(4) # 设置等待20秒钟，等待页面元素加载完成再点下一步操作
driver.get("https://www.mail.com/")

# 点击显示登录页
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div[3]/a[2]").click()
sleep(2)

# 账号 必填
account = 'figovz@mail8.com.cn'

# 密码 必填
password = ''
password = ''

# 新密码 必填
new_password = ''

# 自动输入账号密码
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[2]/form/div[1]/input").send_keys(account)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[2]/form/div[2]/input").send_keys(password)

# 点击登录按钮
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[2]/form/button").click()
sleep(2)

# 获取当前页url
cur_url = driver.current_url

# 提起url中sid
sid = cur_url.split('=')[-1]

url = 'https://navigator-lxa.mail.com/ciss?sid=' + sid
driver.get(url)

# 休眠
sleep(2)

# 对比页面
autoRecognition(img_url='./1.png')
autoRecognition(img_url='./2.png', text=password)
autoRecognition(img_url='./3.png', text=new_password)
autoRecognition(img_url='./4.png', text=new_password)
autoRecognition(img_url='./5.png')

sleep(3)

# 关闭浏览器
driver.quit()
