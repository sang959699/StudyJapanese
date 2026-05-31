# -*- coding: utf-8 -*-
import os
import re
import json
import random

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB_FILE = os.path.join(WORKSPACE_DIR, "3_N2_Vocabulary_Bank_and_Verbs.md")
OUTPUT_FILE = os.path.join(WORKSPACE_DIR, "questions.js")

def clean_markdown_formatting(text):
    """移除 markdown 中的粗體、連結等格式，只保留純文字"""
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'<br\s*/?>', ' ', text)
    return text.strip()

def parse_priority_and_word(col_text):
    """解析第一欄，提取重要度標記（🔴/🟡/🟢）與單詞"""
    col_text = col_text.strip()
    priority = "🟢"
    for p in ["🔴", "🟡", "🟢"]:
        if p in col_text:
            priority = p
            col_text = col_text.replace(p, "").strip()
            break
    # 移除 **粗體** 標記
    word = clean_markdown_formatting(col_text)
    return priority, word

def parse_parenthesis_reading(word_text):
    """解析如 '入る（はいる）' 形式的單詞與讀音"""
    m = re.match(r'^([^\uff08\(\s]+)[\uff08\(]([^\uff09\)\s]+)[\uff09\)]$', word_text.strip())
    if m:
        return m.group(1), m.group(2)
    return word_text.strip(), ""

def extract_example_sentences(details_text, keyword):
    """從記憶要點中提取例句，並用（　　）替換關鍵詞做成填空題"""
    details_text = clean_markdown_formatting(details_text)
    # 尋找包含括號或例句標識的句子
    # 如：'態度を改める（端正態度）' -> 例句為 '態度を改める'
    # 或者 '会議が長引く（會議開得很長/拖拉）' -> '会議が長引く'
    sentences = []
    
    # 匹配 如 'A（B） / C' 格式中的日文句子
    parts = re.split(r'[/／;；]', details_text)
    for part in parts:
        part = part.strip()
        # 尋找日文部分
        m = re.match(r'^([a-zA-Z0-9\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf\u3000-\u303f\uff01-\uff5e]+)[\uff08\(]([^\uff09\)]+)[\uff09\)]', part)
        if m:
            sentence = m.group(1).strip()
            meaning = m.group(2).strip()
            if keyword in sentence and len(sentence) > len(keyword):
                sentences.append((sentence, meaning))
        elif keyword in part and len(part) > len(keyword):
            # 如果沒有括號但包含關鍵字且長度大於關鍵字
            sentences.append((part, ""))
            
    return sentences

def main():
    if not os.path.exists(VOCAB_FILE):
        print(f"Error: {VOCAB_FILE} not found!")
        return

    print("Parsing vocabulary notes...")
    vocab_items = []
    自他_items = []

    with open(VOCAB_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_section = ""
    for line in lines:
        line_strip = line.strip()
        if line_strip.startswith("##") or line_strip.startswith("###"):
            current_section = line_strip
            continue

        if not line_strip.startswith("|"):
            continue

        # 分割表格行
        cols = [c.strip() for c in line_strip.split("|")][1:-1]
        if not cols:
            continue

        # 跳過表頭與分隔線
        if "自動詞" in cols[0] or "漢字" in cols[0] or cols[0].startswith(":---") or cols[0].startswith("---"):
            continue

        # 1. 解析自他動詞對整理 (3個欄位)
        if len(cols) == 3:
            raw_auto, raw_trans, details = cols
            p_auto, word_auto_full = parse_priority_and_word(raw_auto)
            p_trans, word_trans_full = parse_priority_and_word(raw_trans)
            
            auto_kanji, auto_reading = parse_parenthesis_reading(word_auto_full)
            trans_kanji, trans_reading = parse_parenthesis_reading(word_trans_full)
            
            details_clean = clean_markdown_formatting(details)
            
            自他_items.append({
                "priority": p_auto,
                "auto_kanji": auto_kanji,
                "auto_reading": auto_reading,
                "trans_kanji": trans_kanji,
                "trans_reading": trans_reading,
                "details": details_clean
            })

        # 2. 解析普通詞彙表 (4個欄位)
        elif len(cols) == 4:
            raw_kanji, raw_reading, raw_meaning, details = cols
            priority, kanji = parse_priority_and_word(raw_kanji)
            reading = clean_markdown_formatting(raw_reading)
            meaning = clean_markdown_formatting(raw_meaning)
            
            vocab_items.append({
                "priority": priority,
                "kanji": kanji,
                "reading": reading,
                "meaning": meaning,
                "details": details
            })

    print(f"Extracted {len(自他_items)} transitive/intransitive verb pairs.")
    print(f"Extracted {len(vocab_items)} vocabulary items.")

    # 開始生成題目
    questions = []

    # 所有讀音與中文釋義的集合，用來做錯誤選項的干擾項
    all_readings = list(set([item["reading"] for item in vocab_items if item["reading"]]))
    all_meanings = list(set([item["meaning"] for item in vocab_items if item["meaning"]]))
    all_auto_kanji = list(set([item["auto_kanji"] for item in 自他_items if item["auto_kanji"]]))
    all_trans_kanji = list(set([item["trans_kanji"] for item in 自他_items if item["trans_kanji"]]))

    # --- 生成普通單詞題 ---
    for item in vocab_items:
        kanji = item["kanji"]
        reading = item["reading"]
        meaning = item["meaning"]
        priority = item["priority"]
        details = clean_markdown_formatting(item["details"])

        # 題型一：漢字 ➔ 讀音
        if kanji and reading:
            distractors = random.sample([r for r in all_readings if r != reading], min(3, len(all_readings) - 1))
            options = distractors + [reading]
            random.shuffle(options)
            questions.append({
                "type": "reading",
                "priority": priority,
                "question": f"單詞【{kanji}】的正確讀音是什麼？",
                "options": options,
                "answer": reading,
                "explanation": f"讀音：{reading}\n意思：{meaning}\n說明：{details}"
            })

        # 題型二：單詞 ➔ 中文釋義
        if (kanji or reading) and meaning:
            display_word = f"{kanji}（{reading}）" if kanji and reading else (kanji or reading)
            distractors = random.sample([m for m in all_meanings if m != meaning], min(3, len(all_meanings) - 1))
            options = distractors + [meaning]
            random.shuffle(options)
            questions.append({
                "type": "meaning",
                "priority": priority,
                "question": f"單詞【{display_word}】的中文意思是什麼？",
                "options": options,
                "answer": meaning,
                "explanation": f"意思：{meaning}\n說明：{details}"
            })

        # 題型三：例句填空題（如果有例句）
        examples = extract_example_sentences(item["details"], kanji)
        for sentence, translation in examples:
            display_sentence = sentence.replace(kanji, "（　　）")
            # 獲取同類型單詞做干擾項
            distractors = random.sample([v["kanji"] for v in vocab_items if v["kanji"] != kanji], min(3, len(vocab_items) - 1))
            options = distractors + [kanji]
            random.shuffle(options)
            
            exp_text = f"正確句子：{sentence}\n翻譯：{translation}\n單詞釋義：{meaning}"
            if details:
                exp_text += f"\n記憶要點：{details}"
                
            questions.append({
                "type": "fill_in",
                "priority": priority,
                "question": f"請選擇合適的單詞填入空格：\n\n『 {display_sentence} 』",
                "options": options,
                "answer": kanji,
                "explanation": exp_text
            })

    # --- 生成自他動詞題 ---
    for item in 自他_items:
        a_kanji = item["auto_kanji"]
        a_reading = item["auto_reading"]
        t_kanji = item["trans_kanji"]
        t_reading = item["trans_reading"]
        priority = item["priority"]
        details = item["details"]

        # 題型四：自動詞 ➔ 他動詞對應
        if a_kanji and t_kanji:
            distractors = random.sample([k for k in all_trans_kanji if k != t_kanji], min(3, len(all_trans_kanji) - 1))
            options = distractors + [t_kanji]
            random.shuffle(options)
            questions.append({
                "type": "transitive_match",
                "priority": priority,
                "question": f"自動詞【{a_kanji}（{a_reading}）】對應的「他動詞」是哪一個？",
                "options": options,
                "answer": t_kanji,
                "explanation": f"自動詞：{a_kanji}（{a_reading}） ➔ 狀態/自然改變\n他動詞：{t_kanji}（{t_reading}） ➔ 人為動作\n記憶要點：{details}"
            })

        # 題型五：他動詞 ➔ 自動詞對應
        if a_kanji and t_kanji:
            distractors = random.sample([k for k in all_auto_kanji if k != a_kanji], min(3, len(all_auto_kanji) - 1))
            options = distractors + [a_kanji]
            random.shuffle(options)
            questions.append({
                "type": "intransitive_match",
                "priority": priority,
                "question": f"他動詞【{t_kanji}（{t_reading}）】對應的「自動詞」是哪一個？",
                "options": options,
                "answer": a_kanji,
                "explanation": f"他動詞：{t_kanji}（{t_reading}） ➔ 人為動作\n自動詞：{a_kanji}（{a_reading}） ➔ 狀態/自然改變\n記憶要點：{details}"
            })

    print(f"Generated {len(questions)} quiz questions in total!")

    # 寫入 questions.js 檔案
    # 使用 js 格式宣告全域變數，避免 CORS 限制
    js_content = f"// 這是由 Python 自動生成的題庫數據，請勿手動修改\nconst questionBank = {json.dumps(questions, ensure_ascii=False, indent=2)};\n"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully wrote question bank to {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
