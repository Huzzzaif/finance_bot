#implement chromaDB
#for now it will just retrun somehting hardcoded
def retrieve_context(query: str, top_k: int =3):
    return[
        "Context string 1",
        "Context string 2",
        "Context string 3"
    ][::top_k]