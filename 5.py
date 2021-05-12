from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import ssl
import smtplib
import time

sender_email = ""
receiver_email = [""]
sender_password = ""
port = 465
context = ssl.create_default_context()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--ignore-certificate-errors")

chrome_path = r"C:\Users\shaki\PycharmProjects\_ScrappingModule\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)

hours = int(time.strftime("%H", time.localtime()))
mins = time.strftime("%M", time.localtime())
total_hour = hours * 60
current_time_here = total_hour + int(mins)

unban_time_one = current_time_here - 1
unban_time_two = current_time_here - 1

product_combo = "https://www.amazon.in/dp/B07RHJ7H7T/"
product_standard = "https://www.amazon.in/dp/B07RRMPZ4L/"

while True:
    try:
        hours = int(time.strftime("%H", time.localtime()))
        mins = time.strftime("%M", time.localtime())
        total_hour = hours * 60
        current_time_here = total_hour + int(mins)

        driver.get(str(product_combo))
        time.sleep(10)
        if len(driver.find_elements_by_id("submit.buy-now")) > 0:
            print("Combo Pack is Available")
            if current_time_here > unban_time_one:
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login(sender_email, sender_password)
                    for receiver in receiver_email:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                                                    """ % (sender_email, ", ".join(receiver), "Combo Pack Is Available",
                                                           "Combo Pack Is Now Available On " + str(product_combo))

                        server.sendmail(sender_email, receiver, message)
                        time.sleep(10)
                unban_time_one = current_time_here + 15

        else:
            print("Combo Pack is Not Available")

        time.sleep(15)

        driver.get(str(product_standard))
        time.sleep(10)
        if len(driver.find_elements_by_id("submit.buy-now")) > 0:
            print("Standard Pack is Available")
            if current_time_here > unban_time_two:
                with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                    server.login(sender_email, sender_password)
                    for receiver in receiver_email:
                        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
                                                    """ % (
                        sender_email, ", ".join(receiver), "Standard Pack Is Available",
                        "Standard Pack Is Now Available On " + str(product_standard))

                        server.sendmail(sender_email, receiver, message)
                        time.sleep(10)
                unban_time_two = current_time_here + 15

        else:
            print("Standard Pack is not Available")

        time.sleep(15)
    except Exception as e:
        print("Error Occured " + str(e))
        print("Going On a 200 Second Break"+str(time.localtime()))
        time.sleep(200)

