# %%
from langchain_groq import ChatGroq
llm=ChatGroq(api_key="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",model="llama3-70b-8192")

# %%
llm 
# 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

# %%
while True:
    user=input()
    if user=='exit':
        break
    else:
        response=llm.invoke(user).content
        print(response)



