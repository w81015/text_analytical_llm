[中文版 Chinese version](README_zh.md)

# Text Analysis with Large Language Models

Text analysis with large language models is primarily implemented through OpenAI's API. It reads documents in `.docx` format, extracts the text from them, and uses OpenAI for further analysis.

## Installation

```bash
pip install openai python-dotenv python-docx re csv
```

## Setup

1. Add your OpenAI API key to a `.env` file:
```
OPENAI_API_KEY=your API key
```

2. Ensure documents in `.docx` format are available as input files.

## How to Use

Run `text_analysis.py`, making sure the document path is correctly set in the code.

```bash
python text_analysis.py
```

## Features

- **Read Document**: Extracts text from `.docx` files.
- **Text Analysis**: Performs text analysis using OpenAI's large language models.