Module 8 Assignment: Advanced Data Structures
**GlobalTech Solutions - Customer Management System**

## Description
This project demonstrates the use of nested data structures in Python to build a functional Customer Management System (CMS). It simulates a business environment where "GlobalTech Solutions" tracks client contact information, service rates, and active project lifecycles. The system automates financial summaries, validates data integrity, and offers service recommendations based on a client's historical data.

## Files Included
* `customer_management.py`: The primary Python script containing the CMS logic and data structures.
* `README.md`: Documentation for the repository.

## What I Practiced
In this assignment, I moved beyond flat data into more complex, hierarchical structures:
* **Nested Data Management:** Navigating a "master" dictionary that stores sub-dictionaries and lists of projects, practicing data retrieval across multiple levels.
* **Dictionary Comprehensions:** Efficiently transforming data for bulk updates, such as applying across-the-board rate increases and filtering active clients.
* **Financial Aggregation:** Writing logic to flatten nested lists to calculate total hours, average budgets, and identify cost outliers.
* **Functional Programming:** Building reusable functions to validate data entry and a recommendation engine for cross-selling services.
* **Set Operations:** Using Python sets to identify service gaps and suggest new offerings to clients based on their unique history.
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("=" * 40)
print("README.md for Module 8 has been generated!")
print("=" * 40)
