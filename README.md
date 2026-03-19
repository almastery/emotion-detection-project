# Final Project - Emotion Detector

## Overview
This is a web application that detects emotions in text using IBM Watson Natural Language Understanding (NLU) API. The application analyzes text and returns emotion scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Features
- **Emotion Detection**: Analyzes text to detect 5 emotions (anger, disgust, fear, joy, sadness)
- **REST API**: Flask-based web server providing emotion detection endpoints
- **Error Handling**: Comprehensive error handling for invalid inputs
- **Unit Tests**: Complete test suite validating emotion detection
- **Static Code Analysis**: Code quality checks using pylint
- **IBM Watson Integration**: Uses IBM Watson NLP for accurate emotion analysis

## Project Structure
```
emotion-detection-project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation

### Prerequisites
- Python 3.8 or higher
- IBM Cloud account with Watson NLU service

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/almastery/emotion-detection-project.git
cd emotion-detection-project
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure IBM Watson credentials**
   - Get your API key and service URL from IBM Cloud
   - Update `emotion_detection.py` with your credentials:
     - Replace `YOUR_API_KEY_HERE` with your Watson API key
     - Replace `YOUR_SERVICE_URL_HERE` with your Watson service URL

## Usage

### Using the EmotionDetection Package
```python
from EmotionDetection.emotion_detection import emotion_detector

result = emotion_detector("I am so happy!")
print(result)
# Output: {'anger': 0.02, 'disgust': 0.01, 'fear': 0.05, 'joy': 0.85, 'sadness': 0.07, 'dominant_emotion': 'joy'}
```

### Running the Web Server
```bash
python server.py
```
Server will start at `http://localhost:5000`

### Making API Requests
```bash
curl -X POST http://localhost:5000/emotion_detector \
  -H "Content-Type: application/json" \
  -d '{"text_to_analyze": "I am happy today"}'
```

## Running Tests

### Unit Tests
```bash
python -m unittest test_emotion_detection.py -v
```

### Static Code Analysis
```bash
pylint server.py
pylint emotion_detection.py
```

## Emotion Detection Output
The emotion detector returns a JSON object with the following structure:
```json
{
  "anger": 0.02,
  "disgust": 0.01,
  "fear": 0.05,
  "joy": 0.85,
  "sadness": 0.07,
  "dominant_emotion": "joy"
}
```

## Error Handling
- **Empty Input**: Returns 400 status with None values
- **Invalid JSON**: Returns 400 status with error message
- **API Errors**: Returns 400 status with appropriate error handling
- **Not Found**: Returns 404 for undefined endpoints

## Requirements
See `requirements.txt` for all dependencies:
- Flask
- ibm-watson
- ibm-cloud-sdk-core
- pylint (for code analysis)

## License
MIT License

## Author
almastery

## Support
For issues or questions, please open an issue on GitHub.
