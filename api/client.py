import requests
import streamlit

def get_openai_response(input_text):

    response=requests.post(
        "http://localhost:8000/essay/invoke",
        json={'input':{input_text}})
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
        "http://localhost:8000/poem/invoke",
        json={'input':{input_text}})
    return response.json()['output']
    