"""
Index documents.
"""

import os
import json
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from tqdm import tqdm
from embeddings import _embedding_model


def _vector_size():
    """Get length of embedding"""
    return len(_embedding_model().embed_query("faiss index"))


def build_faiss_index(chunks_file_path, index_path):
    """Build faiss index"""
    faiss_index = faiss.IndexFlatL2(_vector_size())

    vector_store = FAISS(
        embedding_function=_embedding_model(),
        index=faiss_index,
        docstore=InMemoryDocstore(),
        index_to_docstore_id={},
    )

    docs = []
    with open(chunks_file_path, encoding="utf-8") as infile:
        for rec in infile:
            rec = json.loads(rec)
            rec.pop("type")
            doc = Document(**rec)
            docs.append(doc)

    for doc in tqdm(docs):
        vector_store.add_documents(documents=[doc])

    faiss_index_path = os.path.join(index_path, "faiss")
    vector_store.save_local(faiss_index_path)
    return faiss_index_path


if __name__ == "__main__":
    build_faiss_index("chunks.jsonl", "./index")
