import re
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text , create_engine
from backEnd.service.external_api.open_ai_request import OpenAiRequest

class OpenAiService:
    def GPT5nano_GetResponse(self , json:str):
        
        pergunta = json.get("pergunta")
        openAiRequest = OpenAiRequest()
        result = openAiRequest.gpt_5_nano_response(pergunta)
                    
        mensagens = []
        for item in result.get("output", []):
            if item.get("type") == "message":
                for content in item.get("content", []):
                    if content.get("type") == "output_text":
                        mensagens.append(content.get("text"))
                
        return mensagens
    
    

    
    