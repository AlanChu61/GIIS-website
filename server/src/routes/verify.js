const express = require('express');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();
const router = express.Router();

// GET /api/verify/:code  — public, no auth, returns minimal student info
router.get('/:code', async (req, res) => {
  const code = (req.params.code || '').trim();
  if (!code) return res.status(400).json({ error: 'Student code required' });

  const student = await prisma.student.findUnique({
    where: { studentCode: code },
    select: {
      name: true,
      studentCode: true,
      graduationDate: true,
      transcriptDate: true,
      withdrawalDate: true,
    },
  });

  if (!student) return res.status(404).json({ error: 'Not found' });

  res.json({
    name: student.name,
    studentCode: student.studentCode,
    graduated: !!student.graduationDate,
    graduationDate: student.graduationDate,
    transcriptDate: student.transcriptDate,
    active: !student.withdrawalDate,
  });
});

module.exports = router;
