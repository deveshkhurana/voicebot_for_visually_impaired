#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:10:46 2024

@author: stlp
"""

from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.prompts.prompt import PromptTemplate
import os 
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceHub(
    huggingfacehub_api_token = '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',
    repo_id="google/gemma-2b-it",
    model_kwargs={'temperature': 0.1, 'num_return_sequences':10, "return_full_text": False, 'max_length': 200}
)



prompt_template = PromptTemplate(
    input_variables=['history', 'input'],   
    template="""Assume the role of a seasoned financial advisor with a strong understanding 
    of investment strategies, budgeting, and retirement planning and answer the questions asked 
    by a young adults who has just started earning. Make sure the response is designed for 
    general purpose use case, talk about benefits of stock investments, dividends, fixed deposits, 
    mutual funds, etc. Ask questions to the user like what is their income, if they have not provided, 
    how much are they willing to invest, how much risk they want in their investment etc. Be proactive 
    and try to help the user who is asking the question as a friendly financial advisor.

    
    conversation history: {history}
    human: {input}
    
    AI: 
    """
)
memory = ConversationBufferWindowMemory(k=1)

conv_chain = ConversationChain(llm=llm,
                 prompt=prompt_template,
                 memory=memory,
                 verbose=True,
                 )

def get_answer(messages):
    response = conv_chain(messages)['response']
    return response
