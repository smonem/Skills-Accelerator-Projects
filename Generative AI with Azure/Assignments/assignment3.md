# Assignment: Cloud-Based Fine-Tuning

### Part 1: Fundamentals of Fine-Tuning

**Application Task:**

1. Medical Question Answering
   - *Model: BioBERT (Biomedical BERT)*
     
     BioBERT is a variation of BERT trained on biomedical literature (such as PubMed abstracts), but fine-tuning it on a dataset of real patient queries and verified medical responses could ensure that it provides more precise, contextually relevant, and trustworthy answers for healthcare questions.

2. Sentiment Analysis for Customer Reviews
   - *Model: BERT*  
     
     While BERT is powerful in understanding language, fine-tuning it on a specific domain’s dataset (like tech products in different domains such as PC parts, phones, etc.) would allow it to capture industry-specific sentiments and jargon, improving classification accuracy for reviews.

3. Exam Success Prediction
   - *Model: XGBoost (Gradient Boosting for Tabular Data)*

     XGBoost is a highly efficient and performant decision-tree-based model, effective for structured data tasks. Fine-tuning it on a dataset of student study patterns, past exam scores, and other academic indicators would optimize its hyperparameters for better predictive performance in determining the likelihood of passing an exam.

### Part 2: Implementing Fine-Tuning on Azure

**Case Study Activity:**

Task: Healthcare Chatbot
Model: GPT-4

1. Dataset:

I would use a dataset comprising diverse and high-quality medical texts, including publicly available medical literature, trusted healthcare websites (such as CDC and WHO), anonymized patient interactions, and curated question-answer pairs from medical professionals. The ideal dataset would cover a wide range of health topics, including symptoms, diseases, medications, preventive care, and emergency guidance while ensuring alignment with ethical and legal standards. To prepare the dataset, I would clean and preprocess the text by removing any personally identifiable information if necessary. Next I would structure the data into a format suitable for training, which includes tokenization and labeling.

2. Evaluation

After fine-tuning the healthcare chatbot model, I would evaluate its performance using a combination of quantitative and qualitative metrics. Quantitative evaluation would involve accuracy measures such as precision, recall, and F1-score, especially for tasks like symptom classification and medication recommendations. For example, I would measure how accurately the model identifies specific conditions based on user inputs. Additionally, more complex metrics such as perplexity and BLEU scores could be used to assess the quality of generated responses, particularly when the chatbot is tasked with answering open-ended questions. However, the real challenge lies in evaluating the model's ability to provide medically accurate and ethical responses in a real world setting. Therefore, expert evaluation from healthcare professionals would be a neccessary step. I would also rely on user satisfaction to gauge the chatbot's overall effectiveness from a patient perspective. Another important metric would be response appropriateness, ensuring that the model adheres to medical guidelines and does not offer harmful or misleading advice. Challenges may include the complexity of handling edge cases, like rare conditions or complex medical scenarios, where the chatbot’s responses might be less reliable. Additionally, continuously ensuring that the model stays updated with the latest medical knowledge and adheres to privacy regulations would be an ongoing issue.

### Part 3: Evaluating and Deploying Models

**Reflection Activity:**

Evaluating a fine-tuned model using metrics like F1-Score and cross-validation is crucial for ensuring its reliability and effectiveness. F1-Score, which balances precision and recall, is particularly useful in cases where class imbalance (such as is common in medicine) exists, preventing misleading accuracy results. Cross-validation helps assess the model’s generalizability by training and testing it on different subsets of data, reducing the risk of overfitting. Without proper evaluation, a model may appear to perform well on training data but fail in real-world applications. For example, in a healthcare ML model predicting disease risk, skipping F1-Score analysis could lead to high accuracy but poor recall, missing critical diagnoses. Similarly, neglecting cross-validation might result in a model that performs well on a specific dataset but generalizes poorly to new patient records. Poor evaluation can lead to biased, unreliable predictions, ultimately reducing trust in the system and causing potential harm in decision-making processes.
