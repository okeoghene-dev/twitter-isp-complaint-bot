# Twitter ISP Complaint Bot 🤖

## What it does
Automatically monitors your internet speed and tweets a complaint 
to your ISP when speeds drop below acceptable levels — fully automated, 
no manual input required.

## How it works
- Checks current internet speed using a speed test API
- Compares result against a defined threshold
- If speed is too low, logs into Twitter via Selenium WebDriver
- Automatically composes and tweets a complaint to the ISP
- Runs on a schedule without any manual intervention

## Tech Stack
- Python
- Selenium WebDriver (browser automation)
- Tweepy / Twitter API
- Speed Test API

## Note
Twitter/X has since restricted automated bots, so the tweeting 
functionality may require API access. The speed monitoring and 
automation logic remains fully functional.
