from flask import render_template,request
import requests
from datetime import datetime
from app import app


@app.route('/', methods = ['GET', 'POST'])
def mainpage():
    dt = datetime.now()
    dt = dt.strftime('%d/%m/%Y %I:%M %p')
    city = ""
    state = ""
    tempf = ""
    skycondition =""
    reportfrom = ""
    currweathericon = ""
    if request.method == 'POST':
        city = request.form['city']
        state = request.form['state']
    if city != "":
        r = requests.get("http://api.wunderground.com/api/b912244185f64b1c/geolookup/conditions/q/"+ state +"/"+ city+".json")
        data = r.json()
        currweathericon = str(data['current_observation']['icon_url'])
        tempf = str(data['current_observation']['temp_f']) + "F"
        skycondition = data['current_observation']['weather']
        reportfrom = data['current_observation']['observation_location']['full']

    return render_template('mainpage.html',city = city,
    state = state,
    dt=dt,
    currweathericon=currweathericon,
    tempf = tempf,
    skycondition = skycondition,
    reportfrom = reportfrom)
