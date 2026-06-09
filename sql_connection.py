"""
This module define the class Connetion to make a bridge between Python and SQL Management Server using pyodbc
"""

import pyodbc


class Connection():

    """
    Here we gonna define the login data, information such as:
        - Driver
        - Server Name
        - Database name
    """

    def __init__(self):
        self.connect_string = (
            r"DRIVER={ODBC Driver 17 for SQL Server};"
            r"SERVER=localhost\SQLEXPRESS;"
            r"DATABASE=Libreria_Online;"
            r"Trusted_Connection=yes;"
        )

    def Test_Connection(self) -> None:
        """
        This method calls out the driver for the connection, also we passed the atributes for the connection,
        if all its ok, the method will print the confirmation message, else will show up the error inside.

        Args: 
            - self.connect_string
        Return:
            - None
        """
        try: 
            conn = pyodbc.connect(self.connect_string)
            print("Connection successful")

            cursor = conn.cursor()
            cursor.execute("SELECT @@VERSION")
            row = cursor.fetchone()
            print(f"SQL VERSION: {row[0]}")

            conn.close()

        except Exception as e:
            print(f"Error while make the connection, please check up:\n{e}")

    def Execute_Query(self, query:str) -> str:
        """
        This method create the method and also wait for the query from gemini.
        """
        conn = pyodbc.connect(self.connect_string)
        cursor = conn.cursor()

        try: 
            cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            rows = cursor.fetchall()

            data_summary = f"columnas: {columns}\n"
            for row in rows:
                data_summary += f"{list(row)}\n"

            return data_summary
        
        except Exception as e:
            return f"Error \n{e}"
        finally:
            conn.close()
            

