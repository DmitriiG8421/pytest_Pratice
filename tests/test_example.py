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

def test_sign_up_log_in(page):
    sign_up_url = "https://faruk-hasan.com/automation/signup.html"
    page.goto(sign_up_url)

    #sing up
    findAndFill("#username","Mario_Dario",page)
    findAndFill("#email","test@gmail.com",page)
    findAndFill("#password","IlikeMathPassword",page)
    findAndFill("#confirmPassword","IlikeMathPassword",page)

    #log in
    random_sleep(0.5,1)
    findAndFill("#password","IlikeMathPassword",page)

    header = page.locator("h1")
    assert header.text_content() == "Automation Adventure"


