import time

import allure
import logging

import requests
from select import select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AllPractice:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(self.driver, 40)  # Initialize WebDriverWait with a 10-second timeout

    def test_radiobutton(self):
        self.logger.info("Radio button practice")
        with allure.step("Radio button practice"):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='radio1']"))).click()
            self.logger.info("Radio button clicked")
    def test_auto_suggest_dropdown(self):
        with allure.step("Enter country"):
            self.logger.info("Enter country")
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='autocomplete']"))).send_keys("can")
            countries =self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,".ui-menu-item")))
            for  coun in countries:
                if coun.text == "Canada":
                    coun.click()
                    break
    def test_dropdown(self):
        with allure.step("Select option from dropdown"):
            self.logger.info("Select option from dropdown")
            dropdown = Select(self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#dropdown-class-example"))))
            dropdown.select_by_index(1)

    def test_checkbox(self):
        with allure.step("Select the checkbox"):
            self.logger.info("Select the checkbox")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#checkBoxOption2"))).click()

    def test_broke_links(self):
        with allure.step("verify the broken links"):
            self.logger.info("verify the broken links")
            links = self.driver.find_elements(By.CSS_SELECTOR, 'a')
            broken_links = 0
            working_links = 0
            for link in links:
                url = link.get_attribute('href')  # get the href attribute
                try:
                    r = requests.head(url, allow_redirects=True)  # send a HEAD request
                    if r.status_code == 200:
                        print(f'{url} is working')
                        working_links += 1
                    else:
                        print(f'{url} is broken with status code {r.status_code}')

                        broken_links += 1
                except requests.RequestException as e:
                    print(f'{url} is broken with error: {e}')
                    broken_links += 1
            print(f"Total links found: {len(links)}")
            print(f"Working links: {working_links}")
            print(f"Broken links: {broken_links}")

    def test_mouse_hover(self):
        with allure.step("Mouse over"):
            self.logger.info("Mouse over")
            actions = ActionChains(self.driver)
            hover = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mousehover")))
            actions.move_to_element(hover).perform()
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href='#top']"))).click()
            time.sleep(5)
            actions.move_to_element(hover).perform()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Reload']"))).click()

    def test_visible(self):
        with allure.step("Verify visibility of element"):
            self.logger.info("Verifying visibility of element")

            text_box_locator = (By.CSS_SELECTOR, "#displayed-text")
            self.logger.info("Showing the text box and verifying it is visible.")
            self.driver.find_element(By.CSS_SELECTOR, "#show-textbox").click()
            visible_text_box = self.wait.until(EC.visibility_of_element_located(text_box_locator))
            assert visible_text_box.is_displayed(), "The text box should be visible after clicking show."
            self.logger.info("Hiding the text box and verifying it is not visible.")
            self.driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
            is_now_invisible = self.wait.until(EC.invisibility_of_element_located(text_box_locator))
            assert is_now_invisible, "The text box should be invisible after clicking hide."

    def test_alert(self):
        with allure.step("verifying alerts"):
            self.logger.info("Verifying alerts")
            self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys("divya")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#alertbtn"))).click()
            alerts = self.driver.switch_to.alert
            alerts.accept()
            self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys("divya")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmbtn"))).click()
            alerts.accept()
            self.driver.find_element(By.CSS_SELECTOR, "#name").send_keys("divya")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmbtn"))).click()
            alerts.dismiss()

    def test_open_tab(self):
        with allure.step("opening new tab"):
            self.logger.info("opening new tab")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#opentab"))).click()
            title = self.driver.title
            print(title)
            tabs = self.driver.window_handles
            current_tab = tabs[0]
            new_tab = tabs[1]
            self.driver.switch_to.window(new_tab)
            msg = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='support float-left'] span"))).text
            print(msg)
            self.driver.switch_to.window(current_tab)

    def test_open_window(self):
        with allure.step("opening new window"):
            self.logger.info("opening new window")
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#openwindow"))).click()
            title1 = self.driver.title
            print(title1)
            windows = self.driver.window_handles
            current_window = windows[0]
            new_window = windows[1]
            self.driver.switch_to.window(new_window)
            msg = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='support float-left'] span"))).text
            print(msg)
            self.driver.switch_to.window(current_window)
    def test_frames(self):
        with allure.step("frames"):
            self.logger.info("frames")
            iframe_element = self.driver.find_element(By.ID, "courses-iframe")
            self.driver.switch_to.frame(iframe_element)
            self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Courses"))
            ).click()

            self.driver.switch_to.default_content()

    def test_tabs(self):
        with allure.step("all tabs"):
            self.logger.info("all tabs right click")
            #self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[text()='REST API']"))).click()
            list = self.driver.find_elements(By.XPATH,"(//td/ul)[1]/li")
            print(len(list))
            for lst in list:
                lst.click()
                self.driver.back()








