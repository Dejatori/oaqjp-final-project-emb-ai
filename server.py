"""
Flask application for emotion detection.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle the emotion detection request.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        output = "Invalid text! Please try again!"
    else:
        output = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']}, "
            f"'sadness': {response['sadness']}."
            f"The dominant emotion is {response['dominant_emotion']}."
        )

    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
