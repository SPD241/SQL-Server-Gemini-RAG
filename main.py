# Importamos las clases de tus otros archivos creados
from sql_connection import Connection
from gemini import Connection_GMN
from consulting import RAGPropmts

def run_rag_system():
    """
    This method create the connection between GMN and SQL SERVER, there we got the questions and the answer from the LLM.
    """
    #connections
    db_agent = Connection()
    conn_gmn = Connection_GMN()

    #querys
    user_question = input().strip()
    print(f"\nCustomer Question: '{user_question}'")
    
    #generate SQL
    schema_context = RAGPropmts.get_sql_schema_context()
    prompt_for_sql = f"{schema_context}\n\nPregunta: {user_question}"
    
    generated_sql = conn_gmn.conn(prompt_for_sql)
    print(f"GMN: {generated_sql}\n")
    
    #look up into SQL Server
    print("consulting SQL SERVER")
    raw_db_data = db_agent.Execute_Query(generated_sql)
    print(f"outcome db:\n{raw_db_data}\n")

    #transform the answer    
    final_prompt = RAGPropmts.get_synthesis_propmt(user_question, raw_db_data)
    final_answer = conn_gmn.conn(final_prompt)
    
    print(f"RAG:\n{final_answer}")
   

if __name__ == "__main__":
    run_rag_system()