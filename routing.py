from typing import Literal, Dict, Any
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parser import StrOutputParser
from pydantic import BaseModel, Field
import json

# C:\Report_agent\llama.cpp>llama-server.exe -m "C:/Report_agent/llm/Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf" -t 8 -tb 8 -c 4096 --top-p 0.9 --repeat-penalty 1.15 --host 127.0.0.1 --port 8080

BASE_URL = 'http://127.0.0.1:8080/v1'

class AgentState(BaseModel):
  user_input: str
  selected_tool: Literal[]
prompt = 
system_prompt = """
  You are AI assistant to help user select proper tool.
  After understanding user`s request, select one key from [Available tools] and provide output only in form of JSON {tool}:'...'. No explanation. Only JSON output
  Available tools = ['corp_loan','fx5220-1st','fx5220-2nd','fx5260', 'bok_10days',fss_10days','RADARS']
  No content, no description, no extra text, no explanation, no code fences, no line breaks.

  """
