# 📌 Prompt Collection for Credit Scoring Project

## Overview
This section contains **structured prompts** used in this project for various tasks, including understanding methodologies, generating code, and analyzing data. The goal is to document effective prompts for reproducibility and optimization when working with **LLMs** such as GPT-4 (ChatGPT) and Claude 3.7.

By maintaining a structured prompt repository, we ensure:  
- **Consistency** in interacting with LLMs.  
- **Efficiency** by reusing well-crafted prompts.  
- **Transparency** in how AI contributes to different phases of the project.  

---

## 📖 1. Understanding Methodologies & Planning (GPT-4)
### Purpose  
This section includes prompts used to **understand concepts, methodologies, and strategies** related to credit risk modeling. Since GPT-4 (ChatGPT) is being used, prompts in this section focus on:  
- Data understanding and feature engineering.  
- Model selection and evaluation strategies.  
- Business logic and compliance considerations.  

### Example Prompts  
**📌 Understanding Credit Score Features**  

---

## 💻 2. Code Generation & Implementation (Claude 3.7)
### Purpose  
This section contains prompts used to **generate and refine code**. Since **Claude 3.7** is preferred for code-related tasks, the prompts in this section focus on:  
- Data preprocessing & cleaning scripts.  
- Model training and evaluation.  
- API and system integration code.  

#### Data Understanding
Using this command, I generate small codes where performance is not important, and they are intended solely for use in a notebook to understand the data.

```
Project: Credit Scoring Analysis  
Stage: Data Understanding (Stage 2 of CRISP-DM)  

Task:  
I am working on the Data Understanding phase of my credit scoring project. I need a simple Python script to explore the dataset stored in the `"data/"` folder.  

### Requirements:
- Load the dataset using pandas.
- Display basic descriptive statistics (e.g., `.describe()` for numerical columns).
- Plot histograms for key numerical features to analyze distributions.
- Handle missing values by showing the count of missing entries per column.

### Custom Section (Do Not Generate Full Script)  
Now, I need a **specific piece of code** to do the following:  
**[INSERT YOUR REQUEST HERE]**  
Make sure to provide only that specific code snippet and not the full exploratory script.  

Performance is not important; the goal is to **test and explore**. Add necessary comments for clarity.


```

### Example Prompts  
**📌 Data Cleaning Script**  
**📌 Model Training Code**  
**📌 API Endpoint for Predictions**  

---

## 🔄 Contribution & Updates
- This section will be updated as new LLM-based strategies and optimizations are tested.
- If an interesting approach emerges from a prompt, it will be documented for future use.
