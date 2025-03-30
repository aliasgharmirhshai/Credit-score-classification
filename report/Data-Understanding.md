
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

## 2. Handling Missing Data

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
  ["Monthly_Inhand_Salary"
  "Type_of_Loan"
  "Num_of_Delayed_Payment"
  "Num_Credit_Inquiries"
  "Credit_History_Age"
  "Amount_invested_monthly"
  "Monthly_Balance"]
    ```
---

## 3. Correct Data Types

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

## 4. Clean Categorical Columns

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
