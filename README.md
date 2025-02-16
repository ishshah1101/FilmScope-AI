# SentimentXpert

# 🎬 IMDb Search Engine

![IMDb Search](https://img.shields.io/badge/IMDb-Search-yellow?style=for-the-badge&logo=imdb)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.x-005571?style=for-the-badge&logo=elasticsearch)

Discover the magic of cinema with our IMDb Search Engine! 🍿✨

## 🚀 Features

- 🔍 Search through IMDb's top 1000 movies
- 📊 Utilize Elasticsearch for lightning-fast queries
- 🧠 Leverage semantic search with sentence embeddings
- 🖥️ User-friendly Streamlit interface

## 🛠️ Installation

1. Clone this repository:
git clone https://github.com/yourusername/imdb-search-engine.git
cd imdb-search-engine



2. Install dependencies:
pip install -r requirements.txt


3. Download and install [Elasticsearch](https://www.elastic.co/downloads/elasticsearch)

## 🏗️ Setup

1. Start Elasticsearch:
./elasticsearch


2. Index the IMDb dataset:
python index_data.py


3. Launch the Streamlit app:
streamlit run search_app.py


## 🎭 Usage

1. Enter your movie search query
2. Click the "Search" button
3. Explore the results and discover new films!

## 🗺️ Project Structure
```
imdb-search-engine/
│
├── data/
│ └── imdb_top_1000.csv
│
├── src/
│ ├── index_data.py
│ ├── index_mapping.py
│ └── search_app.py
│
├── requirements.txt
└── README.md
```


## 🛣️ Roadmap

- [ ] Add advanced filtering options
- [ ] Implement personalized recommendations
- [ ] Integrate with external APIs for additional movie data

## 🤝 Contributing

"While this is a personal project, contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository

Create a new branch

Make your changes

Submit a pull request

For major changes, please open an issue first to discuss what you would like to change."

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- IMDb for the incredible movie dataset
- Elasticsearch team for their powerful search engine
- Streamlit for making web apps a breeze

---

<p align="center">
  Made with ❤️ by cinema enthusiast, for cinema enthusiasts
</p>
