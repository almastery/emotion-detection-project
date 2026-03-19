"""
Emotion Detection Module using IBM Watson NLP (Mock Version)
This module analyzes text and returns emotion detection results
Mock version for testing without real Watson API credentials
"""

import json


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using simulated Watson NLP
    Mock version that returns realistic emotion scores
    
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
    
    # Mock emotion detection - analyze text keywords
    text_lower = text_to_analyze.lower()
    
    # Define emotion keywords
    joy_keywords = ['happy', 'glad', 'excellent', 'love', 'wonderful', 'amazing', 'fantastic', 'great', 'best', 'joy']
    anger_keywords = ['angry', 'mad', 'furious', 'hate', 'awful', 'terrible', 'horrible', 'angry', 'rage']
    sadness_keywords = ['sad', 'unhappy', 'depressed', 'miserable', 'grief', 'sorrow', 'sorrowful', 'down']
    fear_keywords = ['afraid', 'fear', 'scared', 'terrified', 'anxious', 'nervous', 'worried', 'frightened']
    disgust_keywords = ['disgusting', 'disgust', 'gross', 'yuck', 'nasty', 'vile', 'revolting']
    
    # Calculate base scores
    anger_score = 0.02
    disgust_score = 0.01
    fear_score = 0.05
    joy_score = 0.05
    sadness_score = 0.02
    
    # Adjust scores based on keywords found
    if any(keyword in text_lower for keyword in joy_keywords):
        joy_score = 0.85
        anger_score = 0.02
        sadness_score = 0.01
        disgust_score = 0.01
        fear_score = 0.11
    elif any(keyword in text_lower for keyword in anger_keywords):
        anger_score = 0.85
        joy_score = 0.02
        sadness_score = 0.05
        disgust_score = 0.03
        fear_score = 0.05
    elif any(keyword in text_lower for keyword in sadness_keywords):
        sadness_score = 0.82
        joy_score = 0.05
        anger_score = 0.03
        disgust_score = 0.02
        fear_score = 0.08
    elif any(keyword in text_lower for keyword in fear_keywords):
        fear_score = 0.80
        anxiety_score = 0.15
        joy_score = 0.03
        anger_score = 0.01
        sadness_score = 0.01
        disgust_score = 0.00
    elif any(keyword in text_lower for keyword in disgust_keywords):
        disgust_score = 0.85
        anger_score = 0.05
        sadness_score = 0.02
        fear_score = 0.05
        joy_score = 0.03
    
    # Normalize scores to sum close to 1
    total = anger_score + disgust_score + fear_score + joy_score + sadness_score
    if total > 0:
        anger_score = round(anger_score / total, 2)
        disgust_score = round(disgust_score / total, 2)
        fear_score = round(fear_score / total, 2)
        joy_score = round(joy_score / total, 2)
        sadness_score = round(sadness_score / total, 2)
    
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


if __name__ == "__main__":
    # Test the emotion detector
    test_texts = [
        "I am glad this happened",
        "I am really mad about this",
        "I am afraid of the dark",
        "I am so sad",
        "This is disgusting"
    ]
    
    for text in test_texts:
        result = emotion_detector(text)
        print(f"Text: {text}")
        print(json.dumps(result, indent=2))
        print()
