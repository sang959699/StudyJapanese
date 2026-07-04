# -*- coding: utf-8 -*-
import re
import os

vocab_file_path = r"D:\StudyJapanese\3_N2_Vocabulary_Bank_and_Verbs.md"
adverb_file_path = r"D:\StudyJapanese\4_N2_Adverbs_and_Conjunctions.md"
review_file_path = r"D:\StudyJapanese\N2_Kanji_Vocabulary_Final_Review.md"

def extract_red_rows_from_table(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    extracted_rows = []
    headers = []
    in_table = False
    
    for line in lines:
        line_str = line.strip()
        if "|" in line_str:
            # Check if this is a table separator line (e.g. | :--- | :--- |)
            if re.match(r"^\|\s*[:\-]+\s*\|", line_str):
                continue
            
            # Split cells
            cells = [c.strip() for c in line_str.split("|")[1:-1]]
            
            # Check if headers (using substring match to prevent empty lists)
            is_header = any(x in cell for cell in cells for x in ["漢字", "自動詞", "接續詞", "副詞"])
            if is_header:
                headers = cells
                in_table = True
                continue
            
            # If in table, check if any cell contains the red circle 🔴
            has_red = False
            for cell in cells:
                if "🔴" in cell:
                    has_red = True
                    break
            
            if has_red:
                extracted_rows.append((headers, cells))
        else:
            in_table = False
            
    return extracted_rows

# Extract
red_vocab = extract_red_rows_from_table(vocab_file_path)
red_adverbs = extract_red_rows_from_table(adverb_file_path)

print(f"Extracted {len(red_vocab)} high-frequency vocabulary rows.")
print(f"Extracted {len(red_adverbs)} high-frequency adverb/conjunction rows.")

# Group red_vocab into:
# - Transitive/Intransitive pairs
# - Regular vocabulary
trans_intra_pairs = []
regular_vocab = []

for headers, cells in red_vocab:
    is_trans_intra = False
    if headers:
        # Perform substring matching for safety
        header_str = "".join(headers)
        if "自動詞" in header_str or "他動詞" in header_str:
            is_trans_intra = True
        elif len(cells) == 3 and len(headers) >= 3 and "画面" in headers[2]:
            is_trans_intra = True
            
    if is_trans_intra:
        trans_intra_pairs.append(cells)
    else:
        regular_vocab.append(cells)

print(f"Grouped: {len(trans_intra_pairs)} self/other pairs, {len(regular_vocab)} regular vocabulary items.")

# Format to markdown
output_content = """# 🏆 JLPT N2 考前最後衝刺：核心漢字與詞彙秒殺清單 (高頻大詞庫版)

親愛的同學，明天就是 JLPT 日檢考試了！這份複習清單已為你從厚重的筆記中，**自動篩選並提取出所有標註為高頻（🔴 紅圈）的核心自他動詞、高頻單字、副詞與接續詞**。

這是一份「純乾貨」的高 yield 衝刺清單，考前最後一晚，利用這張表快速瀏覽「漢字視覺畫面」與「秒殺考點」，祝你明天順利合格！🏆🌸

---

## 🎯 一、 核心同音異義字辨析表 (🔴)

這一組漢字讀音完全相同，但引進漢字後進行了非常細緻的「功能分工」：

| 讀音 | 漢字 | 核心意象 (視覺畫面) | 經典考點 / 秒殺搭配 |
| :--- | :--- | :--- | :--- |
| **はかる** | **計る** | **計量時間、數字**。 | 時間を**計る** (計時) / 熱を**計る** (量體溫) |
| | **測る** | **測量空間長寬高、深淺、溫度、面積**。 | 長さを**測る** / 熱を**測る** (體溫亦可用測) / 水深を**測る** |
| | **量る** | **稱量重量、體積、容器分量**。 | 重さを**量る** / 体重を**量る** |
| | **図る** | **計畫、企圖、謀求** (以某個目標為終點)。 | 解決を**図る** (謀求解決) / 自殺を**図る** (企圖自殺) |
| | **謀る** | **策劃陰謀、欺騙、陷害**。 | 悪事を**謀る** (策劃壞事) / 騙して**謀る** |
| | **諮る** | **諮詢、開會商討**。 | 委員會に**諮る** (提交給委員會討論) |
| **おさめる** | **納める** | **「交付、收納」**：把該交的東西交出去。 | 税金を**納める** (繳稅) / 授業料を**納める** (繳學費) |
| | **収める** | **「獲得、收進」**：取得好成果或放進箱子。 | 成功を**収める** (獲得成功) / 成果を**収める** / 写真に**収める** |
| | **治める** | **「整治、治理」**：讓混亂、國家或疼痛平靜下來。 | 国を**治める** (治國) / 痛みを**治める** (止痛/平復疼痛) |
| | **修める** | **「修業、學習」**：研讀學問、修行品德。 | 学問を**修める** (修研學問) / 身を**修める** (修身) |
| **つとめる** | **勤める** | **「受僱工作」**：在某機構上班、當職員。 | 会社に**勤める** (在公司上班) |
| | **努める** | **「努力、盡力」**：主觀用意志力去克服困難。 | 解決に**努める** (努力解決) / 服務向上に**努める** |
| | **務める** | **「擔當角色」**：扮演主持人、班長、主角等職務。 | 司会を**務める** (擔任主持人) / 主役を**務める** (擔任主角) |
| **かける** | **掛ける** | **物理吊掛、蓋被子、澆醬汁、乘法、花費**。 | 壁に絵を**掛ける** / 布団を**掛ける** / 3に5を**掛ける** |
| | **懸ける** | **賭上無形物 (生命/名譽/勝負)**。 | 命を**懸ける** / 名誉を**懸ける** / **～にかけては** (在……方面無敵) |
| | **賭ける** | **賭博有形金錢、財產** (貝字旁與錢有關)。 | お金を**賭ける** / 競馬に金を**賭ける** |
| | **駆ける** | **騰空飛奔、跑步** (馬字旁)。 | 草原を**駆ける** / 駆け足 (小跑) / 駆け上がる (跑上樓) |
| | **欠ける** | **物品破損缺口、缺乏**。 | 茶碗が**欠ける** / 常識に**欠ける** (缺乏常識) |
| **うかがう** | **伺う** | **謙讓語**：去拜訪、詢問、聽說。 | お宅に**伺う** (去您家拜訪) / お話を聞きに**伺う** |
| | **窺う** | **窺視、暗中觀察、伺機而動**。 | 様子を**窺う** (觀察動靜) / チャンスを**窺う** (尋找機會) |
| **せめる** | **責める** | **責備、非難、批評對方的過失**。 | 相手のミスを**責める** (責備對方的失誤) |
| | **攻める** | **進攻、攻擊、主動出擊**。 | 敵を**攻める** (進攻敵人) / 攻めの姿勢 (主動進攻的姿態) |
| **あう** | **会う** | **與人見面**。 | 友達に**会う** |
| | **合う** | **相合、匹配、共同做某事**。 | サイズが**合う** / 話し**合う** (互相討論) |
| | **遭う** | **遭遇不好的災難、意外** (如車禍、暴雨)。 | 事故に**遭う** / どしゃ降りに**遭う** (淋成落湯雞) |
| **のびる** | **伸びる** | **物理長高、能力提升、延展** (伸長)。 | 背が**伸びる** (長高) / 才能が**伸びる** / ゴムが**伸びる** |
| | **延びる** | **時間上的延遲、延期** (延長)。 | 会議が**延びる** (會議延期) / 締め切りが**延びる** (截止日延後) |
| **なおす** | **直す** | **修正錯誤、回復原狀、翻譯**。 | 癖を**直す** (改正習慣) / 英語を日本語に**直す** (翻譯) |
| | **治す** | **醫治疾病、身體傷口**。 | 病気を**治す** / 風邪を**治す** |

---

## 🔄 二、 考前最常考：自他動詞高頻對比表 (🔴)

在 N2 的詞彙與聽力中，**自動詞表示狀態或自然發生（主語用 が），他動詞表示人有意施加的動作（賓語用 を）**。以下為你篩選出筆記中最常考的自他動詞對應：

| 自動詞 (が ＋ 狀態/自然改變) | 他動詞 (を ＋ 人為施加動作) | 核心畫面與記憶要點 |
| :--- | :--- | :--- |
"""

for cells in trans_intra_pairs:
    if len(cells) >= 3:
        auto_v = cells[0].replace("\n", "<br>")
        trans_v = cells[1].replace("\n", "<br>")
        memo = cells[2].replace("\n", "<br>")
        output_content += f"| {auto_v} | {trans_v} | {memo} |\n"

output_content += """
---

## ⚡ 三、 核心近義詞精細辨析 (Synonyms)

### 1. 觸碰的藝術：触る（さわる） vs 触れる（ふれる）
*   👉 **触る（さわる）**：**「手掌實體摸到」**。指有意識、主動地去碰觸某物（帶有揉捏、抓握的手感）。
    *   *考點*：常以否定命令出現，如：`美術品に触るな！` (禁止觸摸美術品！)。
*   👉 **触れる（ふれる）**：**「輕輕掠過、提及、違反規則」**。指無意間的輕碰，或抽象層面的涉及（如涉及法律、提及話題、映入眼簾）。
    *   *考點*：`法に**触れる**` (觸法) / `話題に**觸れる**` (提及話題) / `目に**触れる**` (映入眼簾)。

### 2. 「小氣」的大不同：気が小さい vs ケチ vs 器が小さい
*   👉 **気が小さい**：**「膽小、怕事、懦弱」** (心臟很小顆)。
*   👉 **ケチ**：**「吝嗇、捨不得花錢」**。
*   👉 **器が小さい**：**「度量小、愛計較、沒有包容力」** (容器很小裝不下別人的意見)。

### 3. 表達情感注入的萬能動詞：～のこもった（籠る）
*   👉 **こもる（籠る）**：指熱情、心意、情感「充沛地融入在某事物中」。
*   *考點（必背搭配）*：
    *   `心の**こもった**贈り物` (誠心誠意的禮物)
    *   `愛情 of **こもった**手料理` (充滿愛心的手作料理)
    *   `熱の**こもった**演説` (熱情洋溢的演說)

### 4. 準備與調和的自他動詞：整う（ととのう） vs 整える（ととのえる）
*   👉 **整う（ととのう - 自動詞）**：**「物體或事情準備齊全、井然有序」**。
    *   *考點*：`準備が**整う**` (準備齊全) / `交渉が**整う**` (談判達成協議)。
*   👉 **整える（ととのえる - 他動詞）**：**「整理、調整、使之齊備」**。
    *   *考點（必背搭配）*：
        *   `息を**整える**` (調整呼吸/喘口氣 ➔ **考試超高頻！**)
        *   `身なりを**整える**` (整理儀容)
        *   `味を**整える**` (調味)

### 5. 萬能動詞的多義性：配る（くばる）
*   👉 **配る（くばる）**：原意為「分發、分送」，引申為「將注意力分發到各個角落」。
*   *考點（必背搭配）*：
    *   `気を**配る**` (對他人體貼/關照 ➔ **考試超高頻！** 與 `気を遣う` [顧慮/拘束] 語境不同)
    *   `目を**配る**` (四處看守/環顧四周)
    *   `チラシを**配る**` (發傳單)

---

## 📚 四、 分類核心高頻單字表 (🔴)

以下為你整理出筆記中所有標註為 **🔴 高頻** 的核心動詞、名詞與形容詞，按場景與語意進行複習：

| 漢字 | 讀音 | 中文釋義 | 記憶要點 / 例句 |
| :--- | :--- | :--- | :--- |
"""

for cells in regular_vocab:
    if len(cells) >= 4:
        kanji = cells[0].replace("\n", "<br>")
        reading = cells[1].replace("\n", "<br>")
        meaning = cells[2].replace("\n", "<br>")
        memo = cells[3].replace("\n", "<br>")
        output_content += f"| {kanji} | {reading} | {meaning} | {memo} |\n"

output_content += """
---

## 📢 五、 考前必看：高頻副詞與接續詞呼應表 (🔴)

副詞與接續詞是日檢的「秒殺送分題」。看到副詞要直接聯想後方的句尾搭配（例如：看到 `必ずしも` 找 `とは限らない`）！

| 副詞 / 接續詞 | 讀音 | 中文釋義 | 記憶要點 / 核心語意 / 例句 |
| :--- | :--- | :--- | :--- |
"""

for headers, cells in red_adverbs:
    if len(cells) >= 4:
        word = cells[0].replace("\n", "<br>")
        reading = cells[1].replace("\n", "<br>")
        meaning = cells[2].replace("\n", "<br>")
        memo = cells[3].replace("\n", "<br>")
        output_content += f"| {word} | {reading} | {meaning} | {memo} |\n"

output_content += """
---

## 📝 考前心態與答題秒殺技巧

1. **同音異義字快速漢字分工**：
   * **掛 / 架** ➔ 物理吊掛、蓋被子、澆醬汁、乘法、架橋。
   * **懸** ➔ 賭上生命、名譽等「無形物」 (`命を懸ける`、`にかけては`)。
   * **賭** ➔ 賭博「有形金錢、資產」 (`お金を賭ける`)。
   * **駆** ➔ 騰空飛奔、跑步 (`草原を駆ける`)。
   * **整う / 整える** ➔ `準備が整う` (準備好) / `息を整える` (調整呼吸)。
   * **配る** ➔ `気を配る` (細心體貼) / `目を配る` (看守)。

2. **冷靜看字源**：遇到不會的單字，閉上眼睛想一下它的**「大和語讀音（和語）」**。
   * 例如：`かける` ➔ 畫面是「懸空、吊掛、跨越」。
   * `はる` ➔ 畫面是「撐開、拉平、張網」。
   * `ぬく` ➔ 畫面是「穿透、拔出、越過」。
   運用大和語的核心物理畫面，去對推漢字的意思，正確率會極高！

**放鬆心情，正常發揮！明天你一定可以順利合格！加油！🏆🌸**
"""

# Let's fix small typos in templates:
output_content = output_content.replace("愛情 of **こもった**手料理", "愛情の**こもった**手料理")

with open(review_file_path, "w", encoding="utf-8") as f:
    f.write(output_content.replace("\n", "\r\n"))

print("Successfully compiled and updated review sheet with complete Section 2!")
