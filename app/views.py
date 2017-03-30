from flask import render_template
from flask import request
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
		return render_template("freeDesk.html", user=user, hotdesks=hotdesks)
	else:
		return '''<HTML><TITLE>No HotDesk</TITLE><BODY>Sorry ! 
			No Hot Desk available as of now<BR><A href="/">HotDesk App</A>
			</BODY></HTML>'''

@app.route('/confirmBooking', methods=['GET', 'POST'])
def confirmBooking():
	user = {'nickname' : 'Subodh'} ##fake user]#
	if request.form['submit']:
		allocatedDesk = dao.bookDesk(request.form['submit'])
	
	if not allocatedDesk:
		return '''<HTML><TITLE>No HotDesk</TITLE><BODY>Sorry ! 
			No HotDesk allocated as of now<BR><A href="/">HotDesk App</A>
			</BODY></HTML>'''
	else:
		return  render_template("bookedDesk.html", user=user, allocatedDesk=allocatedDesk)

## Route to Show all booked desk until now.
@app.route('/bookedDesks')
def bookedDesks():
	user = {'nickname' : 'Subodh'} ##fake user]#
	allocatedDesk = dao.allocatedDesk()
	if not allocatedDesk:
		return '''<HTML><TITLE>No HotDesk</TITLE><BODY>Sorry ! 
			No HotDesk allocated as of now<BR><A href="/">HotDesk App</A>
			</BODY></HTML>'''
	else:
		return  render_template("DesksAllocated.html", user=user, allocatedDesk=allocatedDesk)	
	
	
@app.route('/addHotDesk')
def addHotDesk():
	user = {'nickname' : 'Subodh'} ##fake user
	addDesk = addSeatForm()
	return render_template("addHotDesk.html", user=user, form=addDesk)
	
@app.route('/confirmAddDesk', methods=['GET', 'POST'])
def confirmAddDesk():
	user = {'nickname' : 'Subodh'} ##fake user
	Desk = dict()
	form = addSeatForm(request.form)

	if request.method == "POST":
		try:
			Desk['ondate'] = str(request.form['indate'])					#form.indate.data
			Desk['floor'] =  str(request.form['infloor'])					#form.infloor.data
			Desk['deskno'] = str(request.form['indeskno'])					#form.indeskno.data
			Desk['remark'] = str(request.form['inremark'])					#form.inremark.data
			dao.AddDesk( Desk['floor'], Desk['deskno'], Desk['ondate'], Desk['remark'])
		except Exception as e:
			return ("<p>Error : %s</p>" %e)
		return render_template("confirmAddDesk.html", user=user, Desk=Desk)
	else:
		return render_template("addHotDesk.html", user=user, form=form)
