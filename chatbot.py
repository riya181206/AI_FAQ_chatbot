import json
from sentence_transformers import SentenceTransformer, util


class FAQChatbot:

    def __init__(self, data_file="faq_data.json"):
        with open(data_file, "r", encoding="utf-8") as file:
            self.faqs = json.load(file)

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.questions = [faq["question"] for faq in self.faqs]

        self.question_embeddings = self.model.encode(
            self.questions,
            convert_to_tensor=True
        )

    def get_answer(self, user_question):

        user_question = user_question.lower().strip()

        greetings = ["hi", "hello", "hey", "hii", "hola"]

        if user_question in greetings:
            return "Hello! 👋 How can I help you today?"

        user_embedding = self.model.encode(
            user_question,
            convert_to_tensor=True
        )

        similarities = util.cos_sim(
            user_embedding,
            self.question_embeddings
        )[0]

        best_match_index = int(similarities.argmax())
        best_score = float(similarities[best_match_index])

        if best_score < 0.40:
            return "I'm currently designed to answer questions about our services, orders, payments, accounts, and support. Please try asking a related question."

        return self.faqs[best_match_index]["answer"]
