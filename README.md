# Reddit Post Analyzer

The **Reddit Post Analyzer** is a data analysis and visualization tool designed to extract insights from Reddit posts. It helps analyze user engagement, sentiment, and trends across subreddits using Python and data science libraries.

## 🔎 Features

* Fetch Reddit posts and comments via Reddit API (PRAW).
* Analyze post metadata (upvotes, comments, awards, etc.).
* Sentiment analysis on post titles and comments.
* Time-based trend analysis (daily/weekly/monthly activity).
* Data visualization with charts and graphs.
* Export analysis results to CSV/Excel for further study.

## 🛠 Tech Stack

* **Language**: Python
* **Libraries**:

  * [PRAW](https://praw.readthedocs.io/) – Reddit API Wrapper
  * Pandas – Data manipulation
  * Matplotlib / Seaborn – Visualization
  * NLTK / TextBlob – Sentiment Analysis
  * NumPy – Numerical computations

## 🚀 How It Works

1. Authenticate using Reddit API credentials (client ID, secret, user agent).
2. Fetch Reddit posts from a given subreddit.
3. Process and analyze metadata (upvotes, comments, time trends).
4. Perform sentiment analysis on text content.
5. Generate charts and export results.

## 📂 Project Structure

```
├── data/                # Saved datasets and CSV exports  
├── notebooks/           # Jupyter notebooks for experiments  
├── scripts/             # Core Python scripts for fetching & analysis  
│   ├── fetch_posts.py  
│   ├── analyze_sentiment.py  
│   ├── visualize.py  
├── requirements.txt     # Dependencies  
├── config.py            # Reddit API credentials (to be added by user)  
├── main.py              # Main execution script  
└── README.md            # Documentation  
```

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/reddit-post-analyzer.git
   cd reddit-post-analyzer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your Reddit API credentials in `config.py`:

   ```python
   CLIENT_ID = "your_client_id"
   CLIENT_SECRET = "your_client_secret"
   USER_AGENT = "reddit_post_analyzer"
   ```

4. Run the analyzer:

   ```bash
   python main.py
   ```

## 📊 Example Outputs

### 🔼 Top Posts by Engagement

![Top Posts Screenshot](screenshots/top_posts.png)

### 😊 Sentiment Distribution

![Sentiment Chart](screenshots/sentiment_chart.png)

### 📈 Activity Trends Over Time

![Time Series Graph](screenshots/time_series.png)

### ☁️ Word Cloud of Frequent Terms

![Word Cloud](screenshots/wordcloud.png)

*(Replace the above with your actual generated outputs and save them under a `screenshots/` folder in your repo.)*

## ✅ Use Cases

* Track subreddit activity trends
* Research online communities
* Sentiment monitoring for brands/products
* Academic research on social media

## 📄 License

This project is licensed under the **MIT License**.

---

💡 *Contributions are welcome! Fork this repository, open issues, or submit pull requests to improve the project.*
