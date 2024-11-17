from langchain_community.vectorstores import FAISS
from embeddings import _embedding_model

VECTOR_DB = None

def init_index():
    global VECTOR_DB
    VECTOR_DB = FAISS.load_local(
    "index/faiss", _embedding_model(), allow_dangerous_deserialization=True
)


def query_index(query, k=3):
    results = VECTOR_DB.similarity_search_with_score(
    query, k=k
    )

    return results