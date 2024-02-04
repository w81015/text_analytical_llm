import openai
import docx
import re
import csv
from dotenv import load_dotenv
import os

# 加載環境變數並設置API
def set_api_key():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = api_key

# 讀取文件內容
def read_file(file_path):
    try:
        doc = docx.Document(file_path)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        return '\n'.join(fullText)
    except Exception as e:
        return str(e)

# 處理發送到OpenAI的請求
def process_openai_request(essay_text, criterion_text):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": f"你是一位助理，專門批改高中生的文學評論文。請根據以下評分標準評分和評論：{criterion_text}。回覆的字數不能超過150字。"},
            {"role": "user", "content": f"請批改這篇由高中生撰寫的文學評論文：{essay_text}。回覆的字數不能超過150字。"}
        ]
    )
    return response

# 計算分數和提取反饋
def calculate_scores_and_feedback(response):
    ai_response = response['choices'][0]['message']['content']
    match = re.search(r'(\d+)(分)?', ai_response)
    if match:
        score = match.group(1)
        feedback = ai_response[match.end():].strip()
    else:
        score = "未提供"
        feedback = ai_response
    return score, feedback

# 將結果保存到CSV檔
def save_results_to_csv(file_path, total_score, results):
    csv_file_path = r'____'  # 提供儲存位置
    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['File Name', 'Total Score', 'Criterion', 'Score', 'Feedback'])
        writer.writerow([os.path.basename(file_path), total_score])
        for result in results:
            writer.writerow(['', '', result[0], result[1], result[2]])

# 主程式
def main():
    set_api_key()
    file_path_essay = r"____"  # 提供文本位置
    essay_text = read_file(file_path_essay)

    total_score = 0
    results = []

    # 讀取評分標準、計算得分
    for i in ['a', 'b', 'c', 'd']:
        file_path_criterion = f"____"  # 提供評分標準
        criterion_text = read_file(file_path_criterion)

        response = process_openai_request(essay_text, criterion_text)
        score, feedback = calculate_scores_and_feedback(response)

        total_score += int(score) if score.isdigit() else 0
        results.append((i, score, feedback))

        print(f"評分標準 {i}：")
        print(f"分數：{score}")
        print(feedback)

    print(f"總分：{total_score}")
    save_results_to_csv(file_path_essay, total_score, results)

if __name__ == "__main__":
    main()
