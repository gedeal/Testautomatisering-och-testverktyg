# playwright codegen https://lejonmanen.github.io/timer-vue/

import re
from asyncio import timeout
from time import sleep

from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_SkapaTabortWidget(playwright: Playwright) -> None:
    """ ========= User story 1 ======================================================
     [U1] Som en användare, vill jag skapa och ta bort widgets - timer och anteckning, så att jag

     Acceptanskriterier:
     [A1.1] Det går att klicka på knappen "somewhere in the middle"


     Scenario:
     [S1.1] . Klicka på knappen "somewhere in the middle"

    """
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.on('console', lambda msg: print(msg.text()))

    page.goto("https://lejonmanen.github.io/timer-vue/")
    expect(page).to_have_title(re.compile("Timer app"))

    expect(page.get_by_role("button").get_by_text(re.compile("Add timer"))).to_be_visible()
    expect(page.get_by_role("button").get_by_text(re.compile("Add note"))).to_be_visible()
    expect(page.get_by_role("button").get_by_text(re.compile("Light"))).to_be_visible()
    expect(page.get_by_role("button").get_by_text(re.compile("Dark"))).to_be_visible()
    expect(page.get_by_role("button").get_by_text(re.compile("Forest"))).to_be_visible()
    expect(page.get_by_role("button").get_by_text(re.compile("Orange"))).to_be_visible()

    expect(page.get_by_role("heading").get_by_text(re.compile("Break"))).not_to_be_visible()
    page.get_by_role("button", name="Add timer").click()
    expect(page.get_by_role("heading").get_by_text(re.compile("Break"))).to_be_visible()

    page.get_by_role("heading", name="Break").click()
    page.get_by_role("textbox", name="Title").fill("Gerson's break")
    sleep(2)

    page.get_by_role("button", name="Add note").click()
    expect(page.get_by_role("heading", name="Click to change text")).to_be_visible()
    page.get_by_role("heading", name="Click to change text").click()
    page.get_by_role("textbox", name="Description").fill("Gerson was here")
    page.get_by_role("textbox", name="Description").press("Enter")
    expect(page.get_by_role("heading", name="Gerson was here")).to_be_visible()
    sleep(2)

    page.get_by_role("button", name="Start").click()

    textboxlocator = page.locator('.row time')
    print("\nPRINT: ", textboxlocator.input_value())

    sleep(2)

    page.get_by_text("🗑️").nth(1).click()
    sleep(1)
    page.get_by_text("🗑️").nth(0).click()
    sleep(2)


""" ========= User story 2 =======================================================

 [U2] Som en användare, vill jag byta plats på två widgets, så att jag 

 Acceptanskriterier:
 [A2.1] Det går att klicka på knappen "somewhere in the middle"


 Scenario:
 [S2.1] . Klicka på knappen "somewhere in the middle"

 """

""" ========= User story 3 =======================================================

 [U3] Som en användare, vill jag ändra tidsinställning på timer, så att jag 

 Acceptanskriterier:
 [A3.1] Det går att klicka på knappen "somewhere in the middle"


 Scenario:
 [S3.1] . Klicka på knappen "somewhere in the middle"

 """

""" ========= User story 4 =======================================================:

 [U4] Som en användare, vill jag starta, pausa, återställ, så att jag 

 Acceptanskriterier:
 [A4.1] Det går att klicka på knappen "somewhere in the middle"


 Scenario:
 [S4.1] . Klicka på knappen "somewhere in the middle"

 """

""" ========= User story 5 =======================================================

 [U5] Som en användare, vill jag ändra texten för anteckning, så att jag 

 Acceptanskriterier:
 [A5.1] Det går att klicka på knappen "somewhere in the middle"


 Scenario:
 [S5.1] . Klicka på knappen "somewhere in the middle"

 """

""" ========= User story 6 =======================================================

 [U6] Som en användare, vill jag ändra temafärg, så att jag 

 Acceptanskriterier:
 [A6.1] Det går att klicka på knappen "somewhere in the middle"


 Scenario:
 [S6.1] . Klicka på knappen "somewhere in the middle"

 """
