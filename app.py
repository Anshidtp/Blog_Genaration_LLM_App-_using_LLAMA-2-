import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# Function to get response from llama-2 model
def llamaresponse(input ,words,style):
    ## loading llama2 model
    llm = CTransformers(model = 'Model\llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type = 'llama',
                        config = {'max_new_tokens':256,
                                  'temperature':0.01})
    
    #prompt template
    template = """
        write a blog for {style} job profile for a topic {input}
        within {words} words""" 
    
    prompt = PromptTemplate(input_variables=["input","words","style"],
                            template=template)
    
    #Generating the response from llama model
    response = llm(prompt.format(style = style, input = input,words = words))
    print(response)
    return response




st.set_page_config(page_title="Generate AI Blogs",
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Blogs Made Easy..")

#Create input field for the user
input = st.text_input("Enter Your Blog Topic")

## Creating 2 more columns for additional 2 fields

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Word Size of Your Blog")

with col2:
    blog_style = st.selectbox('Writing Blog For', 
                              ('Researchers','Data Scientist','Students','Others'),index=0)

# Submit Button
submit  = st.button('Genarate')

#Response section
if submit:
    st.write(llamaresponse(input,no_words,blog_style))