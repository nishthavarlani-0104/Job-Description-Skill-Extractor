# Job-Description-Skill-Extractor
An AI-powered application that extracts **skills, experience, and education** from a given job description using an LLM-based workflow.

---

##  Setup and Installation

### 1. Create a Virtual Environment

Create a virtual environment in the project directory:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows:**
```bash
.venv\Scripts\Activate
```
**macOS/Linux:**
```bash
source .venv\Scripts\Activate
```
### 2. Install Requirements

Install the required dependencies from 
`requirements.txt`:
```bash
python -m pip install -r requirements.txt
```

### 3. Configure Environment Variables

The repository contains a `.env_example` file that shows the required environment variables.

Create a new `.env` file in the root directory of the project.

Add your environment variables in the same format as shown in `.env_example`:

    GROQ_API_KEY=your_groq_api_key
    MODEL_NAME=openai/gpt-oss-120b
    MODEL_PROVIDER=groq

Replace `your_groq_api_key` with your actual Groq API key.

---

## Workflow⚙️
### `prompt.py`

Creates the prompt template and defines the instructions given to the LLM for extracting information from the job description.

### `parser.py`

Defines the Pydantic schema and output parser used to convert the LLM response into structured data.

### `model.py`

Creates and configures the LLM using the environment variables defined in `.env`.

### `main.py`

Connects the prompt, model, and parser to create the complete extraction pipeline.

### `app.py`

Provides the Streamlit interface where the user can enter a job description and view the extracted information.

## ▶️ Run the Application

Make sure the virtual environment is activated and the `.env` file is properly configured.

Run the Streamlit application:
```bash
    python -m streamlit run app.py
```

The application will open in your browser.

Enter a job description and click **Extract Information** to generate the structured output.

