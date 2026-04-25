# 成績單後端設計說明

## 目標

- 持久化儲存每位學生的**成績單抬頭資料**（姓名、地址、日期等）與**各學期課程列**（課名、類型、學分、等第、加權／未加權 GPA 欄位）。
- **管理員**透過帳密登入後，可對任意學生進行新增／編輯／刪除（透過 API；前端管理介面可再接此 API）。

## 技術選型

| 項目 | 建議 | 說明 |
|------|------|------|
| 執行環境 | Node.js 18+ | 與現有 CRA 分離，獨立 `server/` 部署。 |
| HTTP | Express | 簡單、生態成熟。 |
| ORM | Prisma | 型別清楚、遷移與 SQLite/PostgreSQL 切換容易。 |
| 開發用 DB | PostgreSQL（Docker）或 SQLite | 本機可用 repo 根目錄 `docker compose up -d`；`DATABASE_URL` 見 `server/.env.example`。 |
| 管理員認證 | JWT（HS256）+ bcrypt 雜湊密碼 | 無狀態 API；`Authorization: Bearer <token>`。 |

## 資料模型（ER 概要）

```
AdminUser
  id, email (unique), passwordHash, timestamps

Student
  id, name, birthDate, gender, parentGuardian,
  address, city, province, zipCode,
  entryDate, withdrawalDate, graduationDate, transcriptDate,
  timestamps

Semester（屬於某 Student；每學期一筆）
  id, studentId, key（例："Grade 9 - Fall Semester"）, sortOrder
  @@unique([studentId, key])

CourseRow（屬於某 Semester）
  id, semesterId, sortOrder,
  courseName, courseType, credits, letterGrade,
  weightedGpa, unweightedGpa（與前端列一致，可後端重算驗證）
```

學期 `key` 與前端 `TranscriptContent` 中傳入的 `semesterName` 字串對齊，便於之後前端改為「依學生 id 拉資料」。

## API 一覽（建議）

| 方法 | 路徑 | 認證 | 說明 |
|------|------|------|------|
| POST | `/api/auth/register` | 否 | 學生註冊：`{ email, password, name? }` → 建立 `Student` + `StudentAccount`，回 `{ token, role: "student", student }` |
| POST | `/api/auth/login` | 否 | 同一支：先比對 **教職員**，再比對 **學生帳號**。回傳 `role: "admin"` + `admin` 或 `role: "student"` + `student` |
| GET | `/api/auth/me` | 是 | 依 JWT 回傳教職員或學生資訊 |
| GET | `/api/students` | 是（**admin**） | 學生列表（精簡） |
| POST | `/api/students` | 是（**admin**） | 建立學生（僅抬頭；尚無學生登入，除非之後另做綁定） |
| GET | `/api/students/:id` | 是（**admin 或本人學生**） | 單一學生 + 全部學期與課程列 |
| PATCH | `/api/students/:id` | 是（**admin 或本人**） | 更新抬頭欄位 |
| DELETE | `/api/students/:id` | 是（**admin**） | 刪除學生（級聯刪學期／課程／學生帳號） |
| PUT | `/api/students/:id/transcript` | 是（**admin 或本人**） | **整份成績單取代**：body 含 `semesters[]` 與每學期 `courseRows[]` |

JWT payload：`role` 為 `admin`（含 `adminId`）或 `student`（含 `studentId`）。舊版僅含 `adminId` 的 token 仍視為教職員。

## GPA 與前端一致性

前端 `GradeTable*` 內有等第→GPA 與 AP 加權規則。後端 `server/src/lib/gpa.js` 實作相同規則，在寫入時重算 `weightedGpa` / `unweightedGpa`，避免髒資料。

## 安全與部署注意

1. **環境變數**：`JWT_SECRET`（必填）、`DATABASE_URL`、`ADMIN_SEED_PASSWORD`（僅 seed 用）。
2. **HTTPS**：正式環境必須；Cookie 若日後改 Session 也需 `Secure`。
3. **CORS**：只允許你的前端網域（例：`https://genesisideas.school`）。
4. **Rate limit**：登入路由建議加限流（可後續用 `express-rate-limit`）。
5. **備份**：PostgreSQL 定期快照；SQLite 則備份 `dev.db` 檔。

## 與 CRA 前端整合步驟（後續）

1. 設定 `REACT_APP_API_BASE_URL` 指向此 API。
2. 成績單頁：改為 `GET /api/students/:id` 帶入表單；儲存時 `PUT .../transcript`（需 admin 登入後帶 JWT）。
3. 新增獨立 **Admin** 路由或子網域，只做登入 + 學生選擇 + 編輯表單。

## 本目錄指令

```bash
cd server
cp .env.example .env
npm install
npx prisma generate
npx prisma db push
npm run db:seed
npm run dev
```

預設管理員見 `.env.example`；**上線前務必改密碼並改 `JWT_SECRET`。**
