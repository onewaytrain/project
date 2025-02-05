import streamlit as st
import bike

# 사이드바 화면
st.sidebar.title('사이드바')
user_id = st.sidebar.text_input('아이디 입력', value='python', max_chars=10)
user_pw = st.sidebar.text_input('패스워드 입력', value='', type='password')

if user_pw == '1234':
    st.sidebar.header('===포트폴리오===')
    select_data = ['따릉이 분석', '환율 분석']
    menu = st.sidebar.selectbox('메뉴 선택', select_data, index=0)

    if menu == '따릉이 분석':
        st.write('따릉이 분석')
        data = bike.data_preprocessing()
        st.dataframe(data.head(20))
    else: 
        st.write('환율 분석')
