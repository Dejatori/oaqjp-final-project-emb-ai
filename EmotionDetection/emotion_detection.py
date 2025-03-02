import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion in the provided text using Watson NLP Library's Emotion Predict function.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        dict: A dictionary containing the emotion analysis results or error information
    """
    # URL for Watson NLP Emotion Predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Prepare the input data
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the POST request to the service
    try:
        response = requests.post(url, headers=headers, json=input_data)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            response_data = json.loads(response.text)

            # Extact emotion score
            emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})

            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

            # Find the dominant emotion (emotion with highest score)
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)

            # Return the emotion scores and dominant emotion
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
            
        else:
            # Return error in the required formato with zero scores
            return {
                'anger': 0,
                'disgust': 0,
                'fear': 0,
                'joy': 0,
                'sadness': 0,
                'dominant_emotion': None
            }
    except requests.exceptions.RequestException:
        # Return error information in the required formato with zero scores
        return {
            'anger': 0,
            'disgust': 0,
            'fear': 0,
            'joy': 0,
            'sadness': 0,
            'dominant_emotion': None
        }