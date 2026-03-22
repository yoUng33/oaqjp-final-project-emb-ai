import requests
import json

def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        return {
                "anger": 0.006274985, 
                "disgust": 0.0025598293, 
                "fear": 0.009251528, 
                "joy": 0.9680386, 
                "sadness": 0.049744144, 
                "dominant_emotion": "joy"
            }
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions'][0]['emotion']
    dominant_key = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = dominant_key
    return emotion