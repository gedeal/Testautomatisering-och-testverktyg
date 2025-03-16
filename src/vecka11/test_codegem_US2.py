# playwright codegen lejonmanen.github.io/agile-helper

# Som en användare, vill jag se "Daily standup",
# som utspelar sig första dagen i sprinten, så att jag vet vad jag ska göra på mötet.

import re
from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_view_sprint_DailyStandup(playwright: Playwright) -> None:
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

    # page.screenshot(path="./images/screenshot_1.png", full_page=True)
    page.get_by_role("button", name="First").click()

# Page 2
    expect(page.get_by_role("button", name="Daily standup")).to_be_visible;
    page.get_by_role("button", name="Daily standup").click()
    # page.screenshot(path="./images/screenshot_2.png", full_page=True)


# Page 3
    expect(page.get_by_role("heading", name="Daily standup")).to_be_visible;
    expect(page.get_by_text(" Are there any obstacles? ")).to_be_visible;
    page.get_by_role("button", name="Start the standup: 10 minutes").click()
    page.screenshot(path="./src/vecka11/image/screenshot_2_3.png", full_page=True);

    page.get_by_role("button", name="Ok we're done").click()
    expect(page.get_by_role("button").get_by_text(re.compile("Start over"))).to_be_visible()
    page.get_by_role("button", name="Start over").click()
    expect(page.get_by_text('What day of the sprint is it?')).to_be_visible();
    page.screenshot(path="./images/screenshot_4.png", full_page=True)
    # ---------------------
    context.close()
    browser.close()



# with sync_playwright() as playwright:
#     test_view_sprint_SpritnPlanning(playwright)
