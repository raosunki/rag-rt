$ java -version
java version "20.0.2" 2023-07-18
Java(TM) SE Runtime Environment (build 20.0.2+9-78)
Java HotSpot(TM) 64-Bit Server VM (build 20.0.2+9-78, mixed mode, sharing)


$ java -jar tika\tika-app-3.0.0.jar -i data -o data -t
$ python -X utf8 chunker.py > chunks.jsonl
$ python faiss_index.py
$ streamlit run app.py
