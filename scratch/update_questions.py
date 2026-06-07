# -*- coding: utf-8 -*-
import os
import re
import json
import random

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB_FILES = [
    os.path.join(WORKSPACE_DIR, "3_N2_Vocabulary_Bank_and_Verbs.md"),
    os.path.join(WORKSPACE_DIR, "4_N2_Adverbs_and_Conjunctions.md")
]
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
    """解析如 '入る（はいる）' 形式的單詞與讀音，並忽視後面的說明字眼"""
    m = re.match(r'^([^\uff08\(\s]+)[\uff08\(]([^\uff09\)]+)[\uff09\)]', word_text.strip())
    if m:
        return m.group(1), m.group(2)
    # 如果沒有括號但包含【自】或【他】，提取乾淨單詞
    clean_word = re.sub(r'【[^】]+】', '', word_text)
    clean_word = re.split(r'[/／\s]', clean_word)[0].strip()
    return clean_word, ""

def extract_example_sentences(details_text, keyword):
    """從記憶要點中提取例句，並用（　　）替換關鍵詞做成填空題"""
    details_text = re.sub(r'<br\s*/?>', '; ', details_text)
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
def extract_grammar_questions(workspace_dir):
    file1 = os.path.join(workspace_dir, "1_N2_Study_Strategy_and_Grammar.md")
    file2 = os.path.join(workspace_dir, "2_N2_Kanji_and_Synonym_Distinctions.md")
    
    raw_examples = []
    
    for file_path in [file1, file2]:
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            
        current_section = "未分類"
        current_subheading = "未分類"
        priority = "🔴"  # 預設核心文法
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith("### "):
                current_section = line[4:].strip()
                current_subheading = ""
                # 依據標題重要度設定
                if "🔴" in line:
                    priority = "🔴"
                elif "🟡" in line:
                    priority = "🟡"
                elif "🟢" in line:
                    priority = "🟢"
                else:
                    priority = "🔴"
            elif line.startswith("#### "):
                current_subheading = line[5:].strip()
                if "🔴" in line:
                    priority = "🔴"
                elif "🟡" in line:
                    priority = "🟡"
                elif "🟢" in line:
                    priority = "🟢"
                    
            m_code = re.search(r'`([^`]+)`', line)
            if m_code:
                sentence = m_code.group(1).strip()
                
                # 提取翻譯
                translation = ""
                m_trans = re.search(r'\(([^)]+)\)|（([^）]+)）', line.replace(f"`{sentence}`", ""))
                if m_trans:
                    translation = (m_trans.group(1) or m_trans.group(2)).strip()
                else:
                    j = i + 1
                    while j < min(i + 3, len(lines)):
                        next_line = lines[j].strip()
                        m_next_trans = re.match(r'^\(([^)]+)\)$|^\（([^）]+)）$', next_line)
                        if m_next_trans:
                            translation = (m_next_trans.group(1) or m_next_trans.group(2)).strip()
                            break
                        j += 1
                
                # 尋找 **...** 或 「...」 標記
                targets = []
                bolded = re.findall(r'\*\*([^*]+)\*\*', sentence)
                if bolded:
                    targets.extend(bolded)
                quoted = re.findall(r'「([^」]+)」', sentence)
                if quoted:
                    targets.extend(quoted)
                    
                if targets and translation:
                    for target in targets:
                        clean_sentence = sentence
                        if f"**{target}**" in clean_sentence:
                            clean_sentence = clean_sentence.replace(f"**{target}**", "（　　）")
                        elif f"「{target}」" in clean_sentence:
                            clean_sentence = clean_sentence.replace(f"「{target}」", "（　　）")
                        else:
                            clean_sentence = clean_sentence.replace(target, "（　　）")
                            
                        clean_sentence = clean_sentence.replace("**", "").replace("「", "").replace("」", "")
                        
                        raw_examples.append({
                            "section": current_section,
                            "subheading": current_subheading,
                            "sentence": sentence,
                            "clean_sentence": clean_sentence,
                            "target": target,
                            "translation": translation,
                            "priority": priority
                        })
            i += 1
            
    # 生成題目與干擾選項
    grammar_qs = []
    all_targets = list(set([item["target"] for item in raw_examples]))
    
    for item in raw_examples:
        target = item["target"]
        clean_sentence = item["clean_sentence"]
        translation = item["translation"]
        priority = item["priority"]
        section = item["section"]
        subheading = item["subheading"]
        
        # 尋找 3 個干擾項
        # 1. 優先尋找包含相同漢字或字符的選項 (如 足元 看 腳...)
        shared_chars = [c for c in target if not re.match(r'[\u3040-\u309f\u30a0-\u30ff]', c)]
        
        distractors_pool = []
        if shared_chars:
            for t in all_targets:
                if t != target and any(c in t for c in shared_chars):
                    distractors_pool.append(t)
                    
        # 2. 其次尋找同一個 section 或 subheading 的其他目標
        if len(distractors_pool) < 3:
            local_targets = [r["target"] for r in raw_examples if r["section"] == section and r["target"] != target]
            for lt in local_targets:
                if lt not in distractors_pool and lt != target:
                    distractors_pool.append(lt)
                    
        # 3. 再者尋找長度相似的目標
        if len(distractors_pool) < 3:
            similar_len = [t for t in all_targets if t != target and abs(len(t) - len(target)) <= 2]
            for sl in similar_len:
                if sl not in distractors_pool:
                    distractors_pool.append(sl)
                    
        # 4. 隨機兜底
        if len(distractors_pool) < 3:
            for t in all_targets:
                if t != target and t not in distractors_pool:
                    distractors_pool.append(t)
                    
        if len(distractors_pool) >= 3:
            distractors = random.sample(distractors_pool, 3)
        else:
            distractors = distractors_pool
            
        options = distractors + [target]
        random.shuffle(options)
        
        exp_text = f"正確句子：{item['sentence']}\n中文翻譯：{translation}\n文法主題：{section} ➔ {subheading}"
        
        grammar_qs.append({
            "type": "grammar_fill_in",
            "priority": priority,
            "question": f"請選擇合適的文法或詞彙填入空格：\n\n『 {clean_sentence} 』",
            "options": options,
            "answer": target,
            "explanation": exp_text
        })
        
    print(f"Generated {len(grammar_qs)} grammar and distinction questions!")
    return grammar_qs

def main():
    print("Parsing vocabulary notes...")
    vocab_items = []
    自他_items = []

    for vocab_file in VOCAB_FILES:
        if not os.path.exists(vocab_file):
            print(f"Warning: {vocab_file} not found, skipping...")
            continue
            
        print(f"Reading from {os.path.basename(vocab_file)}...")
        with open(vocab_file, "r", encoding="utf-8") as f:
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
                
                details_replaced = re.sub(r'<br\s*/?>', '; ', details)
                details_clean = clean_markdown_formatting(details_replaced)
                
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
                "verb_type": "transitive",
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
                "verb_type": "intransitive",
                "priority": priority,
                "question": f"他動詞【{t_kanji}（{t_reading}）】對應的「自動詞」是哪一個？",
                "options": options,
                "answer": a_kanji,
                "explanation": f"他動詞：{t_kanji}（{t_reading}） ➔ 人為動作\n自動詞：{a_kanji}（{a_reading}） ➔ 狀態/自然改變\n記憶要點：{details}"
            })

        # 題型六：自他動詞句型填空題（透過解析 details 中的例句）
        if details:
            clauses = re.split(r'[/／;；]', details)
            for clause in clauses:
                clause = clause.strip()
                # 尋找日文部分
                m = re.match(r'^([a-zA-Z0-9\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf\u3000-\u303f\uff01-\uff5e\uff08\(\)\uff09]+)', clause)
                if m:
                    sentence = m.group(1).strip()
                    target = None
                    other = None
                    verb_type = None
                    if a_kanji and a_kanji in sentence:
                        target = a_kanji
                        other = t_kanji
                        verb_type = "intransitive"
                    elif t_kanji and t_kanji in sentence:
                        target = t_kanji
                        other = a_kanji
                        verb_type = "transitive"
                    elif a_reading and a_reading in sentence:
                        target = a_reading
                        other = t_reading
                        verb_type = "intransitive"
                    elif t_reading and t_reading in sentence:
                        target = t_reading
                        other = a_reading
                        verb_type = "transitive"
                    
                    if target and other and len(sentence) > len(target):
                        display_sentence = sentence.replace(target, "（　　）")
                        distractors = [other]
                        pool = [k for k in all_auto_kanji + all_trans_kanji if k not in [target, other] and k]
                        if len(pool) >= 2:
                            distractors += random.sample(pool, 2)
                        else:
                            distractors += pool
                        
                        options = distractors + [target]
                        random.shuffle(options)
                        
                        exp_text = f"正確句子：{sentence}\n自動詞：{a_kanji}（{a_reading}）\n他動詞：{t_kanji}（{t_reading}）\n記憶要點：{details}"
                        questions.append({
                            "type": "verb_fill_in",
                            "verb_type": verb_type,
                            "priority": priority,
                            "question": f"請選擇正確的自他動詞填入空格：\n\n『 {display_sentence} 』",
                            "options": options,
                            "answer": target,
                            "explanation": exp_text
                        })

    grammar_qs = extract_grammar_questions(WORKSPACE_DIR)
    questions.extend(grammar_qs)

    print(f"Generated {len(questions)} quiz questions in total!")

    # 寫入 questions.js 檔案
    # 使用 js 格式宣告全域變數，避免 CORS 限制
    js_content = f"// 這是由 Python 自動生成的題庫數據，請勿手動修改\nconst questionBank = {json.dumps(questions, ensure_ascii=False, indent=2)};\n"
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Successfully wrote question bank to {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
