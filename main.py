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


def write_to_json(data):
    with open("data.json", 'a+') as f:
        json.dump(data, f)
        f.write('\n')


def get_result(idText):
    result = {}
    result["date"] = get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/thead/tr/th/span[3]')
    result["date"] = result["date"].replace("-", "/")

    result["dacbiet"] = int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[1]/td[2]/div/div'))

    result["g1"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[2]/td[2]/div/div'))]

    result["g2"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[3]/td[2]/div/div[1]')),
                   int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[3]/td[2]/div/div[2]'))]

    result["g3"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[4]/td[2]/div/div[{i}]')) for i in range(1, 7)]

    result["g4"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[5]/td[2]/div/div[{i}]')) for i in range(1, 5)]

    result["g5"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[6]/td[2]/div/div[{i}]')) for i in range(1, 7)]

    result["g6"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[7]/td[2]/div/div[{i}]')) for i in range(1, 4)]

    result["g7"] = [int(get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[8]/td[2]/div/div[{i}]')) for i in range(1, 5)]

    result["kytu"] = get_element_text(f'//*[@id="skq"]/div/div[{idText}]/div[1]/table/tbody/tr[9]/td[2]/div/div')

    return result


for i in range(1, 360):
    try:
        data = get_result(i)
        write_to_json(data)
    except:
        print(f"Lỗi tại vị trí {i} không có dữ liệu!")


driver.quit()

with open('data.json') as f:
    json_data = [json.loads(line) for line in f]

with open('data.json', 'w+') as f:
    json.dump(json_data, f)
print("Xong")
