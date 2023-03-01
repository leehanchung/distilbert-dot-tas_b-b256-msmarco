import os
import torch
import base64
from io import BytesIO
from transformers import AutoTokenizer, AutoModel


# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global tokenizer, bert_model
    
    MODEL_NAME = os.getenv("MODEL_NAME")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    bert_model = AutoModel.from_pretrained(MODEL_NAME).to("cuda")


# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    """DistilBERT TAS-B is used for encoding passages into latent embeddings
    at inference time.

    Args:
        model_inputs (dict): JSON input with a "passage" field.

    Returns:
        dict: JSON output with an "embeddings" field.
    """
    global tokenizer, bert_model

    # Parse out your arguments
    passage = model_inputs.get('passage', None)
    if passage == None:
        return {'message': "No passage provided"}
    
    # Run the model
    passage_tokenized = tokenizer(passage)
    embeddings = bert_model(**passage_tokenized)[0][:,0,:].squeeze(0)

    # Return the results as a dictionary
    return {'embeddings': embeddings.tolist()}
