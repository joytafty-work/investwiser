def fetch_data(searchkey):
	import os
	import sys
	import urlparse
	import MySQLdb as mdb

	curstr1 = 'SELECT * FROM founder_seed2A_info WHERE company_name like "%s"' % searchkey
	# curstr2 = {"SELECT * FROM seriesApred WHERE company_name like '%(searchkey)'" % vars()}

	# con = mdb.connect('localhost', 'joyinsight', 'san00k', 'insightdata')
	con = mdb.connect('us-cdbr-east-05.cleardb.net', 'b79f007212e595', 'bb086a2b', 'heroku_5b440647f9181bc')
	d1 = con.cursor()
	d1.execute(curstr1)
	founders = d1.fetchall()
	d1.close()
	# d2 = con.curstr1()
	# d2.execute(curstr2)
	# seriesApred = d2.fetchall()

	if len(founders) == 0:
		print 'loading data from AngelList'
		print searchkey

	con.close()

	company_name = []
	company_img = []
	founder_names = []
	founder_imgs = []	
	for f in founders:
		print f
		company_name, company_img, company_ALid, founder_name, founder_followers, founder_img, nfounder, founder_company_ALids, founder_score, ninvestor, investor_company_ALids, investor_score, nboard, board_company_ALids, board_score = f
    	founder_names.append(founder_name)
    	founder_imgs.append(founder_img)		 

	return company_name, company_img, founder_names, founder_imgs

if __name__ == '__main__':
	import sys
	searchkey = sys.argv[1]
	company_name, company_img, founder_names, founder_imgs = get_dataset(searchkey=searchkey) 