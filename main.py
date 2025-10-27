#!/usr/bin/env python3
"""
EcoMarket RAG Solution - Main Entry Point
FastAPI application for RAG-based product queries and recommendations
"""

import sys
from pathlib import Path
from contextlib import asynccontextmanager
from app.api.apiFast import app
from app.langchain.lang import lang_agent_executor, LangAgent
#!/usr/bin/env python3
"""
EcoMarket RAG Solution - Main Entry Point
Lanzador de la API FastAPI
"""
if __name__ == "__main__":
    import uvicorn
    from app.config.settings import get_settings
    from app.langchain.lang import agent, create_react_agent
    settings = get_settings()
    uvicorn.run(
        "app.api.apiFast:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
    consulta = "Dame los detalles de la orden ECO-2509-20001 y registra una devolución"
    lang_agent = LangAgent()
    response = lang_agent.run(consulta)
    print("Respuesta del agente:", response)
