# SemEval-2022 Task 4: Patronizing and Condescending Language Detection

This repository contains code and resources for detecting patronizing and condescending language (PCL) in text. The task was part of the SemEval 2022 competition (Task 4, Subtask 1). The objective is to build a binary classification model that predicts whether a given text contains PCL, surpassing the RoBERTa-base baseline model, which achieved an F1 score of 0.48 on the dev set and 0.49 on the test set.

This project was developed as part of NLP coursework at Imperial College London, achieved high score of 93 out of 100.

## Project Objective
Our primary aim is to improve upon the baseline with an F1 score higher than 0.48 using various models, data pre-processing, augmentation strategies, and hyperparameter tuning techniques. This project focuses on deploying machine learning models like BoW, TF-IDF, RoBERTa, and DeBERTa.

## Dataset
The dataset used is the **Don't Patronize Me!** dataset, which includes over 10,000 paragraphs from English news articles across 20 countries. Each paragraph is annotated with a binary label:
- `0`: No PCL
- `1`: PCL present

The dataset poses challenges due to a significant class imbalance (90.5% non-PCL vs. 9.5% PCL). Vulnerable communities mentioned include migrants, women, disabled individuals, and more.

## Structure of the Repository

### 1. Main Notebook
- **Purpose**: Train the best model (DeBERTa, BoW, TF-IDF) on the dataset and generate predictions for the dev and test sets.
- **Focus**: Covers coursework questions 2.a, 2.b, and 2.d.

### 2. Pre-Processing Notebook
- **Purpose**: Clean, tokenize, and extract features from the dataset while training models with various pre-processing techniques.
- **Focus**: Addresses coursework questions 2.c and 2.d.

### 3. Pre-Processing Script (`pre-process.py`)
- **Purpose**: Implements an alternative pre-processing strategy for experimentation.
- **Focus**: Supports pre-processing explorations for questions 2.c and 2.d.

### 4. Augmentation Notebook
- **Purpose**: Apply data augmentation techniques to increase dataset variability and improve model generalization.
- **Focus**: Related to questions 2.c and 2.d.

### 5. Sampling Notebook
- **Purpose**: Handle class imbalance through various sampling strategies (e.g., upsampling, downsampling).
- **Focus**: Supports question 2.c and 2.d.

### 6. Hypertuning Notebook
- **Purpose**: Perform hyperparameter tuning to optimize model performance.
- **Focus**: Addresses question 2.e.

### 7. Analysis Notebook
- **Purpose**: Analyze model performance and answer analytical questions.
- **Focus**: Provides insights for question 3.

### 8. Q1 Notebook
- **Purpose**: Dedicated notebook for addressing the first question in the coursework.
- **Focus**: Focuses on question 1.

### 9. Scheduler Notebook
- **Purpose**: Implements a learning rate scheduler to evaluate its impact on model performance.
- **Focus**: Covers question 2.b, experimenting with scheduling strategies.

## Results
Our final model (DeBERTa) achieved an F1 score of **0.58** on the development set, outperforming the RoBERTa baseline.

| Model                    | F1 Score (Dev Set) |
|--------------------------|--------------------|
| BoW Baseline              | 0.287              |
| TF-IDF Baseline           | 0.302              |
| RoBERTa (Baseline)        | 0.48               |
| **DeBERTa**               | **0.58**           |

## Analysis
1. **Effectiveness in Detecting High PCL Content**: The model performs best on paragraphs with explicit patronizing content (F1 score: 0.82).
2. **Impact of Text Length**: Medium-length paragraphs (500-800 characters) achieve the best performance with an F1 score of 0.72.
3. **Category-Based Performance**: The model performs best in the "disabled" category (F1 score: 0.61) and struggles with "migrant" and "women" categories.

## Report
For a detailed explanation of our methodology, model performance, and analysis, refer to the [final report](https://github.com/kyrran/NLP_DONT_Patronize_Me/blob/main/report%20(1).pdf).

## References
- [SemEval 2022 Task 4](https://sites.google.com/view/pcl-detection-semeval2022/)
- [Don't Patronize Me! Dataset](https://github.com/CRLala/NLPLabs-2024/tree/main/Dont_Patronize_Me_Trainingset)
- Almendros, C. P., et al. (2020). Don’t Patronize Me! An Annotated Dataset with Patronizing and Condescending Language Towards Vulnerable Communities. *28th International Conference on Computational Linguistics*.

## Equal Contributors
- **Michael Hollins**  
- **Vinayak Modi**  
- **Kangle Yuan**

