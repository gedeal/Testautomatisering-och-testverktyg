# playwright codegen lejonmanen.github.io/agile-helper


#  ## [User story 1]
#  Som en användare, vill jag se mötet "sprint planning", som utspelar sig
#  första dagen i sprinten, så att jag vet vad jag ska göra på mötet.

import re
from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_view_sprint_SpritnPlanning(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://lejonmanen.github.io/agile-helper/")

# Page 1
    page.get_by_role("heading", name="Agile helper");
    expect(page).to_have_title(re.compile("Agile helper"));
    page.get_by_text("What day of the sprint is it?");
    expect(page.get_by_text('What day of the sprint is it?')).to_be_visible();
    expect(page.get_by_role("button", name="First")).to_be_visible;
    # page.screenshot(path="../../images/screenshot.png", full_page=True)
    page.screenshot(path="./images/screenshot_1.png", full_page=True)

    page.get_by_role("button", name="First").click()
 # Page 2
    expect(page.get_by_role("button", name="Sprint planning")).to_be_visible;
    page.get_by_role("button", name="Sprint planning").click()
    page.screenshot(path="./images/screenshot_2.png", full_page=True)

 # Page 3 
    expect(page.get_by_role("heading", name="Sprint planning")).to_be_visible;   
    expect(page.get_by_text("6. When your time is up, you")).to_be_visible;
    page.get_by_role("button", name="Ok we're done. Start").click()
    page.screenshot(path="./images/screenshot_3.png", full_page=True)

    expect(page.get_by_role("button").get_by_text(re.compile("Start over"))).to_be_visible()
    page.get_by_role("button", name="Start over").click()
    page.get_by_text("What day of the sprint is it?")
    expect(page.get_by_text('What day of the sprint is it?')).to_be_visible();
    page.screenshot(path="./images/screenshot_4.png", full_page=True)
    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_view_sprint_SpritnPlanning(playwright)
