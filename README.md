# Credit score classification

---

## Business Understanding Report 

#### Project Overview
The goal of this project is to **develop a machine learning model that classifies customers as either low-risk or high-risk borrowers**. This model will leverage historical credit data, income information, and past loan performance to assist financial institutions in making informed lending decisions.

#### Business Objectives
- **Primary Objective:**  
  Develop a predictive model that accurately identifies whether a customer is a low-risk or high-risk borrower.

- **Secondary Objectives:**  
  - Improve loan approval processes.  
  - Reduce the rate of defaults by flagging high-risk applicants.  
  - Offer more favorable terms to low-risk borrowers.

#### Data Overview
The dataset contains a variety of features that shed light on a customer's financial behavior and credit history. Key fields include:

- **Personal & Identification:**  
  - `ID`, `Customer_ID`, `Name`, `Age`, `SSN`, `Occupation`

- **Income & Financial Details:**  
  - `Annual_Income`, `Monthly_Inhand_Salary`, `Monthly_Balance`, `Amount_invested_monthly`

- **Credit & Loan Information:**  
  - `Num_Bank_Accounts`, `Num_Credit_Card`, `Num_of_Loan`, `Type_of_Loan`, `Credit_Score`

- **Loan Performance & Credit Behavior:**  
  - `Interest_Rate`, `Delay_from_due_date`, `Num_of_Delayed_Payment`, `Changed_Credit_Limit`, `Num_Credit_Inquiries`  
  - `Credit_Mix`, `Outstanding_Debt`, `Credit_Utilization_Ratio`, `Credit_History_Age`, `Payment_of_Min_Amount`, `Total_EMI_per_month`, `Payment_Behaviour`

#### Stakeholders
- **Financial Institutions:**  
  Banks and lending organizations that require robust risk assessment models to mitigate default risks.

- **Customers:**  
  Individuals seeking fair and transparent evaluations for credit applications.

- **Regulatory Authorities:**  
  Entities ensuring compliance with fair lending practices and data privacy laws.

- **Data Science & IT Teams:**  
  Responsible for model development, deployment, and integration into existing systems.

#### Success Criteria
- **Accuracy and Reliability:**  
  - High classification performance (e.g., F1-Score ≥ 85%, Precision & Recall > 80%).

- **Risk Minimization:**  
  - Reduced false positives and negatives to avoid misclassifying credit risk.

- **Model Fairness:**  
  - Ensuring the model does not introduce bias, especially regarding sensitive attributes such as age, occupation, or income.

- **Operational Efficiency:**  
  - Seamless integration with existing IT infrastructure for real-time or batch processing.

#### Business Constraints
- **Data Quality:**  
  - Potential issues like missing or inconsistent records need to be addressed during data preparation.

- **Regulatory Compliance:**  
  - The model must adhere to data privacy (e.g., GDPR) and fair lending regulations.

- **Integration Considerations:**  
  - The solution should work within the constraints of existing IT systems and operational workflows.
