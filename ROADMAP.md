# GIIS Platform — Product Roadmap

> 最後更新：2026-05-02  
> **核心目標：讓家長願意付錢，並且持續付錢。**

---

## 為什麼家長會付錢？

家長付錢給一間學校，判斷的依據只有三件事：

1. **信任** — 這是一間真正的學校嗎？我的孩子拿到的文憑有意義嗎？
2. **透明** — 我看得到孩子在學什麼、學得怎麼樣嗎？
3. **結果** — 孩子有在進步嗎？這筆錢花得值得嗎？

目前系統對**學生**來說功能已經相當完整，但對**家長**來說幾乎完全不存在。家長要付錢，卻沒有任何介面、任何溝通、任何保證。這是最大的問題。

---

## 三個視角的目標

### 家長視角 — 願意付錢的條件
- [ ] 不用登入就能收到孩子的進度報告（週報 email）
- [ ] 有家長帳號，隨時可以看孩子在學什麼
- [ ] 知道有真人老師在批改作業、給回饋
- [ ] 文憑和成績單在大學申請時被認可（可驗證）
- [ ] 付款流程清楚、簡單，支援信用卡
- [ ] 入學流程不需要找人幫忙，自己就能完成
- [ ] 每學期有一份正式的報告單
- [ ] 遇到問題有管道聯絡學校

### 管理員 / 老師視角 — 能有效管理的條件
- [ ] 一個頁面看到所有學生的學習進度（誰卡關、誰沒動）
- [ ] 待批作業清單，不用去資料庫找
- [ ] 批改作業後系統自動通知學生和家長
- [ ] 能幫學生加退課，不只是學生自己操作
- [ ] 收到付款、入學申請的即時通知
- [ ] 能對每位學生寫學習建議筆記
- [ ] 批量建立學生帳號（CSV 匯入）
- [ ] 直接從 UI 新增 / 編輯課程內容，不用改 JSON 再 re-seed

### 學生視角 — 願意持續學習的條件
- [ ] 每門課有清楚的進度條，知道自己完成了多少
- [ ] Quiz 沒過時，明確告訴我該複習哪裡，不是直接擋住
- [ ] 考試失敗後顯示還要等幾小時才能重考
- [ ] 作業有了老師評語時，主動通知我（不用自己去翻）
- [ ] 忘記密碼可以自己重設，不用找 admin
- [ ] 可以直接上傳 PDF / 圖片作為作業，不只是貼連結
- [ ] 有地方可以問老師問題（不只是 Google）
- [ ] 推薦下一步選什麼課，而不是自己在 91 門課裡猜
- [ ] 用手機也能正常學習（目前 Learn Portal 手機版跑版）

---

## 現況（已建立的）

**學生端（✅ 功能完整）**
- 登入、選課、學習 Module、交作業
- Quiz、期中考、期末考（含 gated unlock 邏輯）
- 成績計算（加權 GPA、學分累計）
- 成績單查看、文憑下載（24 學分後）
- 個人 Profile

**管理員端（✅ 基本可用）**
- 學生名冊、新增/停用學生
- 成績單編輯、Audit Log
- 作業 feedback API 已建（無 UI）

**網站公開頁面（✅ 已有）**
- 首頁、Academics、Discovery、Pathways（8 個 pathway）
- Admission 頁面（4 步驟流程、文件要求、文憑認可說明、FAQ、定價）
- Pricing 頁面（$199/月 或 $1,799/年）
- 法律頁面（隱私政策、使用條款）
- 首頁 Contact Form（Netlify Forms，已可接收詢問）

## ⚠️ 已發現的內容問題（上線前必須修正）

這些是**現在就存在的錯誤承諾**，家長付錢後發現不符會要求退款：

| 問題 | 位置 | 實際狀況 |
|------|------|---------|
| FAQ 寫「透過 Moodle 系統學習」 | AdmissionMain.js FAQ | 系統是自建的 Learn Portal，不是 Moodle |
| FAQ 寫「有直播課程，配合中國時區」 | AdmissionMain.js FAQ | 完全沒有直播基礎設施 |
| FAQ 寫「每位學生有 dedicated academic advisor」 | AdmissionMain.js FAQ + PricingPage.js | 系統沒有顧問互動功能，只是 admin 手動 |
| Pricing 頁的「Enroll」按鈕是 `mailto:` 連結 | PricingPage.js | 點下去只是開 email client，不是真正付款 |

---

---

## 缺口分析：從家長付錢的角度

### 家長完全看不到的東西

| 問題 | 影響 |
|------|------|
| 沒有家長帳號 | 家長無法追蹤孩子進度，只能靠孩子自己說 |
| 沒有進度報告 | 孩子一個月沒動，家長也不知道 |
| 沒有與學校溝通的管道 | 有問題只能發 email 或打電話，沒有正式渠道 |
| 沒有付款流程 | 定價頁面有數字，但無法實際付款 |
| 沒有入學流程 | 家長不知道怎麼幫孩子報名，要找 admin 手動建帳號 |

### 讓家長「不確定要不要付」的東西

| 問題 | 影響 |
|------|------|
| 課程內容無法預覽 | 家長不知道孩子會學到什麼，只有課程名稱，付錢前看不到實際內容 |
| 沒有老師/顧問的形象 | 看不到誰在教，感覺像無人機器，沒有真人背書 |
| 學生交了作業沒有 feedback | 家長問孩子學到什麼，孩子說不知道老師什麼時候回覆 |
| 沒有 social proof | Admission 頁已有 Yunfan / Baoyi 的錄取案例，但首頁沒有，需要更多 |
| 手機體驗很差 | Learn Portal 幾乎沒有 mobile CSS，家長用手機看會跑版 |

---

---

## Phase 0 — 上線前必須修正（錯誤承諾）

> **這些問題現在就存在，不修就不應該開始收錢。**

### 0-A. 修正 FAQ 的錯誤描述

**Admission 頁面 FAQ 裡有三個不符合實際的承諾：**

1. **Moodle** → 改成「我們自建的學習平台」
2. **直播課程** → 改成「非同步自學為主，可預約顧問視訊」（如果真的有的話）或直接刪除
3. **Dedicated academic advisor** → 說清楚是什麼：定期 email 回覆？還是只是 admin？定義清楚再寫上去

**涉及檔案：** `src/components/pages/Admission/AdmissionMain.js`

---

### 0-B. Pricing 頁面的 Enroll 按鈕

**目前 Pricing 頁的「Enroll」按鈕是 `mailto:` 連結**，點下去只是開 email client。

在 Stripe 接好之前的過渡方案：
- 按鈕改成連到 `/apply` 入學申請表（Phase 2 建）
- 或直接連到 Contact Form（已有 Netlify Forms）
- 不要讓家長以為點了就完成付款

**涉及檔案：** `src/components/pages/Pricing/PricingPage.js`

---

### 0-C. 手機版基本可用性

**Learn Portal 幾乎沒有 mobile CSS。** 目前整個 `src/components/pages/Learn/` 只有 13 處 maxWidth 設定，沒有任何 `@media` query。家長用手機看學習進度會跑版。

最低標準（不需要完美，但不能跑版）：
- `LearnDashboard.js` — 課程卡片在小螢幕換成單欄
- `CoursePage.js` — Module 列表在手機可讀
- `ModulePage.js` — 文字和按鈕不超出螢幕

---

## Phase 1 — 讓家長能「看到」孩子在學習

> **目標：** 家長打開手機就能知道孩子這週做了什麼。這是信任的基礎。

### 1. 每週進度 Email 報告（自動寄給家長）

**這是最重要的單一功能。** 不需要家長登入，不需要他們做任何事，系統自動告訴他們孩子在做什麼。

**內容：**
- 這週完成了哪些 Module
- Quiz / 考試分數
- 作業提交狀態
- 累計學分進度（X / 24）
- 一句話結語（「Yunfan 本週完成了 Calculus Module 3，保持得很好！」）

**需求：**
- `Student` 新增 `parentEmail` 欄位
- Admin 建立學生時可填家長 email
- 每週一固定時間（cron job）寄出
- 如果這週沒有任何活動，改寄「提醒」版本

**Schema 異動：**
- `Student` 新增 `parentEmail String?`

**外部依賴：** Resend（免費 tier：3,000 封/月，夠用）

---

### 2. 作業批改介面 + 批改後通知家長

**家長最常問：「老師有在看我孩子的作業嗎？」** 目前作業交了就沒下文。

**需求：**
- Admin Dashboard 新增「待批作業」清單
  - 欄位：學生姓名、課程、Module、提交時間、內容連結
  - 篩選：未批 / 已批
- 批改後 email 同時寄給：學生（「你的作業有了新評語」）+ 家長（「老師批改了 [孩子名字] 的作業」）
- 學生端 Module 頁面高亮顯示新的 feedback

**API 新增：** `GET /api/admin/assignments/pending`  
**Schema 異動：** `AssignmentSubmission` 新增 `score Decimal?`

---

### 3. 家長入口（Parent View）

**家長需要一個地方登入，看到一個簡單的 dashboard。**

**需求：**
- 新增 `ParentAccount` — `{ id, email, passwordHash, studentId }`
- `/parent/login` — 家長登入頁
- `/parent/dashboard` — 只讀：
  - 孩子的照片 / 姓名 / 年級
  - 目前選課清單 + 每門課完成 % 進度條
  - 最近 5 筆活動（完成 Module、通過考試、交作業）
  - 累計學分 / GPA
  - 聯絡學校按鈕（開啟 email 或 contact form）
- Admin 建立學生時可同時建立家長帳號（或獨立寄邀請連結）

**Schema 新增：** `ParentAccount` model

---

## Phase 2 — 讓家長能「付款並信任」

> **目標：** 付款流程順暢，學校看起來是一間真正的機構。

### 4. 付款整合

**定價頁面有數字，但沒有辦法付錢，等於白搭。**

**方案：** Stripe（支援信用卡、分期，介面可嵌入，最快整合）

**需求：**
- Pricing 頁面加入「Enroll Now」按鈕 → Stripe Checkout
- 付款方案：月費 / 學期費 / 年費（依你的定價策略）
- 付款成功後：
  - 自動建立學生帳號（或啟用帳號）
  - 自動寄歡迎 email（含登入資訊）給學生 + 家長
- Admin 後台顯示付款狀態 / 到期日

**Schema 新增：**
- `Subscription` — `{ id, studentId, stripeCustomerId, status, currentPeriodEnd }`

---

### 5. 入學流程（Self-service Onboarding）

**目前沒有家長可以自己完成的入學流程。** 全靠 admin 手動建帳號。

**需求：**
- `/apply` 入學表單：學生姓名、生日、家長姓名、家長 email、電話
- 提交後：
  - Admin 收到通知 email
  - 家長收到「申請已收到，我們會在 24 小時內聯絡您」確認信
- Admin 審核後一鍵建立帳號 + 觸發付款連結 / 歡迎信

---

### 6. 成績單與文憑的公信力強化

**家長付錢的一大原因是拿到有意義的文憑。** 目前文憑和成績單外觀已經做得不錯，但公信力不夠清楚。

**需求：**
- 成績單 / 文憑上加入驗證 QR code，掃描後顯示「此文件由 GIIS 官方發出，學生：XXX，日期：XXXX」
- `/verify/:studentCode` 公開驗證頁面（不需登入，輸入學號或掃 QR 即可確認真實性）
- Cognias 認證 logo 在網站首頁、About 頁更顯眼
- School Profile 頁面補充「我們的文憑被哪些大學認可 / 提交過哪些申請案例」

---

## Phase 3 — 讓家長「一直付錢」（Retention）

> **目標：** 不只是第一次付，而是每學期續費。

### 7. 學習顧問功能（Advisor 角色）

家長付錢後，最常問的問題是：「我的孩子下一步該選什麼課？」目前系統沒有人回答這個問題。

**需求：**
- Admin 可以對每位學生留下「學習建議」筆記
- 每學期初自動寄給家長：「根據 Yunfan 的學習進度，我們建議下學期選修以下課程...」
- 家長 Dashboard 顯示「顧問建議」區塊

### 8. 學期總結報告（Semester Report Card）

- 每學期末自動生成 PDF 報告寄給家長
- 內容：這學期完成的課程、GPA、老師評語、下學期建議
- 感覺像真正的學校在認真追蹤孩子的學習

### 9. 忘記密碼（學生自助）

- 學生 / 家長自己可以 reset 密碼，不用找 admin
- 需要接 email 服務（Phase 1 就應該接了）

### 10. 考試冷卻倒計時

- 考試失敗後顯示「還要等 X 小時才能重考」
- 小改動，但讓體驗更清楚

---

## Phase 4 — 規模化

> 有了穩定付費用戶後才考慮

### 管理員端
| 功能 | 對應目標 |
|------|---------|
| 課程 / 題目管理 UI | admin 可從 UI 新增 / 編輯課程，不用改 JSON + re-seed |
| 批量學生匯入（CSV）| 一次建立多個帳號，自動寄歡迎信 |
| 學生進度看板 | 一頁看所有學生進度、誰卡關、誰超過 14 天沒動 |
| Admin 代替學生加退課 | 學生 Profile 頁可直接管理 Enrollment |

### 學生端
| 功能 | 對應目標 |
|------|---------|
| 課程進度條 | Dashboard 每張課程卡顯示 `已完成 X / Y Modules` |
| Quiz 失敗引導 | 沒過時顯示「建議複習這個 Module 的哪個部分」 |
| 考試冷卻倒計時 | 失敗後顯示「還要等 X 小時才能重考」 |
| 作業檔案上傳 | 支援 PDF / DOCX（Cloudflare R2 或 S3）|
| 學生討論 / Q&A | 每個 Module 下方討論區，老師可回覆 |
| 課程推薦優化 | 根據 GPA、已選課程、Pathway 推薦下一步 |

### 成長機制
| 功能 | 說明 |
|------|------|
| 推薦人機制 | 現有家長推薦新生，雙方獲得學費折扣 |
| Alumni 展示頁 | 畢業生去了哪間大學，增加公信力 |

---

## 技術債（隨時可處理，不影響家長付錢）

| 項目 | 影響 |
|------|------|
| 移除 Bootstrap（僅用了幾個 class）| Bundle 減少 ~200KB |
| 移除 react-slick → CSS scroll-snap | 少 2 個套件 |
| 首頁圖片轉 WebP（9.9MB → ~2MB）| 首頁載入快 3–4 倍 |
| Login / exam submit 加 rate limiting | 安全性 |
| Server-side PDF（Puppeteer）| PDF 品質更穩定，不受瀏覽器影響 |

---

## 開發優先序總結

```
立刻做（Phase 1）：
  週報 email → 作業批改 + 通知 → 家長 Portal

讓錢進來（Phase 2）：
  Stripe 付款 → 入學表單 → 文憑驗證

留住付費用戶（Phase 3）：
  顧問建議 → 學期報告 → 密碼重設

等有規模再做（Phase 4）：
  課程管理 UI → 批量操作 → 討論區
```

---

## 環境資訊

- **Frontend:** React 18 / react-router-dom v6 / Netlify
- **Backend:** Express + Prisma ORM + PostgreSQL / 目標 AWS Lightsail
- **Email（待接）:** Resend（免費 3,000 封/月，API key 在 resend.com）
- **付款（待接）:** Stripe（Phase 2）
- **學生資料備份:** `server/data-backup/students_transcript_export.json`

## 測試帳號

| Code | 姓名 | Email |
|------|------|-------|
| 26-001 | Ruwen Li | ruwen.li@genesisideas.school |
| 26-002 | Tao Zhang | tao.zhang@genesisideas.school |
| 26-003 | Baoyi Lu ★ | baoyi.lu@genesisideas.school |
| 26-004 | Yunfan Yang ★ | yunfan.yang@genesisideas.school |

★ Yunfan Yang 有最多考試記錄，最適合測試。
