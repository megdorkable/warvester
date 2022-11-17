# warvester
Web scraping utilities

### Download correct chrome driver from https://chromedriver.chromium.org/downloads, extract the driver from the ZIP file, and place in the project folder as 'chromedriver.exe'.

### Copy:
`.env-example` --> `.env`

### Non-default Google Chrome path
If running on with a non-default chrome path, modify the following line in `.env` to instead be equal to your Chrome path:
```commandline
CHROME_BINARY_PATH = 'default'
```