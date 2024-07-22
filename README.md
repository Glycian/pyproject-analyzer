# PyProject Analyzer

PyProject Analyzer is a tool designed to provide a summary of a Python project's structure and contextual information. This can be particularly useful for developers and AI tools to understand the initial context of a project.

## Current Features

- **Project Structure Analysis**: Analyzes Python files to gather module, class, and function information.
- **ZIP File Extraction**: Extracts the contents of a ZIP file to a specified directory.
- **Result Output**: Writes the analysis results to a `code_summary.txt` file.

## Installation and Usage

To install PyProject Analyzer, clone this repository:

```bash
git clone https://github.com/your-username/pyproject-analyzer.git
cd pyproject-analyzer
```

Usage
You can use PyProject Analyzer by running the main script with the path to your Python project ZIP file:

```bash
Copy code
python analyze_zip.py /path/to/your/project.zip
```
This will output a summary of the project structure and other relevant information to code_summary.txt.

## Example Output
Here is an example output for a sample Python project:

```
Example Output
Analysis Results:
Modules and their contents:

Module: Invest.main
  Classes: []
  Functions: ['main']

Module: Invest.account.account
  Classes: ['Account']
  Functions: ['__init__', 'add_period', 'remove_period', 'get_period']

Module: Invest.account.account_manager
  Classes: ['AccountManager']
  Functions: ['__init__', 'add_account', 'remove_account', 'get_account', 'get_account_data', 'calculate_growth', 'remove_period', 'update_account_name', 'update_period_name']

Module: Invest.account.period
  Classes: ['Period']
  Functions: ['__init__']
 ```
  
## Future Development
- Detailed Project Structure Overview: Provide a full directory and file structure overview.
- Dependency Analysis: List all dependencies and their versions used in the project.
- Code Metrics: Calculate and display various code metrics such as lines of code, number of functions, and classes.
- Contextual Information: Extract docstrings, comments, and other contextual information to give a better understanding of the project's components.
- Visualization: Add graphical representations of the project structure and dependencies.


## Changelog
- [1.0.0] - 2024-07-22
 Initial release with basic functionality:
 Extract ZIP files.
 Analyze Python files to gather module, class, and function information.
 Write analysis results to code_summary.txt.

 - 
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
