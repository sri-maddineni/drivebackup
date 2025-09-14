from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Path to the ChromeDriver executable
chrome_driver_path = "C:/Users/sriha/Downloads/chromedriver"

# Create a Service object for ChromeDriver
chrome_service = Service(chrome_driver_path)

# Start the service
chrome_service.start()

try:
    reg = "y20ait"
    start_no = 455
    end_no = 463

    browser = webdriver.Chrome(service=chrome_service)
    

    for i in range(start_no, end_no + 1):
        time.sleep(0.2)
        browser.get("http://becbapatla.ac.in:8080/STUDENTINFO/index_r20.html")

        hbox = browser.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[5]/div/div/form/center/font/input[1]")
        hbox.send_keys(reg + str(i))

        submit = browser.find_element(by=By.XPATH, value="/html/body/div/div[1]/div[5]/div/div/form/center/font/input[2]")
        submit.click()

        f = open("result42.txt", "a+")

        try:
            name=browser.find_element(by=By.XPATH, value="/html/body/div/div/div[5]/div/div/div/table[1]/tbody/tr[2]/td").text
            
            cgpa = browser.find_element(by=By.XPATH, value="/html/body/div/div/div[5]/div/div/div/center/strong/font").text
            f.write(reg + str(i) + "\t" + cgpa[::-1][0:7][::-1][0:4]+"\t"+name+"\n")
        except Exception as e:
            f.write(reg + str(i) + "\tError\n")

        f.close()

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Make sure to stop the service when done
    chrome_service.stop()
    browser.quit()
