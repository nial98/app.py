from flask import Flask
from flask import request
from flask import render_template
import pickledb

app = Flask(__name__)

db = pickledb.load('/var/www/html/application/status.db', False)

@app.route('/', methods=['GET', 'POST'])
@app.route('/<status>', methods=['GET','POST'])
def serve(status=db.get('state')):
    return render_template('page.html', status=status)
#def serve():
#    return 'Status: %s' % db.get('state')

@app.route('/occupied', methods=['GET', 'POST'])
def occupied():
    db.set('state','occupied')
    db.dump()
    return 'updated: occupied'

@app.route('/unoccupied', methods=['GET', 'POST'])
def unoccupied():
    db.set('state', 'unoccupied')
    db.dump()
    return 'updated: unoccupied'

if __name__ == "__main__":
    app.run()
~                                                                                                                       
~                                                                                                                       
~                                                                                                                       
~                                                                                                                       
~                                                                                                                       
~                                                                                                                       
