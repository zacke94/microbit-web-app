from flask import render_template, redirect, url_for, request
from werkzeug.urls import url_parse
from app import app
from app.modules import *
import json

@app.route('/show-current-readings', methods=['POST'])
def show_curr_read_route():
    json_data = json.loads(show_current_read())
    a_warnings = {}
    b_warnings = {}

    for key, value in json_data.items():
        if key == "a_temp":
            if int(value) > 35:
                a_warnings[key] = value
        elif key == "a_light":
            if int(value) == 0:
                a_warnings[key] = value
        elif key == "b_temp":
            if int(value) > 35:
                b_warnings[key] = value
        elif key == "b_light":
            if int(value) == 0:
                b_warnings[key] = value

    if a_warnings or b_warnings:
        if a_warnings and b_warnings:
            return render_template('show-current-read.html', data=json_data, a_warnings=a_warnings, b_warnings=b_warnings)
        elif a_warnings:
            return render_template('show-current-read.html', data=json_data, a_warnings=a_warnings)
        elif b_warnings:
            return render_template('show-current-read.html', data=json_data, b_warnings=b_warnings)
    return render_template('show-current-read.html', data=json_data)
    
@app.route('/show-highest-lowest', methods=['POST'])
def show_highest_lowest():
    json_data = json.loads(highest_lowest())
    return render_template('show-highest-lowest.html', data=json_data)

@app.route('/del-low-high-log', methods=['POST'])
def del_low_high_log():
    delete_saved_log()
    json_data = json.loads(highest_lowest())
    return render_template('show-highest-lowest.html', data=json_data)

@app.route('/select-locations', methods=['GET', 'POST'])
def select_locations():
    json_data = json.loads(show_locations())
    return render_template('select-locations.html', data=json_data)

@app.route('/save-locations', methods=['POST'])
def save_locations():
    if request.method == 'POST':
        mb_A_coord = request.form.get('mb_A')
        mb_B_coord = request.form.get('mb_B')
    save_mb_coords(mb_A_coord, mb_B_coord)

    return redirect(url_for('select_locations'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Welcome')

