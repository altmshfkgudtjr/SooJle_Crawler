"""     2019.02.10		"""
"""   SooJel Project	"""
""" BY *IML *NB *837477 """

import sj_path	#환경변수 지정
from url_list import List
from crawling_select import Crawling	#크롤링 전체
import db_manager
from db_url import init_url_collection
from datetime import datetime
from info_id import post_info
from posts_cnt import posts_cnt
from tag_info import tag_info



db_manager.init_db()	#DB가 없으면 생성
URLS = List[:]	#url_list에서 List를 URL으로 가져옴

if __name__ == '__main__':
	print("\n\n")
	print(":::< SooJle Project >:::")
	print("TODAY : ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "\n\n")

	#post_info 테이블, sj_domain 테이블 생성, lastly_post 테이블 생성
	post_info()
	#tag_info 테이블 생성
	tag_info()
	#url 테이블 생성
	init_url_collection()

	print("\n\nCrawling Start!\n\n")



	for URL in URLS:	#List에서 하나의 요소 = URL
		print('URL parsing Start! : ' + str(URL["url"]))
		Crawling(URL)
		#print("Number of DB_posts : ", db_manager.get_table_posts(URL))		# 현재 DB에 있는 테이블의 게시글 수를 출력한다
		print('-----------------------------------------------------------------------------------------------------------------\n')

	print(":::: Posts in Boards Count ::::")
	posts_cnt()															# 모든 게시물 빈도 출력

	print("\n\nCrawling End!\n\n")