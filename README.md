# Finance Analyzer
A Python-based tool to process and classify financial transactions from a single CSV data source.

## Logic & Processing
The script implements a **classification engine** that iterates through a unified transaction log. It dynamically groups data by:
- **Month:** Temporal key.
- **Category:** Categorizes amounts into Income, Fixed Expenses, or Variable Expenses.

## Usage
Ensure you have a CSV file with the following headers: "Category", "Amount", "Description".
