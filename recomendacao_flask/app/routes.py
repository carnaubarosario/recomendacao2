from flask import render_template, request
from app import app
from app.recommend import recommend_tracks

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/recomendacao_2', methods=['POST'])
def recommendations():
    user_input_name = request.form['name']
    user_input_artist = request.form['artist']
    recommended_tracks = recommend_tracks(user_input_name, user_input_artist)
    return render_template('template.html', recommended_tracks=recommended_tracks)
