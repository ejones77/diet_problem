# diet_problem
Diet Problem using linear programming 

## Documentation 

- full ingredient & meal documentation is provided in `Diet Problem Documentation.xlsx`
    - includes ingredient breakdown for each meal selected
    - sources used include USDA nutrition facts for each food item & the Kroger website
    - any calculations to reach the portion value are referenced in the `notes` field
- output from the program is provided in `output.txt`
- testing the LLM's attempt at the assignment is shown in `llm_output.txt`
    - the executable code from the LLM output is in `llm_code.py`

## Problem Defintion

Given a list of five meals, minimize the food cost for each meal, while meeting the necessary nutrition constraints:

| Component | Max/Min  | Weekly Amount and Measure      |
|-----------|----------|-------------------------------|
| Sodium    | Maximum  | 35,000 milligrams (mg)         |
| Energy    | Minimum  | 14,000 Calories (kilocalories, kcal) |
| Protein   | Minimum  | 350 grams (g)                  |
| Vitamin D | Minimum  | 140 micrograms (mcg)           |
| Calcium   | Minimum  | 9100 milligrams (mg)         |
| Iron      | Minimum  | 126 milligrams (mg)            |
| Potassium | Minimum  | 32,900 milligrams (mg)         |

The linear program in standard form is provided in the paper `Diet Problem Assignment Jones.pdf`

## set up
- python version -- 3.11.9
- in the respository directory, create and activate a virtual environment (assuming powershell)
    - ` py -m venv .venv`
    - `./.venv/scripts/activate`
- install dependencies with
    - `py -m pip install --upgrade pip`
    - `py -m pip install -r requirements.txt`

- execute the main program
    - `py diet_problem.py`
