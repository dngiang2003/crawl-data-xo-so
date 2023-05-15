from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json

options = webdriver.ChromeOptions()
options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=options)
driver.set_window_rect(0, 0, 810, 1030)

driver.get("https://www.thantai.net/so-ket-qua")
sleep(2)
driver.find_element(By.ID, "daycount").clear()
sleep(0.5)
driver.find_element(By.ID, "daycount").send_keys(300)
sleep(0.5)
driver.find_element(By.XPATH, '//*[@id="skq"]/form/div[3]/div/button').click()
sleep(3)

def get_element_text(xpath):
    return driver.find_element(By.XPATH, xpath).text

with open("data.csv", "w") as f:
    f.write("DATE, DB, G1, G2, G3, G4, G5, G6, G7, KT\n")
f.close()

def write_to_csv(data):
    with open("data.csv", "a") as f:
        f.write(data)
    f.close()

def get_result(idText):
    date = get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/thead/tr/th/span[3]')
    date = date.replace("-", "/")

    dacbiet = get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[1]/td[2]/div/div')

    g1 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[2]/td[2]/div/div')])

    g2 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[3]/td[2]/div/div[{i}]') for i in range(1, 3)])

    g3 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[4]/td[2]/div/div[{i}]') for i in range(1, 7)])

    g4 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[5]/td[2]/div/div[{i}]') for i in range(1, 5)])

    g5 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[6]/td[2]/div/div[{i}]') for i in range(1, 7)])

    g6 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[7]/td[2]/div/div[{i}]') for i in range(1, 4)])

    g7 = '-'.join([get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[8]/td[2]/div/div[{i}]') for i in range(1, 5)])

    kytu = get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[9]/td[2]/div/div')

    return f"{date}, {dacbiet}, {g1}, {g2}, {g3}, {g4}, {g5}, {g6}, {g7}, {kytu}\n"


for i in range(1, 360):
    try:
        data = get_result(i)
        write_to_csv(data)
        sleep(0.2)
    except:
        print(f"Lỗi tại vị trí {i} không có dữ liệu!")
driver.quit()
