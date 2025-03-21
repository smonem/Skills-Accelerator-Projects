# Capstone Project Report

## User Story 1: Cloud-Based Sentiment Analysis

### Task Definition: 

The objective of this prototype is to create a sentiment analysis tool that is able to classify customer reviews as being either positive or negative. An appropriate dataset for this fine-tuning task will include a large corpus of reviews and their associated scores. This tool can be applied for a wide variety of usages, such as assessing sentiment towards a brand and its products. 

### Data Collection & Preparation: 

The dataset used for this task consists of a large collection of customer reviews across different products, paired with their respective ratings. These ratings range from positive (5 stars) to negative (1 star), indicating user sentiment towards the product. Pre-processing steps included cleaning the data by removing any non-text elements such as URLs, special characters, and other irrelevant information. Ratings were converted to label comments as either positive (4 or above), neutral, or negative (2 or below) as appropriate. Other standard pre-processing steps such as splitting the data into training, validation, and test sets were performed before uploading the dataset.

### Model Development: 

The model selected for fine-tuning is a standard pre-trained transformer-based BERT model (bert-base-uncased) from Azure's catalog. Initially, the pre-trained model was loaded with its default weights, which were trained on a large corpus of text data. The fine-tuning process involved training the model on the prepared dataset, with the goal of adapting it to classify reviews based on sentiment. The model was trained using a supervised learning approach, where the inputs (reviews) were paired with their corresponding labels (positive or negative sentiment based on the rating). The learning rate was optimized to avoid overfitting, and a validation set was used to monitor the model’s performance during training. Hyperparameters such as batch size, epochs, and dropout rates were tuned based on the results from the validation phase. The model was trained until it demonstrated an acceptable level of accuracy.

### Testing and Optimization, Cloud Integration and Application Deployment:

Once the model was trained, its performance was evaluated using several key metrics to ensure it met the required standards for sentiment analysis. The primary evaluation metrics included accuracy, precision, recall, and F1 score. Accuracy was used to measure the overall correctness of the model's predictions, while precision, recall, and F1 score provided a more detailed understanding of the model's performance. The prototype was developed using Azure and tested via implementation in a simple application developed using Azure Prompt Flow, with the model being incorporated as the model node of the sentiment classifier.

## User Story 2: Document Summarization Service

### Task Definition: 

The objective of this prototype is to create a document summarization tool that efficiently generates concise and informative summaries of academic papers. Researchers can use this tool to extract key insights from lengthy research documents, helping them save time and focus on the most relevant information. The summarization should capture essential concepts while maintaining accuracy and coherence in the generated text.

### Data Collection & Preparation: 

The dataset used for this task consists of a collection of academic papers and their corresponding summaries. These documents were sourced from publicly available research databases, and the summaries were manually created by experts in the respective fields. Pre-processing steps included cleaning the data by removing non-relevant elements, such as references, which are not essential for summarization. The documents were processed in a standard way utilizing tokenization. The dataset was divided into training, validation, and test sets, in a way that ensured each set contained diverse academic papers from multiple disciplines for the robustness of the model.

### Model Development: 

The model selected for fine-tuning is a pre-trained transformer-based GPT language model from Azure's Model AI Catalog, suitable for text generation tasks. The fine-tuning process focused on training the model to produce coherent and relevant summaries from academic documents. During fine-tuning, the model was provided with the input text (academic papers) and the target output (summaries), with a supervised learning approach. Key considerations during the fine-tuning process included adjusting the model's learning rate to prevent overfitting, optimizing batch size, epochs, and the maximum length of summaries to ensure the generated output was both concise and informative. The training procedure also utilized a validation set to monitor the model’s performance and make adjustments as needed. Hyperparameters were tuned based on validation results to ensure that the model could handle varying document lengths and complexities.

### Testing and Optimization, Cloud Integration and Application Deployment:

Once the model was fine-tuned, the performance of the summarization was assessed using multiple metrics, including ROUGE scores, which measure the overlap between the generated summaries and the reference summaries. To ensure the model’s robustness, it was tested with a variety of academic papers across different fields of study, such as computer science, medicine, and social sciences. This helped assess the model's ability to generalize and provide accurate summaries regardless of the domain. The fine-tuned prototype model was deployed using Azure's services and tested via implementation in a simple application developed using Azure Prompt Flow, with the model being incorporated as the model node of the summarization application.

## User Story 3: Ethical NLP Implementation

To implement the solution of ensuring that NLP models deployed in the cloud are unbiased and meet ethical standards, the first step is to integrate bias-mitigation techniques during the development phase. This could include methods such as re-weighting the training data, using adversarial training, or implementing fairness constraints. Next, conducting comprehensive evaluations of the models involves assessing their performance across diverse demographic groups, identifying potential biases, and ensuring that they align with ethical guidelines. Even after deployment, regular audits and updates should be scheduled to monitor the model's behavior in production and make adjustments as needed. By following these practices, we can ensure that the NLP models remain trustworthy, fair, and aligned with ethical standards throughout their lifecycle in the cloud.