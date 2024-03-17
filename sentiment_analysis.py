from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import spacy
import pandas as pd

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load the dataset
def load_dataset(file_path):
    """
    Load the Amazon product reviews dataset from the specified file path.
    Args:
        file_path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    dataframe = pd.read_csv(file_path)
    return dataframe

# Preprocess text data
def preprocess_text(text):
    """
    Preprocess text by tokenizing, removing stopwords, and lemmatizing.
    Args:
        text (str): Input text.
    Returns:
        str: Processed text.
    """
    doc = nlp(text.lower())  # Normalize text to lowercase
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

# Define sentiment analysis function with threshold parameter
def predict_sentiment(review, threshold=0.1):
    """
    Predict sentiment (positive, negative, or neutral) based on SpaCy's sentiment analysis.
    Args:
        review (str): Input review text.
        threshold (float): Polarity threshold for classification.
    Returns:
        str: Predicted sentiment label.
    """
    doc = nlp(review)
    sentiment_score = doc.sentiment
    polarity = sentiment_score[0] if isinstance(sentiment_score, tuple) else sentiment_score
    if polarity > threshold:
        return 'Positive'
    elif polarity < -threshold:
        return 'Negative'
    else:
        return 'Neutral'

# Main function
def main():
    # Add the file path of the Amazon product reviews dataset
    file_path = r"C:/Users/lambe\Documents/amazon_product_reviews.csv"
    # Change this to the actual file path

    # Load dataset
    dataframe = load_dataset(file_path)

    # Preprocess the 'review.text' column
    reviews_data = dataframe['reviews.text'].dropna()
    clean_data = reviews_data.apply(preprocess_text)

    # Test the sentiment analysis function on sample reviews
    sample_reviews = ["Well they are not Duracell but for the price i am happy.",
                    "they seemed to not last as long as other name brand names disappointed!",
                    "Bulk is always the less expensive way to go for products like these"]
    predicted_sentiments = []
    for review in sample_reviews:
        sentiment = predict_sentiment(review, threshold=0.2)  # Adjust threshold here
        predicted_sentiments.append(sentiment)
        print(f"Review: {review} | Predicted Sentiment: {sentiment}")

    # Write summary report
    with open("sentiment_analysis_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write("Sentiment Analysis Report\n\n")
        report_file.write("Dataset Description:\n")
        report_file.write("\nThis dataset contains product reviews from Amazon. It consists of various products across different categories and includes textual reviews provided by users along with corresponding ratings.\n")

        report_file.write("\n\nDetails of Preprocessing Steps:\n")
        report_file.write("\nThe preprocessing steps include tokenization, stop word removal, and lemmatization. Each review text is normalized to lowercase, tokenized into words, and then stop words are removed. Finally, the remaining words are lemmatized to their base form.\n")

        report_file.write("\n\nEvaluation of Results:\n")
        report_file.write("\nThe sentiment analysis model was tested on a sample of product reviews. However, all sentiments were classified as 'Neutral', indicating that the model may not be accurately capturing the polarity of the reviews. Further investigation is required to improve model performance.\n")

        report_file.write("\n\nInsights into Model's Strengths and Limitations:\n")
        report_file.write("\nThe model's strength lies in its simplicity and ease of use. It leverages SpaCy's pre-trained model for natural language processing tasks, making it suitable for quick sentiment analysis tasks.\n\nHowever, the model's limitation is evident in its inability to accurately classify sentiments in the given dataset. This may be due to the dataset's characteristics or the model's lack of fine-tuning specifically for sentiment analysis tasks.\n")

    # Generate PDF report
    create_report("sentiment_analysis_report.pdf", "This dataset contains product reviews from Amazon. It consists of various products across different categories and includes textual reviews provided by users along with corresponding ratings.", "The preprocessing steps include tokenization, stop word removal, and lemmatization. Each review text is normalized to lowercase, tokenized into words, and then stop words are removed. Finally, the remaining words are lemmatized to their base form.", "The sentiment analysis model was tested on a sample of product reviews. However, all sentiments were classified as 'Neutral', indicating that the model may not be accurately capturing the polarity of the reviews. Further investigation is required to improve model performance.", "The model's strength lies in its simplicity and ease of use. It leverages SpaCy's pre-trained model for natural language processing tasks, making it suitable for quick sentiment analysis tasks. However, the model's limitation is evident in its inability to accurately classify sentiments in the given dataset. This may be due to the dataset's characteristics or the model's lack of fine-tuning specifically for sentiment analysis tasks.")

def create_report(file_path, dataset_description, preprocessing_details, evaluation_results, model_insights):
    doc = SimpleDocTemplate(file_path, pagesize=letter)
    styles = getSampleStyleSheet()
    style_heading = styles['Heading1']
    style_body = styles['BodyText']

    report_content = []

    # Add heading
    report_content.append(Paragraph("Sentiment Analysis Report", style_heading))
    report_content.append(Spacer(1, 12))

    # Add dataset description
    report_content.append(Paragraph("Dataset Description:", style_heading))
    report_content.append(Paragraph(dataset_description, style_body))
    report_content.append(Spacer(1, 12))

    # Add preprocessing details
    report_content.append(Paragraph("Details of Preprocessing Steps:", style_heading))
    report_content.append(Paragraph(preprocessing_details, style_body))
    report_content.append(Spacer(1, 12))

    # Add evaluation results
    report_content.append(Paragraph("Evaluation of Results:", style_heading))
    report_content.append(Paragraph(evaluation_results, style_body))
    report_content.append(Spacer(1, 12))

    # Add model insights
    report_content.append(Paragraph("Insights into Model's Strengths and Limitations:", style_heading))
    report_content.append(Paragraph(model_insights, style_body))

    # Build and save the PDF report
    doc.build(report_content)

# Run the main function
if __name__ == "__main__":
    main()
