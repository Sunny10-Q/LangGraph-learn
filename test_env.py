"""Verify the local LangGraph course environment without calling a model API."""
import importlib
import os
import sys
from importlib.metadata import version
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"), override=True)
print(f"Python: {sys.version.split()[0]}")
for package in ("langgraph", "langgraph-prebuilt", "langchain-core", "langchain-deepseek", "jupyter", "ipykernel", "pydantic"):
    print(f"{package}: {version(package)}")

# Import checks cover the core graph, prebuilt agent nodes, and DeepSeek adapter.
importlib.import_module("langgraph")
from langgraph.prebuilt import ToolNode
from langchain_deepseek import ChatDeepSeek
print("Core imports: OK")

# Never print the secret; model calls are intentionally left to the user.
print("DEEPSEEK_API_KEY: configured" if os.getenv("DEEPSEEK_API_KEY") else "DEEPSEEK_API_KEY: missing")