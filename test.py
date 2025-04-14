import streamlit as st

# アプリのタイトルを設定
st.title('シンプルなStreamlitアプリ')

# テキストを表示
st.write('こんにちは、Streamlit！')

# ボタンを追加（オプション）
if st.button('クリック！'):
    st.write('ボタンがクリックされました！')