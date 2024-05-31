import json
import pandas as pd
import traceback
import streamlit as st
from langchain.callbacks import get_openai_callback
from src.mcq_generator.utils import get_table_data,read_file
from src.mcq_generator.mcqgenerator import generate_evaluate_chain

with open(r'response.json','r') as file:
    RESPONSE_JSON = json.load(file)


st.title("MCQs Creator Application with LangChain")

with st.form("user_inputs"):
    uploaded_file=st.file_uploader("upload a PDF or txt file")
    mcq_count=st.number_input("No. of MCQs",min_value=3,max_value=50)
    subject=st.text_input("Insert Subject",max_chars=20)
    tone=st.text_input("Complxity Level of Questions",max_chars=20,placeholder="Simple")
    button=st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain({
                        "text":text,
                        "number":mcq_count,
                        "subject":subject,
                        "tone":tone,
                        "response_json":json.dumps(RESPONSE_JSON)
                    })
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")
            else:
                print()
                if isinstance(response,dict):
                    quiz=response.get("quiz",None)
                    if quiz is not None:
                        table_data=get_table_data(quiz)
                        if table_data is not None:
                            df=pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("Error in the table data")
                    

                    else:
                        st.write(response)
