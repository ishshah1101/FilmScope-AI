import streamlit as st
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

indexName = "search"

try:
    es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("Isha", "Isha1111") 
    )
except ConnectionError as e:
    print("Connection Error:", e)
    
if es.ping():
    print("Succesfully connected to ElasticSearch!!")
else:
    print("Oops!! Can not connect to Elasticsearch!")

def search(input_keyword):
    model = SentenceTransformer('all-mpnet-base-v2')
    input_representation = model.encode(input_keyword)

    query = {
        "field": "SearchVector",
        "query_vector": input_representation,
        "k": 5,
        "num_candidates": 999
    }
    res = es.knn_search(index="search"
                        , knn=query 
                        , source=["Series_Title","Overview", "Genre", "Director"]
                        )
    results = res["hits"]["hits"]

    return results

def main():
    # Clear the default Streamlit background
    st.markdown(
        """
        <style>
            .stApp {
                background-color: black;
                font-family: Arial, sans-serif;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Film Feedback Analytics")

    # Input: User enters search query
    search_query = st.text_input("Enter your search query")

    # Button: User triggers the search
    if st.button("Search"):
        if search_query:
            # Perform the search and get results
            results = search(search_query)
 
            # Display search results
            st.subheader("Search Results")
            for result in results:
                with st.container():
                    if '_source' in result:
                        try:
                            st.header(f"{result['_source']['Series_Title']}")
                        except Exception as e:
                            print(e)
                        
                        try:
                            st.write(f"Genre: {result['_source']['Genre']}")
                        except Exception as e:
                            print(e)
                        try:
                            st.write(f"OverView: {result['_source']['Overview']}")
                        except Exception as e:
                            print(e)
                        try:
                            st.write(f"Director: {result['_source']['Director']}")
                        except Exception as e:
                            print(e)                                                        
                        st.divider()

if __name__ == "__main__":
    main()
