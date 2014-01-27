import os, json
from flask import Flask, render_template, request, jsonify
import MySQLdb
from fetch_data import *

app = Flask(__name__)

def initialize_data():
    # get jobQuery and start
    q = request.form['jobQuery']
    searchkey = "+".join(q.split())
    company_name, company_img, founder_names, founder_imgs = fetch_data(searchkey=searchkey)
    return searchkey, company_name, company_img, founder_names, founder_imgs

@app.route("/")
def hello():
    return render_template('index.html') 

@app.route('/fetchcompany')
def fetchcompany():
    query = request.args.get('q', '')
    return render_template('fetchcompany.html', query=query)

@app.route('/fetchcompany?q=<query>')
def fetchcompanyTo(query):
    query = query.replace('+',' ')
    return render_template('fetchcompany.html', query=query)

@app.route('/fetchfounder')
def fetchfounder():
    query = request.args.get('q', '')
    return render_template('fetchfounder.html', query=query)

@app.route('/fetchfounder?q=<query>')
def fetchfounderTo():
    query = query.replace('+',' ')
    return render_template('fetchfounder.html', query=query)

@app.route('/analyze', methods=['POST'] )
def runAnalyze():

    searchkey, company_name, company_img, founder_names, founder_imgs = initialize_data()

    dictResult = {}
    dictResult['query'] = searchkey

    dictResult['items'] = []    
    for idx in range(len(founder_names)):
        dictResult['items'].append({
            'company_name': company_name, 
            'company_img': company_img,
            'founder_name': founder_names[idx],
            'founder_img': founder_imgs[idx]})
    return jsonify(dictResult) 

@app.route("/founder", methods=['POST'])
def runGetFounder():
    pass

@app.route('/<pagename>') 
def regularpage(pagename=None): 
    """ 
    Route not found by the other routes above. May point to a static template. 
    """ 
    return "You've arrived at " + pagename
    if pagename==None: 
       raise Exception, 'page_not_found' 
    return render_template(pagename) 

# if __name__ == '__main__':
#     print "Starting debugging server."
#     app.run(debug=True, host='localhost', port=8000)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)