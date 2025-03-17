from playwright.sync_api import Page, expect

def test_name_field(page:Page):
    page.goto("http://")

    button= page.get_by_role("button").last
    expect(button).to_be_disabled(timeout=100)


    name
