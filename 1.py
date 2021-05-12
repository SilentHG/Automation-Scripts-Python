from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from tkinter import *
import ssl
import smtplib
from plyer import notification as notifications
import gspread
from oauth2client.service_account import ServiceAccountCredentials

email_alerts = True
notification = True
live_data = True

start_hours = int(time.strftime("%H", time.localtime()))
start_mins = time.strftime("%M", time.localtime())

start_total_hour = start_hours * 60
start_time_here = []
start_time_here.append(start_total_hour + int(start_mins))

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("silenthg-5eb4891adeb0.json", scope)

client = gspread.authorize(creds)

sheet = client.open("live data").sheet1
sheet.clear()
current_index = []
current_index.append(2)

notifications.notify(
    title='Please Wait 30 Secs',
    message='Minimize Console and Browser when page is loaded',
    timeout=10
)

sender_email = ""
receiver_email = sender_email
sender_password = ""
port = 465
context = ssl.create_default_context()
buy_tuple = ("Buy", "Strong Buy")
sell_tuple = ("Sell", "Strong Sell")

chrome_path = r"C:\Users\shaki\PycharmProjects\_ScrappingModule\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
# driver.get("https://www.investing.com/currencies/gbp-usd")


myWindow = Tk()
myWindow.title("Live Data")
myWindow.geometry("500x600")
myWindow.configure(bg="light blue")

EUROne = Label(myWindow, text="One_min_Data", font="none 12 bold")
EURFive = Label(myWindow, text="Five_min_Data", font="none 12 bold")
EURFifteen = Label(myWindow, text="Fifteen_min_Data", font="none 12 bold")
EURThirty = Label(myWindow, text="Thirty_min_Data", font="none 12 bold")
EURHour = Label(myWindow, text="Hour_min_Data", font="none 12 bold")
EURFiveHour = Label(myWindow, text="5 Hour_min_Data", font="none 12 bold")

BankLine3 = Label(myWindow, text="", bg="light blue")

EUROne.pack()
EURFive.pack()
EURFifteen.pack()
EURThirty.pack()
EURHour.pack()
EURFiveHour.pack()
BankLine3.pack()

GBPOne = Label(myWindow, text="One_min_Data", font="none 12 bold")
GBPFive = Label(myWindow, text="Five_min_Data", font="none 12 bold")
GBPFifteen = Label(myWindow, text="Fifteen_min_Data", font="none 12 bold")
GBPThirty = Label(myWindow, text="Thirty_min_Data", font="none 12 bold")
GBPHour = Label(myWindow, text="Hour_min_Data", font="none 12 bold")
GBPFiveHour = Label(myWindow, text="5 Hour_min_Data", font="none 12 bold")

BankLine1 = Label(myWindow, text="", bg="light blue")

GBPOne.pack()
GBPFive.pack()
GBPFifteen.pack()
GBPThirty.pack()
GBPHour.pack()
GBPFiveHour.pack()
BankLine1.pack()

USDOne = Label(myWindow, text="One_min_Data", font="none 12 bold")
USDFive = Label(myWindow, text="Five_min_Data", font="none 12 bold")
USDFifteen = Label(myWindow, text="Fifteen_min_Data", font="none 12 bold")
USDThirty = Label(myWindow, text="Thirty_min_Data", font="none 12 bold")
USDHour = Label(myWindow, text="Hour_min_Data", font="none 12 bold")
USDFiveHour = Label(myWindow, text="5 Hour_min_Data", font="none 12 bold")

BankLine2 = Label(myWindow, text="", bg="light blue")

USDOne.pack()
USDFive.pack()
USDFifteen.pack()
USDThirty.pack()
USDHour.pack()
USDFiveHour.pack()
BankLine2.pack()

Time_Label = Label(myWindow, text="Current Time", font="none 16 bold")
Time_Label.pack()

eur_fifteen_old_signal = []
eur_one_hour_old_signal = []
eur_five_hour_old_signal = []

gbp_fifteen_old_signal = []
gbp_one_hour_old_signal = []
gbp_five_hour_old_signal = []

usd_fifteen_old_signal = []
usd_one_hour_old_signal = []
usd_five_hour_old_signal = []

check_list = [0]

time.sleep(2)


def my_mainloop():
    try:
        if check_list[-1] == 0:
            check_list.append(1)

            driver.get("https://www.investing.com/currencies/gbp-usd")
            time.sleep(10)
            element = driver.find_element_by_xpath("/html/body/div[5]/aside/div[6]/div[2]/div[2]/div[1]/select")
            drp = Select(element)

            drp.select_by_visible_text("1")
            element.send_keys("1")
            time.sleep(2)

            eur_one_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_one_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_one_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_One_min_Data = str(
                "1 min Data : " + eur_one_min_name + "  " + eur_one_min_price + "  " + eur_one_min_signal)

            gbp_one_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_one_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_one_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_One_min_Data = str(
                "1 min Data : " + gbp_one_min_name + "  " + gbp_one_min_price + "  " + gbp_one_min_signal)

            usd_one_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_one_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_one_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_One_min_Data = str(
                "1 min Data : " + usd_one_min_name + "  " + usd_one_min_price + "  " + usd_one_min_signal)

            time.sleep(2)

            element.send_keys("2")  # 5 Min
            time.sleep(2)

            eur_five_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_five_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_five_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Five_min_Data = str(
                "5 min Data : " + eur_five_min_name + "  " + eur_five_min_price + "  " + eur_five_min_signal)

            gbp_five_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_five_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_five_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Five_min_Data = str(
                "5 min Data : " + gbp_five_min_name + "  " + gbp_five_min_price + "  " + gbp_five_min_signal)

            usd_five_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_five_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_five_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Five_min_Data = str(
                "5 min Data : " + usd_five_min_name + "  " + usd_five_min_price + "  " + usd_five_min_signal)

            time.sleep(2)

            element.send_keys("3")  # 15 Min
            time.sleep(2)

            eur_fifteen_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_fifteen_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_fifteen_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Fifteen_min_Data = str(
                "15 min Data : " + eur_fifteen_min_name + "  " + eur_fifteen_min_price + "  " + eur_fifteen_min_signal)

            gbp_fifteen_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_fifteen_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_fifteen_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Fifteen_min_Data = str(
                "15 min Data : " + gbp_fifteen_min_name + "  " + gbp_fifteen_min_price + "  " + gbp_fifteen_min_signal)

            usd_fifteen_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_fifteen_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_fifteen_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Fifteen_min_Data = str(
                "15 min Data : " + usd_fifteen_min_name + "  " + usd_fifteen_min_price + "  " + usd_fifteen_min_signal)

            time.sleep(2)

            element.send_keys("3")  # 30 Min
            time.sleep(2)

            eur_thirty_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_thirty_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_thirty_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Thirty_min_Data = str(
                "30 min Data : " + eur_thirty_min_name + "  " + eur_thirty_min_price + "  " + eur_thirty_min_signal)

            gbp_thirty_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_thirty_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_thirty_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Thirty_min_Data = str(
                "30 min Data : " + gbp_thirty_min_name + "  " + gbp_thirty_min_price + "  " + gbp_thirty_min_signal)

            usd_thirty_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_thirty_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_thirty_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Thirty_min_Data = str(
                "30 min Data : " + usd_thirty_min_name + "  " + usd_thirty_min_price + "  " + usd_thirty_min_signal)

            time.sleep(2)

            element.send_keys("1 h")  # 1 Hour
            time.sleep(2)

            eur_one_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_one_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_one_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_One_Hour_Data = str(
                "1 hour Data : " + eur_one_hour_name + "  " + eur_one_hour_price + "  " + eur_one_hour_signal)

            gbp_one_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_one_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_one_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_One_Hour_Data = str(
                "1 hour Data : " + gbp_one_hour_name + "  " + gbp_one_hour_price + "  " + gbp_one_hour_signal)

            usd_one_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_one_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_one_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_One_Hour_Data = str(
                "1 hour Data : " + usd_one_hour_name + "  " + usd_one_hour_price + "  " + usd_one_hour_signal)

            time.sleep(2)

            element.send_keys("5 h")  # 5 Hour
            time.sleep(2)

            eur_five_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_five_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_five_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Five_Hour_Data = str(
                "5 hour Data : " + eur_five_hour_name + "  " + eur_five_hour_price + "  " + eur_five_hour_signal)

            gbp_five_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_five_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_five_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Five_Hour_Data = str(
                "5 hour Data : " + gbp_five_hour_name + "  " + gbp_five_hour_price + "  " + gbp_five_hour_signal)

            usd_five_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_five_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_five_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Five_Hour_Data = str(
                "5 hour Data : " + usd_five_hour_name + "  " + usd_five_hour_price + "  " + usd_five_hour_signal)

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            if eur_one_min_signal in buy_tuple:
                EUROne.config(text=EUR_One_min_Data, bg="green yellow")
            elif eur_one_min_signal in sell_tuple:
                EUROne.config(text=EUR_One_min_Data, bg="indian red")
            else:
                EUROne.config(text=EUR_One_min_Data, bg="dodger blue")

            if eur_five_min_signal in buy_tuple:
                EURFive.config(text=EUR_Five_min_Data, bg="green yellow")
            elif eur_five_min_signal in sell_tuple:
                EURFive.config(text=EUR_Five_min_Data, bg="indian red")
            else:
                EURFive.config(text=EUR_Five_min_Data, bg="dodger blue")

            if eur_fifteen_min_signal in buy_tuple:
                EURFifteen.config(text=EUR_Fifteen_min_Data, bg="green yellow")
            elif eur_fifteen_min_signal in sell_tuple:
                EURFifteen.config(text=EUR_Fifteen_min_Data, bg="indian red")
            else:
                EURFifteen.config(text=EUR_Fifteen_min_Data, bg="dodger blue")

            if eur_thirty_min_signal in buy_tuple:
                EURThirty.config(text=EUR_Thirty_min_Data, bg="green yellow")
            elif eur_thirty_min_signal in sell_tuple:
                EURThirty.config(text=EUR_Thirty_min_Data, bg="indian red")
            else:
                EURThirty.config(text=EUR_Thirty_min_Data, bg="dodger blue")

            if eur_one_hour_signal in buy_tuple:
                EURHour.config(text=EUR_One_Hour_Data, bg="green yellow")
            elif eur_one_hour_signal in sell_tuple:
                EURHour.config(text=EUR_One_Hour_Data, bg="indian red")
            else:
                EURHour.config(text=EUR_One_Hour_Data, bg="dodger blue")

            if eur_five_hour_signal in buy_tuple:
                EURFiveHour.config(text=EUR_Five_Hour_Data, bg="green yellow")
            elif eur_five_hour_signal in sell_tuple:
                EURFiveHour.config(text=EUR_Five_Hour_Data, bg="indian red")
            else:
                EURFiveHour.config(text=EUR_Five_Hour_Data, bg="dodger blue")

            if gbp_one_min_signal in buy_tuple:
                GBPOne.config(text=GBP_One_min_Data, bg="green yellow")
            elif gbp_one_min_signal in sell_tuple:
                GBPOne.config(text=GBP_One_min_Data, bg="indian red")
            else:
                GBPOne.config(text=GBP_One_min_Data, bg="dodger blue")

            if gbp_five_min_signal in buy_tuple:
                GBPFive.config(text=GBP_Five_min_Data, bg="green yellow")
            elif gbp_five_min_signal in sell_tuple:
                GBPFive.config(text=GBP_Five_min_Data, bg="indian red")
            else:
                GBPFive.config(text=GBP_Five_min_Data, bg="dodger blue")

            if gbp_fifteen_min_signal in buy_tuple:
                GBPFifteen.config(text=GBP_Fifteen_min_Data, bg="green yellow")
            elif gbp_fifteen_min_signal in sell_tuple:
                GBPFifteen.config(text=GBP_Fifteen_min_Data, bg="indian red")
            else:
                GBPFifteen.config(text=GBP_Fifteen_min_Data, bg="dodger blue")

            if gbp_thirty_min_signal in buy_tuple:
                GBPThirty.config(text=GBP_Thirty_min_Data, bg="green yellow")
            elif gbp_thirty_min_signal in sell_tuple:
                GBPThirty.config(text=GBP_Thirty_min_Data, bg="indian red")
            else:
                GBPThirty.config(text=GBP_Thirty_min_Data, bg="dodger blue")

            if gbp_one_hour_signal in buy_tuple:
                GBPHour.config(text=GBP_One_Hour_Data, bg="green yellow")
            elif gbp_one_hour_signal in sell_tuple:
                GBPHour.config(text=GBP_One_Hour_Data, bg="indian red")
            else:
                GBPHour.config(text=GBP_One_Hour_Data, bg="dodger blue")

            if gbp_five_hour_signal in buy_tuple:
                GBPFiveHour.config(text=GBP_Five_Hour_Data, bg="green yellow")
            elif gbp_five_hour_signal in sell_tuple:
                GBPFiveHour.config(text=GBP_Five_Hour_Data, bg="indian red")
            else:
                GBPFiveHour.config(text=GBP_Five_Hour_Data, bg="dodger blue")

            if usd_one_min_signal in buy_tuple:
                USDOne.config(text=USD_One_min_Data, bg="green yellow")
            elif usd_one_min_signal in sell_tuple:
                USDOne.config(text=USD_One_min_Data, bg="indian red")
            else:
                USDOne.config(text=USD_One_min_Data, bg="dodger blue")

            if usd_five_min_signal in buy_tuple:
                USDFive.config(text=USD_Five_min_Data, bg="green yellow")
            elif usd_five_min_signal in sell_tuple:
                USDFive.config(text=USD_Five_min_Data, bg="indian red")
            else:
                USDFive.config(text=USD_Five_min_Data, bg="dodger blue")

            if usd_fifteen_min_signal in buy_tuple:
                USDFifteen.config(text=USD_Fifteen_min_Data, bg="green yellow")
            elif usd_fifteen_min_signal in sell_tuple:
                USDFifteen.config(text=USD_Fifteen_min_Data, bg="indian red")
            else:
                USDFifteen.config(text=USD_Fifteen_min_Data, bg="dodger blue")

            if usd_thirty_min_signal in buy_tuple:
                USDThirty.config(text=USD_Thirty_min_Data, bg="green yellow")
            elif usd_thirty_min_signal in sell_tuple:
                USDThirty.config(text=USD_Thirty_min_Data, bg="indian red")
            else:
                USDThirty.config(text=USD_Thirty_min_Data, bg="dodger blue")

            if usd_one_hour_signal in buy_tuple:
                USDHour.config(text=USD_One_Hour_Data, bg="green yellow")
            elif usd_one_hour_signal in sell_tuple:
                USDHour.config(text=USD_One_Hour_Data, bg="indian red")
            else:
                USDHour.config(text=USD_One_Hour_Data, bg="dodger blue")

            if usd_five_hour_signal in buy_tuple:
                USDFiveHour.config(text=USD_Five_Hour_Data, bg="green yellow")
            elif usd_five_hour_signal in sell_tuple:
                USDFiveHour.config(text=USD_Five_Hour_Data, bg="indian red")
            else:
                USDFiveHour.config(text=USD_Five_Hour_Data, bg="dodger blue")

            Time_Label.config(text="Last Update At " + current_time, bg="yellow")

            eur_fifteen_old_signal.append(eur_fifteen_min_signal)
            eur_one_hour_old_signal.append(eur_one_hour_signal)
            eur_five_hour_old_signal.append(eur_five_hour_signal)

            gbp_fifteen_old_signal.append(gbp_fifteen_min_signal)
            gbp_one_hour_old_signal.append(gbp_one_hour_signal)
            gbp_five_hour_old_signal.append(gbp_five_hour_signal)

            usd_fifteen_old_signal.append(usd_fifteen_min_signal)
            usd_one_hour_old_signal.append(usd_one_hour_signal)
            usd_five_hour_old_signal.append(usd_five_hour_signal)
        else:
            driver.get("https://www.investing.com/currencies/gbp-usd")
            time.sleep(10)
            element = driver.find_element_by_xpath("/html/body/div[5]/aside/div[6]/div[2]/div[2]/div[1]/select")
            #drp = Select(element)

            #drp.select_by_value("60")  # 1 Min.
            element.send_keys("1 min.")

            time.sleep(2)

            eur_one_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_one_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_one_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_One_min_Data = str(
                "1 min Data : " + eur_one_min_name + "  " + eur_one_min_price + "  " + eur_one_min_signal)

            gbp_one_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_one_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_one_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_One_min_Data = str(
                "1 min Data : " + gbp_one_min_name + "  " + gbp_one_min_price + "  " + gbp_one_min_signal)

            usd_one_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_one_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_one_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_One_min_Data = str(
                "1 min Data : " + usd_one_min_name + "  " + usd_one_min_price + "  " + usd_one_min_signal)

            time.sleep(2)

            element.send_keys("5 mins")  # 5 Min
            time.sleep(2)

            eur_five_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_five_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_five_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Five_min_Data = str(
                "5 min Data : " + eur_five_min_name + "  " + eur_five_min_price + "  " + eur_five_min_signal)

            gbp_five_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_five_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_five_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Five_min_Data = str(
                "5 min Data : " + gbp_five_min_name + "  " + gbp_five_min_price + "  " + gbp_five_min_signal)

            usd_five_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_five_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_five_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Five_min_Data = str(
                "5 min Data : " + usd_five_min_name + "  " + usd_five_min_price + "  " + usd_five_min_signal)

            time.sleep(2)

            element.send_keys("15 mins")  # 15 Min
            time.sleep(2)

            eur_fifteen_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_fifteen_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_fifteen_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Fifteen_min_Data = str(
                "15 min Data : " + eur_fifteen_min_name + "  " + eur_fifteen_min_price + "  " + eur_fifteen_min_signal)

            gbp_fifteen_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_fifteen_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_fifteen_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Fifteen_min_Data = str(
                "15 min Data : " + gbp_fifteen_min_name + "  " + gbp_fifteen_min_price + "  " + gbp_fifteen_min_signal)

            usd_fifteen_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_fifteen_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_fifteen_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Fifteen_min_Data = str(
                "15 min Data : " + usd_fifteen_min_name + "  " + usd_fifteen_min_price + "  " + usd_fifteen_min_signal)

            time.sleep(2)

            element.send_keys("30 mins")  # 30 Min
            time.sleep(2)

            eur_thirty_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_thirty_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_thirty_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Thirty_min_Data = str(
                "30 min Data : " + eur_thirty_min_name + "  " + eur_thirty_min_price + "  " + eur_thirty_min_signal)

            gbp_thirty_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_thirty_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_thirty_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Thirty_min_Data = str(
                "30 min Data : " + gbp_thirty_min_name + "  " + gbp_thirty_min_price + "  " + gbp_thirty_min_signal)

            usd_thirty_min_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_thirty_min_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_thirty_min_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Thirty_min_Data = str(
                "30 min Data : " + usd_thirty_min_name + "  " + usd_thirty_min_price + "  " + usd_thirty_min_signal)

            time.sleep(2)

            element.send_keys("Hourly")  # 1 Hour
            time.sleep(2)

            eur_one_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_one_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_one_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_One_Hour_Data = str(
                "1 hour Data : " + eur_one_hour_name + "  " + eur_one_hour_price + "  " + eur_one_hour_signal)

            gbp_one_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_one_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_one_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_One_Hour_Data = str(
                "1 hour Data : " + gbp_one_hour_name + "  " + gbp_one_hour_price + "  " + gbp_one_hour_signal)

            usd_one_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_one_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_one_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_One_Hour_Data = str(
                "1 hour Data : " + usd_one_hour_name + "  " + usd_one_hour_price + "  " + usd_one_hour_signal)

            time.sleep(2)

            element.send_keys("5 Hours")  # 5 Hour
            time.sleep(2)

            eur_five_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[3]/a").text
            eur_five_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[4]").text
            eur_five_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[1]/td[5]").text
            EUR_Five_Hour_Data = str(
                "5 hour Data : " + eur_five_hour_name + "  " + eur_five_hour_price + "  " + eur_five_hour_signal)

            gbp_five_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[3]/a").text
            gbp_five_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[4]").text
            gbp_five_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[2]/td[5]").text
            GBP_Five_Hour_Data = str(
                "5 hour Data : " + gbp_five_hour_name + "  " + gbp_five_hour_price + "  " + gbp_five_hour_signal)

            usd_five_hour_name = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[3]/a").text
            usd_five_hour_price = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[4]").text
            usd_five_hour_signal = driver.find_element_by_xpath(
                "/html/body/div[5]/aside/div[6]/div[2]/div[4]/table/tbody/tr[3]/td[5]").text
            USD_Five_Hour_Data = str(
                "5 hour Data : " + usd_five_hour_name + "  " + usd_five_hour_price + "  " + usd_five_hour_signal)

            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)

            if eur_one_min_signal in buy_tuple:
                EUROne.config(text=EUR_One_min_Data, bg="green yellow")
            elif eur_one_min_signal in sell_tuple:
                EUROne.config(text=EUR_One_min_Data, bg="indian red")
            else:
                EUROne.config(text=EUR_One_min_Data, bg="dodger blue")

            if eur_five_min_signal in buy_tuple:
                EURFive.config(text=EUR_Five_min_Data, bg="green yellow")
            elif eur_five_min_signal in sell_tuple:
                EURFive.config(text=EUR_Five_min_Data, bg="indian red")
            else:
                EURFive.config(text=EUR_Five_min_Data, bg="dodger blue")

            if eur_fifteen_min_signal in buy_tuple:
                EURFifteen.config(text=EUR_Fifteen_min_Data, bg="green yellow")
            elif eur_fifteen_min_signal in sell_tuple:
                EURFifteen.config(text=EUR_Fifteen_min_Data, bg="indian red")
            else:
                EURFifteen.config(text=EUR_Fifteen_min_Data, bg="dodger blue")

            if eur_thirty_min_signal in buy_tuple:
                EURThirty.config(text=EUR_Thirty_min_Data, bg="green yellow")
            elif eur_thirty_min_signal in sell_tuple:
                EURThirty.config(text=EUR_Thirty_min_Data, bg="indian red")
            else:
                EURThirty.config(text=EUR_Thirty_min_Data, bg="dodger blue")

            if eur_one_hour_signal in buy_tuple:
                EURHour.config(text=EUR_One_Hour_Data, bg="green yellow")
            elif eur_one_hour_signal in sell_tuple:
                EURHour.config(text=EUR_One_Hour_Data, bg="indian red")
            else:
                EURHour.config(text=EUR_One_Hour_Data, bg="dodger blue")

            if eur_five_hour_signal in buy_tuple:
                EURFiveHour.config(text=EUR_Five_Hour_Data, bg="green yellow")
            elif eur_five_hour_signal in sell_tuple:
                EURFiveHour.config(text=EUR_Five_Hour_Data, bg="indian red")
            else:
                EURFiveHour.config(text=EUR_Five_Hour_Data, bg="dodger blue")

            if gbp_one_min_signal in buy_tuple:
                GBPOne.config(text=GBP_One_min_Data, bg="green yellow")
            elif gbp_one_min_signal in sell_tuple:
                GBPOne.config(text=GBP_One_min_Data, bg="indian red")
            else:
                GBPOne.config(text=GBP_One_min_Data, bg="dodger blue")

            if gbp_five_min_signal in buy_tuple:
                GBPFive.config(text=GBP_Five_min_Data, bg="green yellow")
            elif gbp_five_min_signal in sell_tuple:
                GBPFive.config(text=GBP_Five_min_Data, bg="indian red")
            else:
                GBPFive.config(text=GBP_Five_min_Data, bg="dodger blue")

            if gbp_fifteen_min_signal in buy_tuple:
                GBPFifteen.config(text=GBP_Fifteen_min_Data, bg="green yellow")
            elif gbp_fifteen_min_signal in sell_tuple:
                GBPFifteen.config(text=GBP_Fifteen_min_Data, bg="indian red")
            else:
                GBPFifteen.config(text=GBP_Fifteen_min_Data, bg="dodger blue")

            if gbp_thirty_min_signal in buy_tuple:
                GBPThirty.config(text=GBP_Thirty_min_Data, bg="green yellow")
            elif gbp_thirty_min_signal in sell_tuple:
                GBPThirty.config(text=GBP_Thirty_min_Data, bg="indian red")
            else:
                GBPThirty.config(text=GBP_Thirty_min_Data, bg="dodger blue")

            if gbp_one_hour_signal in buy_tuple:
                GBPHour.config(text=GBP_One_Hour_Data, bg="green yellow")
            elif gbp_one_hour_signal in sell_tuple:
                GBPHour.config(text=GBP_One_Hour_Data, bg="indian red")
            else:
                GBPHour.config(text=GBP_One_Hour_Data, bg="dodger blue")

            if gbp_five_hour_signal in buy_tuple:
                GBPFiveHour.config(text=GBP_Five_Hour_Data, bg="green yellow")
            elif gbp_five_hour_signal in sell_tuple:
                GBPFiveHour.config(text=GBP_Five_Hour_Data, bg="indian red")
            else:
                GBPFiveHour.config(text=GBP_Five_Hour_Data, bg="dodger blue")

            if usd_one_min_signal in buy_tuple:
                USDOne.config(text=USD_One_min_Data, bg="green yellow")
            elif usd_one_min_signal in sell_tuple:
                USDOne.config(text=USD_One_min_Data, bg="indian red")
            else:
                USDOne.config(text=USD_One_min_Data, bg="dodger blue")

            if usd_five_min_signal in buy_tuple:
                USDFive.config(text=USD_Five_min_Data, bg="green yellow")
            elif usd_five_min_signal in sell_tuple:
                USDFive.config(text=USD_Five_min_Data, bg="indian red")
            else:
                USDFive.config(text=USD_Five_min_Data, bg="dodger blue")

            if usd_fifteen_min_signal in buy_tuple:
                USDFifteen.config(text=USD_Fifteen_min_Data, bg="green yellow")
            elif usd_fifteen_min_signal in sell_tuple:
                USDFifteen.config(text=USD_Fifteen_min_Data, bg="indian red")
            else:
                USDFifteen.config(text=USD_Fifteen_min_Data, bg="dodger blue")

            if usd_thirty_min_signal in buy_tuple:
                USDThirty.config(text=USD_Thirty_min_Data, bg="green yellow")
            elif usd_thirty_min_signal in sell_tuple:
                USDThirty.config(text=USD_Thirty_min_Data, bg="indian red")
            else:
                USDThirty.config(text=USD_Thirty_min_Data, bg="dodger blue")

            if usd_one_hour_signal in buy_tuple:
                USDHour.config(text=USD_One_Hour_Data, bg="green yellow")
            elif usd_one_hour_signal in sell_tuple:
                USDHour.config(text=USD_One_Hour_Data, bg="indian red")
            else:
                USDHour.config(text=USD_One_Hour_Data, bg="dodger blue")

            if usd_five_hour_signal in buy_tuple:
                USDFiveHour.config(text=USD_Five_Hour_Data, bg="green yellow")
            elif usd_five_hour_signal in sell_tuple:
                USDFiveHour.config(text=USD_Five_Hour_Data, bg="indian red")
            else:
                USDFiveHour.config(text=USD_Five_Hour_Data, bg="dodger blue")

            Time_Label.config(text="Last Update At " + current_time, bg="yellow")
            if live_data:
                index_after = 2
                hours = int(time.strftime("%H", time.localtime()))
                mins = time.strftime("%M", time.localtime())
                total_hour = hours * 60
                current_time_here = total_hour + int(mins)
                if start_time_here[-1] != current_time_here:
                    if abs(current_time_here - start_time_here[-1]) % 5 == 0 or abs(
                            current_time_here - start_time_here[-1]) % 5 == 1:
                        sheet.update_cell(1, 1, "Time")
                        sheet.update_cell(2, 1, "EUR")
                        sheet.update_cell(3, 1, "1 MIN")
                        sheet.update_cell(4, 1, "5 MIN")
                        sheet.update_cell(5, 1, "15 MIN")
                        sheet.update_cell(6, 1, "30 MIN")
                        sheet.update_cell(7, 1, "1 HOUR")
                        sheet.update_cell(8, 1, "5 HOUR")

                        sheet.update_cell(10, 1, "GBP")
                        sheet.update_cell(11, 1, "1 MIN")
                        sheet.update_cell(12, 1, "5 MIN")
                        sheet.update_cell(13, 1, "15 MIN")
                        sheet.update_cell(14, 1, "30 MIN")
                        sheet.update_cell(15, 1, "1 HOUR")
                        sheet.update_cell(16, 1, "5 HOUR")

                        sheet.update_cell(18, 1, "USD")
                        sheet.update_cell(19, 1, "1 MIN")
                        sheet.update_cell(20, 1, "5 MIN")
                        sheet.update_cell(21, 1, "15 MIN")
                        sheet.update_cell(22, 1, "30 MIN")
                        sheet.update_cell(23, 1, "1 HOUR")
                        sheet.update_cell(24, 1, "5 HOUR")

                        sheet.update_cell(1, current_index[-1], time.strftime("%H:%M", time.localtime()))
                        sheet.update_cell(2, current_index[-1], eur_one_min_price)
                        sheet.update_cell(3, current_index[-1], eur_one_min_signal)
                        sheet.update_cell(4, current_index[-1], eur_five_min_signal)
                        sheet.update_cell(5, current_index[-1], eur_fifteen_min_signal)
                        sheet.update_cell(6, current_index[-1], eur_thirty_min_signal)
                        sheet.update_cell(7, current_index[-1], eur_one_hour_signal)
                        sheet.update_cell(8, current_index[-1], eur_five_hour_signal)

                        sheet.update_cell(10, current_index[-1], gbp_one_min_price)
                        sheet.update_cell(11, current_index[-1], gbp_one_min_signal)
                        sheet.update_cell(12, current_index[-1], gbp_five_min_signal)
                        sheet.update_cell(13, current_index[-1], gbp_fifteen_min_signal)
                        sheet.update_cell(14, current_index[-1], gbp_thirty_min_signal)
                        sheet.update_cell(15, current_index[-1], gbp_one_hour_signal)
                        sheet.update_cell(16, current_index[-1], gbp_five_hour_signal)

                        sheet.update_cell(18, current_index[-1], usd_one_min_price)
                        sheet.update_cell(19, current_index[-1], usd_one_min_signal)
                        sheet.update_cell(20, current_index[-1], usd_five_min_signal)
                        sheet.update_cell(21, current_index[-1], usd_fifteen_min_signal)
                        sheet.update_cell(22, current_index[-1], usd_thirty_min_signal)
                        sheet.update_cell(23, current_index[-1], usd_one_hour_signal)
                        sheet.update_cell(24, current_index[-1], usd_five_hour_signal)

                        current_index.append(current_index[-1] + 1)

                        notifications.notify(
                            title="DATA IS LOADED INTO EXCEL",
                            message=" DATA IS LOADED FOR "+current_time, timeout=10)
                        time.sleep(11)

                    if current_index[-1] == 60:
                        start_time_here.append(current_time_here)
                        sheet.clear()
                        current_index.clear()
                        current_index.append(2)
                        index_after = 2

            if email_alerts:

                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login(sender_email, sender_password)
                    # 15 Min LOGIC FOR 3 Currencies
                    if eur_fifteen_min_signal != eur_fifteen_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "EUR 15 MIN SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + eur_fifteen_min_signal + " Previous Signal Was " +
                               eur_fifteen_old_signal[-1])
                        message1 = "EUR 15 Signal Changed TO " + eur_fifteen_min_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + eur_fifteen_old_signal[-1], timeout=10)
                        time.sleep(11)
                        eur_fifteen_old_signal.append(eur_fifteen_min_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    if gbp_fifteen_min_signal != gbp_fifteen_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 15 MIN SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + gbp_fifteen_min_signal + " Previous Signal Was " +
                               gbp_fifteen_old_signal[-1])
                        message1 = "GBP 15 Signal Changed TO " + gbp_fifteen_min_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + gbp_fifteen_old_signal[-1], timeout=10)
                        time.sleep(11)
                        gbp_fifteen_old_signal.append(gbp_fifteen_min_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    if usd_fifteen_min_signal != usd_fifteen_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "USD 15 MIN SIGNAL CHANGED",
                               "CURRENT SIGNAL IS" + usd_fifteen_min_signal + " Previous Signal Was " +
                               usd_fifteen_old_signal[-1])
                        message1 = "USD 15 Signal Changed TO " + usd_fifteen_min_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + usd_fifteen_old_signal[-1], timeout=10)
                        time.sleep(11)
                        usd_fifteen_old_signal.append(usd_fifteen_min_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    # 1 Hour Logic For 3 Currencies
                    if eur_one_hour_signal != eur_one_hour_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "EUR 1 HOUR SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + eur_one_hour_signal + " Previous Signal Was " +
                               eur_one_hour_old_signal[-1])
                        message1 = "EUR 1 Hour Signal Changed TO " + eur_one_hour_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + eur_one_hour_old_signal[-1], timeout=10)
                        time.sleep(11)
                        eur_one_hour_old_signal.append(eur_one_hour_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    if gbp_one_hour_signal != gbp_one_hour_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 1 HOUR SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + gbp_one_hour_signal + " Previous Signal Was " +
                               gbp_one_hour_old_signal[
                                                                 -1])
                        message1 = "GBP 1 Hour Signal Changed TO " + gbp_one_hour_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + gbp_one_hour_old_signal[-1], timeout=10)
                        time.sleep(11)
                        gbp_one_hour_old_signal.append(gbp_one_hour_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    if usd_one_hour_signal != usd_one_hour_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 1 HOUR SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + usd_one_hour_signal + " Previous Signal Was " +
                               usd_one_hour_old_signal[
                                                                 -1])
                        message1 = "USD 1 Hour Signal Changed TO " + usd_one_hour_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + usd_one_hour_old_signal[-1], timeout=10)
                        time.sleep(11)
                        usd_one_hour_old_signal.append(usd_one_hour_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    # 5 Hour Logic For 3 Currencies

                    if eur_five_hour_signal != eur_five_hour_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 1 HOUR SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + eur_five_hour_signal + " Previous Signal Was " +
                               eur_five_hour_old_signal[-1])
                        message1 = "EUR 5 Hour Signal Changed TO " + eur_five_hour_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + eur_five_hour_old_signal[-1], timeout=10)
                        time.sleep(11)
                        eur_five_hour_old_signal.append(eur_five_hour_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    if gbp_five_hour_signal != gbp_five_hour_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 1 HOUR SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + gbp_five_hour_signal + " Previous Signal Was " +
                               gbp_five_hour_old_signal[-1])
                        message1 = "GBP 5 Hour Signal Changed TO " + gbp_five_hour_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + gbp_five_hour_old_signal[-1], timeout=10)
                        time.sleep(11)
                        gbp_five_hour_old_signal.append(gbp_five_hour_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    if usd_five_hour_signal != usd_five_hour_old_signal[-1]:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 1 HOUR SIGNAL CHANGED",
                               "CURRENT SIGNAL IS " + usd_five_hour_signal + " Previous Signal Was " +
                               usd_five_hour_old_signal[-1])
                        message1 = "USD 5 Hour Signal Changed TO " + usd_five_hour_signal
                        notifications.notify(
                            title=message1,
                            message='Previous Signal Was' + usd_five_hour_old_signal[-1], timeout=10)
                        time.sleep(11)
                        usd_five_hour_old_signal.append(usd_five_hour_signal)
                        server.sendmail(sender_email, receiver_email, message)

                    # 1,5,15,1 hour and 5 hour signal same

                    if eur_one_min_signal in buy_tuple and eur_five_min_signal in buy_tuple and eur_fifteen_min_signal in buy_tuple and eur_one_hour_signal in buy_tuple and eur_five_hour_signal in buy_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "EUR 5 SIGNAL SAME (BUY/STRONG BUY)",
                               "1 min, 5 min, 15 min, 1 hour  and 5 hour all are in BUY or Strong Buy State")
                        message1 = "EUR 5 Signal Same BUY/STRONG BUY"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour and 5 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)
                    elif eur_one_min_signal in buy_tuple and eur_five_min_signal in buy_tuple and eur_fifteen_min_signal in buy_tuple and eur_one_hour_signal in buy_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "EUR 4 SIGNAL SAME (BUY/STRONG BUY)",
                               "1 min, 5 min, 15 min and 1 hour  all are in BUY or Strong Buy State")
                        message1 = "EUR 4 Signal Same BUY/STRONG BUY"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)

                    if gbp_one_min_signal in buy_tuple and gbp_five_min_signal in buy_tuple and gbp_fifteen_min_signal in buy_tuple and gbp_one_hour_signal in buy_tuple and gbp_five_hour_signal in buy_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 5 SIGNAL SAME (BUY/STRONG BUY)",
                               "1 min, 5 min, 15 min, 1 hour  and 5 hour all are in BUY or Strong Buy State")
                        message1 = "GBP 5 Signal Same BUY/STRONG BUY"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour and 5 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)
                    elif gbp_one_min_signal in buy_tuple and gbp_five_min_signal in buy_tuple and gbp_fifteen_min_signal in buy_tuple and gbp_one_hour_signal in buy_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 4 SIGNAL SAME (BUY/STRONG BUY)",
                               "1 min, 5 min, 15 min and 1 hour  all are in BUY or Strong Buy State")
                        message1 = "GBP 4 Signal Same BUY/STRONG BUY"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)

                    if usd_one_min_signal in buy_tuple and usd_five_min_signal in buy_tuple and usd_fifteen_min_signal in buy_tuple and usd_one_hour_signal in buy_tuple and usd_five_hour_signal in buy_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "USD 5 SIGNAL SAME (BUY/STRONG BUY)",
                               "1 min, 5 min, 15 min, 1 hour  and 5 hour all are in BUY or Strong Buy State")
                        message1 = "USD 5 Signal Same BUY/STRONG BUY"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour and 5 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)
                    elif usd_one_min_signal in buy_tuple and usd_five_min_signal in buy_tuple and usd_fifteen_min_signal in buy_tuple and usd_one_hour_signal in buy_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "USD 4 SIGNAL SAME (BUY/STRONG BUY)",
                               "1 min, 5 min, 15 min and 1 hour  all are in BUY or Strong Buy State")
                        message1 = "USD 4 Signal Same BUY/STRONG BUY"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)

                    if eur_one_min_signal in sell_tuple and eur_five_min_signal in sell_tuple and eur_fifteen_min_signal in sell_tuple and eur_one_hour_signal in sell_tuple and eur_five_hour_signal in sell_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "EUR 5 SIGNAL SAME (SELL/STRONG SELL)",
                               "1 min, 5 min, 15 min, 1 hour  and 5 hour all are in SELL or Strong SELL State")
                        message1 = "EUR 5 Signal Same SELL/STRONG SELL"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour and 5 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)
                    elif eur_one_min_signal in sell_tuple and eur_five_min_signal in sell_tuple and eur_fifteen_min_signal in sell_tuple and eur_one_hour_signal in sell_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "EUR 4 SIGNAL SAME (SELL/STRONG SELL)",
                               "1 min, 5 min, 15 min and 1 hour  all are in SELL or Strong SELL State")
                        message1 = "EUR 4 Signal Same SELL/STRONG SELL"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)

                    if gbp_one_min_signal in sell_tuple and gbp_five_min_signal in sell_tuple and gbp_fifteen_min_signal in sell_tuple and gbp_one_hour_signal in sell_tuple and gbp_five_hour_signal in sell_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 5 SIGNAL SAME (SELL/STRONG SELL)",
                               "1 min, 5 min, 15 min, 1 hour  and 5 hour all are in SELL or Strong SELL State")
                        message1 = "GBP 5 Signal Same SELL/STRONG SELL"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour and 5 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)
                    elif gbp_one_min_signal in sell_tuple and gbp_five_min_signal in sell_tuple and gbp_fifteen_min_signal in sell_tuple and gbp_one_hour_signal in sell_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 4 SIGNAL SAME (SELL/STRONG SELL)",
                               "1 min, 5 min, 15 min and 1 hour  all are in SELL or Strong SELL State")
                        message1 = "GBP 4 Signal Same SELL/STRONG SELL"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)

                    if usd_one_min_signal in sell_tuple and usd_five_min_signal in sell_tuple and usd_fifteen_min_signal in sell_tuple and usd_one_hour_signal in sell_tuple and usd_five_hour_signal in sell_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "USD 5 SIGNAL SAME (SELL/STRONG SELL)",
                               "1 min, 5 min, 15 min, 1 hour  and 5 hour all are in SELL or Strong SELL State")
                        message1 = "USD 5 Signal Same SELL/STRONG SELL"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour and 5 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)
                    elif usd_one_min_signal in sell_tuple and usd_five_min_signal in sell_tuple and usd_fifteen_min_signal in sell_tuple and usd_one_hour_signal in sell_tuple:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                        """ % (sender_email, ", ".join(receiver_email), "GBP 4 SIGNAL SAME (SELL/STRONG SELL)",
                               "1 min, 5 min, 15 min and 1 hour  all are in SELL or Strong SELL State")
                        message1 = "USD 4 Signal Same SELL/STRONG SELL"
                        notifications.notify(
                            title=message1,
                            message="1, 5 , 15, 1 hour are same", timeout=10)
                        time.sleep(11)
                        server.sendmail(sender_email, receiver_email, message)

            elif email_alerts == False and notification == True:
                if eur_fifteen_min_signal != eur_fifteen_old_signal[-1]:
                    message = "EUR 15 MIN SIGNAL CHANGED To : " + eur_fifteen_min_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + eur_fifteen_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    eur_fifteen_old_signal.append(eur_fifteen_min_signal)

                if gbp_fifteen_min_signal != gbp_fifteen_old_signal[-1]:
                    message = "GBP 15 MIN SIGNAL CHANGED To : " + gbp_fifteen_min_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + gbp_fifteen_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    gbp_fifteen_old_signal.append(gbp_fifteen_min_signal)

                if usd_fifteen_min_signal != usd_fifteen_old_signal[-1]:
                    message = "USD 15 MIN SIGNAL CHANGED To : " + usd_fifteen_min_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + usd_fifteen_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    usd_fifteen_old_signal.append(usd_fifteen_min_signal)

                # 1 Hour Logic For 3 Currencies
                if eur_one_hour_signal != eur_one_hour_old_signal[-1]:
                    message = "EUR 1 HOUR SIGNAL CHANGED To : " + eur_one_hour_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + eur_one_hour_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    eur_one_hour_old_signal.append(eur_one_hour_signal)

                if gbp_one_hour_signal != gbp_one_hour_old_signal[-1]:
                    message = "GBP 1 HOUR SIGNAL CHANGED To : " + gbp_one_hour_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + gbp_one_hour_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    gbp_one_hour_old_signal.append(gbp_one_hour_signal)

                if usd_one_hour_signal != usd_one_hour_old_signal[-1]:
                    message = "USD 1 HOUR SIGNAL CHANGED To : " + usd_one_hour_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + usd_one_hour_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    usd_one_hour_old_signal.append(usd_one_hour_signal)

                # 5 Hour Logic For 3 Currencies

                if eur_five_hour_signal != eur_five_hour_old_signal[-1]:
                    message = "EUR 5 HOUR SIGNAL CHANGED To : " + eur_five_hour_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + eur_five_hour_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    eur_five_hour_old_signal.append(eur_five_hour_signal)

                if gbp_five_hour_signal != gbp_five_hour_old_signal[-1]:
                    message = "GBP 5 HOUR SIGNAL CHANGED To : " + gbp_five_hour_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + gbp_five_hour_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    gbp_five_hour_old_signal.append(gbp_five_hour_signal)

                if usd_five_hour_signal != usd_five_hour_old_signal[-1]:
                    message = "USD 5 HOUR SIGNAL CHANGED To : " + usd_five_hour_signal
                    notifications.notify(
                        title=message,
                        message="Previous Signal Was : " + usd_five_hour_old_signal[-1], timeout=10
                    )
                    time.sleep(11)
                    usd_five_hour_old_signal.append(usd_five_hour_signal)

                # 1,5,15,1 hour and 5 hour signal same

                if eur_one_min_signal in buy_tuple and eur_five_min_signal in buy_tuple and eur_fifteen_min_signal in buy_tuple and eur_one_hour_signal in buy_tuple and eur_five_hour_signal in buy_tuple:
                    message = "EUR 5 Signal Same BUY/Strong BUY"
                    notifications.notify(
                        title=message,
                        message='1,5,15, 1 hour and 5 hour are same', timeout=10
                    )
                    time.sleep(11)

                elif eur_one_min_signal in buy_tuple and eur_five_min_signal in buy_tuple and eur_fifteen_min_signal in buy_tuple and eur_one_hour_signal in buy_tuple:
                    message = "EUR 4 Signal Same BUY/Strong BUY"
                    notifications.notify(
                        title=message,
                        message='1,5,15 and 1 hour are same', timeout=10
                    )
                    time.sleep(11)

                if gbp_one_min_signal in buy_tuple and gbp_five_min_signal in buy_tuple and gbp_fifteen_min_signal in buy_tuple and gbp_one_hour_signal in buy_tuple and gbp_five_hour_signal in buy_tuple:
                    message = "GBP 5 Signal Same BUY/Strong BUY"
                    notifications.notify(
                        title=message,
                        message='1,5,15, 1 hour and 5 hour are same', timeout=10
                    )
                    time.sleep(11)

                elif gbp_one_min_signal in buy_tuple and gbp_five_min_signal in buy_tuple and gbp_fifteen_min_signal in buy_tuple and gbp_one_hour_signal in buy_tuple:
                    message = "GBP 4 Signal Same BUY/Strong BUY"
                    notifications.notify(
                        title=message,
                        message='1,5,15 and 1 hour are same', timeout=10
                    )
                    time.sleep(11)

                if usd_one_min_signal in buy_tuple and usd_five_min_signal in buy_tuple and usd_fifteen_min_signal in buy_tuple and usd_one_hour_signal in buy_tuple and usd_five_hour_signal in buy_tuple:
                    message = "USD 5 Signal Same BUY/Strong BUY"
                    notifications.notify(
                        title=message,
                        message='1,5,15, 1 hour and 5 hour are same', timeout=10
                    )
                    time.sleep(11)

                elif usd_one_min_signal in buy_tuple and usd_five_min_signal in buy_tuple and usd_fifteen_min_signal in buy_tuple and usd_one_hour_signal in buy_tuple:
                    message = "USD 4 Signal Same BUY/Strong BUY"
                    notifications.notify(
                        title=message,
                        message='1,5,15 and 1 hour are same', timeout=10
                    )
                    time.sleep(11)

                if eur_one_min_signal in sell_tuple and eur_five_min_signal in sell_tuple and eur_fifteen_min_signal in sell_tuple and eur_one_hour_signal in sell_tuple and eur_five_hour_signal in sell_tuple:
                    message = "EUR 5 Signal Same SELL/Strong SELL"
                    notifications.notify(
                        title=message,
                        message='1,5,15, 1 hour and 5 hour are same', timeout=10
                    )
                    time.sleep(11)

                elif eur_one_min_signal in sell_tuple and eur_five_min_signal in sell_tuple and eur_fifteen_min_signal in sell_tuple and eur_one_hour_signal in sell_tuple:
                    message = "EUR 4 Signal Same SELL/Strong SELL"
                    notifications.notify(
                        title=message,
                        message='1,5,15 and 1 hour are same', timeout=10
                    )
                    time.sleep(11)
                if gbp_one_min_signal in sell_tuple and gbp_five_min_signal in sell_tuple and gbp_fifteen_min_signal in sell_tuple and gbp_one_hour_signal in sell_tuple and gbp_five_hour_signal in sell_tuple:
                    message = "GBP 5 Signal Same SELL/Strong SELL"
                    notifications.notify(
                        title=message,
                        message='1,5,15, 1 hour and 5 hour are same', timeout=10
                    )
                    time.sleep(11)

                elif gbp_one_min_signal in sell_tuple and gbp_five_min_signal in sell_tuple and gbp_fifteen_min_signal in sell_tuple and gbp_one_hour_signal in sell_tuple:
                    message = "GBP 4 Signal Same SELL/Strong SELL"
                    notifications.notify(
                        title=message,
                        message='1,5,15 and 1 hour are same', timeout=10
                    )
                    time.sleep(11)

                if usd_one_min_signal in sell_tuple and usd_five_min_signal in sell_tuple and usd_fifteen_min_signal in sell_tuple and usd_one_hour_signal in sell_tuple and usd_five_hour_signal in sell_tuple:
                    message = "USD 5 Signal Same SELL/Strong SELL"
                    notifications.notify(
                        title=message,
                        message='1,5,15, 1 hour and 5 hour are same', timeout=10
                    )
                    time.sleep(11)

                elif usd_one_min_signal in sell_tuple and usd_five_min_signal in sell_tuple and usd_fifteen_min_signal in sell_tuple and usd_one_hour_signal in sell_tuple:
                    message = "USD 4 Signal Same SELL/Strong SELL"
                    notifications.notify(
                        title=message,
                        message='1,5,15 and 1 hour are same', timeout=10
                    )
                    time.sleep(11)

        # myWindow.mainloop()

        time.sleep(2)

        myWindow.after(1000, my_mainloop)
    except:
        myWindow.after(1000, my_mainloop)


myWindow.after(1000, my_mainloop)
myWindow.mainloop()
