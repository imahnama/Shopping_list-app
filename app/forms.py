 from flask_wtf import FlaskForm
 from wtforms import StringField,SubmitField
 from wtforms.validators import DataRequired,InputRequired,Regexp,length

 class NewList(FlaskForm):
     name = StringField("listname",validators=[InputRequired(), DataRequired(),Length(1,64),
                                                        Regexp("^[A-Za-z_-]+(\s+[A-Za-z_-]+)*$", 0,
                                                       'Input should contain [A-Za-z_-] spaces')])
     submit = SubmitField("Add Item")
