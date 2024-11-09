from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

api = os.getenv("GEMINI_API_KEY")
print(api)