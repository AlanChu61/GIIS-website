#!/usr/bin/env node
/**
 * Runs Prisma CLI with the same DATABASE_URL resolution as src/index.js (dev SQLite → local Postgres).
 * Usage: node scripts/prisma-env.cjs db push
 */
require('../lib/resolveDatabaseUrl');
const { execSync } = require('child_process');
const args = process.argv.slice(2).join(' ');
execSync(`npx prisma ${args}`, { stdio: 'inherit', env: process.env });
