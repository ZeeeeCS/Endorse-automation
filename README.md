# Endorse-automation (LinkedIn Skill Endorsement) ? Selenium

Automates visiting LinkedIn **Skills** pages and clicking an **Endorse** button when its available.

> **Important**: Automating actions on LinkedIn may violate LinkedIn Terms of Service and can lead to account restrictions. Use responsibly and at your own risk.

## What this does

The script `rrrselenuim.py`:

- Opens the LinkedIn login page
- Signs in (currently hardcoded in the script)
- Visits each profile URL in the `profiles` list (skills pages)
- Tries to locate an **Endorse** button and click it
- Uses a small random delay to reduce ?bot-like? timing

## Requirements

- Python 3.8+
- Google Chrome installed

Python packages:

- `selenium`
- `webdriver-manager`

## Setup

Create a virtual environment (recommended) and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U selenium webdriver-manager
```

## Configure

### 1) Remove hardcoded credentials (do this before sharing)

`rrrselenuim.py` currently contains hardcoded login credentials. **Remove them immediately** and never commit credentials to GitHub.

Recommended approach: use environment variables.

In your shell:

```bash
export LINKEDIN_EMAIL="you@example.com"
export LINKEDIN_PASSWORD="your_password"
```

Then update the script to read them (example snippet):

```python
import os

email = os.environ.get("LINKEDIN_EMAIL")
password = os.environ.get("LINKEDIN_PASSWORD")
login_linkedin(email, password)
```

### 2) Update the profiles list

Edit the `profiles` list in `rrrselenuim.py` and add your target **skills** URLs, for example:

- `https://www.linkedin.com/in/<username>/details/skills/`

## Run

From this folder:

```bash
python3 rrrselenuim.py
```

Chrome will open, the script will attempt login, then it will visit each URL in `profiles` and click **Endorse** when it can.

## Troubleshooting

- **?Could not find or click the endorse button?**
  - LinkedIn UI and DOM frequently change; the XPath may need updating.
  - Confirm the URL is the **Skills** page (`/details/skills/`).
- **CAPTCHA / extra verification**
  - LinkedIn may show CAPTCHA or additional checks; automation often fails in these cases.
- **Timeouts / element not clickable**
  - Increase `WebDriverWait` timeouts, add more scrolling, or refine the locator.

## Notes

- This script uses `webdriver-manager` to download/manage the ChromeDriver automatically.
- For reliability, consider using explicit waits everywhere instead of `time.sleep()`.
