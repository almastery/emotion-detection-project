"""
Emotion Detection Module using IBM Watson NLP
This module analyzes text and returns emotion detection results
"""

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using IBM Watson NLP
    
    Args:
        text_to_analyze (str): The text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores and dominant emotion
              Returns status code 400 if text is empty or None
    """
    
    # Check for empty or None input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400
        }
    
    # Initialize the Watson NLU client
    authenticator = IAMAuthenticator(apikey='YOUR_API_KEY_HERE')
    nlu_client = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator,
        service_url='YOUR_SERVICE_URL_HERE'
    )
    
    try:
        # Call Watson NLP API with emotion analysis
        response = nlu_client.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        )
        
        # Extract emotion scores from response
        emotion_data = response.get_result()['emotion']['document']['emotion']
        
        # Extract individual emotion scores
        anger_score = emotion_data.get('anger', 0)
        disgust_score = emotion_data.get('disgust', 0)
        fear_score = emotion_data.get('fear', 0)
        joy_score = emotion_data.get('joy', 0)
        sadness_score = emotion_data.get('sadness', 0)
        
        # Create emotion scores dictionary
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        # Find dominant emotion (highest score)
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Return formatted result
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
    except Exception as e:
        # Handle API errors
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
            'status_code': 400,
            'error': str(e)
        }


if __name__ == "__main__":
    # Test the emotion detector
    test_text = "I am glad this happened"
    result = emotion_detector(test_text)
    print(json.dumps(result, indent=2))
