# 🌸 JLPT N2 學習筆記索引與分類指南 (Index & AI Guide)

歡迎使用 N2 學習筆記系統！為了避免單一文件過大導致 Token 消耗過快與學習負載過重，本筆記系統已拆分為 **3 個核心模組**。

本文件為 **主導引與分類規則 (Instruction & Index)**。當你在 [note.txt](file:///D:/StudyJapanese/note.txt) 中追加新的學習內容、錯題或疑問時，AI 與你將依據以下規則將內容分類歸檔至對應的筆記文件中。

---

## 🎯 備考核心目標與定位 (Exam Focus & Strategy)

本筆記系統與後續學習對接遵循以下兩大核心原則：
1.  **專注於 JLPT N2 核心**：所有的詞彙、語法、漢字分析均以 N2 大綱為絕對重心。對於超出 N2 範圍（如 N1）的超綱詞彙，僅在能提供「字根聯想」或「語源比對」的輔助情況下適度提及，不作為記憶重點。
2.  **向下複習 N3 文法**：鑑於 N2 文法多是由 N3 文法延伸或精細進化而來，當學習 N2 新句型時，AI 應**主動對接並複習相關的 N3 語法**（例如：學習 N2 `～がたい` 時，複習 N3 `～にくい`；學習 N2 `～つつある` 時，對比 N3 `～ている`），以鞏固語法地基。

---

## 📂 筆記架構與文件連結

### 1. 📝 [第一部分：學習策略與文法句型](file:///D:/StudyJapanese/1_N2_Study_Strategy_and_Grammar.md)
*   **收錄內容**：
    *   個人化學習背景與備考策略。
    *   學習進度與每日複習建議 (1-3-7-14 追蹤表)。
    *   核心學習方法論（「切西瓜」拆解法、字根聯想法、猜字三大工具）。
    *   ⚠️ **文法句型易錯點**、職場社交敬語、時間接續等文法專項。
    *   實用長句拆解與告示牌免責聲明語法分析。

### 2. 🔍 [第二部分：核心漢字與近義詞辨析](file:///D:/StudyJapanese/2_N2_Kanji_and_Synonym_Distinctions.md)
*   **收錄內容**：
    *   同音異義漢字辨析（如六個 `はかる`、四個 `おさめる`）。
    *   近義詞情境區分（如 `集める` vs `まとめる`、`共通` vs `共同`、`汚い` 系列）。
    *   複合詞辨析（如 `～合わせ` 系列、`取り/やり` 系列）。
    *   多義詞與雙音字解析（如 `切る/切れる`、`額` 的多重讀音與語意）。

### 3. 📚 [第三部分：自他動詞與分類詞彙表](file:///D:/StudyJapanese/3_N2_Vocabulary_Bank_and_Verbs.md)
*   **收錄內容**：
    *   🔄 **自他動詞對照整理表**（自動詞與他動詞的配對與畫面感記憶法）。
    *   分類核心詞彙表：
        *   `Ⅰ. 職場與商務`
        *   `Ⅱ. 家庭與日常生活`
        *   `Ⅲ. 動作、身體與狀態`
        *   `Ⅳ. 金融與銀行操作`
        *   `Ⅴ. 描述、程度與副詞`

### 4. 🎮 [第四部分：本地智慧刷題系統](file:///D:/StudyJapanese/index.html)
*   **收錄內容與功能**：
    *   [index.html](file:///D:/StudyJapanese/index.html)：網頁端互動刷題面板，支持讀音選擇、釋義選擇、自他動詞配對及句子填空題。
    *   [scratch/update_questions.py](file:///D:/StudyJapanese/scratch/update_questions.py)：本地 Python 題庫生成與更新腳本，讀取第三部分詞彙表自動編譯生成題目。
    *   [questions.js](file:///D:/StudyJapanese/questions.js)：存放編譯後題庫數據的 JavaScript 檔案（已在 [.gitignore](file:///D:/StudyJapanese/.gitignore) 中設定忽略，切勿提交至 Git）。

---

## 🎮 本地智慧刷題系統使用指南 (Local Quiz App Guide)

為了配合日常筆記更新並隨時練習，本系統配備了本地互動式網頁刷題系統。

### 🔄 題庫更新流程與使用步驟
1.  **更新筆記**：在 [第三部分：自他動詞與分類詞彙表](file:///D:/StudyJapanese/3_N2_Vocabulary_Bank_and_Verbs.md) 中新增或修改單字。
2.  **重新編譯題庫**：在終端機中執行以下命令，以執行 Python 腳本更新題庫數據：
    ```bash
    python scratch/update_questions.py
    ```
    該腳本會解析單字表中的優先級、漢字、讀音、釋義及記憶要點中的例句，自動生成對應的四種題型並寫入 [questions.js](file:///D:/StudyJapanese/questions.js)。
3.  **開啟網頁刷題**：在瀏覽器中直接開啟 [index.html](file:///D:/StudyJapanese/index.html) 即可開始練習！錯題會顯示詳盡的解答說明，答對則自動進入下一題。

---

## 🛠️ AI 歸檔與更新指令 (Instruction for AI)

當用戶在 [note.txt](file:///D:/StudyJapanese/note.txt) 中寫入新筆記，或在對話中提出新的日語學習問題時，AI 應遵循以下步驟進行處理：

### 📥 步驟一：讀取與分析（核心學習法投射）
1.  讀取用戶在 [note.txt](file:///D:/StudyJapanese/note.txt) 中的新增內容。
2.  ⚠️ **字根與畫面感優先**：用戶極其擅長「大和語字根（Yamato Kotoba Roots）」與「畫面感聯想」記憶。AI 在解析單字時，必須**主動挖掘其語源、字根家族**（例如 `せ` 字根、`うつ` 字根、`おごる` 字根），並寫出具體的視覺聯想，避免死記硬背。
3.  **主動聯想反義與近義詞**：當用戶寫入一個單字時，AI 應主動聯想並補充其 N2 常考的反義詞或近義詞對（例如：`ケチ` ➔ `太っ腹` / `氣前がいい`；`几帳面` ➔ `大雑把`），將它們成對整理歸檔。
4.  所有解釋必須維持 **繁體中文**。

### 🗂️ 步驟二：決定歸檔目標文件
*   **規則 A**：如果是**句型、語意理解邏輯、長句拆解或純文法規則**，將其追加至 **[第一部分（策略與文法）](file:///D:/StudyJapanese/1_N2_Study_Strategy_and_Grammar.md)** 的末尾。
*   **規則 B**：如果是**漢字寫法辨析、同音字對比、字根家族、近義詞/反義詞（Synonyms/Antonyms）對比**，在 **[第二部分（漢字與近義詞）](file:///D:/StudyJapanese/2_N2_Kanji_and_Synonym_Distinctions.md)** 新增一個 numbered section 追加進去，並同步更新該文件最上方的目錄（TOC）。
*   **規則 C**：如果是**單一單字、短語、自他動詞配對**，將其新增至 **[第三部分（自他動詞與分類詞彙）](file:///D:/StudyJapanese/3_N2_Vocabulary_Bank_and_Verbs.md)** 對應的分類表格中。

### 🏷️ 步驟三：標註優先級與格式化
1.  所有新加入的單字或漢字辨析，必須明確標上優先級標記：
    *   `🔴` (優先級 1)：核心考點、自他動詞、同音異義字、近義反義對、敬語（⚠️ 權重極高）。
    *   `🟡` (優先級 2)：副詞、接續詞、動作與身體狀態動詞（🌟 權重高）。
    *   `🟢` (優先級 3)：日常專有名詞、電腦文書編輯詞彙（📊 權重中低）。
2.  新加入的單字表格格式需與原有表格保持一致：
    `| 優先級 | 漢字 | 讀音 | 中文釋義 | 記憶要點 / 例句 |`

### 🧹 步驟四：清空緩衝區與 Git 提交與更新提示
1.  當成功將筆記歸檔至對應的 Markdown 文件後，應將 [note.txt](file:///D:/StudyJapanese/note.txt) 內容清空重置，僅保留 `# 在此輸入你的新筆記` 與一行空行。
2.  使用 Git 命令將修改後的 `.md` 檔案進行 stage 與 commit，確保工作目錄乾淨。
3.  ⚠️ **注意**：動態生成的題庫檔案 [questions.js](file:///D:/StudyJapanese/questions.js) 絕對不可提交至 Git，已在 [.gitignore](file:///D:/StudyJapanese/.gitignore) 中設定忽略。
4.  📢 **提醒更新**：每次 AI 歸檔筆記並重置 `note.txt` 後，**必須在對話結尾主動提醒用戶在本地執行 `python scratch/update_questions.py`**，以確保新增的單字能同步編譯至網頁刷題系統。

