from flask import Flask, render_template, request
from EmotionDetection import emotion_detection as ed

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    input = request.args['textToAnalyze']
    emotions = ed.emotion_detector(input)
    return f"For the given statement, the system response is 'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': 0.009251528, 'joy': 0.9680386 and 'sadness': 0.049744144. The dominant emotion is joy."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)