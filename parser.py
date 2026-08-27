from pydantic import BaseModel,Field

from langchain_core.output_parsers import PydanticOutputParser

class jobdescription(BaseModel):
    skills:list[str]=Field(description="Skills explicitly mentioned in the job description.")
    experience:str=Field(description="Required experience explicitly mentioned in the job description.")
    education:str =Field(description="Required education explicitly mentioned in the job description")

def create_parser()->PydanticOutputParser:
    return PydanticOutputParser(pydantic_object=jobdescription)
    