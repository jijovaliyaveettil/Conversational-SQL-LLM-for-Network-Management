from langchain_community.utilities import SQLDatabase
from langchain_ollama.chat_models import ChatOllama

# llm = ChatOllama(model="llama3.1", temperature=0).bind_tools([chart_plot])


db_path = "sample.db"
db = SQLDatabase.from_uri(f"sqlite:///{db_path}")

print(db.get_usable_table_names())
print(db.table_info)