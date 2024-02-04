
# Text Analysis with Large Language Models

利用大型語言模型進行文本分析，主要通過OpenAI的API實現。它讀取`.docx`格式的文件，從中提取文本，並使用OpenAI進行進一步的分析。

## 安裝

```bash
pip install openai python-dotenv python-docx re csv
```

## 設置

1. 將OpenAI API鍵添加到`.env`文件中：
```
OPENAI_API_KEY=您的API鍵
```

2. 確保`.docx`格式的文檔作為輸入文件。

## 使用方法

運行`text_analysis.py`，確保文檔路徑已正確設置於程式碼中。

```bash
python text_analysis.py
```

## 功能

- **讀取文檔**：從`.docx`文件中提取文本。
- **文本分析**：使用OpenAI的大型語言模型進行文本分析。
