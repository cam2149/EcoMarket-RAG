
from app.api.apiFast_tools import (
    GetOrdersDatasetTool,
    GetOrderTool,
    QueryRAGTool,
    RegisterReturnOrderTool,
    VerifyEligibilityOrderTool
)
from langchain_openai import AzureChatOpenAI
from app.config import settings
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, END

class LangAgent:

    # --- LangGraph Agent Implementation ---
    class LangGraphAgent:
        def __init__(self):
            allSettings = settings.get_settings()
            get_orders_dataset_tool = GetOrdersDatasetTool()
            get_order_tool = GetOrderTool()
            query_rag_tool = QueryRAGTool()
            register_return_order_tool = RegisterReturnOrderTool()
            verify_eligibility_order_tool = VerifyEligibilityOrderTool()

            tools = [
                get_orders_dataset_tool,
                get_order_tool,
                query_rag_tool,
                register_return_order_tool,
                verify_eligibility_order_tool
            ]

            llm = AzureChatOpenAI(
                azure_deployment=allSettings.azure_openai_deployment_name,
                temperature=0,
                azure_endpoint=allSettings.azure_openai_endpoint,
                api_key=allSettings.azure_openai_key,
                api_version=allSettings.azure_openai_api_version
            )

            # Crear el agente ReAct de LangGraph
            agent_node = create_react_agent(llm, tools)

            # Define el grafo de estados
            workflow = StateGraph()
            workflow.add_node("agent", agent_node)
            workflow.add_edge("agent", END)
            workflow.set_entry_point("agent")
            self.graph = workflow.compile()

        def run(self, prompt: str):
            result = self.graph.invoke({"input": prompt})
            return result

    # Instancia global para compatibilidad
    lang_agent = LangGraphAgent()
    lang_agent_executor = lang_agent.graph


    def run(self, prompt: str):

        return self.agent_executor.run(prompt)



 
