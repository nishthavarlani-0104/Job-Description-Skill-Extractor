from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
def create_prompt(format_instructions):
    system_prompt="""
    You are an expert Job Description Information Extractor.

    Your task is to analyze a job description and extract ONLY
    the information explicitly stated in the provided text.

    Extract the following:

    1. Skills
    - List all technical and professional skills explicitly mentioned.

    2. Experience
    - Extract the required years or level of experience exactly as stated.

    3. Education
    - Extract the educational qualification explicitly mentioned.

    IMPORTANT RULES:
    - Do NOT assume or invent information.
    - Do NOT infer qualifications, skills, or experience.
    - If a field is not mentioned in the job description, return
    "not_available".
    - Keep the extracted information concise.
    - Return the result according to the required structured output schema.

    Use the following formatting instructions:
    {format_instructions}
    """

    prompt=ChatPromptTemplate.from_messages([("system",system_prompt),MessagesPlaceholder(variable_name="chat_history"),
                            ("human","Extract the required information from this job description:\n\n{job_description}")]).partial(format_instructions = format_instructions)

    return prompt