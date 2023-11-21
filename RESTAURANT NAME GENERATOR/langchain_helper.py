import os
from langchain.prompts import PromptTemplate
from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


os.environ['HUGGINGFACEHUB_API_TOKEN']="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"

llm = HuggingFaceHub(repo_id="declare-lab/flan-alpaca-large",model_kwargs={"temperature":0,"max_length":512})



def Restaurant_name_generator(cuisine):
    
    prompt_template_name = PromptTemplate(
        template = "I want to name my new food. Suggest me some {cuisine} food",
        input_variables=["cuisine"]
    )

    name_chain = LLMChain(llm=llm,prompt=prompt_template_name,output_key = "restaurant_name")

    prompt_template_items = PromptTemplate(
        template = "Suggest me some menu items for {restaurant_name}. Return it as a comma separated list",
        input_variables=["restaurant_name"]
    )


    food_item_chain = LLMChain(llm=llm,prompt = prompt_template_items, output_key = "menu_items")
    
    chains = SequentialChain(
        chains = [name_chain,food_item_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name','menu_items'])
    
    response = chains({'cuisine':cuisine})
    return response

    


