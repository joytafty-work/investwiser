from flask import Flask, render_template
import MySQLdb
app = Flask(__name__)
import os
pwd = os.getenv('MYSQLROOTPWD')
db = MySQLdb.connect(user="root",host="localhost", port=3386, db="upsdata", passwd=pwd)

# prepare a cursor object using cursor() method
cursor = db.cursor()

@app.route('/')
def hello_world():
	return render_template('index.html')
    # return "Yay!! It's live"

@app.route('/db')
def activity_page(pagename=None):
	querystr = "SELECT DATE FROM activity;"
	res = db.query(querystr)
	print res
	return render_template('index.html')

	# query_results = db.store_result().fetch_row(maxrow=0)
	# print "query finished"
	# activities=""
	# for result in query_results:
	# 	print result[0]
	# 	activities += unicode(result[0], 'utf-8')
	# 	activities += "<br>"
	# return activities

@app.route('/blocker')
def block(pagename=None):
	return "Blocked!"

@app.route('/<pagename>')
def regularpage(pagename=None):
	return "You've arrived at "+pagename

if __name__ == '__main__':
    app.run()