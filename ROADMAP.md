# GIIS Platform — Product Roadmap

> 最後更新：2026-05-04（晚間）
> **核心目標：讓家長願意付錢，並且持續付錢。**
>
> 這份 roadmap 是給 **Claude Code CLI（code mode）** 的工作清單。
> 每個未完成項目都標註：檔案、acceptance criteria、依賴。挑一個就能直接開動。
>
> ---
>
> ### 🔁 Agent working ritual — never skip
>
> **Before any task** → read this whole file first. Find what's done, what's pending, where your task fits.
> **After any task** → update this file immediately. Mark ✅ with a one-line summary, or add new items found during the work.
>
> The roadmap is the only persistent memory across sessions. If it's not here, the next agent won't know.
> Full conventions live in [`CLAUDE.md`](./CLAUDE.md) — read once per session.

---

## 為什麼家長會付錢？

家長付錢給一間學校，判斷的依據只有三件事：

1. **信任** — 這是一間真正的學校嗎？我的孩子拿到的文憑有意義嗎？
2. **透明** — 我看得到孩子在學什麼、學得怎麼樣嗎？
3. **結果** — 孩子有在進步嗎？這筆錢花得值得嗎？

---

## ✅ Phase 0 — 上線前堵漏洞（已完成）

> 修掉錯誤承諾與基本可用性問題。家長看到這些不一致就會立刻離開。

- ✅ **0-A FAQ 錯誤承諾** — `AdmissionMain.js` 的 FAQ 早期已修；本輪補修 Tuition 區塊兩處漏網之魚（"Dedicated academic advisor" / "Priority advisor response" → 改成 "Personalized course planning support" / "Priority email support (24h)"）
- ✅ **0-B Pricing Enroll 按鈕** — 早期已從 `mailto:` 改成 `<Link to="/admission">`，本輪驗證確認 OK
- ✅ **0-C Learn Portal 手機版** — 新增 `src/components/pages/Learn/learn-mobile.css`，用 `data-m="..."` attribute 統一 hook 進三個 Learn 頁。768px 以下 stat 卡 4→2、banner 直立、課程卡單欄；380px 以下更緊湊
- ✅ **0-D 拿掉 Cognia 引用** — 不是會員不能寫，全站 0 殘留
- ✅ **0-E 「US-accredited」→「Florida-registered」** — accreditation ≠ private school registration。Footer / Hero / Introduction / AcademicsMain / CourseCatalog / SEO meta 全改完。SchoolProfile 既有「in the process of pursuing regional accreditation」誠實說法保留
- ✅ **0-F 大學校名統一** — Syracuse University (SIT) → Syracuse University；NJIT → New Jersey Institute of Technology；UCSB → UC Santa Barbara。SuccessStories / HeroSection / AdmissionMain / walkthrough.html 全部對齊
- ✅ **0-G Yunfan/Baoyi GPA 校準** — 從 `server/prisma/seed.js` 重算，兩人之前在 SuccessStories 是顛倒的：
  - Yunfan: 3.78 → **3.85** (UW, 28 完成學分)
  - Baoyi:  3.90 → **3.77** (UW, 29 完成學分)
  - walkthrough.html dashboard + transcript scene 都對齊到 Yunfan 真實數據

---

## ✅ 視覺風格大整修（已完成）

> 把 AI 生成圖換成真實產品截圖。家長對 AI 圖很敏感，看到=立刻打折扣。

- ✅ **首頁 hero** — 移除 `<ImgSlider />` AI 7 張輪播圖，改成 `HeroSection.js`：左側雙語標題 + Founders pricing + 兩 CTA，右側真實 Dashboard 截圖（從 walkthrough 抓的，含 Yunfan 名字、GPA、進度條）+ 信任 strip（Florida Statute · 24-credit · Class of 2026 · Real teacher feedback）
- ✅ **4 個內頁 hero 全換** — 從 walkthrough 各 scene 抓的真實截圖：
  - **Admission** ← `transcript-screen.jpg`（被錄取家長最關心的官方文件）
  - **Discovery** ← `pathways-screen.jpg`（8 條 pathway 全展示）
  - **Academics** ← `module-screen.jpg`（Module 學習頁，看真實內容）
  - **Support** ← `diploma-screen.jpg`（最終目的地：文憑）
- ✅ **孤兒 AI 檔案**（沒被引用，可刪）：`src/img/Homepage/homepage[1-8].png`、`src/img/cognia.png`、`src/img/Homepage/cognia_logo.jpg`、`src/components/pages/Homepage/Homepage/ImgSlider.js`

---

## ✅ Founders Pricing 上線（已完成）

> 降低入手門檻又不打折信任：誠實說「這是限量創校價」。

- **公開價格**：~~$199/月~~ → **$19.90/月** Founders（前 100 名 · 鎖定 12 個月）
- **年付**：~~$1,799/年~~ → **$199/年** Founders（月均約 $16.60）
- **共識**：12 個月後是否漲到原價（或維持），需要 Alan 在 Stripe 整合時設好
- 已改：`HeroSection.js`、`PricingPage.js`、`AdmissionMain.js` Tuition、`walkthrough.html` CTA scene

⚠️ **後續觀察**：$19.9/月 vs Khan Academy ($4-44/月) 同 segment 重疊。如果 Founders 賣完想穩定 retention，需要：
- 推出第二層 tier（$19.9 自學 vs $99 含批改 vs $199 含 advisor）
- 或者誠實漲價時推出有信用的「Beta 用戶終身 50% 折扣」之類

---

## ✅ 行銷資產 — Demo 影片（已完成）

> 解決 ROADMAP 列出的「課程內容無法預覽」流失點。

- ✅ **80 秒自播放 walkthrough** — `public/demo/walkthrough.html`。九個 scene（hook → 8 pathways → dashboard → module → exam → transcript → diploma → parent view → CTA），英文旁白 + 中英雙語字幕
- ✅ **多角色配音** — 4 個 edge-tts 神經語音輪流講：Aria（學校代言）、Guy（學術權威）、Jenny（學生視角）、Andrew（家長視角）
- ✅ **MP4 渲染 pipeline** — `scripts/make-demo.mjs`（idempotent + 多階段 cache）、`scripts/README-demo.md`、`npm run make-demo` 一鍵跑完，且自動 deploy 到 `public/demo/giis-demo.mp4`
- ✅ **首頁嵌入** — `src/components/pages/Homepage/Homepage/HomepageDemo.js`，塞在 Introduction 與 8 Pathways 之間（含 `id="demo"` anchor 給 hero 的「Watch tour」按鈕跳轉）
- ✅ **家長 Dashboard mockup** — `public/demo/parent-dashboard-mockup.html`（給 Phase 1 當設計參考）

### 🔧 Demo 後續小事

- [ ] **(needs Mac)** 在 Mac 上跑一次 `npm run make-demo` 取代 sandbox espeak 預覽版（產出真神經語音版，自動覆蓋到 `public/demo/giis-demo.mp4`）
- ✅ **DemoEmbed 抽成共用 component** — 新建 `src/components/main/DemoEmbed.js`，接受 `language` / `variant` (full|compact) / `eyebrow` / `headline` / `subline` / `showCtas` / `primaryCtaTo` 等 props。`HomepageDemo.js` 改成 wrapper 用 full variant；`AdmissionMain.js` 在 Steps 後 + Requirements 前用 compact variant（"Before You Apply · 看清楚孩子會經歷什麼"）；`PricingPage.js` 在價格卡前用 compact variant（"$19.90 unlocks · 付費前先看清楚平台"）。grep `<source src="/demo/giis-demo.mp4"` 只剩 DemoEmbed.js 一處

---

## 🚧 Phase 1 — 讓家長能「看到」孩子在學習

> 目標：家長打開手機就能知道孩子這週做了什麼。

### ✅ 0. 公開可瀏覽的 Parent Dashboard demo（已完成 — 早期）

`src/components/pages/Parent/ParentDashboardDemo.js` 上線於 `/parent/demo`。完整重現未來家長面板的視覺，含 Yunfan 真實 seed 數據（22/24 學分、3.85 GPA、3 進行中課程、advisor note 用 Shiyu Zhang Ph.D. 名義）。雙語、頂部黃色 PREVIEW banner 強調是示例資料、底部 CTA 引導 Apply / Pricing。Pricing 頁的 CTA 區塊也加了「Or preview the parent dashboard you'll get」連結指過來。

未來 Phase 1 #1 真實 logged-in 版上線時，這頁保留作為 marketing 入口（不需要登入）。

---

### 1. 把家長 Dashboard mockup 轉成真的 React 頁面

**設計來源**：`public/demo/parent-dashboard-mockup.html`（已完成的視覺草稿，含 student hero、active courses、recent activity、advisor note、upcoming、quick links、weekly digest）

**檔案**：
- 新建 `src/components/pages/Parent/ParentDashboard.js`
- 新建 `src/components/pages/Parent/ParentLogin.js`
- `src/App.js` 加 routes：`/parent/login`、`/parent/dashboard`
- `src/api/parentAuth.js` — 仿 `src/api/authStorage.js` 寫一個 parent session

**Acceptance**：
- 家長用 email + password 登入
- Dashboard 顯示孩子的學分、GPA、進行中課程、最近活動、advisor note
- 跑 `npm run build` 沒 error
- 手機 (≤768px) sidebar 折到下方、stat 變 2 欄

**依賴**：先做下面的 #2 schema 與 API。

---

### 2. Schema：`ParentAccount` 與 `Student.parentEmail`

**檔案**：`server/prisma/schema.prisma`

**新增 model**：
```prisma
model ParentAccount {
  id           String   @id @default(cuid())
  email        String   @unique
  passwordHash String
  studentId    String
  student      Student  @relation(fields: [studentId], references: [id])
  createdAt    DateTime @default(now())
  lastLoginAt  DateTime?
}
```

**改 Student**：加 `parentEmail String?`、加 `parentAccounts ParentAccount[]` 反向關聯。

**Acceptance**：
- `npx prisma migrate dev --name add_parent_account` 過
- Admin UI 建立學生時可填 parentEmail（先放 form，後端寫入即可）
- 一個 student 可以有多個 ParentAccount（離婚家長 / 雙親各自登入）

---

### 3. API：家長登入 + Dashboard 資料

**新檔**：
- `server/src/routes/parent-auth.js`
  - `POST /api/parent/login` → bcrypt 比對 → 回傳 JWT
  - `POST /api/parent/setup` → 用一次性 token 設定密碼（admin 寄邀請信用）
- `server/src/routes/parent-data.js`
  - `GET /api/parent/me` → 認證後回傳家長綁定的 student 資料（複用現有的 transcript / enrollments query，但只能看自己孩子）

**Acceptance**：
- Postman 測試：登入後 `Authorization: Bearer <token>` 能拿到 JSON 結構（student, enrollments[], recentActivity[], advisorNote）
- 沒登入 / 用別的 student id → 401 / 403
- `server/src/index.js` 把新 routes 掛上去

---

### 4. 每週進度 Email 報告（Resend）

> 不需要家長登入，系統主動推訊息。Phase 1 最重要的單一功能。

**檔案**：
- 新建 `server/src/jobs/weekly-digest.js` — 計算過去 7 天每個學生的活動，組成 HTML email
- 新建 `server/src/templates/weekly-digest.html` — Handlebars / nunjucks 模板
- `server/src/lib/resend.js` — Resend SDK wrapper
- 部署：用 Render Cron / AWS EventBridge / 簡單 node-cron 每週日 19:00 CST 觸發

**Email 內容**（中英雙語，模仿 mockup 的 advisor note 語氣）：
- 完成的 Module
- Quiz / 考試分數
- 累計學分進度（X / 24）
- 一句話結語（先 hardcode，Phase 3 改成 advisor 真寫）

**Acceptance**：
- 跑 `node server/src/jobs/weekly-digest.js --dry-run` 列出會寄哪些 email
- `--dry-run=false` 真寄出
- 寄出記錄存到 `EmailLog` table（避免重複寄）
- 寄到測試學生 `26-004 Yunfan Yang` 自己的 admin email 看 render

**依賴**：Resend API key（Alan 在 resend.com 拿，存 `server/.env` 的 `RESEND_API_KEY`）

---

### 5. 作業批改 UI + 批改後通知家長

**家長最常問**：「老師有在看我孩子的作業嗎？」

**檔案**：
- 新建 `src/components/pages/Admin/AssignmentQueue.js` — 待批清單（學生姓名、課程、Module、提交時間、內容連結、批分、評語、submit）
- `src/App.js` 加 route `/admin/assignments`
- `server/src/routes/admin-assignments.js`
  - `GET /api/admin/assignments/pending`
  - `PATCH /api/admin/assignments/:id` → 寫 score + feedback，觸發兩封 email（學生 + 家長）
- Schema：`AssignmentSubmission` 新增 `score Decimal?`、`gradedAt DateTime?`、`gradedById String?`

**Acceptance**：
- Admin 在 `/admin/assignments` 看到所有 submission，篩選未批 / 已批
- 批改 submit 後，學生在 `ModulePage` 的 feedback card 立刻顯示新 feedback
- 家長收到 email：「老師批改了 Yunfan 的 [Module 8 作業]」

**依賴**：#4 的 Resend wrapper

---

### ✅ 6. Demo embed 抽成共用 component（已完成）

`src/components/main/DemoEmbed.js` 上線。三個頁面都已切換：
- HomepageDemo (full variant) — Introduction 與 8 Pathways 之間
- AdmissionMain (compact variant, "Before You Apply") — Steps 後
- PricingPage (compact variant, "What $19.90 unlocks") — 價格卡前

Acceptance ✅：video 路徑只在 DemoEmbed.js 寫死。

---

## 💰 Phase 2 — 讓家長能「付款並信任」

### 7. Stripe Checkout 整合

**檔案**：
- `server/src/routes/checkout.js` — `POST /api/checkout/create-session`（建 Stripe Checkout Session，return url 帶 session_id）
- `server/src/routes/webhooks-stripe.js` — `POST /api/webhooks/stripe`（驗 signature、處理 `checkout.session.completed` → 建學生帳號 / 啟用 subscription / 寄歡迎信）
- 新 schema：`Subscription { id, studentId, stripeCustomerId, stripeSubscriptionId, status, currentPeriodEnd }`
- 前端 `PricingPage.js` Apply Now → POST `/api/checkout/create-session` → `window.location = checkoutUrl`

**Acceptance**：
- Stripe test mode 跑通：填 `4242 4242 4242 4242` 之後自動建學生帳號 + 寄出歡迎信
- Webhook 在 Stripe Dashboard 測試 `checkout.session.completed` 能收到並回 200
- Subscription 過期前 7 天自動寄續費提醒（Phase 3 再做）

**依賴**：#4 的 Resend wrapper

---

### 8. 入學流程（`/apply`）

**檔案**：
- 新建 `src/components/pages/Apply/ApplyForm.js` — 學生姓名、生日、grade level、家長姓名、家長 email、電話
- `server/src/routes/applications.js` — `POST /api/applications`（存 `Application` row、寄 admin 通知 + 家長確認信）
- 新 schema：`Application { id, studentName, dob, gradeLevel, parentName, parentEmail, phone, status, createdAt, reviewedAt, reviewedById }`
- Admin 介面 `src/components/pages/Admin/ApplicationsQueue.js` — 一鍵 approve → 觸發 Stripe checkout link 寄給家長

**Acceptance**：訪客填表→admin 審核→家長收到付款 link→付完款→學生帳號自動建立。

---

### 9. 文憑 / 成績單驗證 QR

**檔案**：
- `src/components/pages/Diploma/DiplomaPage.js` 與 `Transcript/TranscriptContent.js` 加 QR code（`qrcode.react`）指向 `/verify/:studentCode`
- 新建 `src/components/pages/Verify/VerifyPage.js` — 公開頁，輸入學號或掃 QR 顯示「此文件由 GIIS 官方發出，學生：XXX，發證日期：XXXX」
- `server/src/routes/verify.js` — `GET /api/verify/:code` 回傳最小公開資料（姓名、發證日期、是否畢業）

**Acceptance**：列印的成績單上掃 QR 就能驗證真偽，不需登入。

---

## 🔁 Phase 3 — 留住付費用戶

### 10. Advisor 筆記 + 學期建議

- Admin 對每位學生留 markdown 筆記（`AdvisorNote { studentId, body, createdAt, authorId }`）
- 家長 Dashboard 的「Advisor note」區塊讀最新一筆（mockup 已有版位）
- 每學期初 cron job 自動寄出「建議下學期選修」email（用 pathway + 已完成課程算）

### 11. 學期總結報告 PDF

- 既有的 `transcriptPdf.js` 已能生成成績單 PDF，extend 為 semester report
- cron job 每學期末（5/31, 12/31）自動生成 + 寄出

### 12. 忘記密碼（學生 + 家長）

- `POST /api/auth/forgot-password` → 寄 reset link（24h 有效）
- `src/components/pages/Auth/ResetPassword.js`
- 學生 + 家長共用同一條 flow

### 13. 考試冷卻倒計時

- 既有的 exam attempt 有 `nextAttemptAt`，UI 把這欄轉成 "還要等 X 小時 Y 分鐘"
- 改 `src/components/pages/Learn/ExamPage.js`

---

## 📈 Phase 4 — 規模化

> 等有穩定付費用戶後才考慮，列項即可。

| 區塊 | 功能 | 對應檔案概念 |
|------|------|-------------|
| Admin | 課程 / 題目管理 UI | 取代手改 JSON + re-seed |
| Admin | 批量學生匯入 CSV | `/admin/students/bulk-import` |
| Admin | 學生進度看板 | `/admin/students/dashboard` 一頁看誰卡關 |
| Admin | 代替學生加退課 | 在 student profile 頁加 enrollment 編輯 |
| Student | 課程進度條 | `LearnDashboard.js` 課程卡顯示 X/Y modules |
| Student | Quiz 失敗引導 | 沒過時建議複習特定章節 |
| Student | 作業檔案上傳 | Cloudflare R2 / S3 |
| Student | Q&A 討論區 | 每個 Module 下方 |
| 成長 | 推薦人機制 | 雙方學費折扣 |
| 成長 | Alumni 展示頁 | 畢業生大學去處 |

---

## 🛠️ 技術債

| 項目 | 影響 | 對應檔案 |
|------|------|---------|
| 移除 Bootstrap | Bundle 減 ~200KB | grep `bootstrap`，主要在 `Header/`、`Footer/` |
| 移除 react-slick → CSS scroll-snap | 少 2 個套件 | `ImgSlider.js` |
| 首頁圖片轉 WebP | 載入快 3-4 倍 | `src/img/Homepage/*.png` → 用 sharp 一次轉 |
| Login / exam submit rate limiting | 安全 | `server/src/middleware/rate-limit.js` (新建) |
| Server-side PDF（Puppeteer） | PDF 品質穩定 | 取代現有 jspdf |

---

## 📝 Code Mode 須知（這輪建立的慣例）

### Demo pipeline
- 字幕 source of truth：`public/demo/walkthrough.html` 的 `const CAPTIONS = [...]`
- `make-demo.mjs` 自動 parse 出來，不要在 `make-demo.mjs` 裡另外 hardcode 字幕
- 改字幕後跑 `npm run make-demo:audio && npm run make-demo:merge`（不用全 force）

### 4-voice cast convention
- Aria（學校代言）、Guy（學術權威）、Jenny（學生視角）、Andrew（家長視角）
- 新增 scene 時要決定哪個 persona 講
- 列所有可選聲音：`edge-tts --list-voices | grep en-`

### 手機 CSS pattern
- 不重寫 inline style，新增 `data-m="..."` attribute hook 到 `learn-mobile.css`
- 命名：`learn-page` / `welcome-row` / `stat-grid` / `banner-row` / `course-grid` / `breadcrumb` / `course-stats`
- 新頁也用同一條 css，加新 `data-m` 命名先看 css 已有哪些可重用

### 雙語慣例
- 所有家長 / 行銷面文案用 `language` prop 切換 EN/中文
- 中文用簡體（`zh-CN`），跟既有 `siteStrings.js` 一致
- Admin 介面英文即可（給 Alan 用）

### 校長簽名（不要再寫錯）
- 校長：**Shiyu Zhang, Ph.D.**，職稱 **President & Principal**
- 第二簽名線是畢業生本人
- 參考：`src/components/pages/Diploma/DiplomaPage.js` line 337

---

## 開發優先序總結

```
Phase 1（讓家長看到）：
  Demo 補放 Admission/Pricing → Parent Dashboard 真版 → Schema + API → 週報 email → 作業批改 UI

Phase 2（讓錢進來）：
  Stripe → /apply → 文憑驗證 QR

Phase 3（留住付費用戶）：
  Advisor 筆記 → 學期報告 → 密碼重設 → 考試冷卻

Phase 4（有規模再做）：
  Admin 課程 UI → 批量操作 → 討論區
```

---

## 環境資訊

- **Frontend:** React 18 / react-router-dom v6 / Netlify
- **Backend:** Express + Prisma ORM + PostgreSQL / 目標 AWS Lightsail
- **Email（待接）:** Resend（免費 3,000 封/月，API key 在 resend.com）
- **付款（待接）:** Stripe（Phase 2）
- **TTS（demo 用）:** edge-tts（`pip3 install edge-tts`）
- **學生資料備份:** `server/data-backup/students_transcript_export.json`

## 測試帳號

| Code | 姓名 | Email |
|------|------|-------|
| 26-001 | Ruwen Li | ruwen.li@genesisideas.school |
| 26-002 | Tao Zhang | tao.zhang@genesisideas.school |
| 26-003 | Baoyi Lu ★ | baoyi.lu@genesisideas.school |
| 26-004 | Yunfan Yang ★ | yunfan.yang@genesisideas.school |

★ Yunfan Yang 有最多考試記錄，最適合測試（demo 也以他為主角）。
