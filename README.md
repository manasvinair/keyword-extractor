# YouTube Keyword Extractor

A simple Streamlit web app that extracts keywords (tags) from a YouTube video URL using web scraping.

## Features

- Extracts keywords (tags) from the `<meta name="keywords">` tag of a YouTube video page.
- Displays the video title and its corresponding tags in a clean interface.

## Requirements

Install the required Python libraries before running the app:

```bash
pip install streamlit beautifulsoup4 requests lxml
```

## How to Run

Run the Streamlit app with:

```bash
streamlit run keyword-extractor.py
```

## Usage

1. Open the app in your browser.
2. Enter the URL of a YouTube video.
3. The app will display:
   - The video’s title.
   - A list of tags (keywords) extracted from the video.

## Note

This app scrapes data directly from the YouTube video’s HTML meta tags. If YouTube changes its structure or restricts access, the functionality may break.
