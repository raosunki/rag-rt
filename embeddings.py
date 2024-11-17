"""
Generate embeddings using sequence transformers from HuggingFace.
"""

from langchain_huggingface import HuggingFaceEmbeddings


def _embedding_model(model_name=None):
    if model_name is None:
        model_name = "all-MiniLM-L6-v2"
        # model_name="NeuML/pubmedbert-base-embeddings"

    return HuggingFaceEmbeddings(model_name=model_name)


if __name__ == "__main__":
    documents = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        "Duis aute irure dolor in reprehenderit in voluptate",
        "Excepteur sint occaecat cupidatat non proident",
    ]

    embeddings = _embedding_model().embed_documents(documents)

    for i, embedding in enumerate(embeddings):
        print(i, len(embedding), embedding)
        print()
