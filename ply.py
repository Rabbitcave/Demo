import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def search_wikipedia_and_snapshot():
    # Define where to save screenshot (Desktop)
    desktop_path = Path("C:/Users/harip/OneDrive/Desktop") / "ui_developer_search.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.wikipedia.org/")

        # Fill the search input and submit
        page.fill("input[name='search']", "UI developer")
        page.press("input[name='search']", "Enter")

        # Wait for the search results title (or any element in results)
        page.wait_for_selector("h1#firstHeading")

        # Take full page screenshot
        page.screenshot(path=str("C:/Users/harip/OneDrive/Desktop/ui_developer_search.png"), full_page=True)
        print(f"📸 Screenshot saved to: {"C:/Users/harip/OneDrive/Desktop/ui_developer_search.png"}")

        browser.close()

if __name__ == "__main__":
    search_wikipedia_and_snapshot()
