import unittest
from EmotionDetection import emotion_detection as ed

class TestEmotion(unittest.TestCase): 
    def test1(self): 
        self.assertEqual( ed.emotion_detector('I am glad this happened')['dominant_emotion'] , 'joy' )
        self.assertEqual( ed.emotion_detector('I am really mad about this')['dominant_emotion'] , 'anger' )
        self.assertEqual( ed.emotion_detector('I feel disgusted just hearing about this')['dominant_emotion'] , 'disgust' )
        self.assertEqual( ed.emotion_detector('I am so sad about this')['dominant_emotion'] , 'sadness' )
        self.assertEqual( ed.emotion_detector('I am really afraid that this will happen')['dominant_emotion'] , 'fear' )

unittest.main()