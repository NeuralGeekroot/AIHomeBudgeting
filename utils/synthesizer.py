def synthesize_outputs(architecture: str, devices: str, budget: str) -> str:
    return f"""
    SMART HOME DESIGN REPORT
    -------------------------------------------------------------------------
    
    ARCHITECTURE PLAN:
    {architecture}
    
    RECOMMENDED DEVICES:
    {devices}
    
    BUDGET ESTIMATE:
    {budget}
    
    NEXT STEPS:
    - Review the plan
    - Contact contractors
    - Schedule installation
    """