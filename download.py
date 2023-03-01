# In this file, we define download_model
# It runs during container build time to get model weights built into the container
import os
from transformers import AutoTokenizer, AutoModel

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    MODEL_NAME = os.getenv("MODEL_NAME")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    bert_model = AutoModel.from_pretrained(MODEL_NAME)


if __name__ == "__main__":
    download_model()