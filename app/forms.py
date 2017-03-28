from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired

class addSeatForm(FlaskForm):
	indate = wtforms.DateField('Desk Free on Date :', validators=[DataRequired()])
	infloor = wtforms.IntegerField('Desk is on floor :',validators=[DataRequired()])
	indeskno = wtforms.IntegerField('Desk Number :',validators=[DataRequired()])
	inremark = wtforms.StringField('Any Comments :')
	submit = wtforms.SubmitField()