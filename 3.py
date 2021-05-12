from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from gspread.models import Cell
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--ignore-certificate-errors")

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("silenthg-5eb4891adeb0.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Amazon").worksheet("sheet")

chrome_path = r"C:\Users\shaki\PycharmProjects\_ScrappingModule\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)
# driver = webdriver.Chrome(chrome_path)
curr_count = []
curr_count.append(1)
ava = "Available"
unava = "unavailable"
limited = "left"
changer = []
changer.append(1)
region = []
region.append("us")
while True:
    try:
        curr_price1 = ""
        curr_price2 = ""
        curr_link = sheet.cell(curr_count[-1], 1).value
        curr_link1 = sheet.cell(curr_count[-1] + 1, 1).value
        curr_link2 = sheet.cell(curr_count[-1] + 2, 1).value
        if curr_link != "":
            driver.get("https://www.proxysite.com/")
            time.sleep(10)
            url = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[3]/form/div[2]/input")
            url.send_keys(Keys.CONTROL + "a")
            url.send_keys(Keys.DELETE)
            url.send_keys(str(curr_link))
            element = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[3]/form/div[1]/select")
            drp = Select(element)
            drp.select_by_value(region[-1] + str(changer[-1]))

            button_cli = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[3]/form/div[2]/button")
            button_cli.click()
            time.sleep(15)


            try:
                curr_price1 = str(driver.find_element_by_xpath(
                    "/html/body/div[5]/div[3]/div/div[1]/div/div/div/div[2]/div[1]/span[1]").text)

            except Exception as exp:
                curr_price1 = ""

            if curr_price1 != "":
                sheet.update_cell(curr_count[-1], 5, str(curr_price1))
                sheet.update_cell(curr_count[-1], 4, "Available")
            else:
                sheet.update_cell(curr_count[-1], 4, "Unavailable")

        elif curr_link == "" and curr_link1 == "" and curr_link2 == "":
            print("Going on a 15 min Break" + str(time.localtime()))
            time.sleep(30)
            curr_count.append(curr_count[-1] - 1)
    except Exception as e:
        print(e)
        print("Something happened, Going for a 100 Second Break")
        time.sleep(100)
    curr_count.append(curr_count[-1] + 1)
    time.sleep(15)
    if curr_count[-1] % 20 == 0:
        changer.append(changer[-1] + 1)

    if changer[-1] == 11:
        changer.clear()
        changer.append(1)
    print("Running Product No: " + str(curr_count[-1]))
    print("Current Region:" + str(region[-1]))
    print("Current Region Code: " + str(changer[-1]))
