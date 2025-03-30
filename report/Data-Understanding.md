
# Data Cleanup Workflow

## 1. Load and Inspect the Dataset

#### Overview
- **Number of rows**: 100,000  
- **Total data memory usage**: 120.56 MB  
- **Total Columns:** 28
- **Total Entries (cells):** 2,800,000

#### Columns

| Column Name                | Data Type |
| -------------------------- | --------- |
| Age                        | object    |
| Occupation                 | object    |
| Annual_Income              | object    |
| Monthly_Inhand_Salary      | float64   |
| Num_Bank_Accounts          | int64     |
| Num_Credit_Card            | int64     |
| Interest_Rate              | int64     |
| Num_of_Loan                | object    |
| Type_of_Loan               | object    |
| Delay_from_due_date        | int64     |
| Num_of_Delayed_Payment     | object    |
| Changed_Credit_Limit       | object    |
| Num_Credit_Inquiries       | float64   |
| Credit_Mix                 | object    |
| Outstanding_Debt           | object    |
| Credit_Utilization_Ratio   | float64   |
| Credit_History_Age         | object    |
| Payment_of_Min_Amount      | object    |
| Total_EMI_per_month        | float64   |
| Amount_invested_monthly    | object    |
| Payment_Behaviour          | object    |
| Monthly_Balance            | object    |
| Credit_Score               | object    |

---

## 2. Correct Data Types

### ⚠️ Incorrect Data Types & Solutions

- **Annual_Income (object → float64/int64)**  
  - Stored as an object due to formatting issues (e.g., commas, currency symbols).  
  - **Fix**: Clean non-numeric characters and convert to float.

- **Num_of_Loan (object → int64)**  
  - Should be an integer but is stored as an object, likely due to missing values or formatting inconsistencies.  
  - **Fix**: Handle NaNs and convert to int.

- **Num_of_Delayed_Payment (object → int64)**  
  - Represents a count but is stored as an object.  
  - **Fix**: Convert to integer after handling non-numeric values.

- **Changed_Credit_Limit (object → float64)**  
  - Should be numeric but may contain missing values or inconsistent formats.  
  - **Fix**: Convert to float.

- **Outstanding_Debt (object → float64)**  
  - Stored as an object due to currency symbols or missing values.  
  - **Fix**: Convert to float.

- **Credit_History_Age (object → int64/float64)**  
  - Likely stored as text (e.g., "10 Years 5 Months").  
  - **Fix**: Extract total months or years and convert to numeric.

- **Amount_invested_monthly (object → float64)**  
  - Should be numeric but may have missing or improperly formatted values.  
  - **Fix**: Convert to float.

- **Monthly_Balance (object → float64)**  
  - Stored as an object due to formatting issues.  
  - **Fix**: Clean data and convert to float.

- **Age (object → int64)**  
  - Age should be stored as an integer.  
  - **Fix**: Convert to int after handling inconsistencies.

### ✅ Columns That Are Fine

- **Numerical**: Monthly_Inhand_Salary, Num_Bank_Accounts, Num_Credit_Card, Interest_Rate, Delay_from_due_date, Num_Credit_Inquiries, Credit_Utilization_Ratio, Total_EMI_per_month.  
- **Categorical**: Credit_Mix, Payment_of_Min_Amount, Payment_Behaviour, Credit_Score.

## Mixed Data Types Issues

During our analysis, we detected mixed data types in the following columns:

- **Type_of_Loan**: Mixed types detected: `{<class 'str'>, <class 'float'>}`  
- **Num_of_Delayed_Payment**: Mixed types detected: `{<class 'str'>, <class 'float'>}`  
- **Credit_History_Age**: Mixed types detected: `{<class 'str'>, <class 'float'>}`  
- **Amount_invested_monthly**: Mixed types detected: `{<class 'str'>, <class 'float'>}`  
- **Monthly_Balance**: Mixed types detected: `{<class 'str'>, <class 'float'>}`

## Final Column Classification

this table represents the final column classification for modeling purposes after data cleaning and type corrections

| Column Name               | Variable Type          | Final Data Type |
|---------------------------|------------------------|----------------|
| Age                       | Numerical (Discrete)   | int64         |
| Occupation                | Categorical (Nominal)  | object        |
| Annual_Income             | Numerical (Continuous) | float64/int64 |
| Num_Bank_Accounts         | Numerical (Discrete)   | int64         |
| Num_Credit_Card           | Numerical (Discrete)   | int64         |
| Interest_Rate             | Numerical (Continuous) | int64         |
| Num_of_Loan               | Numerical (Discrete)   | int64         |
| Type_of_Loan              | Categorical (Nominal)  | object        |
| Delay_from_due_date       | Numerical (Discrete)   | int64         |
| Num_of_Delayed_Payment    | Numerical (Discrete)   | int64         |
| Credit_Mix                | Categorical (Nominal)  | object        |
| Outstanding_Debt          | Numerical (Continuous) | float64       |
| Credit_Utilization_Ratio  | Numerical (Continuous) | float64       |
| Credit_History_Age        | Numerical (Continuous) | int64/float64 |
| Credit_Score              | Categorical (Ordinal)  | object        |
| Payment_Behaviour         | Categorical (Nominal)  | object        |

---

## 3. Clean Categorical Columns

- **Columns** 
  ``` 
  [
    "Occupation", 
    "Type_of_Loan", 
    "Credit_Mix", 
    "Payment_of_Min_Amount", 
    "Payment_Behaviour", 
    "Credit_Score"
  ]
    ```
### Categorical Columns Issues Report

#### 1. Occupation
**Summary:**

- Unique values: 16
- Most common value: "_______" (7.06%, 7,062 occurrences)
- Top categories: "_______" (7.06%), Lawyer (6.58%), Architect (6.35%), Engineer (6.35%), Scientist (6.3%)

**Issues:**

- The most frequent value, "_______", likely indicates missing or unknown occupations.

**Cleaning Steps:**

- **Handle "_______":**
  - Replace "_______" with "Unknown" to clearly mark missing data. This maintains transparency without assuming an occupation.
  - Alternative: Leave it as is if "_______" represents a valid category (e.g., unemployed), but "Unknown" is more explicit.
- **Standardize Format:**
  - Convert all values to title case (e.g., "lawyer" → "Lawyer") for consistency.
  - Remove any leading/trailing spaces.
- **Check for Duplicates:**
  - Review all 16 unique values for misspellings or variations (e.g., "Eng." vs. "Engineer"). Merge duplicates if found.

#### 2. Type_of_Loan
**Summary:**

- Unique values: 6,261
- Most common value: "Not Specified" (1.41%, 1,408 occurrences)
- Top categories: "Not Specified" (1.41%), Credit-Builder Loan (1.28%), Personal Loan (1.27%), Debt Consolidation Loan (1.26%), Student Loan (1.24%)

**Issues:**

- 6,261 unique values suggest this column contains combinations of loans or free-text entries.
- "Not Specified" indicates missing data.

**Cleaning Steps:**

- **Handle "Not Specified":**
  - Replace "Not Specified" with "Unknown" for clarity and consistency with other columns.
- **Parse Combinations:**
  - Check if entries are combinations (e.g., "Auto Loan, Personal Loan"). If so:
    - Split into separate columns (e.g., "Loan_Type_1", "Loan_Type_2") or create binary indicators (e.g., "Has_Personal_Loan: Yes/No").
    - If splitting isn’t feasible, group similar loans into broader categories (e.g., "Consumer Loans" for Personal, Auto, etc.).
- **Reduce Categories:**
  - With 6,261 unique values, consider clustering similar loans (e.g., all "Student Loan" variants into one category) to simplify analysis.
- **Standardize Format:**
  - Use title case (e.g., "credit-builder loan" → "Credit-Builder Loan") and ensure consistent separators (e.g., commas) in combinations.

#### 3. Credit_Mix
**Summary:**

- Unique values: 4
- Most common value: "Standard" (36.48%, 36,479 occurrences)
- Top categories: "Standard" (36.48%), "Good" (24.34%), "_" (20.2%), "Bad" (18.99%)

**Issues:**

- "_" likely represents missing or unknown values.

**Cleaning Steps:**

- **Handle "_":**
  - Replace "_" with "Unknown" to explicitly mark missing data.
  - Alternative: Impute with the mode ("Standard"), but this risks introducing bias; "Unknown" is safer.
- **Standardize Format:**
  - Ensure all values are in title case (e.g., "standard" → "Standard") and free of extra spaces.

#### 4. Payment_of_Min_Amount
**Summary:**

- Unique values: 3
- Most common value: "Yes" (52.33%, 52,326 occurrences)
- Top categories: "Yes" (52.33%), "No" (35.67%), "NM" (12.01%)

**Issues:**

- "NM" likely means "Not Mentioned," indicating missing or unspecified values.

**Cleaning Steps:**

- **Handle "NM":**
  - Replace "NM" with "Unknown" to align with other columns.
  - Alternative: Treat "NM" as a separate category if it’s meaningful (e.g., data not provided), but "Unknown" standardizes missing values.
- **Standardize Format:**
  - Ensure "Yes" and "No" are consistently formatted (e.g., not "yes" or "NO").

#### 5. Payment_Behaviour
**Summary:**

- Unique values: 7
- Most common value: "Low_spent_Small_value_payments" (25.51%, 25,513 occurrences)
- Top categories: Various spending/payment behaviors (e.g., "High_spent_Medium_value_payments" at 17.54%)

**Issues:**

- No obvious missing values, but inconsistent formatting could exist.

**Cleaning Steps:**

- **Standardize Format:**
  - Use a consistent separator and case (e.g., "Low_spent_Small_value_payments" → "Low Spent Small Value Payments" with spaces or keep underscores but standardize across all entries).
  - Remove extra spaces or inconsistencies in naming.
- **Check for Duplicates:**
  - Ensure no similar behaviors are split due to typos (e.g., "Low Spent Small" vs. "Low_spent_Small_value_payments").

#### 6. Credit_Score
**Summary:**

- Unique values: 3
- Most common value: "Standard" (53.17%, 53,174 occurrences)
- Top categories: "Standard" (53.17%), "Poor" (29.0%), "Good" (17.83%)

**Issues:**

- No apparent issues; the column looks clean.

**Cleaning Steps:**

- **Verify:**
  - Confirm no hidden variations (e.g., "standard" vs. "Standard" or extra spaces).
- **Standardize Format:**
  - Ensure title case (e.g., "poor" → "Poor") for consistency.

---

## 4. Handling Missing Data

### Missing Data Report

#### Variables with Missing Data 
- **Name:** 9985 missing values (9.98%)  
- **Monthly_Inhand_Salary:** 15002 missing values (15.00%)  
- **Type_of_Loan:** 11408 missing values (11.41%)  
- **Num_of_Delayed_Payment:** 7002 missing values (7.00%)  
- **Num_Credit_Inquiries:** 1965 missing values (1.97%)  
- **Credit_History_Age:** 9030 missing values (9.03%)  
- **Amount_invested_monthly:** 4479 missing values (4.48%)  
- **Monthly_Balance:** 1200 missing values (1.20%)  

#### Overall Missing Data 
- **Total Missing Values:** 60071  
- **Total Missing Percentage:** 2.15%  

#### Chart 

![alt text](image.png)

### 🔧 How to Fix ? 

- **Remove the "Name" column** : no analytical value.
- **Use MICE** : This method leverages relationships between variables and provides multiple imputed datasets for robust analysis

  ``` 
  [
    "Monthly_Inhand_Salary"
    "Type_of_Loan"
    "Num_of_Delayed_Payment"
    "Num_Credit_Inquiries"
    "Credit_History_Age"
    "Amount_invested_monthly"
    "Monthly_Balance"
  ]
    ```
---


---

## 5. Handle Special Columns

---

## 6. Check for Outliers

---

## 7. Remove Duplicates

---

## 8. Drop Columns

### Which Columns Should Be Used and Why?

##### 1️⃣ Financial Stability & Income  
- **Age**: Correlates with credit history.  
- **Occupation**: Indicates job stability.  
- **Annual_Income** and **Monthly_Inhand_Salary**: Measure financial strength.

##### 2️⃣ Credit Exposure & Debt Management  
- **Num_Bank_Accounts** and **Num_Credit_Card**: Show financial activity.  
- **Interest_Rate**: Reflects borrowing cost.  
- **Num_of_Loan** and **Type_of_Loan**: Indicate current debt obligations.

##### 3️⃣ Payment Behavior & Creditworthiness  
- **Delay_from_due_date** and **Num_of_Delayed_Payment**: Track payment discipline.  
- **Changed_Credit_Limit**: Indicates lender trust.  
- **Num_Credit_Inquiries**: High inquiries may signal risk.

##### 4️⃣ Credit Score Factors  
- **Credit_Mix**: Diverse credit types are favorable.  
- **Outstanding_Debt** and **Credit_Utilization_Ratio**: Show liabilities and credit use.  
- **Credit_History_Age**: Longer history = better reliability.

##### 5️⃣ Spending & Financial Behavior  
- **Payment_of_Min_Amount**: Tracks minimum payments.  
- **Total_EMI_per_month** and **Monthly_Balance**: Show cash flow impact.  
- **Amount_invested_monthly** and **Payment_Behaviour**: Indicate financial habits.

### Drop 

```
columns_to_drop = [
    "name",
    "Credit_Score",  
    "Num_of_Loan",  
    "Type_of_Loan",  
    "Changed_Credit_Limit",  
    "Monthly_Balance",  
    "Amount_invested_monthly"
]
```

---
