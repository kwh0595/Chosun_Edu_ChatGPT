from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate, ChatPromptTemplate
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler
_=load_dotenv(find_dotenv())

# 1. Chat 모델 생성
chat = ChatOpenAI( 
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature = 0.1,
    # 답변 생성하는 과정을 시각화 가능
    streaming=True,
    callbacks = [StreamingStdOutCallbackHandler()]
)
