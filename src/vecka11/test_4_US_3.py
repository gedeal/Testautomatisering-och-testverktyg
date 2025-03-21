# ## [User story 3]
#  Som en användare, vill jag se "Daily standup", som utspelar sig i
#  första dagen i sprinten och kan starta 10 min tid så att jag vet när möte ska slutas.
# ## [User story 4]
#  Som en användare, efter jag se "sprint planning" ,som utspelar sig
#  första dagen i sprinten, jag kan starta över.
# ## [User story 5]
#  Som en användare, efter jag se "Daily standup" eller "sprint planning",
#  som utspelar sig första dagen i sprinten, jag kan starta över.



import re
from playwright.sync_api import Page, expect


def test_view_sprint_StandupTime(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Daily standup"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Daily standup")
    expect(sp_heading).to_be_visible()

    # Start time
    sp_starttime = page.get_by_role("button").get_by_text("Start the standup: 10 minutes")
    expect(sp_starttime).to_be_visible()
    sp_starttime.click(timeout=100)

    sp_timing = page.get_by_role("paragraph").get_by_text(" Time left: ")
    expect(sp_timing).to_be_visible()
    # TODO :  verify if the value goes down

    # go back - page#2
    sp_button = page.get_by_role("button").get_by_text(re.compile("Ok we're done"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    # go back - page#1
    sp_button = page.get_by_role("button").get_by_text(re.compile("Start over"))
    expect(sp_button).to_be_visible()
    sp_button.click(timeout=100)

    sp_heading = page.get_by_role("paragraph") .get_by_text("What day of the sprint is it?")
    expect(sp_heading).to_be_visible()
