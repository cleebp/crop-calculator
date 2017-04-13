from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Brian'} # fake user
	crops = [# fake array of crops
		{
			'name': 'Apples',
			'price': '$1.99 (/lb)'
		},
		{
			'name': 'Corn',
			'price': '$.99 (/lb)'
		}
	]
	return "Hello, World!"
	#return render_template('index.html', title='CropCalculators', user=user, crops=crops)
