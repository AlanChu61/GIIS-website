# GIIS Platform — Product Roadmap

> 最後更新：2026-05-10（成績單/文憑視覺整修 · 公開校曆頁 · 畢業資格判定 · Nav Login 整合）
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

## ✅ UI/UX 整修（2026-05-10）

> 本輪改善「信任感」三個層面：文件視覺（成績單 + 文憑）、導覽體驗（Login 入口）、管理功能（畢業資格）。

### 成績單 PDF（`transcriptPdf.js`）
- ✅ **顏色統一**：`NAVY = '#1a2d5a'`、`GOLD = '#b8962e'`，Header 底色、badge 邊框、分隔線全部對齊
- ✅ **"OFFICIAL TRANSCRIPT" badge**：金色邊框 + `letterSpacing: 1.5px`，增加正式感
- ✅ **印章鋼印效果**：`grayscale(100%) opacity(0.42) contrast(110%) brightness(130%)` + 雙層 drop-shadow（白色高光 + 深藍陰影），視覺上像金屬壓印
- ✅ **簽名區佈局**：25%（印章）| 15%（空白）| 60%（校長簽名），不再擠在一起
- ✅ **"Official(s) Certifying Transcript:" 佔全寬**，下方底線也全寬對齊
- ✅ **校長資訊修正**：`President & Principal`（之前寫錯）

### 文憑（`DiplomaPage.js`）
- ✅ **印章白色背景修復**：`border-radius:50%; overflow:hidden` clip 掉 JPG 白角 + cream 底色容器
- ✅ **校長簽名**：Pinyon Script 32px `whiteSpace: nowrap`（單行，像真筆跡）
- ✅ **畢業生簽名**：Great Vibes 32px `whiteSpace: nowrap`
- ✅ **移除 "WITH HONORS"**：學校尚未建立 Honors 判定政策，暫不顯示

### 導覽列 Login（`Header.js` + `Nav.js` + `HeroSection.js`）
- ✅ **Header 簡化**：只留 LOGO，移除 Login 按鈕
- ✅ **Nav 完全不放 Login**：Nav 只負責「瀏覽」，不讓 Login 干擾行銷動線
- ✅ **Login 入口移至 Hero**：「Already enrolled? Sign in →」小字，低調放在兩個 CTA 按鈕下方（SaaS 標準做法）
- ✅ **已登入狀態**：Nav 右側仍顯示 My Courses + Profile（學生）或 Parent Portal（家長），session 判定統一用 `studentSession || parentSession`
- ✅ **手機/桌面一致**：三種狀態（未登入 / 學生 / 家長）在手機和桌面顯示相同邏輯

### 公開校曆（`CalendarPage.js`）
- ✅ **`/calendar` 公開頁**：顯示全 5 個學年（2022-23 → 2026-27），雙語（language prop）
- ✅ **從 Nav 可達**：ACADEMICS 下拉 → "Academic Calendar" / "学校日历"
- ✅ **視覺標記**：當前年份標 "CURRENT YEAR"，未來 30 天內的日期綠色標記，過去日期灰色

### 畢業資格判定（`AdminTranscriptPage.js GraduationSection`）
- ✅ **從成績單 CourseRow 計算學分**（`letterGrade` 非空才計入），不從 Enrollment 抓
- ✅ **進度條**：即時顯示 X / 24 學分，及格線 24 學分
- ✅ **校曆整合**：自動顯示 `SPRING_END`（學分截止）和 `CEREMONY_DATE`（典禮日）
- ✅ **"Mark as Graduated" 按鈕**：學分 ≥ 24 才解鎖，點擊後 PATCH `graduationDate = ceremonyDate`
- ✅ **CI/CD 修復**：`netlify.toml CI="false"`（防止 ESLint warning 當 error）、GitHub Actions 升 Node 24

---

## ✅ YouTube 上傳 Scheduler（2026-05 新增）

> 解決「影片做完了沒人記得上傳，等實際上線時 quota 又卡住」的痛點。每天 9am 自動上 4 支，剩下的隔天自動接著。

- ✅ **`tools/youtube-upload/queue.py`** — `status` 子指令掃 `teaching-videos/`，分類成 uploaded / pending / no-mp4 / broken。By-course 條形圖、pending queue、最近上傳清單。`upload` 子指令一次跑 N 支（預設 4，留 quota headroom）
- ✅ **`tools/youtube-upload/daily.sh`** — launchd 用的 wrapper，每次 run 先印 status 再 upload，全部 log 到 `~/Library/Logs/giis-youtube-daily.log`
- ✅ **`tools/youtube-upload/com.giis.youtube-daily.plist`** — macOS launchd job，每天 09:00 自動觸發。`cp` 到 `~/Library/LaunchAgents/` + `launchctl load` 一次性裝完
- ✅ **`npm run yt:status` / `npm run yt:upload`** package.json scripts，日常用最順
- ✅ **Quota maths**：每支 ~2,100 units（upload 1600 + thumbnail 50 + captions 400 + playlist 50），4 支 8,400 / 10,000 daily 留 1,550 headroom
- ✅ **Fail-fast 邏輯**：upload 失敗時 abort 整批，避免燒更多 quota 在同一錯誤
- ✅ **README**：`tools/youtube-upload/QUEUE.md` 完整操作手冊（日常 flow + 一次性安裝 + 故障排除）

**現況**（執行 `npm run yt:status` 結果）：
- ✓ uploaded: 5（4 Algebra I + 1 English I）
- ● pending:  17（含 16 AP Psych 中 15 支 + AP Calc M1 + Algebra I M5）
- ○ no MP4:   4（1 個是 AP Psych M14，可能 make_lesson 沒跑完；3 個是 Algebra 沒做的 module）

**家長可見的影響**：
17 支已渲成的 lecture 每天 4 支上傳，4-5 天內**全部 AP Psychology + AP Calc + Algebra M5 進 Learn Portal**。學生打開 module 頁就看到 `<LessonVideoEmbed>` 拉的對應 YouTube 影片，「家長看得到孩子在學什麼」承諾直接兌現。

---

## ✅ School Calendar 系統（2026-05 新增）

> 為什麼重要：FL 私立學校（Statute 1002.42）的合規要求之一就是公開校曆。同時是家長最常問的三個問題：「什麼時候開學/放假？」「什麼時候出成績單？」「什麼時候發畢業證？」。

- ✅ **`src/config/schoolCalendar.js`** — 單一資料源（兩個 academic year：2025-26 已配齊、2026-27 框架）。導出 `getCurrentAcademicYear()` / `getCurrentTerm()` / `getUpcomingEvents()` / `formatDate()`，今天會自動算進對應 term
- ✅ **`/school-profile` 加 Academic Calendar section**（curriculum 之前）— 5-row table（Fall · Winter Break · Spring · Summer · Graduation 醒目黃底），跑出來會自動帶下方「未來 4 個 key dates」一行；下載成 PDF 時也會印出來給大學申請用
- ✅ **`/parent/demo` 家長 Dashboard quick link 接好** — 「📅 School calendar」現在連到 `/school-profile`；右側欄新增 `UpcomingFromCalendar` 卡，顯示未來 4 個事件 + 「Full calendar →」連結
- ✅ **校曆覆蓋 GIIS 創校以來全部 5 個學年**（2022-23 至 2026-27）：歷史年份 graduation = null（Class of 2026 是第一屆 senior）；SchoolProfile PDF 印出 current-year detail + all-years summary table；強調「online async, Portal 24/7」、把 winter/summer 改成 "recess (admin pause)" 風格、key dates 精簡到只剩 term-meaningful（final exam window + close date）

- ✅ **2025-26 關鍵日期**（FL 私校標準）：
  - Fall: **2025-08-18 → 2025-12-19** · 期末考視窗 12/8 開
  - Winter Break: 12/22 → 1/4
  - Spring: **2026-01-05 → 2026-05-22** · 期末考視窗 5/11 開
  - **畢業典禮 + 數位文憑發放：2026-06-05（週五）**
  - 紙本文憑寄出：2026-06-12
  - 學年末成績單發出：2026-06-12

### 📅 對 Class of 2026 四位學生的具體影響

- ✅ **Fall 2025 (G12 Fall) 成績已在** seed.js（所有 4 人都已 graded）
- ✅ **Spring 2026 (G12 Spring) 真實成績已寫進 seed.js** — 但用 `courseRowGated()` helper gate 在 **2026-05-25** release date。今天 5/10 re-seed 仍顯示空白（in-progress）；5/25 之後 re-seed 自動顯示真實成績。任何日期 re-seed 都「自己對」
  - Ruwen (Business): Eng-Adv-Comp A-, Sociology A-, Business Law A, Corp Finance A → Spring 3.85 GPA, +4 cr
  - Tao (Psychology): Eng-Adv-Comp A, **AP Human Geography A-**, Abnormal Psych A, Counseling A → Spring 4.17W / 3.92U GPA, +4 cr
  - Baoyi (Info Studies): Eng-Adv-Comp/Media A, Sociology A-, Personal Finance A, Digital Media A → Spring 3.92 GPA, +4 cr
  - Yunfan (Engineering/Sports): Eng-Media&Analytical A, Media Psych A, Sports Mgmt&Leadership A → Spring 4.00 GPA, +3 cr
- 🎓 **全部 4 人都會在 2026-06-05 拿到文憑**（都遠超 24 學分門檻）
- 🔧 **覆寫 release date 測試**：`GIIS_SEED_DATE=2026-05-25 npx prisma db seed` 立即看到 grades

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

### 🆕 AP 課程擴充（2026-05 新增）

> 解決「Walkthrough demo 提到的 AP Calc AB 與 AP CS A，seed 裡卻沒有」的不一致問題，順便補 pathway 缺口。

- ✅ **AP Calculus AB**（14 modules，College Board CED 對齊）— `server/prisma/courses/math/ap-calculus-ab.json`，department "Mathematics"。服務 CS / Engineering / Math 三條 pathway
- ✅ **AP Computer Science A**（14 modules，CSAwesome / CodingBat / Practice-It 連結）— `server/prisma/courses/electives/ap-computer-science-a.json`，department "Technology"。服務 CS pathway
- ✅ **AP Calc AB Module 1 — Limits & Continuity** 教學影片 ready：14 sections，~6 min，AriaNeural 語音、math 主題（gold + cream），4 張視覺自製（halfway-to-the-wall hook、one-sided 數線、3 種 DNE mini-graphs、3 種 discontinuity mini-graphs、speedometer real-world）
  - 位置：`teaching-videos/ap-calculus-ab-module-1-limits/`
  - 還缺：audio + MP4。Alan Mac 跑 `python3 tools/lesson-video/make_lesson.py teaching-videos/ap-calculus-ab-module-1-limits/` 即可
- ✅ **AP Psychology Module 2 — Research Methods** script + slides ready：14 sections，~8.7 min（1311 詞 / 150wpm），BrianNeural 語音、psychology 主題（lavender + cream），3 張視覺自製（5-rung methods ladder、−1↔+1 r-coefficient ruler、ice cream / drowning / hot-weather spurious-correlation diagram）。Hook 用 TikTok "coffee makes you live longer" claim 切入 correlation-vs-causation
  - 位置：`teaching-videos/ap-psych-module-2-research-methods/`
  - 還缺：audio + MP4。Alan Mac 跑 `python3 tools/lesson-video/make_lesson.py teaching-videos/ap-psych-module-2-research-methods/` 即可
- ✅ **AP Psychology Module 3 — Biological Bases of Behavior** script + slides ready：14 sections，~8.9 min（1335 詞 / 150wpm），BrianNeural 語音、psychology 主題（lavender + cream），4 張視覺自製（2am-scrolling dopamine/caffeine hook、labeled neuron diagram dendrites→soma→axon→myelin→terminals、6-NT effects table、4-lobe brain diagram with color-coded regions）。Hook 用 2am scrolling + dopamine hits + caffeine blocking adenosine 切入 chemistry-driving-behavior。Pause-answer = GABA inhibitory + glutamate-as-gas/GABA-as-brake mnemonic
  - 位置：`teaching-videos/ap-psych-module-3-biological-bases/`
  - 還缺：audio + MP4。Alan Mac 跑 `python3 tools/lesson-video/make_lesson.py teaching-videos/ap-psych-module-3-biological-bases/` 即可

### 🎯 AP 缺口分析（pathway support）

目前共 **6 支 AP** 在 seed（4 既有 + 2 新增）：
- Statistics (Math) · Psychology · Biology (Science) · Human Geography (Social Studies) · **Calculus AB (Math/Eng/CS)** · **Computer Science A (Tech)**

仍缺（依 pathway 重要性排序）：
- [ ] **AP Microeconomics** + **AP Macroeconomics** — 服務 Business + Economics 兩條 pathway
- [ ] **AP English Language & Composition** — 服務 Communications pathway
- [ ] **AP Physics 1** — 服務 Engineering pathway
- [ ] **AP Calculus BC**（進階）— 服務 Math & Data Science pathway 有志大學數學的學生
- [ ] **AP Art History** 或 **AP 2-D Art and Design** — 服務 Arts & Design pathway

加完後 8 條 pathway 都有至少 1 支 AP 撐場。

### 🎬 下個教學影片建議

- [ ] **AP CS A Module 1 — Primitive Types & Variables**（不同科目 = 不同聲音 = 不同老師感）
  - 建議聲音：`en-US-GuyNeural`（"academic authority" — 跟 walkthrough demo 的 Pathway 場景同個聲音，建立連續感；跟 Math 的 Aria 區分）
  - 需要在 `tools/lesson-video/SKILL.md` 加一行：「Technology / CS → en-US-GuyNeural」

### ✅ AP Psychology 完整一整支課（16 支 modules · 全部 ready 等 Mac TTS）

> 用 parallel agents 把整支 AP Psych 從零做完——這是**第一支完整 GIIS 自製 AP 課程**。
> Total: **16 modules · 224 slides · ~166 分鐘 (2.75 小時) lecture content** · 全部 BrianNeural 配音，lavender 主題。

| # | Module | Slides | ~Min | Hook · 重點 visual |
|---|---|---|---|---|
| M1 | History & Approaches | 13 | 5.9 | 6 心理學家看一個青少年 |
| M2 | Research Methods | 14 | 8.7 | TikTok 咖啡/壽命 · correlation ruler, IV/DV diagram, ice-cream/drowning spurious |
| M3 | Biological Bases | 14 | 8.9 | 2am 滑手機 dopamine · neuron diagram, NT table, 4-lobe brain |
| M4 | Sensation & Perception | 14 | 12.2 | 隱形大猩猩 · Weber's Law, signal detection 2×2, Gestalt 6-cell |
| M5 | States of Consciousness | 15 | 10.7 | all-nighter-feeling-broken · sleep hypnogram, drug categories, 3 dream theories |
| M6 | Learning & Conditioning | 14 | 10.0 | phone buzz/Discord · classical chain, **operant 2×2 (neg-reinforce TRAP)**, schedules quad, Bobo doll |
| M7 | Memory | 14 | 10.3 | 1st-day-of-HS-clothes vs Tuesday-lunch · 3-store flow, Baddeley working memory, levels-of-processing depth, LTM types tree |
| M8 | Cognition & Language | 14 | 12.5 | 飛機新聞→怕飛行 (availability) · heuristics card-row, biases gallery, language timeline, Whorf hypothesis |
| M9 | Motivation & Emotion | 14 | 11.4 | Spotify playlist (intrinsic) · **Yerkes-Dodson inverted-U**, Maslow pyramid, 4-emotion-theories side-by-side |
| M10 | Developmental | 14 | 11.3 | Erikson "you are here" · Piaget timeline, Erikson 8-stage ladder, attachment 4-quadrant, Kohlberg+Gilligan |
| M11 | Personality | 14 | 11.8 | shy-at-school-vs-loud-at-home · Freud iceberg, defense mechanisms 3×2, **Big Five OCEAN spectrum**, reciprocal determinism triangle |
| M12 | Testing & Intelligence | 14 | 11.7 | 浴室秤4次4不同數字 · **dartboard 2×2 (R vs V)**, IQ bell curve ±SD, 3 theories cards, Flynn line chart |
| M13 | Abnormal | 14 | 9.0 | 1-in-5 classroom · 4 D's grid, schizophrenia +/- columns, **3-cluster personality disorders** |
| M14 | Treatment overview | 14 | 10.5 | hopeful pivot from M13 · **Beck cognitive triad triangle**, CBT 3-tools, drug categories table |
| M15 | Treatment Advanced | 14 | 10.3 | 治療要選對工具 · **disorder→treatment matrix**, 3 case vignettes (Maya/Jordan/Alex), group/family/individual compare |
| M16 | Synthesis & AP exam prep | 14 | 10.8 | exam strategy · **M13→M14→M15 flow diagram**, biopsychosocial Venn, **MCQ pattern decoder table**, FRQ rules |

設計重點：
- **每支都有 pause-and-try + 答案**（除 M1 用較舊 layout 13 sections，其餘統一 14）
- **Recap = 5-6 takeaways**
- **Path slide 統一 4 步**：Myers reading + AP Classroom MCQ + dashboard assignment + advisor check-in；M16 例外（exam-prep tone：practice exam + weakest-module review + AP Classroom past FRQs + advisor readiness）
- **校長簽名/政策**：全部誠實（Florida-registered，無 Cognia，無 US-accredited）
- **Treatment trilogy 不重複**（M14 overview / M15 applied cases / M16 exam strategy）

### 🚀 批次 TTS + MP4 指令（Alan 在 Mac 上跑）

整支 AP Psych + AP Calc AB Module 1 一行 for-loop 全部產出 17 支 MP4（**~166 分鐘 lecture + AP Calc 6 分鐘 = 172 分鐘 content**）：

```bash
cd /Users/alanhdchu/GIIS/giis-website

# 一次性裝置（之前若沒裝過）
pip install edge-tts imageio-ffmpeg

# AP Psych 全 16 + AP Calc AB M1 一氣呵成
for d in teaching-videos/ap-psych-module-1-history \
         teaching-videos/ap-psych-module-2-research-methods \
         teaching-videos/ap-psych-module-3-biological-bases \
         teaching-videos/ap-psych-module-4-sensation-perception \
         teaching-videos/ap-psych-module-5-consciousness \
         teaching-videos/ap-psych-module-6-learning \
         teaching-videos/ap-psych-module-7-memory \
         teaching-videos/ap-psych-module-8-cognition \
         teaching-videos/ap-psych-module-9-motivation-emotion \
         teaching-videos/ap-psych-module-10-developmental \
         teaching-videos/ap-psych-module-11-personality \
         teaching-videos/ap-psych-module-12-testing-intelligence \
         teaching-videos/ap-psych-module-13-abnormal \
         teaching-videos/ap-psych-module-14-treatment \
         teaching-videos/ap-psych-module-15-treatment-advanced \
         teaching-videos/ap-psych-module-16-treatment-synthesis \
         teaching-videos/ap-calculus-ab-module-1-limits; do
  echo "=== $d ==="
  python3 tools/lesson-video/make_lesson.py "$d/"
done
```

**估時**：edge-tts 每支 ~2 min synth → ffmpeg 每支 ~5-10 min encode → **整批 17 支跑完約 2-3 小時**（背景跑、不卡 terminal）。每支輸出 MP4 在自己資料夾。

**跑完之後 YouTube 上傳**：用既有的 `tools/youtube-upload/upload_video.py`。建議建一個 "AP Psychology" playlist 把 16 支按順序排好，然後在 Learn Portal 對應 module 頁面自動會用 LessonVideoEmbed 顯示。

跑完之後 YouTube 上傳就用既有的 `tools/youtube-upload/upload_video.py`。

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

## 🏗️ 架構決定（已確認，未來新學生照此實作）

### 學分 → 成績單的單向資料流（已確認，2026-05-10）

> **目標**：Learn Portal 是唯一的數據入口，成績單是衍生輸出，畢業資格由成績單學分決定。

**確認的流向：**
```
學生在 Learn Portal 完成課程
  → Admin 審核 / 系統自動更新 CourseRow（letterGrade + credits）
    → 成績單 PDF 從 CourseRow 生成（已完成）
      → 畢業資格從 CourseRow 學分計算（已完成）
```

**現狀（Class of 2026 四位學生）：**
- CourseRow 是手動維護的，和 Enrollment 系統是兩套獨立數據
- 畢業資格已改成從 CourseRow 計算（`AdminTranscriptPage.js GraduationSection`）
- Enrollment 的 `creditEarned` 不參與畢業計算

**未來新學生需要做的（Phase 3/4 再實作）：**
1. **Learn Portal 完成 → 自動寫 CourseRow**：當學生 `creditEarned = true`（通過期末考），後端自動在對應 Semester 的 CourseRow 插入一行（`courseName`, `credits`, `letterGrade` 從考試分數換算）
2. **Admin 審核流程**：CourseRow 自動生成後標記 `status: 'pending'`，admin 確認或修改後才變 `confirmed`，才會出現在 PDF 成績單
3. **grade release 邏輯保持不變**：`Semester.releaseDate` 控制學生/家長看到成績的時間
- 相關檔案：`server/src/routes/students.js`（PATCH enrollments 觸發 CourseRow）、`server/prisma/schema.prisma`（CourseRow 加 `status` 欄位）

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
