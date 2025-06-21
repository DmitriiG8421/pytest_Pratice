import time
import random

# def test_google_homepage(page):
#     page.goto("https://www.google.com")
#     assert "Google" in page.title()

def random_sleep(min_time=0, max_time=1):
    time.sleep(random.uniform(min_time, max_time))

def findAndFill(chosenId,chosenFill,page): 
    search_box = page.locator(chosenId)
    search_box.click()
    random_sleep()
    search_box.fill(chosenFill)
    random_sleep()
    search_box.press("Enter")
    random_sleep()

def test_sign_up(page):
    sign_up_url = "https://faruk-hasan.com/automation/signup.html"
    page.goto(sign_up_url)
    findAndFill("#username","Mario_Dario",page)
    findAndFill("#email","test@gmail.com",page)
    findAndFill("#password","IlikeMathPassword",page)
    findAndFill("#confirmPassword","IlikeMathPassword",page)
    random_sleep(0.5,1)
    print(page.title())
    assert "Login" in page.title()


def test_log_in(page):
    # log_in_url = "https://faruk-hasan.com/automation/login.html"
    # page.goto(log_in_url)
    random_sleep(0.5,1)
    # findAndFill("#username","Mario_Dario",page)
    findAndFill("#password","IlikeMathPassword",page)
    random_sleep(10,10)
    assert "playwright-selenium-cypress-practice" in page.URL