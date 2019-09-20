from selenium import webdriver
from platform import platform

def chromedriver():
	#만약 driver이 켜져있으면 끄고, 없으면 그냥 진행
	try:
		driver.quit()
	except:
		pass

	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome")
	options.add_argument("lang=ko_KR")

	if platform().startswith("Windows"):
		driver = webdriver.Chrome('../chromedriver.exe', chrome_options=options)
	else:
		driver = webdriver.Chrome('home/iml/SOOJLE_Crawler/chromedriver', chrome_options=options)

	return driver