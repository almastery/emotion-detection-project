"""
Unit Tests for Emotion Detection Module
Tests different emotions and edge cases
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion detection functionality"""
    
    def test_emotion_detection_joy(self):
        """Test that happy text is detected as joy"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    
    def test_emotion_detection_anger(self):
        """Test that angry text is detected as anger"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    
    def test_emotion_detection_fear(self):
        """Test that fearful text is detected as fear"""
        result = emotion_detector("I am afraid of the dark")
        self.assertEqual(result['dominant_emotion'], 'fear')
    
    def test_emotion_detection_sadness(self):
        """Test that sad text is detected as sadness"""
        result = emotion_detector("I am so sad")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    
    def test_emotion_detection_disgust(self):
        """Test that disgusting text is detected as disgust"""
        result = emotion_detector("This is disgusting")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    
    def test_emotion_detection_empty_string(self):
        """Test that empty string returns None for dominant emotion"""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertEqual(result['status_code'], 400)
    
    def test_emotion_detection_none_input(self):
        """Test that None input returns None for dominant emotion"""
        result = emotion_detector(None)
        self.assertIsNone(result['dominant_emotion'])
        self.assertEqual(result['status_code'], 400)


if __name__ == '__main__':
    unittest.main()
