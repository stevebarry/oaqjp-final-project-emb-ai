import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):

    if text_to_analyze == '':
        return  {
'anger': None,
'disgust': None,
'fear': None,
'joy': None,
'sadness': None,
'dominant_emotion': None
}

    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post( URL, headers=headers, data = json.dumps(input_json) )
    emotions={}

    r_dict = json.loads(response.text)

    return_val = r_dict["emotionPredictions"][0]["emotion"]
    return_val['dominant_emotion'] = max(return_val, key=return_val.get)

    return return_val

if __name__ == "__main__":
    print( emotion_detector('I love this technology.') )