REQUIREMENT_GATHER_PROMPT = """
You are a smart home design assistant. Analyze this user input and extract key requirements:

User Input: {input}

Extract and list the following details:
1. Home size (number of rooms, square footage)
2. Priority systems (security, comfort, energy efficiency)
3. Preferred smart home ecosystems (Google, Apple, etc.)
4. Budget range
5. Any special needs or preferences

Format as a bulleted list of clear requirements.
"""

ARCHITECTURE_PROMPT = """
Based on these requirements: {requirements}

Create a detailed architectural plan including:
1. Room-by-room layout
2. Wiring and network infrastructure
3. Sensor placement
4. Central control system design
5. Integration points for smart devices

Format as a structured report with clear sections.
"""

DEVICE_PROMPT = """
For these smart home requirements: {requirements}

Recommend specific devices including:
1. Brand and model numbers
2. Key features matching the requirements
3. Compatibility notes
4. Price ranges
5. Installation complexity

Organize by room/system.
"""

BUDGET_PROMPT = """
For these recommended devices: {devices}

Create a detailed budget including:
1. Total estimated cost in INR
2. Cost breakdown by category
3. Potential savings options
4. Installation costs in INR
5. Ongoing maintenance estimates

Format as a financial report with clear budget details
"""

CONTRACTOR_PROMPT = """
For this smart home design:
{design}

And these available contractors:
{contractors}

1. Select the most suitable contractor based on:
   - Project scope match
   - Ratings and reviews
   - Pricing competitiveness
2. Draft a professional contact email including:
   - Project summary
   - Request for quote
   - Timeline expectations
3. Format as a ready-to-send email
"""

SCHEDULING_PROMPT = """
For this smart home installation:
{design}

With selected contractor:
{contractor}

Available installation dates: {available_dates}

1. Propose 3 specific installation options (dates/times)
2. Draft a scheduling email including:
   - Project confirmation
   - Date options
   - Preparation requirements
3. Format as a ready-to-send email
"""