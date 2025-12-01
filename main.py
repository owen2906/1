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




streamlit
pandas
pymysql
sqlalchemy
# ... 그 외 필요한 라이브러리 (joblib, matplotlib 등)

