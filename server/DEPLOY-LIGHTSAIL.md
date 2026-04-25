# Transcript API on AWS Lightsail

This server is a plain Node.js + Express + Prisma app. **PostgreSQL** is required (same as local Docker).

## Architecture (typical)

| Piece | Options on Lightsail |
|--------|------------------------|
| API | Ubuntu instance running Node (`node src/index.js` or PM2) |
| Database | **Lightsail PostgreSQL** (managed) *or* Postgres on the same instance |
| Frontend (CRA) | Static build on Lightsail, S3+CloudFront, or Netlify — set `REACT_APP_API_URL` to the API’s public URL |

Keep the database **private**: only allow the API security group / localhost to port `5432`, not the whole internet.

## Environment on the server

1. Copy `server/.env.example` → `server/.env` on the instance.
2. Set **`DATABASE_URL`** to your Postgres connection string.  
   Managed AWS/Lightsail DBs usually need **`sslmode=require`** (see comments in `.env.example`).
3. Set a strong **`JWT_SECRET`** (e.g. `openssl rand -hex 32`).
4. Set **`CORS_ORIGIN`** to your live site, e.g. `https://genesisideas.school` (comma-separated if multiple).
5. If the API is behind the Lightsail load balancer or nginx with HTTPS, set **`TRUST_PROXY=1`**.

## First deploy (schema)

From `server/` on the machine that can reach the database:

```bash
npm ci
npx prisma generate
# Early prototyping only (no migration history):
# npm run db:push
#
# Recommended once you have real data:
# 1) Create migrations in dev:   npm run db:migrate:dev
# 2) Apply in production:        npm run db:migrate:deploy
#
# For a brand-new production database, `migrate deploy` will create tables based on committed migrations.
npm run db:push

# Optional demo admin + demo students (avoid in production if undesired)
npm run db:seed
npm start
```

For ongoing changes, use **Prisma migrations** (`migrate dev` / `migrate deploy`) instead of `db push` once you are past early prototyping.

## Frontend (CRA)

Build with the **public API URL** baked in:

```bash
REACT_APP_API_URL=https://api.your-domain.com npm run build
```

Use the same origin scheme (`https://`) as in `CORS_ORIGIN` on the API.

## Local vs AWS summary

| | Local | Lightsail |
|---|--------|-----------|
| Postgres | `docker compose up -d` (repo root) | Managed DB or self-hosted |
| `DATABASE_URL` | `localhost:5432` (see `.env.example`) | Hostname from AWS console + SSL params if required |
| `CORS_ORIGIN` | `http://localhost:3000` | `https://your-site` |
