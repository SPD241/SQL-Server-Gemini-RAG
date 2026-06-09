from gemini import Connection_GMN

class RAGPropmts():

        """
        In this class we create the prompt about what we wanna gemini exactly does, here we give all necessary information and constraings in static methods.
            - get_sql_schema_context() -> str
            - get_synthesis_propmt(user_question:str, db_results: str) -> str
        """
        @staticmethod
        def get_sql_schema_context() -> str:
            """
            This method returns the constraings in order to be processed by gemini and translate NLP to SQL
            """
            return """
            You are a strict SQL Server database assistant. Your only job is to write a valid T-SQL query based on the user's question.
            
            Database Structure:
            - Table: dbo.Categoria (id_cat INT PK, nombre_editorial VARCHAR, descripcion VARCHAR)
            - Table: dbo.Editorial (id_editorial INT PK, nombre_editorial VARCHAR, pais VARCHAR)
            - Table: dbo.Libro (id_libro INT PK, titulo VARCHAR, isbn VARCHAR ,precio DECIMAL, stock INT, tipo_libro VARCHAR, fecha_publicacion DATE, id_cat INT)

            
            Rules:
            - Respond ONLY with the raw SQL code.
            - Do NOT include markdown styling like ```sql or ```.
            - Do NOT include explanations, introduction, or text outside the query.
            - Important: If the user asks for the "cheapest and most expensive" item simultaneously, write a single query using subqueries or plain T-SQL syntax that works in SQL Server without syntax errors. For example, you can query both values using a structure like: 
          SELECT * FROM dbo.Libro WHERE precio = (SELECT MAX(precio) FROM dbo.Libro) OR precio = (SELECT MIN(precio) FROM dbo.Libro).
             """
            
        @staticmethod
        def get_synthesis_propmt (user_question:str, db_results: str) -> str:
              
              return f"""
              Answer the question in a clear, objetive and professional way using UNIQUELY the following outcomes gotten by the database
              customer question: {user_question}
              Database outcomes: {db_results}
              """

    

            
    