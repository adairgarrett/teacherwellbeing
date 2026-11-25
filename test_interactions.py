import asyncio
import os
from playwright.async_api import async_playwright

async def run_tests():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        html_path = os.path.abspath('index.html')
        file_url = f'file:///{html_path.replace(os.sep, "/")}'
        await page.goto(file_url, wait_until='networkidle')

        # Test 1: Select options on Request Help
        print("Testing Request Help options...")
        await page.click('#opt-watch-class')
        duration_visible = await page.is_visible('#sub-duration-box')
        print(f"Duration box visible: {duration_visible}")

        await page.click('#opt-need-nurse')
        selected_text = await page.inner_text('#selectedOptionsCounter')
        print(f"Selected count: {selected_text}")

        # Submit new request
        await page.fill('#reqNotes', 'Testing automated teacher coverage request')
        await page.click('button:has-text("Broadcast Request to Staff")')
        await page.wait_for_timeout(500)

        # Verify new request appeared in feed
        feed_text = await page.inner_text('#requestsFeedList')
        assert 'Testing automated teacher coverage request' in feed_text
        print("PASS: New help request broadcasted and appeared in feed!")

        # Test 2: Claiming a request
        claim_btn = await page.query_selector('button:has-text("I Can Step In!")')
        if claim_btn:
            await claim_btn.click()
            await page.wait_for_timeout(500)
            feed_text_after = await page.inner_text('#requestsFeedList')
            assert 'Claimed' in feed_text_after
            print("PASS: Claim request successfully updated status!")

        # Test 3: Test School Switcher
        print("Testing School Switcher...")
        await page.click('#schoolDropdownBtn')
        await page.wait_for_timeout(200)
        await page.click('button:has-text("Oak Ridge Middle School")')
        await page.wait_for_timeout(300)
        school_name = await page.inner_text('#currentSchoolName')
        print(f"Current school after switch: {school_name}")
        assert 'Oak Ridge Middle School' in school_name
        print("PASS: School context switch verified!")

        # Test 4: SMART Goals Template Loading
        print("Testing SMART Goals...")
        await page.click('#nav-smart-goals')
        await page.wait_for_timeout(300)
        await page.click('button:has-text("Load Preset Template")')
        await page.wait_for_timeout(200)
        await page.click('button:has-text("Departure Boundary")')
        await page.wait_for_timeout(300)
        val = await page.input_value('#smartSpecific')
        print(f"Loaded SMART Specific: {val}")
        assert '4:15 PM' in val
        print("PASS: SMART Goals template loaded!")

        # Test 5: Box Breathing Guide Toggle
        print("Testing Breathing Guide...")
        await page.click('#nav-wellbeing')
        await page.wait_for_timeout(300)
        await page.click('#toggleBreathBtn')
        await page.wait_for_timeout(1500)
        label = await page.inner_text('#breathPlayLabel')
        print(f"Breath button label while running: {label}")
        assert 'Pause' in label
        print("PASS: Interactive Breathing Guide is running!")

        await browser.close()
        print("\nALL 5 INTERACTIVE FUNCTIONAL TESTS PASSED SUCCESSFULLY!")

if __name__ == '__main__':
    asyncio.run(run_tests())
