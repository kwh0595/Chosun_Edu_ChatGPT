from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv, find_dotenv
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.globals import set_llm_cache, set_debug
from langchain.cache import InMemoryCache, SQLiteCache

#Caching을 사용하는 이유?
# -> LLM 모델의 생성된 답변을 저장할 수 있음
# -> 반복된 동일한 질문이 계속되면 새로 생성하지 않고 
#    Cache에 저장한 내용을 재사용!
# -> 금전적으로 효율

set_llm_cache(InMemoryCache) #메모리에 저장(휘발성)
set_llm_cache(SQLiteCache("cache.db"))

_=load_dotenv(find_dotenv())


chat = ChatOpenAI( 
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    # temperature: 0.1~1.0 : 0에 가까울수록 사실기반, 1에 가까울수록 창의력
    temperature = 0.1,
    # 답변 생성하는 과정을 시각화 가능
    streaming=True,
    callbacks = [StreamingStdOutCallbackHandler()]
)

chat.predict("한국인은 돈까스를 어떻게 만드나요?")