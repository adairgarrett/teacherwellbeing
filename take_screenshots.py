import asyncio
import os
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 900})
        page = await context.new_page()

        html_path = os.path.abspath('index.html')
        file_url = f'file:///{html_path.replace(os.sep, "/")}'
        print(f"Loading {file_url}")
        await page.goto(file_url, wait_until='networkidle')
        await page.wait_for_timeout(1000)

        # 1. Screenshot View 1: Request Help
        await page.screenshot(path='screenshot_request_help.png', full_page=True)
        print("Captured screenshot_request_help.png")

        # 2. Navigate to Offer Help
        await page.click('#nav-offer-help')
        await page.wait_for_timeout(500)
        await page.screenshot(path='screenshot_offer_help.png', full_page=True)
        print("Captured screenshot_offer_help.png")

        # 3. Navigate to Wellbeing
        await page.click('#nav-wellbeing')
        await page.wait_for_timeout(500)
        await page.screenshot(path='screenshot_wellbeing.png', full_page=True)
        print("Captured screenshot_wellbeing.png")

        # 4. Navigate to SMART Goals
        await page.click('#nav-smart-goals')
        await page.wait_for_timeout(500)
        await page.screenshot(path='screenshot_smart_goals.png', full_page=True)
        print("Captured screenshot_smart_goals.png")

        # 5. Navigate to About
        await page.click('#nav-about')
        await page.wait_for_timeout(500)
        await page.screenshot(path='screenshot_about.png', full_page=True)
        print("Captured screenshot_about.png")

        # 6. Mobile view of Request Help
        await context.close()
        mobile_ctx = await browser.new_context(viewport={'width': 390, 'height': 844})
        mobile_page = await mobile_ctx.new_page()
        await mobile_page.goto(file_url, wait_until='networkidle')
        await mobile_page.wait_for_timeout(500)
        await mobile_page.screenshot(path='screenshot_mobile.png', full_page=True)
        print("Captured screenshot_mobile.png")

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
