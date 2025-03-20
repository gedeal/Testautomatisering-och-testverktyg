# playwright codegen https://lejonmanen.github.io/timer-vue/

import re
from asyncio import timeout
from time import sleep

from playwright.sync_api import Page, Playwright, sync_playwright, expect



def test_SkapaTabortWidget(playwright: Playwright) -> None:
    """ ========= User story 6 =======================================================

     [U6] Som en användare, vill jag ändra temafärg, så att jag

     Acceptanskriterier:
     [A6.1] Det går att klicka på knappen "somewhere in the middle"


     Scenario:
     [S6.1] . Klicka på knappen "somewhere in the middle"

     """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://lejonmanen.github.io/timer-vue/")
    page.get_by_role("button", name="Add timer").click()

    sleep(2)



