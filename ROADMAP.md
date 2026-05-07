# GIIS Platform — Product Roadmap

> 最後更新：2026-05-06（QR 驗證上線 · 考試冷卻倒計時 · 雙層 nav bug 修復）
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

## 🎓 教學影片產線（pilot 完成，等批次擴大）

> 為什麼重要：每個 module 一支 5-30 分鐘授課影片，是家長「看得到孩子在學什麼」的最直接證據（Phase 1 透明度的核心）。Khan Academy 用這條路長大；我們用同一條路 + GIIS 品牌風格 + 中文/英文雙語潛力。

- ✅ **Pilot #1：Algebra I — Module 4（One-Step & Two-Step Equations）** — `teaching-videos/algebra-i-module-4-sample/`。約 6 分鐘，1920×1080，GIIS 校徽配色（maroon `#6B1F2A` + gold `#D4A634` + cream `#FAF6EC`），16 sections 含 2 次 pause-and-try、3s intro/outro 自製合成 chord、英文 Aria 神經語音 + 燒入英文字幕。第一段用珍奶找錢做 hook
- ✅ **Pilot #2：Algebra I — Module 9（Slope & Rate of Change）** — `teaching-videos/algebra-i-module-9-slope/`。約 6 分鐘，15 sections，含**真實 Cartesian graph 視覺**（rise/run 黃線標註）、樓梯陡緩對比 hook、four-flavors-of-slope 卡牌、real-life rate-of-change 對應（速度/儲蓄/坡度/降溫）、常見「混亂順序 sign 錯」陷阱頁
- ✅ **老師人格** — 高中老師 + 一點粘的口吻（"You've been doing algebra since you were a kid", "knock these out like they owe you money", "Module 5 — get spicy", "rate of change — that's just slope wearing a different jacket"）
- ✅ **Lesson-video skill（自包整套）** — `tools/lesson-video/SKILL.md` + `make_lesson.py`（一指令：synth + merge）+ `merge_lesson.py`（合成主程式）+ `intro_music.wav`/`outro_music.wav`（numpy 合成的 C 大調 chord，無版權）。Claude 看到「merge the lesson」就會跑 merge skill
- ✅ **Mac 零依賴** — 透過 `imageio-ffmpeg`（PyPI 套件內建 ffmpeg static binary）讓 Mac 完全不需 `brew install ffmpeg`。`pip install edge-tts imageio-ffmpeg` 一次性裝完就好
- ✅ **跨 ffmpeg 版本 robust** — 解決 ffmpeg 8.1.1 的兩個 breaking changes：(1) `force_style=...` 內逗號 escape 規則改了 → 改用直接生 `subtitles.ass`（樣式內嵌，不靠 cli 參數）；(2) brew 8.x 預設沒 `--enable-libass`（subtitles filter 整個不存在！）→ `find_ffmpeg()` 自動偵測 libass 支援，沒有就 fallback 到 imageio_ffmpeg 的 static binary
- ✅ **Pipeline 全鏈確認** — Claude 寫 `script.json` + 生 slides → user `python3 tools/lesson-video/make_lesson.py teaching-videos/<lesson>/` → 自動 edge-tts 生 Aria MP3 → 自動 merge → MP4 落地。一個指令、ZERO Mac 系統依賴、可重複
- ✅ **跨科目驗證 — English I Module 1（Reading Comprehension）** — `teaching-videos/english-i-module-1-reading/`。約 6 分鐘，14 sections。視覺風格從方程式換成 quote 卡 + parchment 段落底色 + inference 箭頭，但同一個 `make_lesson.py`/`merge_lesson.py` 不用改。Pipeline 確認跨科目通用
- ✅ **每科一位老師（聲音指派）** — Math=Aria 女、Science=Emma 女、English=Andrew 男（最會說故事）、Social Studies=Christopher 男（紀錄片感）、Psychology=Brian 男（溫和）、PE/Health=Jenny 女（教練）、Electives=Aria。寫進 `tools/lesson-video/SKILL.md` 對照表，未來新 module Claude 自動套用。設計用意：每科不同聲音 = 像真學校有不同老師

- ✅ **3 支「正式版」script + slides 完成**（Module 1 EASY 5min / Module 7 MED-HARD 9min / Module 14 HARDEST 12min）— 驗證難度縮放策略可行：簡單模組 ~12 sections，最難模組 ~21 sections 含三種解法 + 鑑別式 + 常見錯誤頁。每支結尾都有「How to actually master this module」slide，明確告訴學生影片只是 ~10-15% 學習量，剩下要做 OpenStax / Khan / assignment / advisor

---

## 🎬 YouTube 自動上傳 + Learn Portal 整合（Phase 1 透明度核心 commit ✅）

> **為什麼這個是 Phase 1 的關鍵成就**：家長 / 潛在家長現在打開 Learn Portal 任何一個有 GIIS 影片的 module，看到的是內嵌 YouTube 播放器播自己學校老師講課 — 不再只有外部 Khan Academy 連結。「我看得到孩子在學什麼」這個承諾從文字變成可點擊。

- ✅ **YouTube channel 上線** — Brand Account「Genesis of Ideas International」，校徽 logo，Florida-registered 描述，phone-verified（自訂縮圖權限解鎖）
- ✅ **Google Cloud + OAuth 設定** — `giis-youtube-uploader` GCP project，YouTube Data API v3 啟用，Desktop OAuth client，`client_secret.json` + `token.json` 在 `tools/youtube-upload/` 並寫進 .gitignore
- ✅ **`tools/youtube-upload/` 套組** — 4 支 Python：
  - `upload_video.py`（底層）— 任何 MP4 + metadata 上傳
  - `upload_lesson.py`（高層）— 吃 lesson folder，自動建 title / description / chapter timestamps（從 wav 算）/ 附 SRT / 縮圖 / **加進 course playlist**（不存在自動建）/ **寫 video ID 回 script.json** / **重 build manifest**
  - `playlist.py` — list / show / create / add / remove / reorder / delete
  - `build_manifest.py` — 走過所有 `teaching-videos/*/script.json`，聚合到 `public/data/lessons-manifest.json` 給 React 讀
- ✅ **3 支 lesson 已上 YouTube + 在對的 playlist**：
  - Algebra I — Module 4 (`AMF3Wj4cycs`) → Algebra I playlist
  - Algebra I — Module 9 (`TovkiAsNLms`) → Algebra I playlist
  - English I — Module 1 (`tt_hC7TqUPA`) → English I playlist
  - 所有 unlisted（link 才能看，不出現在 channel 公開頁）
- ✅ **`<LessonVideoEmbed />` React 元件** — `src/components/main/LessonVideoEmbed.js`。吃 `course` + `moduleNumber` props，fetch manifest 找對應 video，找到顯示 16:9 in-page YouTube embed + GIIS-branded header（紅色 maroon），找不到 render `null`（安全 — 還沒上的 module 自動隱藏）
- ✅ **`ModulePage.js` 已接通** — Learn Portal 任何 module 頁都有 `<LessonVideoEmbed course={course.name} moduleNumber={mod.order} />` 在 Objectives 之後 / Study Resources 之前。零 schema 改動，未來新上傳的影片自動出現在對的 module 頁
- ✅ **Pipeline 端到端 idempotent** — 從「Claude 寫 script」一路到「家長在 Learn Portal 看到影片」，過程中每一步都可以重跑、重組合、不會破壞前面的成果

### 🔧 教學影片產線後續

- [ ] **(needs feedback)** Alan 看完 3 支已上 YouTube 的 sample 後，對 tone / 配色 / pause 節奏 / 字幕字級 / 語速給 feedback → 微調 baseline。Quota 警告：今天已用 ~9,750 / 10,000，接近上限
- [ ] **明天上 school intro** — 80 秒 walkthrough 影片 (`public/demo/giis-demo.mp4`) 用 `upload_video.py` 直傳，**privacy=public**（區別於 lesson 的 unlisted），不進任何 lesson playlist。指令在 `tools/youtube-upload/RUN_AFTER_VERIFICATION.md` Step 4
- [ ] **批次第一批：Algebra I 剩下 11 個 modules**（Module 2, 3, 5, 6, 8, 10, 11, 12, 13；其中 1, 7, 14 的 script+slides 已寫好但還沒上）— 每支 ~5-12 min。每天上限 4 支（quota），預計分 3 天。
- [ ] **slide_kit 模板化** — `tools/lesson-video/slide_kit.py`，抽出重複的 `title_slide() / pause_slide() / equation_slide() / graph_slide() / path_slide()` helpers。讓寫新 module 從 ~250 行 PIL 代碼降到 ~50 行純 data
- [ ] **跨科目擴充** — Algebra I 完成後，依家長 demo 頻率排序：English I 全 14 module → Biology → Psychology Foundations → Chemistry → Economics → ...
- [ ] **AI tutor / quiz 自動批改**（Phase 1 → Phase 2 過渡）— 影片只是 lecture，學生看完需要練 + 反饋。Khan Academy 模型成功的關鍵不是影片是 graded practice。我們現在 module 頁有 quiz section 但內容空，要規劃題庫怎麼產生（人工 vs AI），怎麼批改

### 📁 Pilot 目錄索引

```
teaching-videos/algebra-i-module-4-sample/
├── algebra_i_module_4_sample.mp4    # 最終影片（覆蓋舊版時跑 merge skill 即可）
├── subtitles.srt                    # 英文字幕（可獨立丟 YouTube）
├── script.json                      # 講課腳本（16 sections + 旁白 + 設定）
├── slides/                          # 16 張 1920×1080 PNG（GIIS 配色）
├── build_slides.py                  # 重新生 slides 用
├── synth_audio_local.py             # Mac 端跑 edge-tts 出 Aria MP3
└── audio/                           # 旁白音檔（mp3/wav）

tools/lesson-video/                  # 共用 merge skill（所有未來 lesson 共用）
├── SKILL.md                         # Claude 觸發說明
├── merge_lesson.py                  # 主程式
├── intro_music.wav                  # 3s 開場合成 chord
└── outro_music.wav                  # 3s 結尾合成 chord
```

---

## ✅ Phase 1 — 讓家長能「看到」孩子在學習（核心已完成）

> 目標：家長打開手機就能知道孩子這週做了什麼。

- ✅ **1-0 公開 Parent Dashboard demo** — `/parent/demo`（`ParentDashboardDemo.js`）：Yunfan 真實 seed 數據、雙語、PREVIEW banner、Pricing 頁 CTA 連結過來
- ✅ **1-1 Parent Dashboard 真版** — `ParentDashboard.js` 登入後顯示真實 API 數據（學分、GPA、進行中課程、活動紀錄）；`ParentLogin.js` cookie-based 登入；`src/api/authStorage.js` 加 parent session helpers
- ✅ **1-2 Schema** — `ParentAccount`、`Application`、`Student.parentEmail`、`AssignmentSubmission.{score, gradedAt, gradedById}` 全加進 `schema.prisma`
  - ⚠️ **待執行**：在 server 上跑 `npx prisma db push` 讓 schema 同步到 PostgreSQL
- ✅ **1-3 API** — `POST /api/parent/login|logout|setup`、`GET /api/parent/me`（學分 + GPA + enrollments + 活動 feed）掛進 `server/src/index.js`
- ✅ **1-5 作業批改 UI** — `AdminAssignmentQueue.js` at `/admin/assignments`：inline 評語 + 分數 + pending/graded filter；`server/src/routes/admin-assignments.js`（GET pending、GET all、PATCH grade）
- ✅ **1-6 Demo embed 共用 component** — `DemoEmbed.js` single source；Homepage / Admission / Pricing 三頁共用；`HomepageDemo.js` 刪除

### 🔧 Phase 1 剩餘（需要外部服務或 Alan 操作）

- [ ] **1-4 每週進度 Email 報告（Resend）** — 需要 `RESEND_API_KEY`（Alan 在 resend.com 拿，免費 3,000 封/月）
  - 檔案：`server/src/jobs/weekly-digest.js`、`server/src/lib/resend.js`、`EmailLog` schema model
  - Acceptance：`node server/src/jobs/weekly-digest.js --dry-run` 可列出；`--dry-run=false` 真寄
  - 作業批改後通知家長的 email 也在這裡補上（`admin-assignments.js` 裡已有 `// TODO` 占位）

- [ ] **Schema 同步** — server 上跑 `npx prisma db push` 讓 ParentAccount / Application / AssignmentSubmission 新欄位生效

- ✅ **Admin 新增學生時填 parentEmail** — `AdminDashboard.js` 新增學生 modal 加 "Parent Portal Email" 欄位；`AdminTranscriptPage.js` 加 `ParentEmailSection` panel（inline edit + PATCH）；server `students.js` schema + allowed list + profileData 全部加了 `parentEmail`

---

### ✅ 1. 把家長 Dashboard mockup 轉成真的 React 頁面（已完成）

`src/components/pages/Parent/ParentDashboard.js` + `ParentLogin.js` 上線於 `/parent/dashboard` 與 `/parent/login`。Cookie-based JWT auth、顯示學生學分 / GPA / 進行中課程 / 最近活動、進度條（completedModules / totalModules，已修復 totalModules 缺失 bug）。雙欄佈局含 `.giis-parent-grid` class，手機版 `@media (max-width: 880px)` 折成單欄。

---

### ✅ 2. Schema：`ParentAccount` 與 `Student.parentEmail`（已完成）

`server/prisma/schema.prisma` 已加入：`ParentAccount`（email, passwordHash, studentId, lastLoginAt）、`Application`（studentName, dob, gradeLevel, parentName, parentEmail, phone, notes, status）、`Student.parentEmail String?`、`AssignmentSubmission.score Decimal?`、`gradedAt DateTime?`、`gradedById String?`。`npx prisma db push` 已同步到本地 DB。

---

### ✅ 3. API：家長登入 + Dashboard 資料（已完成）

- `server/src/routes/parent-auth.js`：`POST /api/parent/login`（bcrypt + cookie JWT）、`POST /api/parent/logout`、`POST /api/parent/setup`（admin 建帳用）
- `server/src/routes/parent-data.js`：`GET /api/parent/me`（cookie auth，回傳 student / stats / enrollments[含 totalModules] / recentActivity）
- 掛載於 `server/src/index.js`

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

### ✅ 5. 作業批改 UI（已完成，email 通知待 Resend）

`src/components/pages/Admin/AssignmentQueue.js` 上線於 `/admin/assignments`。篩選 Pending / Graded / All，展開可填 feedback + score，submit 後即更新。`server/src/routes/admin-assignments.js`：`GET /pending`、`GET /`（帶 `?graded=`）、`PATCH /:id`（寫入 feedback / score / gradedAt / gradedById）。Schema 字段已在 #2 同步。**Email 通知（Resend）留待 #4 的 Resend wrapper 完成後補充。**

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

### ✅ 8. 入學流程 `/apply`（UI 完成，Stripe link 待接）

`src/components/pages/Apply/ApplyForm.js` 上線於 `/apply`（雙語，含驗證，送出後顯示確認畫面）。`server/src/routes/applications.js`：`POST /api/applications`（public）、`GET /api/applications?status=`（admin）、`PATCH /api/applications/:id`（approve/reject）。`src/components/pages/Admin/ApplicationsQueue.js` 上線於 `/admin/applications`。Schema 已同步。**Approve → 寄 Stripe checkout link 待 #7 Stripe 完成後補。**

---

### ✅ 9. 文憑 / 成績單驗證 QR — 已完成

- ✅ `DiplomaPage.js` + `TranscriptContent.js` 加 QR code（`qrcode.react`）指向 `/verify/:studentCode`
- ✅ `VerifyPage.js` at `/verify/:code` — 公開驗證頁，掃 QR 顯示「GIIS 官方發出、學生姓名、發證日期、是否畢業」
- ✅ `server/src/routes/verify.js` — `GET /api/verify/:code`（只回最小公開資料）

Acceptance ✅：列印成績單掃 QR 不需登入可驗真偽。

---

## 🔁 Phase 3 — 留住付費用戶

### ✅ 13. 考試冷卻倒計時 — 已完成

- ✅ `ExamPage.js` — `nextAttemptAt` 轉成 "還要等 X 小時 Y 分鐘" 倒計時 UI，每分鐘自動 refresh

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


---

## 📈 Phase 4 — 規模化

> 等有穩定付費用戶後才考慮，列項即可。

| 區塊 | 功能 | 對應檔案概念 |
|------|------|-------------|
| Admin | 課程 / 題目管理 UI | 取代手改 JSON + re-seed |
| Admin | 批量學生匯入 CSV | `/admin/students/bulk-import` |
| ✅ Admin | 學生進度看板 | `/admin/progress`：活動時間、學分進度條、進行中 / 完成課程數、color-coded badge（今天 / N天前 / Never active）。`server/src/routes/students.js` GET /progress，`src/components/pages/Admin/AdminProgressPage.js`，AdminDashboard 已加入口按鈕 |
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
✅ Phase 1（讓家長看到）— 核心已完成
  剩：週報 email（等 RESEND_API_KEY）、Admin 建學生時填 parentEmail、npx prisma db push

✅ Phase 2 部分完成
  ✅ /apply + ApplicationsQueue
  ✅ 文憑/成績單 QR 驗證
  待：Stripe（等 STRIPE_SECRET_KEY）

Phase 3（留住付費用戶）：
  Advisor 筆記 → 學期報告 → 密碼重設（需要 Resend）
  ✅ 考試冷卻倒計時

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
