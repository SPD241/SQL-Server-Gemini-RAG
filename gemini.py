"""
This module create the connection to Gemini as LLM in order to assist to a customer bassed on the database
"""
from google import genai
import os

class Connection_GMN():
    """
    This class resume all necessary to create a connection with GMN, it has init and conn function
    """
    def __init__(self):
        """
        The constructor will initialize the global variables as the key or client with model of GMN.
        The api key must be given by terminal
        """
        api_key = os.environ["GEMINI_API_KEY"]
        self.client = genai.Client(api_key=api_key)
        self.model = 'gemini-2.5-flash'

    def conn(self, propmt: str) -> str:
        
        """
        This fuction will send like a request to gemini, if all its ok the output will be the text that GMN has response
        """
        response = self.client.models.generate_content(
            model= self.model,
            contents = propmt
        )

        return response.text.strip()
'''    
if __name__ == "__main__":
    try: 
        gemini = Connection_GMN()
        test   = gemini.conn()
        print(f"Connection sucessful:\n{test}")

    except Exception as e:
        print(f"Error while connect with gemini:\n{e}")'''