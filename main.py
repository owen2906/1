altair==5.5.0
attrs==25.4.0
blinker==1.9.0
cachetools==6.2.2
certifi==2025.11.12
cffi==2.0.0
charset-normalizer==3.4.4
click==8.3.1
colorama==0.4.6
contourpy==1.3.3
cryptography==46.0.3
cycler==0.12.1
fonttools==4.61.0
gitdb==4.0.12
GitPython==3.1.45
greenlet==3.2.4
idna==3.11
Jinja2==3.1.6
joblib==1.5.2
jsonschema==4.25.1
jsonschema-specifications==2025.9.1
kiwisolver==1.4.9
MarkupSafe==3.0.3
matplotlib==3.10.7
mysql-connector-python==9.5.0
narwhals==2.12.0
numpy==2.3.5
packaging==25.0
pandas==2.3.3
pillow==12.0.0
protobuf==6.33.1
pyarrow==21.0.0
pycparser==2.23
pydeck==0.9.1
PyMySQL==1.1.2
pyparsing==3.2.5
python-dateutil==2.9.0.post0
pytz==2025.2
referencing==0.37.0
requests==2.32.5
rpds-py==0.30.0
six==1.17.0
smmap==5.0.2
SQLAlchemy==2.0.44
streamlit==1.51.0
tenacity==9.1.2
toml==0.10.2
tornado==6.5.2
typing_extensions==4.15.0
tzdata==2025.2
urllib3==2.5.0
watchdog==6.0.0
# import library
import streamlit as st
import pandas as pd
# DB connection
import pymysql
from sqlalchemy import create_engine

# 화면 설정
st.set_page_config(page_title="윤성의 데이터사이언스 포트폴리오", layout="wide")

# --- 타이틀 가운데 정렬 ---
st.markdown('<h1 style="text-align: center;">윤성의 데이터사이언스 포트폴리오</h1>', unsafe_allow_html=True)

# --- 서브헤더 가운데 정렬 ---
st.markdown('<h3 style="text-align: center;">윤성의 데이터사이언스 포트폴리오입니다.</h3>', unsafe_allow_html=True)

# -----------------------------------------------
# 🌟 첫 번째 행 (사진 3개) 🌟
# -----------------------------------------------

# 1. 페이지를 3개의 동일한 너비의 열로 나눕니다.
col1, col2, col3 = st.columns(3)

# 2. 각 열(column)에 이미지를 삽입합니다.

# 첫 번째 열에 이미지 삽입
with col1:
    st.image("1.png", caption="스타벅스 메뉴 군집분석 프로젝트", use_container_width=True)

# 두 번째 열에 이미지 삽입
with col2:
    st.image("2.png", caption="뉴스 토픽 추출 프로젝트", use_container_width=True)

# 세 번째 열에 이미지 삽입
with col3:
    st.image("3.png", caption="사진 분류", use_container_width=True)


# -----------------------------------------------
# 🌟 두 번째 행 (사진 2개 추가) 🌟
# -----------------------------------------------

# 새로운 행을 만들고 2개의 동일한 너비의 열로 나눕니다.
# 두 번째 행이므로 col4, col5라는 변수 이름을 사용합니다.
col4, col5 = st.columns(2) 

# 첫 번째 새로운 열에 이미지 삽입
with col4:
    # 이미지 파일 경로와 캡션을 실제 내용으로 수정하세요.
    st.image("4.png", caption="데이터분석준전문가", use_container_width=True) 

# 두 번째 새로운 열에 이미지 삽입
with col5:
    # 이미지 파일 경로와 캡션을 실제 내용으로 수정하세요.
    st.image("5.png", caption="사회조사분석사2급", use_container_width=True)

