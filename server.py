"""
Flask Web Server for Emotion Detection Application
Provides REST API endpoints for emotion analysis
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/emotion_detector', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in provided text.

    Expected JSON input:
    {
        "text_to_analyze": "Your text here"
    }

    Returns:
    {
        "anger": float,
        "disgust": float,
        "fear": float,
        "joy": float,
        "sadness": float,
        "dominant_emotion": str
    }
    """

    # Get JSON data from request
    data = request.get_json()

    # Handle missing JSON body
    if data is None:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # Extract text_to_analyze
    text_to_analyze = data.get('text_to_analyze', '')

    # Check for blank input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return jsonify({
            'error': 'Please provide text to analyze',
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    # Call emotion detector
    result = emotion_detector(text_to_analyze)

    # Check for errors from emotion_detector
    if result.get('status_code') == 400:
        return jsonify({
            'error': 'Could not process text',
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }), 400

    # Return successful result
    return jsonify(result), 200


@app.route('/', methods=['GET'])
def index():
    """Home endpoint providing API information."""
    return jsonify({
        'message': 'Emotion Detection API',
        'version': '1.0.0',
        'endpoint': '/emotion_detector',
        'method': 'POST'
    }), 200


@app.errorhandler(400)
def bad_request(_):
    """Handle 400 Bad Request errors."""
    return jsonify({
        'error': 'Bad Request',
        'message': 'Invalid request'
    }), 400


@app.errorhandler(404)
def page_not_found(_):
    """Handle 404 Not Found errors."""
    return jsonify({
        'error': 'Not Found',
        'message': 'Endpoint does not exist'
    }), 404


@app.errorhandler(500)
def internal_error(_):
    """Handle 500 Internal Server errors."""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred'
    }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
