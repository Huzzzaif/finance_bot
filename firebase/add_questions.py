from firebase_config import db

def add_question(question : str, answer:str):
    doc = {
        "question": question,
        "answer": answer
    }
    db.collection("knowledge_base").add(doc)
    print("Added question:" + {question})


if __name__ == "__main__":
    add_question("How can I start saving money?", "Start by creating a budget and setting aside money each month.")
    add_question("What is compound interest?", "Compound interest is interest calculated on both principal and accumulated interest.")