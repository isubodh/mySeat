from flask import render_template
form flask import request
from app import app
from .forms import addSeatForm
import HotDeskDAO as dao

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname' : 'Subodh'} ##fake user
	return render_template("index.html", user=user)

@app.route('/freeDesk')
def freeDesk():
	user = {'nickname' : 'Subodh'} ##fake user
	hotdesks = dao.findAllDesk()
	if hotdesks:
		return render_template("freeDesk.html", user=user, hotdesk=hotdesks)
	else
		return '''<HTML><TITLE>No HotDesk</TITLE><BODY>Sorry ! 
			No Hot Desk available as of now<BR><A href="/">HotDesk App</A>
			</BODY></HTML>'''

@app.route('/bookedDesk', methods=['GET', 'POST'])
def bookedDesk():
	user = {'nickname' : 'Subodh'} ##fake user]
	allocatedDesk = dao.allocatedDesk()
	if not allocatedDesk:
		return '''<HTML><TITLE>No HotDesk</TITLE><BODY>Sorry ! 
			No HotDesk allocated as of now<BR><A href="/">HotDesk App</A>
			</BODY></HTML>'''
	else
		return  render_template("DesksAllocated.html", user=user, allocatedDesk=allocatedDesk)
		
@app.route('/addHotDesk')
	user = {'nickname' : 'Subodh'} ##fake user]
	addDesk = addSearForm()
	return render_template("addHotDesk.html", user=user, form=addDesk)
	
@app.route('/confirmAddDesk', methods=['GET', 'POST'])
def confirmAddDesk():
	user = {'nickname' : 'Subodh'} ##fake user]
	Desk = dict()
	form = addSeatForm()
	if form.validate_on_submit():
		Desk['ondate'] = form.indate.data
		Desk['floor'] = form.floor.data
		Desk['deskno'] = form.indeskno.data
		Desk['remark'] = form.inremark.data
		dao.AddDesk( Desk['floor'], Desk['deskno'], Desk['ondate'], Desk['remark'])	
		return render_template("confrimAddDesk.html", user=user, Desk=Desk)
	else:
		return render_template("addHotDesk.html", user=user, form=addDesk)
		