# Chosun_Edu_ChatGPT
OpenAI사의 GPT 모델을 활용한 챗봇 개발하기

# VScode를 사용한 Python 개발환경 구축
    1. vscode 설치
    2. python 설치(python.org)+환경변수(path)체크!
    3. vscode Extensions에서 (python, Python Extension Pack, gitgraph or gitlens)추가
    4. vscode에서 github 계정으로 로그인(연동)
    5. github에서 Repository(프로젝트) 생성
    6. vscode "git clone repository"로 5번에서 생성한 프로젝트 내려받기
    7. 가상환경 생성(venv) : 가상환경 구축 참조
    8. vscode에서 python interpreter 설정

### Python 가상환경 구축
1. venv
    - python -m venv ./venv (가상환경 생성)
    - .\venv\Scripts\activate (가상환경 접속)
    - pip install [라이브러리명] (가상환경 라이브러리 설치) ex) 라이브러리명 -> openai