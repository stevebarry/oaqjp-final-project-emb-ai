''' flask web application '''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detection as ed

app = Flask(__name__)

@app.route('/')
def index():
    ''' return index template '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector():
    ''' API for analysing emotion for a given string '''
    _input = request.args['textToAnalyze']
    emotions = ed.emotion_detector(_input)

    if emotions['dominant_emotion'] is None:
        return ' Invalid text! Please try again!'

    return f"For the given statement, the system response is 'anger': {emotions['anger']}, \
    'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']} \
    and 'sadness': {emotions['sadness']}. The dominant emotion is {emotions['dominant_emotion']}."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
