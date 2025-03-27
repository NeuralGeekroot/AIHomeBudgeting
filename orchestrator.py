from langgraph.graph import StateGraph
from typing import TypedDict, Optional, Annotated
from typing_extensions import TypedDict
from utils.llm_models import load_llm
from utils.prompts import (
    REQUIREMENT_GATHER_PROMPT,
    ARCHITECTURE_PROMPT,
    DEVICE_PROMPT,
    BUDGET_PROMPT,
    CONTRACTOR_PROMPT,
    SCHEDULING_PROMPT
)
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random

load_dotenv()

class SmartHomeState(TypedDict):
    user_input: str
    requirements: Optional[str]
    architecture: Optional[str]
    devices: Optional[str]
    budget: Optional[str]
    final_output: Optional[str]
    contractors: Optional[str]
    installation_schedule: Optional[str]
    completion_status: Annotated[list[str], lambda x, y: x + [y]]

def create_smart_home_workflow():
    llm = load_llm()
    
    def gather_requirements(state: SmartHomeState):
        response = llm.invoke(
            REQUIREMENT_GATHER_PROMPT.format(input=state["user_input"]),
            config={"run_name": "GatherRequirements"}
        )
        return {"requirements": response.content, "completion_status": "Requirements gathered"}
    
    def design_architecture(state: SmartHomeState):
        response = llm.invoke(
            ARCHITECTURE_PROMPT.format(requirements=state["requirements"]),
            config={"run_name": "DesignArchitecture"}
        )
        return {"architecture": response.content, "completion_status": "Architecture designed"}
    
    def recommend_devices(state: SmartHomeState):
        response = llm.invoke(
            DEVICE_PROMPT.format(requirements=state["requirements"]),
            config={"run_name": "RecommendDevices"}
        )
        return {"devices": response.content, "completion_status": "Devices recommended"}
    
    def estimate_budget(state: SmartHomeState):
        response = llm.invoke(
            BUDGET_PROMPT.format(devices=state["devices"]),
            config={"run_name": "EstimateBudget"}
        )
        return {"budget": response.content, "completion_status": "Budget estimated"}
    
    def synthesize_design(state: SmartHomeState):
        final_output = f"""
        SMART HOME DESIGN COMPLETE
        =========================
        Architecture: {state["architecture"]}
        Devices: {state["devices"]}
        Budget: {state["budget"]}
        """
        return {
            "final_output": final_output,
            "completion_status": "Design finalized"
        }
    
    def find_contractors(state: SmartHomeState):
        contractors = [
            "TechHome Installations (Rating: 4.8/5)",
            "SmartHouse Pros (Rating: 4.9/5)",
            "Future Living Solutions (Rating: 4.7/5)"
        ]
        selected = random.choice(contractors)
        response = llm.invoke(
            CONTRACTOR_PROMPT.format(
                design=state["final_output"],
                contractors="\n".join(contractors)
            )
        )
        return {
            "contractors": f"Selected: {selected}\n\n{response.content}",
            "completion_status": "Contractors contacted"
        }
    
    def schedule_installation(state: SmartHomeState):
        start_date = datetime.now() + timedelta(days=random.randint(1, 14))
        end_date = start_date + timedelta(days=random.randint(1, 3))
        
        response = llm.invoke(
            SCHEDULING_PROMPT.format(
                design=state["final_output"],
                contractor=state["contractors"],
                available_dates=f"{start_date.strftime('%b %d')} to {end_date.strftime('%b %d')}"
            )
        )
        
        return {
            "installation_schedule": response.content,
            "completion_status": "Installation scheduled"
        }
    
    workflow = StateGraph(SmartHomeState)
    
    workflow.add_node("gather_requirements", gather_requirements)
    workflow.add_node("design_architecture", design_architecture)
    workflow.add_node("recommend_devices", recommend_devices)
    workflow.add_node("estimate_budget", estimate_budget)
    workflow.add_node("synthesize_design", synthesize_design)
    workflow.add_node("find_contractors", find_contractors)
    workflow.add_node("schedule_installation", schedule_installation)
    
    workflow.add_edge("gather_requirements", "design_architecture")
    workflow.add_edge("gather_requirements", "recommend_devices")
    workflow.add_edge("recommend_devices", "estimate_budget")
    workflow.add_edge("design_architecture", "synthesize_design")
    workflow.add_edge("estimate_budget", "synthesize_design")
    workflow.add_edge("synthesize_design", "find_contractors")
    workflow.add_edge("find_contractors", "schedule_installation")
    
    workflow.set_entry_point("gather_requirements")
    workflow.set_finish_point("schedule_installation")
    
    return workflow.compile()