"""
Chunk documents

python -X utf8 chunker.py > chunks.json
"""

from uuid import uuid4
from glob import glob
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(file_paths):
    """Chunk documents into smaller pieces using the RecursiveCharacterTextSplitter.

    Args:
        file_paths (list): A list of file paths to the documents to be chunked.
    Yields:
        Document: A chunked document with unique ID and metadata.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=200,
        length_function=len,
        is_separator_regex=False,
    )

    for file_ in file_paths:
        with open(file_, encoding="utf-8") as infile:
            doc = infile.read()
            chunks = text_splitter.create_documents([doc])
            for idx, chunk in enumerate(chunks):
                chunk.id = uuid4().hex
                chunk.metadata = {"URI": file_, "chunk": idx}
                yield chunk


def main(doc_store):
    """
    Main function to process and chunk documents from the specified document store.

    Args:
        doc_store (str): The path to the document store containing text files.
    """

    file_paths = glob(f"{doc_store}/**/*.txt", recursive=True)

    for chunk in chunk_documents(file_paths):
        print(chunk.model_dump_json())


if __name__ == "__main__":
    main("C:\\Users\\sunki\\rag_app\\data")
