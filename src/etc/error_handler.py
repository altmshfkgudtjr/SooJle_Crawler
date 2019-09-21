from db_health import url_health_check
from datetime import datetime
import time
from platform import platform

def error_handler(e, URL, page_url, db):
	# 앞으로 10번동안 이 사이트 크롤링 일시중지
	url_health_check(URL['url'], db)
	log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	log_info = URL['info']
	log_url = page_url
	print("[ERROR]=====================================================================")
	print(log_time, " :: ", log_info, "\nURL :: ", log_url)
	print(type(e), "\n", e, "\n\n\n\n")
	if platform().startswith("Windows"):
		f = open("/home/iml/log/crawler_log.log", 'a')
	else:
		f = open("crawler_log.log", 'a')
	f_data = "[ERROR]=====================================================================\n"
	f_data = f_data + log_time + " :: " + log_info + "\nURL :: " + log_url + "\n"
	f_data = f_data + str(type(e)) + "\n" + str(e) + "\n\n"
	f.write(f_data)
	f.close()
	time.sleep(2)