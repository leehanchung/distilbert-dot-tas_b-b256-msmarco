
# 🍌 Banana Serverless

This repo gives a framework to serve ML models in production using simple HTTP servers. The model can be found on [huggingface here](https://huggingface.co/sebastian-hofstaetter/distilbert-dot-tas_b-b256-msmarco).

# Quickstart
**[Follow the quickstart guide in Banana's documentation to use this repo](https://docs.banana.dev/banana-docs/quickstart).** 

*(choose "GitHub Repository" deployment method)*

# Testing Locally

## Virtual Environment
1) Install package requirements with:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
2) Modify and run download.py to get your model weights locally, if needed:
```bash
python download.py
```

3) Make your edits to app.py 

4) Run the Banana development server with:
```bash
python server.py
```

5) Modify and run test.py with your expected json payload as model_inputs
```bash
python test.py
```
6) Repeat steps 2-5 until ready to deploy

## Docker Environment
7) Verify that the application builds into Docker, with:
```bash
docker build -t banana .
```
8) Verify that the application runs in Docker on the GPUs, with:
```bash
docker run --gpus=all -p 8000:8000 banana
```
9) To teardown the Docker deployment, do:
```bash
docker ps # find the container id of banana
docker stop <container id> # this stops the container
docker images # find the image id of banana
docker rmi <image id>
```

If all of this works, push to the main branch on GitHub to start your build on Banana!
<br>

# Helpful Links
Understand the 🍌 [Serverless framework](https://docs.banana.dev/banana-docs/core-concepts/inference-server/serverless-framework) and functionality of each file within it.

Generalize this framework to [deploy anything on Banana](https://docs.banana.dev/banana-docs/resources/how-to-serve-anything-on-banana).

<br>

## Use Banana for scale.
