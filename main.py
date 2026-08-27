from prompt import create_prompt
from model import create_model
from parser import create_parser

def extract_job_description(job_description:str):
    parser=create_parser()
    format_instructions=parser.get_format_instructions()
    prompt=create_prompt(format_instructions)
    model=create_model()

    chain=prompt | model | parser

    result= chain.invoke({"job_description":job_description,"chat_history":[]})
    return result

def main():
        while True:
            user_input=input("Enter the job description:\n").strip()

            if user_input=="exit":
                break
            job_description=user_input

            if not job_description:
                print("job description cannot be empty")
                return

            output=extract_job_description(job_description)

            print("Extracted Information:\n",output)


if __name__=="__main__":
    main()    

    