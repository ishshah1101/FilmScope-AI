IndexMapping = {
    "properties": {
        "Series_Title": {
            "type": "text"
        },
        "Released_Year": {
            "type": "text"
        },
        "Certificate": {
            "type": "text"
        },
        "Runtime": {
            "type": "text"
        },
        "Genre": {
            "type": "text"
        },
        "IMDB_Rating": {
            "type": "double"
        },
        "Overview": {
            "type": "text"
        },
        "Director": {
            "type": "text"
        },
        "SearchVector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "cosine"
        }
    }
}
