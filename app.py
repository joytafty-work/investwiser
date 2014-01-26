from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)


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

@app.route('/<pagename>') 
def regularpage(pagename=None): 
    """ 
    Route not found by the other routes above. May point to a static template. 
    """ 
    return "You've arrived at " + pagename
    if pagename==None: 
       raise Exception, 'page_not_found' 
    return render_template(pagename) 

if __name__ == '__main__':
    print "Starting debugging server."
    app.run(debug=True, host='localhost', port=8000)