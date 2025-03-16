# playwright codegen lejonmanen.github.io/agile-helper

# Som en användare, vill jag se "Daily standup",
# som utspelar sig första dagen i sprinten, så att jag vet vad jag ska göra på mötet.


import re
from playwright.sync_api import Page, Playwright, sync_playwright, expect


def test_view_SprintRetrospective(playwright: Playwright)-> None:
    browser = playwright.chromium.launch(headless=False);
    context = browser.new_context();
    page = context.new_page();
    page.goto("https://lejonmanen.github.io/agile-helper/");

# Page 1
    expect(page).to_have_title(re.compile("Agile helper"));
    expect(page.get_by_text('What day of the sprint is it?')).to_be_visible();
    # page.screenshot(path="./images/screenshot_1_12.png", full_page=True);
    page.get_by_role("button", name="Last").click();

# Page 2
    expect(page.get_by_role("button", name="Sprint retrospective")).to_be_visible;
    # page.screenshot(path="./images/screenshot_2_12.png", full_page=True);
    page.get_by_role("button", name="Sprint retrospective").click();

# Page 3
    expect(page.get_by_role("heading", name="Sprint retrospective")).to_be_visible;
    page.screenshot(path="./src/vecka11/image/screenshot_12_3.png", full_page=True);
    page.get_by_role("button", name="The sprint is complete").click();

    page.get_by_role("button", name="Start over").click();
    expect(page.get_by_text('What day of the sprint is it?')).to_be_visible();
    # page.screenshot(path="./images/screenshot_4_12.png", full_page=True);
    # ---------------------
    context.close()
    browser.close()
