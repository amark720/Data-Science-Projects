# Install selenium using command " pip install selenium "

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Update the URL of Naukri Page! ( Make Sure that the page link which you're putting must be a job listing page and it must have Next page buttons. )
driver.get("https://www.naukri.com/jobs-in-chennai-1")

count = 100  # Update the Number of Vacancy count you want to scrape.

index, new_index, i = '0', 1, 0  # index variable of the elements from which data will be Scraped
# Xpaths of the various element from which data will be scraped.
heading_xpath = '(//*[@class="srp-jobtuple-wrapper"])['+index+']/div/div/a'
link_xpath = '(//*[@class="srp-jobtuple-wrapper"])['+index+']/div/div/a'
subheading_xpath = '(//*[@class="srp-jobtuple-wrapper"])['+index+']/div/div[2]//a'
experience_xpath = '(//*[@class="srp-jobtuple-wrapper"])['+index+']/div/div[3]/div/span[1]/span/span'
salary_xpath = '(//*[@class="srp-jobtuple-wrapper"])['+index+']/div/div[3]/div/span[2]/span/span'

csv_file = open('Naukri_scrape.csv', 'a', encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)
# Writing the Heading of CSV file.
csv_writer.writerow(['Heading', 'Sub Heading', 'Vacancy Link', 'Experience Needed', 'Salary'])

while i < count:

    for j in range(20):
        # Here we're replacing the Old index count of Xpath with New Index count.
        temp_index = str(new_index).zfill(2)  # Zfill(2) is used to put zeros to the left of any digit till 2 decimal places.
        heading_xpath = heading_xpath.replace(index, temp_index)
        link_xpath = link_xpath.replace(index, temp_index)
        subheading_xpath = subheading_xpath.replace(index, temp_index)
        experience_xpath = experience_xpath.replace(index, temp_index)
        salary_xpath = salary_xpath.replace(index, temp_index)
        index = str(new_index).zfill(2)
        try:
            # Capturing the Heading from webpage and storing that into Heading variable.
            heading = wait.until(EC.presence_of_element_located((By.XPATH, heading_xpath))).text
            print(heading)
        except:
            heading = "NULL"
        try:
            link = wait.until(EC.presence_of_element_located((By.XPATH, link_xpath))).get_attribute('href')
            print(link)
        except:
            link = "NULL"
        try:
            subheading = wait.until(EC.presence_of_element_located((By.XPATH, subheading_xpath))).text
            print(subheading)
        except:
            subheading = "NULL"
        try:
            experience = wait.until(EC.presence_of_element_located((By.XPATH, experience_xpath))).text
            print(experience)
        except:
            experience = "NULL"
        try:
            salary = wait.until(EC.presence_of_element_located((By.XPATH, salary_xpath))).text
            print(salary)
        except:
            salary = "Not Disclosed"
        new_index += 1
        i += 1
        print("--------------------------- "+str(i)+" ----------------------------------")
        # Writing all the Scrapped data into CSV file.
        csv_writer.writerow([heading, subheading, link, experience, salary])
        if i >= count:
            break
    if i >= count:
        break
    element = driver.find_element(By.XPATH, '//*[text() = "Next"]').location_once_scrolled_into_view
    driver.execute_script("window.scrollBy(0,-120)")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Next"]'))).click()
    new_index = 1
csv_file.close()
