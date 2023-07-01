# pip install google-search-results

from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI

# cargamos openai api key
load_dotenv()

llm = OpenAI(temperature=0.3)

# cargamos dos tools
tools = load_tools(["serpapi"], llm=llm)

# iniciamos un agent con los tools que necesitamos ejecutar
# 1- Tools
# 2- modelo
# 3- El tipo de agente que vamos a ejecutar
# 4- verbose=True para mostra en consola lo que hace el agente

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# ejecutamos el agente
print(agent.run("quien ganó la copa mundial de francia 98?"))


