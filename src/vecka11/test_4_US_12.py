# ## [User story 12]
#  Som en användare, vill jag se "Sprint retrospective", som utspelar sig
#  sista dagen i sprinten, så att jag vet vad jag ska göra på retrospective  mötet.

import re
from playwright.sync_api import Page, expect


def test_view_sprint_SprintReRetrospective(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

    # Klicka på button " Somewhere in the middle "
    locator = page.get_by_role("button")
    last_button = locator.get_by_text("Last")
    last_button.click(timeout=100)

    # Hitta button med texten "Sprint retrospective"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint retrospective"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint retrospective"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(sp_heading).to_be_visible()


    # go back - page#2
    sp_button = page.get_by_role("button").get_by_text(re.compile(" The sprint is complete "))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    # go back - page#1
    sp_button = page.get_by_role("button").get_by_text(re.compile("Start over"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    sp_heading = page.get_by_role("paragraph") .get_by_text("What day of the sprint is it?")
    expect(sp_heading).to_be_visible()

