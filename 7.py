group_delay = 5
post_delay = 900
limit_posts = 10
post_groups = ["https://www.facebook.com/groups/232848693818309/",
               "https://www.facebook.com/groups/1804746966454771/",
               "https://www.facebook.com/groups/CoderJobs/",
               "https://www.facebook.com/groups/AusschreibungenITJobsProjekte/",
               "https://www.facebook.com/groups/566876643474621/"]

job_groups = ["https://www.facebook.com/groups/1601046156812191/",
              "https://www.facebook.com/groups/556739801135588/",
              "https://www.facebook.com/groups/programmierboerse/",
              "https://www.facebook.com/groups/webentwickler.jobs/",
              "https://www.facebook.com/groups/startupberlinjobs/",
              "https://www.facebook.com/groups/2298093126996608/"
              ]

#live_groups = ["https://www.facebook.com/groups/designer.entwickler.boerse/",
 #              ]

facebook_id = ""
facebook_password = ""

curr_count = []
curr_count.append(2)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.keys import Keys

group_counter = 0
prev_ids = []
with open('tester.txt', 'r') as the_file:
    prev_ids = list(the_file)

with open('group_records.txt', 'r') as the_file:
    prev_id_and_group = list(the_file)

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-notifications")

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pythonproject-535d6c8b2e42.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Facebook job ads-shareable").worksheet("Sheet2")

#chrome_path = r"C:\Users\cscha\Desktop\Neuer Ordner\Facebook Group Poster\chromedriver.exe"
chrome_path = r"C:\Users\shaki\PycharmProjects\_ScrappingModule\chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_path)

driver.get("https://www.facebook.com/")

time.sleep(5)

try:
    email = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input")
    email.click()

    email.send_keys(facebook_id)

    time.sleep(5)

    passowrd = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]")
    passowrd.click()

    passowrd.send_keys(facebook_password)

    time.sleep(5)

    btn = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")

    btn.click()
except:
    email = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input")
    email.click()
    email.send_keys(facebook_id)
    time.sleep(5)

    passowrd = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input")
    passowrd.click()
    passowrd.send_keys(facebook_password)
    time.sleep(5)

    btn = driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
    btn.click()

post_inc = 1

while post_inc <= limit_posts:
    try:
        curr_id = sheet.cell(curr_count[-1], 1).value
        if str(curr_id) + "\n" not in prev_ids:
            curr_title = sheet.cell(curr_count[-1], 2).value
            curr_brand = sheet.cell(curr_count[-1], 9).value
            curr_link = sheet.cell(curr_count[-1], 7).value

            if curr_title == "" and curr_brand == "" and curr_link == "":
                driver.quit()
                break

            #for group in live_groups:
                group_counter = group_counter + 1
                print("Doing Group Number " + str(group_counter) + " Now.")
                if str(curr_id) + str(group) + "\n" not in prev_id_and_group:

                    driver.get(str(group))
                    time.sleep(10)
                    # Click on Post
                    lat_post = driver.find_element_by_xpath(
                        "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/li[2]/a")
                    lat_post.click()
                    time.sleep(3)

                    lat_post = driver.find_element_by_xpath(
                        "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/li[1]/a")
                    lat_post.click()
                    time.sleep(3)
                    # Getting The Main Div
                    chan_div = driver.find_element_by_class_name("_5rpb")

                    # INSIDE TEXT AREA
                    text_area = chan_div.find_element_by_xpath("div/div/div")

                    # Format
                    text_area.send_keys(str(curr_link))
                    time.sleep(1)
                    text_area.send_keys(" ")
                    time.sleep(4)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys("More amazing developer jobs from top employers in Europe.")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("Just like this one:")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys(str(curr_title) + " at " + str(curr_brand))
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("--------------------------------------------")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("❤️ Like WeAreDevelopers to get more offers like this!")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("❤️ WeAreDevelopers.com - developers-only job board with pre-vetted jobs")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)

                    pst_btn = driver.find_element_by_class_name("_332r")

                    pst_btn.click()
                    print("Post: " + str(post_inc) + " POSTED ON, GROUP: " + str(group_counter))

                    with open('group_records.txt', 'a') as the_file:
                        the_file.write(str(curr_id) + str(group))
                        the_file.write("\n")

                    time.sleep(group_delay)
                else:
                    print("THE POSTS HAS ALREADY BEEN POSTED BEFORE ON GROUP " + str(group_counter))

            for group in post_groups:
                group_counter = group_counter + 1
                print("Doing Group Number " + str(group_counter) + " Now.")
                if str(curr_id) + str(group) + "\n" not in prev_id_and_group:

                    driver.get(str(group))
                    time.sleep(10)
                    # Click on Post
                    lat_post = driver.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div")
                    lat_post.click()
                    time.sleep(3)

                    lat_post = driver.find_element_by_xpath(
                        "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div")
                    lat_post.click()
                    time.sleep(3)
                    # Getting The Main Div
                    chan_div = driver.find_element_by_class_name("_5rpb")

                    # INSIDE TEXT AREA
                    text_area = chan_div.find_element_by_xpath("div/div/div")

                    # Format
                    text_area.send_keys(str(curr_link))
                    time.sleep(1)
                    text_area.send_keys(" ")
                    time.sleep(4)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys("More amazing developer jobs from top employers in Europe.")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("Just like this one:")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys(str(curr_title) + " at " + str(curr_brand))
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("--------------------------------------------")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("❤️ Like WeAreDevelopers to get more offers like this!")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("❤️ WeAreDevelopers.com - developers-only job board with pre-vetted jobs")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)

                    pst_btn = driver.find_element_by_class_name("_332r")

                    pst_btn.click()
                    print("Post: " + str(post_inc) + " POSTED ON, GROUP: " + str(group_counter))

                    with open('group_records.txt', 'a') as the_file:
                        the_file.write(str(curr_id) + str(group))
                        the_file.write("\n")

                    time.sleep(group_delay)
                else:
                    print("THE POSTS HAS ALREADY BEEN POSTED BEFORE ON GROUP " + str(group_counter))

            for group in job_groups:
                group_counter = group_counter + 1
                print("Doing Group Number " + str(group_counter) + " Now.")
                if str(curr_id) + str(group) + "\n" not in prev_id_and_group:

                    driver.get(str(group))
                    time.sleep(10)
                    # Click on Job
                    lat_post = driver.find_element_by_xpath(
                        "/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/li[3]/a")
                    lat_post.click()
                    time.sleep(3)
                    # Getting The Main Div
                    chan_div = driver.find_element_by_class_name("_5rpb")

                    # INSIDE TEXT AREA
                    text_area = chan_div.find_element_by_xpath("div/div/div")

                    # Format
                    text_area.send_keys(str(curr_link))
                    time.sleep(1)
                    text_area.send_keys(" ")
                    time.sleep(4)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys(Keys.CONTROL, 'z')
                    time.sleep(2)
                    text_area.send_keys("More amazing developer jobs from top employers in Europe.")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("Just like this one:")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys(str(curr_title) + " at " + str(curr_brand))
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("--------------------------------------------")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("❤️ Like WeAreDevelopers to get more offers like this!")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)
                    text_area.send_keys("❤️ WeAreDevelopers.com - developers-only job board with pre-vetted jobs")
                    time.sleep(1)
                    text_area.send_keys(Keys.SHIFT, Keys.ENTER)
                    time.sleep(1)

                    pst_btn = driver.find_element_by_class_name("_332r")
                    pst_btn.click()
                    print("Post: " + str(post_inc) + " POSTED ON, GROUP: " + str(group_counter))

                    with open('group_records.txt', 'a') as the_file:
                        the_file.write(str(curr_id) + str(group))
                        the_file.write("\n")

                    time.sleep(group_delay)
                else:
                    print("THE POSTS HAS ALREADY BEEN POSTED BEFORE ON GROUP " + str(group_counter))
            post_inc = post_inc + 1
            curr_count.append(curr_count[-1] + 1)
            group_counter = 0
            with open('tester.txt', 'a') as the_file:
                the_file.write(str(curr_id))
                the_file.write("\n")
            time.sleep(post_delay)
            print("Going on the post delay " + str(time.localtime()))
        else:
            curr_count.append(curr_count[-1] + 1)
            print("Post Already Done: " + str(curr_id))
            time.sleep(2)




    except Exception as e:
        print("Something happened, going on a 100 second break " + str(e) + " TIME: " + str(time.localtime()))
        time.sleep(100)
        curr_count.append(curr_count[-1] + 1)
        print("After the error, doing row no  " + str(curr_count[-1]) + " on google sheet Now.")
    # Store ID
