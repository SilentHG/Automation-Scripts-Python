from selenium import webdriver
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from gspread.models import Cell
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--ignore-certificate-errors")


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Intraday Stock Finder Tool").sheet1

chrome_path = r"C:\Shakir\chromedriver.exe"
#chrome_path = r"C:\Users\shaki\PycharmProjects\_ScrappingModule\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)
#driver = webdriver.Chrome(chrome_path)

driver.get("https://chartink.com/login")
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/form/div[1]/div/input").send_keys(
    "email.com")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/form/div[2]/div/input").send_keys("password")
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/form/div[4]/div/button").click()



time.sleep(10)

driver.get("https://chartink.com/dashboard/7135")

time.sleep(5)

t_a_list = []
t_b_list = []
t_c_list = []
t_d_list = []
t_x_list = []

while True:
    try:
        row_change_a = 7
        row_change_b = 7
        row_change_c = 7

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print(str(current_time))

        driver.get("https://chartink.com/dashboard/7135")
        time.sleep(10)
        t_a_list.clear()
        t_b_list.clear()
        t_c_list.clear()
        t_d_list.clear()
        t_x_list.clear()
        t_a_rows = len(driver.find_elements(By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr'))

        for i in range(1, t_a_rows + 1):
            t_a_list.append(driver.find_element(
                By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/span/a').text)

            # B START

        t_b_rows = len(driver.find_elements(By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[5]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr'))


        for i in range(1, t_b_rows + 1):
            t_b_list.append(driver.find_element(
                By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[5]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/span/a').text)

            # C START

        t_c_rows = len(driver.find_elements(By.XPATH, '/html/body/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr'))

        for i in range(1, t_c_rows + 1):
            t_c_list.append(driver.find_element(
                By.XPATH, '/html/body/div/div/div[3]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/span/a').text)

            # D START

        t_d_rows = len(driver.find_elements(By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[4]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr'))

        for i in range(1, t_d_rows + 1):
            t_d_list.append(driver.find_element(
                By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[4]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/span/a').text)

            # X START HERE
        t_x_rows = len(driver.find_elements(By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr'))
        html_tag = driver.find_element_by_tag_name("html")
        t_x_click = driver.find_element(By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div/div/div[2]/table/thead/tr/th[2]/span').click()
        for i in range(1, t_x_rows + 1):
            t_x_list.append(driver.find_element(
                By.XPATH, '//*[@id="atlas-grid-layout"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div/div/div[2]/table/tbody/tr['+str(i)+']/td[1]/span/a').text)
            html_tag.send_keys(Keys.ARROW_DOWN)
            time.sleep(1)

        while ("" in t_a_list):
            t_a_list.remove("")
        while ("" in t_b_list):
            t_b_list.remove("")
        while ("" in t_c_list):
            t_c_list.remove("")
        while ("" in t_d_list):
            t_d_list.remove("")

            sheet.update_cell(3, 2, str(current_time))
            cells = []
            cells.append(Cell(row=7, col=1, value=''))
            cells.append(Cell(row=8, col=1, value=''))
            cells.append(Cell(row=9, col=1, value=''))
            cells.append(Cell(row=10, col=1, value=''))
            cells.append(Cell(row=11, col=1, value=''))
            cells.append(Cell(row=12, col=1, value=''))
            cells.append(Cell(row=13, col=1, value=''))
            cells.append(Cell(row=7, col=2, value=''))
            cells.append(Cell(row=8, col=2, value=''))
            cells.append(Cell(row=9, col=2, value=''))
            cells.append(Cell(row=10, col=2, value=''))
            cells.append(Cell(row=11, col=2, value=''))
            cells.append(Cell(row=12, col=2, value=''))
            cells.append(Cell(row=13, col=2, value=''))
            cells.append(Cell(row=7, col=4, value=''))
            cells.append(Cell(row=8, col=4, value=''))
            cells.append(Cell(row=9, col=4, value=''))
            cells.append(Cell(row=10, col=4, value=''))
            cells.append(Cell(row=11, col=4, value=''))
            cells.append(Cell(row=12, col=4, value=''))
            cells.append(Cell(row=13, col=4, value=''))
            cells.append(Cell(row=7, col=5, value=''))
            cells.append(Cell(row=8, col=5, value=''))
            cells.append(Cell(row=9, col=5, value=''))
            cells.append(Cell(row=10, col=5, value=''))
            cells.append(Cell(row=11, col=5, value=''))
            cells.append(Cell(row=12, col=5, value=''))
            cells.append(Cell(row=13, col=5, value=''))
            cells.append(Cell(row=7, col=7, value=''))
            cells.append(Cell(row=8, col=7, value=''))
            cells.append(Cell(row=9, col=7, value=''))
            cells.append(Cell(row=10, col=7, value=''))
            cells.append(Cell(row=11, col=7, value=''))
            cells.append(Cell(row=12, col=7, value=''))
            cells.append(Cell(row=13, col=7, value=''))
            cells.append(Cell(row=14, col=7, value=''))
            cells.append(Cell(row=15, col=7, value=''))
            cells.append(Cell(row=16, col=7, value=''))
            cells.append(Cell(row=17, col=7, value=''))
            cells.append(Cell(row=18, col=7, value=''))
            cells.append(Cell(row=19, col=7, value=''))
            cells.append(Cell(row=20, col=7, value=''))
            sheet.update_cells(cells)

        for i in range(0,len(t_b_list)):
            if t_b_list[i] in t_a_list:
                sheet.update_cell(row_change_a, 1, str(i+1))
                sheet.update_cell(row_change_a, 2, str(t_b_list[i]))
                row_change_a += 1

        for i in range(0,len(t_d_list)):
            if t_d_list[i] in t_c_list:
                sheet.update_cell(row_change_b, 4, str(i+1))
                sheet.update_cell(row_change_b, 5, str(t_d_list[i]))
                row_change_b += 1


        for i in range(0,len(t_b_list)):
            if t_b_list[i] in t_a_list and t_b_list[i] in t_x_list:
                sheet.update_cell(row_change_c, 7, str(t_b_list[i]))
                row_change_c += 1


        for i in range(0,len(t_b_list)):
            if t_d_list[i] in t_c_list and t_d_list[i] in t_x_list:
                sheet.update_cell(row_change_c, 7, str(t_d_list[i]))
                row_change_c += 1



        for i in range(len(t_a_list)):
            print(t_a_list[i])

        print("A END HERE")
        for i in range(len(t_b_list)):
            print(t_b_list[i])

        print("B END HERE")
        for i in range(len(t_c_list)):
            print(t_c_list[i])

        print("C END HERE")
        for i in range(len(t_d_list)):
            print(t_d_list[i])

        print("D END HERE")
        for i in range(len(t_x_list)):
            print(t_x_list[i])

        print("X END HERE")

        time.sleep(60)
    except Exception as e:
        print(str(e)+ "GOING ON A 60 SECOND BREAK")
        time.sleep(60)

