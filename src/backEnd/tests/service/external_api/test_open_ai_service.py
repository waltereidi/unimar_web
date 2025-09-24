import pytest
from backEnd.service.external_api.open_ai_request  import OpenAiRequest
# ---- Testes reais ----
def test_gpt_5_nano_response():
    openaiRequest = OpenAiRequest()
    
    result =openaiRequest.gpt_5_nano_response('Cite uma conclusão de alan turing sobre o desenvolvimento de software ser uma disciplina, citação livro black swan')
    # httpbin sempre retorna um JSON com 'url'
    assert "id" in result
