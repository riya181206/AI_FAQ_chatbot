import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:

    def __init__(self, data_file="faq_data.json"):
        with open(data_file, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        self.questions = [faq["question"] for faq in self.faqs]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

    def get_answer(self, user_question):

        user_question = user_question.lower().strip()

        greetings = ["hi", "hello", "hey", "hii", "hola"]

        if user_question in greetings:
            return "Hello! 👋 How can I help you today?"

        user_vector = self.vectorizer.transform([user_question])

        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        best_match_index = similarities.argmax()
        best_score = similarities[best_match_index]

        if best_score < 0.20:
            return (
                "I'm currently designed to answer questions about "
                "our services, orders, payments, accounts, and support. "
                "Please try asking a related question."
            )

        return self.faqs[best_match_index]["answer"]