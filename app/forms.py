from flask_wtf import Form
import wtforms
from wtforms.validators import DataRequired

class addSeatForm(Form):
	indate = wtforms.DateField('Desk Free on Date :', validators=[DataRequired()])
	infloor = wtforms.IntegerField('Desk is on floor :',validators=[DataRequired()])
	indeskno = wtforms.IntegerField('Desk Number :',validators=[DataRequired()])
	inremark = wtforms.StringField('Any Comments :')
	
class bookSeatForm(Form):
	submit = wtforms.SubmitField()