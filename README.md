Project Overview
This project investigates how increasing the symbolic complexity of mathematical equations affects the accuracy of large language models (LLMs).

Our main research question is:

Does increasing the symbolic complexity of an equation reduce the accuracy of LLMs when solving mathematically equivalent or structurally similar problems?

We expect model accuracy to decrease as equations become more complex, even when the underlying mathematical concepts remain the same.

Dataset
We plan to use approximately 50–75 algebra problems from the MATH dataset introduced by Hendrycks et al. (2021).

The MATH dataset contains competition-level mathematics problems with solutions and difficulty ratings. We will focus on its algebra category.

Dataset: MATH – Hugging Face
Category: Algebra
Training problems available: 1,744
Testing problems available: 1,187
Planned Models
We plan to evaluate two open-weight language models:

Qwen2.5-Math-7B-Instruct: A model designed for mathematical reasoning.
Llama 3.1 8B Instruct: A general-purpose language model.
Methodology
Our project will involve the following steps:

Select approximately 50–75 algebra problems from the MATH dataset.
Divide the original problems into development (20%), validation (20%), and test (60%) sets.
Generate increasingly complex variations of the selected problems while preserving their underlying mathematical structure.
Use Python and SymPy to verify mathematical validity and correct answers.
Evaluate both language models on the original problems and modified variations.
Compare model accuracy across different complexity levels.
Evaluation
Our primary evaluation metric will be accuracy, measured as the percentage of correctly solved problems at each complexity level.

We will compare the performance of both models and investigate which mathematical modifications cause the largest decreases in accuracy.

Technologies
Python
Hugging Face Datasets
Hugging Face Transformers
PyTorch
SymPy
Pandas
Google Colab
