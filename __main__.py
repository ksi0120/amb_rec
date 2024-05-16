#import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
def main(params):

    with open('lots.txt', 'r') as file:
        data = file.read().split('\n')
    prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|> \n From the following list of parking lots, identify the best parking lot based on the user's input. Pick 3 options and briefly explain why. Just give the recommendation."
    prompt=prompt+str(data)
    credentials = {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey":  "OYSbGJ9TlRadkDTdvE4eJF4Y3u6TqCCWKoa16cMQ4buw"
    }
    project_id="1038e636-3049-44a2-8414-931da3ba58d7"
    model_id = 'meta-llama/llama-3-70b-instruct'
    parameters = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 300,
        GenParams.MIN_NEW_TOKENS: 1
    }
    from ibm_watsonx_ai.foundation_models import ModelInference

    model = ModelInference(
        model_id=model_id, 
        params=parameters, 
        credentials=credentials,
        project_id=project_id)
    
    demand=params.get("input")
    prompt=prompt + "\n" +demand+"\n Output:<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    return {
    "headers": {
        "Content-Type": "application/json",
    },
    "statusCode": 200,
    "body": model.generate_text(prompt)
    }
