import sys
import os

# ✅ Add your project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from difflib import get_close_matches
from firebase.firebase_config import db


def get_answer_from_query(query:str) -> dict:
    #1.fetch all quetions and answers from firestore
    docs = db.collection("knowledge_base").stream()
    qa_pairs={}

    for doc in db.collection("knowledge_base").stream():
        data = doc.to_dict()
        print("📄 Firebase entry:", data)
    for doc in docs:
        data = doc.to_dict()
        question = data.get("question")
        print(question)
        answer = data.get("answer")
        print(answer)
        if question and answer:
            qa_pairs[question] = answer

    # try to find the closest matching pair
    all_questions = list(qa_pairs.keys())
    matches = get_close_matches(query, all_questions, n =1,cutoff=0.5)

    if matches:
        best_match = matches[0]
        return{
            "matched_question": best_match,
            "answer": qa_pairs[best_match]
        }
    else:
        return{
            "matched_question": None,
            "answer": "Sorry cannot find relevant answer"
        }