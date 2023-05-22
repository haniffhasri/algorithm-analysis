from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load pre-trained BERT model with a classification head
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

# Pre-process new review text
new_review_text = "This product was amazing! I would highly recommend it."

inputs = tokenizer.encode_plus(new_review_text, add_special_tokens=True, return_tensors="pt")

# Pass the pre-processed input through the fine-tuned model to obtain the predicted sentiment
outputs = model(**inputs)
predicted_sentiment = "Positive" if outputs.logits.argmax().item() == 1 else "Negative"

print(f"The predicted sentiment of the review '{new_review_text}' is '{predicted_sentiment}'.")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
