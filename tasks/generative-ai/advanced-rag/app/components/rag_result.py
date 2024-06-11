import re
import streamlit as st
from utils.rag_api import generate_rag_answer
from utils.s3_utils import generate_presigned_url_from_s3_uri

def rag_result(query, settings):
    # RAGの回答をチャンクで生成するジェネレータを呼び出す
    #for chunk in generate_rag_answer(query, settings):
    #    yield chunk
    generate_rag_answer(query, settings)
    #st.markdown(final_state["keys"]["generation"])

    # xml = final_state["keys"]["generation"]
    # st.markdown(parse_answer(xml))


