#  ## [User story 1]
#  Som en användare, vill jag se mötet "sprint planning", som utspelar sig
#  första dagen i sprinten, så att jag vet vad jag ska göra på mötet.

import re
from playwright.sync_api import Page, expect



def test_view_sprint_SpritnPlanning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()

    # Klicka den
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

    # go back - page#2
    sp_button = page.get_by_role("button").get_by_text(re.compile("Ok we're done. Start the sprint!"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    # go back - page#1
    sp_button = page.get_by_role("button").get_by_text(re.compile("Start over"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    sp_heading = page.get_by_role("paragraph") .get_by_text("What day of the sprint is it?")
    expect(sp_heading).to_be_visible()
