# Modular Text-to-SQL RAG System (SQL Server Express and Gemini 2.5 Flash)

This repository contains a modular, object-oriented Retrieval-Augmented Generation (RAG) pipeline designed to bridge human natural language queries with a local Microsoft SQL Server Express relational database.

Instead of translating data into unstructured vector embeddings, this system implements a Text-to-SQL architectural pattern. Google's Gemini 2.5 Flash model acts as a compiler that translates natural language into schema-compliant T-SQL statements. These queries are executed against the database engine via pyodbc, and the raw database results are synthesized back into a structured, human-readable response.

---

## Project Architecture

The codebase strictly follows object-oriented programming principles and separates core components into individual modules:

* **main.py**: The central orchestrator that manages the application lifecycle and execution flow.
* **sql_connection.py**: Manages database connections, execution contexts, and cursor operations using pyodbc.
* **gemini.py**: Handles direct API payload exchanges and initialization with the official google-genai SDK.
* **consulting.py**: Houses static DDL definitions, relational schema constraints, and behavioral prompts for the LLM.
* **requirements.txt**: Lists the specific library dependencies for the environment.
* **.gitignore**: Prevents local virtual environments and caching files from being tracked by version control.

---

## Technical Stack

* **Language**: Python 3.8 or higher
* **Database Engine**: Microsoft SQL Server 2025 Express Edition
* **Database Driver**: Microsoft ODBC Driver 17 for SQL Server
* **AI Integration**: google-genai SDK (Gemini 2.5 Flash model)

---

## Execution Workflow Example

The following sequence demonstrates a live execution trace within the terminal environment:

1. **User Input Query:**
   "What is the most expensive and the cheapest book in the library?"

2. **Generated T-SQL Statement:**
   ```sql
   SELECT * FROM dbo.Libro 
   WHERE precio = (SELECT MAX(precio) FROM dbo.Libro) 
      OR precio = (SELECT MIN(precio) FROM dbo.Libro);
