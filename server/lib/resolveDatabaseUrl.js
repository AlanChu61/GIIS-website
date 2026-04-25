/**
 * Loads server/.env then fixes DATABASE_URL in development when it is missing,
 * still SQLite (file:), or non-Postgres — matches docker-compose local Postgres.
 */
require('dotenv').config();

const LOCAL_DOCKER_PG =
  'postgresql://giis:giis_dev@localhost:5432/giis_transcript?schema=public';

function applyDevDatabaseUrlFallback() {
  if (process.env.NODE_ENV === 'production') return;
  const u = (process.env.DATABASE_URL || '').trim();
  if (!u || /^file:/i.test(u) || !/^postgres(ql)?:\/\//i.test(u)) {
    if (u && /^file:/i.test(u)) {
      console.warn(
        '[warn] DATABASE_URL in server/.env points to SQLite (file:). This API uses PostgreSQL only.'
      );
      console.warn('      Using local Docker Postgres instead. Update server/.env or run: docker compose up -d');
    }
    process.env.DATABASE_URL = LOCAL_DOCKER_PG;
  }
}

applyDevDatabaseUrlFallback();

module.exports = { LOCAL_DOCKER_PG, applyDevDatabaseUrlFallback };
