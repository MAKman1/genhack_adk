# Moneypenny's Bank Agent System

This project contains the Moneypenny's Bank Financial Concierge agent and related components.

## Main Agent Package

The core agent logic is located in the `financial_advisor/` directory. This includes:
- The main `financial_coordinator` agent.
- Specialized sub-agents for various tasks (FAQ, account data, credit eligibility, etc.).
- API client for interacting with (simulated) bank APIs.
- Prompts and evaluation data.

## Running Evaluations

To run the agent evaluations using the ADK (Agent Development Kit), navigate to this project root directory (`/Users/arhamkhan/Data/agenthack/financial-advisor/`) in your terminal and execute the following command:

```bash
PYTHONPATH=. adk eval financial_advisor financial_advisor/eval/data/financial-advisor.test.json
```

**Explanation of the command:**
- `PYTHONPATH=.`: This ensures that the Python interpreter can find your `financial_advisor` package from the current directory (project root).
- `adk eval`: Invokes the ADK evaluation tool.
- `financial_advisor`: Specifies the main agent module/package to be evaluated (points to the `financial_advisor/` directory which contains an `__init__.py` and the root agent definition).
- `financial_advisor/eval/data/financial-advisor.test.json`: This is the path to the JSON file containing the evaluation test cases.

Make sure you have activated your Python virtual environment (e.g., `venv`) and installed all dependencies from `requirements.txt` before running the evaluation.

### AML Agent Evaluations

To run evaluations for the `aml_agent`, navigate to the project root directory and use:

```bash
python aml_agent/eval/test_aml_eval.py
```
Alternatively, using the `adk eval` CLI command (ensure `PYTHONPATH` is set if running from project root):
```bash
PYTHONPATH=. adk eval aml_agent aml_agent/eval/data/aml_agent.test.json
```
