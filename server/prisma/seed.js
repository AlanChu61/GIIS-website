/* eslint-disable no-console */
require('../lib/resolveDatabaseUrl');
const { PrismaClient } = require('@prisma/client');
const bcrypt = require('bcryptjs');
const { computeRowGpa } = require('../src/lib/gpa');

const prisma = new PrismaClient();

function courseRow(sortOrder, courseName, courseType, credits, letterGrade) {
  const gp = computeRowGpa({ courseName, courseType, letterGrade });
  return {
    sortOrder,
    courseName,
    courseType,
    credits: Number.isFinite(parseFloat(String(credits))) ? parseFloat(String(credits)) : null,
    letterGrade,
    weightedGpa: gp.weightedGpa,
    unweightedGpa: gp.unweightedGpa,
  };
}

function makeSemesters(coursesBySemester) {
  return coursesBySemester.map(({ key, sortOrder, courses }) => ({
    key,
    sortOrder,
    courseRows: { create: courses },
  }));
}

// ── Ruwen Li (Class of 2026, #001) ────────────────────────────────────────────
const ruwenLiSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English I',                           'Core',     '1',   'A-'),
      courseRow(1, 'Algebra I',                           'Core',     '1',   'A-'),
      courseRow(2, 'Biology',                             'Core',     '1',   'B+'),
      courseRow(3, 'World History',                       'Core',     '0.5', 'A-'),
      courseRow(4, 'Business Technology & Digital Literacy', 'Elective', '0.5', 'A'),
      courseRow(5, 'Introduction to Business & Economics', 'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English I - Writing',                 'Core',     '1',   'A-'),
      courseRow(1, 'Geometry',                            'Core',     '1',   'A-'),
      courseRow(2, 'Environmental Science',               'Core',     '1',   'A-'),
      courseRow(3, 'Geography',                           'Core',     '0.5', 'A-'),
      courseRow(4, 'Business Media Literacy',             'Elective', '0.5', 'A'),
      courseRow(5, 'Entrepreneurship Fundamentals',       'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English II',                          'Core',     '1',   'A-'),
      courseRow(1, 'Algebra II',                          'Core',     '1',   'A-'),
      courseRow(2, 'Chemistry',                           'Core',     '1',   'B+'),
      courseRow(3, 'U.S. History',                        'Core',     '0.5', 'A'),
      courseRow(4, 'Marketing & Communication',           'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English II - Literature',             'Core',     '1',   'A-'),
      courseRow(1, 'Pre-Calculus',                        'Core',     '1',   'A-'),
      courseRow(2, 'Physics Fundamentals',                'Core',     '1',   'B+'),
      courseRow(3, 'Global Economics & Politics',         'Core',     '0.5', 'A'),
      courseRow(4, 'Leadership Communication',            'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'English III',                         'Core',     '1',   'A'),
      courseRow(1, 'Statistics',                          'Core',     '1',   'A-'),
      courseRow(2, 'Economics',                           'Core',     '1',   'A-'),
      courseRow(3, 'Digital Marketing',                   'Elective', '0.5', 'A'),
      courseRow(4, 'Business Writing',                    'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'English III - Literature',            'Core',     '1',   'A'),
      courseRow(1, 'Government',                          'Core',     '1',   'A-'),
      courseRow(2, 'Business Research Methods',           'Core',     '1',   'A-'),
      courseRow(3, 'Principles of Marketing',             'Elective', '0.5', 'A'),
      courseRow(4, 'Business Ethics & Critical Thinking', 'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'English IV - Writing & Communication', 'Core',    '1',   'A'),
      courseRow(1, 'Economics Seminar',                   'Core',     '1',   'A'),
      courseRow(2, 'Statistics for Social Sciences',      'Core',     '1',   'A-'),
      courseRow(3, 'Organizational Behavior & Communication', 'Elective', '0.5', 'A'),
      courseRow(4, 'Business Strategy & Writing',         'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'English IV - Advanced Composition',   'Core',     '1',   ''),
      courseRow(1, 'Sociology',                           'Core',     '1',   ''),
      courseRow(2, 'Business Law',                        'Elective', '1',   ''),
      courseRow(3, 'Corporate Finance',                   'Elective', '1',   ''),
    ],
  },
]);

// ── Tao Zhang (Class of 2026, #002) ───────────────────────────────────────────
const taoZhangSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English I',                           'Core',     '1',   'A-'),
      courseRow(1, 'Algebra I',                           'Core',     '1',   'A-'),
      courseRow(2, 'Biology',                             'Core',     '1',   'B+'),
      courseRow(3, 'World History',                       'Core',     '0.5', 'A-'),
      courseRow(4, 'Introduction to Psychology',          'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English I - Writing',                 'Core',     '1',   'A-'),
      courseRow(1, 'Geometry',                            'Core',     '1',   'A-'),
      courseRow(2, 'Environmental Science',               'Core',     '1',   'A-'),
      courseRow(3, 'Geography',                           'Core',     '0.5', 'A-'),
      courseRow(4, 'Human Development',                   'Elective', '0.5', 'A'),
      courseRow(5, 'Health & Wellness',                   'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English II',                          'Core',     '1',   'A'),
      courseRow(1, 'Algebra II',                          'Core',     '1',   'A-'),
      courseRow(2, 'Chemistry',                           'Core',     '1',   'A-'),
      courseRow(3, 'U.S. History',                        'Core',     '0.5', 'A'),
      courseRow(4, 'Psychology Foundations',              'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English II - Literature',             'Core',     '1',   'A'),
      courseRow(1, 'Pre-Calculus',                        'Core',     '1',   'A-'),
      courseRow(2, 'Physics Fundamentals',                'Core',     '1',   'A-'),
      courseRow(3, 'World Politics',                      'Core',     '0.5', 'A'),
      courseRow(4, 'Social Psychology',                   'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'English III',                         'Core',     '1',   'A-'),
      courseRow(1, 'Statistics',                          'Core',     '1',   'A-'),
      courseRow(2, 'AP Psychology',                       'Core (AP)', '1',  'A'),
      courseRow(3, 'Biology Advanced',                    'Core',     '1',   'A-'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'English III - Literature',            'Core',     '1',   'A-'),
      courseRow(1, 'AP Statistics',                       'Core (AP)', '1',  'A-'),
      courseRow(2, 'Government',                          'Core',     '1',   'B+'),
      courseRow(3, 'Cognitive Psychology',                'Elective', '0.5', 'A'),
      courseRow(4, 'Experimental Psychology',             'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'English IV - Analytical Writing',     'Core',     '1',   'A'),
      courseRow(1, 'AP Biology',                          'Core (AP)', '1',  'A-'),
      courseRow(2, 'Psychology Seminar / Capstone',       'Core',     '1',   'A'),
      courseRow(3, 'Behavioral Science',                  'Elective', '0.5', 'A'),
      courseRow(4, 'College Research & Writing',          'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'English IV - Advanced Composition',   'Core',     '1',   ''),
      courseRow(1, 'AP Human Geography',                  'Core (AP)', '1',  ''),
      courseRow(2, 'Abnormal Psychology',                 'Elective', '1',   ''),
      courseRow(3, 'Counseling & Mental Health Studies',  'Elective', '1',   ''),
    ],
  },
]);

// ── Baoyi Lu (Class of 2026, #003) ────────────────────────────────────────────
const baoyiLuSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English I',                           'Core',     '1',   'A-'),
      courseRow(1, 'Algebra I',                           'Core',     '1',   'A-'),
      courseRow(2, 'Biology',                             'Core',     '1',   'B+'),
      courseRow(3, 'World History',                       'Core',     '0.5', 'A-'),
      courseRow(4, 'Digital Literacy',                    'Elective', '0.5', 'A'),
      courseRow(5, 'Introduction to Economics',           'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English I - Writing',                 'Core',     '1',   'A-'),
      courseRow(1, 'Geometry',                            'Core',     '1',   'A-'),
      courseRow(2, 'Environmental Science',               'Core',     '1',   'A-'),
      courseRow(3, 'Geography',                           'Core',     '0.5', 'A-'),
      courseRow(4, 'Media Studies',                       'Elective', '0.5', 'A'),
      courseRow(5, 'Study Skills',                        'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English II',                          'Core',     '1',   'A-'),
      courseRow(1, 'Algebra II',                          'Core',     '1',   'A-'),
      courseRow(2, 'Chemistry',                           'Core',     '1',   'B+'),
      courseRow(3, 'U.S. History',                        'Core',     '0.5', 'A'),
      courseRow(4, 'Introduction to Communication',       'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English II - Literature',             'Core',     '1',   'A-'),
      courseRow(1, 'Pre-Calculus',                        'Core',     '1',   'A-'),
      courseRow(2, 'Physics Fundamentals',                'Core',     '1',   'B+'),
      courseRow(3, 'World Politics',                      'Core',     '0.5', 'A'),
      courseRow(4, 'Public Speaking',                     'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'English III',                         'Core',     '1',   'A'),
      courseRow(1, 'Statistics',                          'Core',     '1',   'A-'),
      courseRow(2, 'Economics',                           'Core',     '1',   'A-'),
      courseRow(3, 'Media & Society',                     'Elective', '0.5', 'A'),
      courseRow(4, 'Academic Writing',                    'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'English III - Literature',            'Core',     '1',   'A'),
      courseRow(1, 'Government',                          'Core',     '1',   'A-'),
      courseRow(2, 'Research Methods in Social Science',  'Core',     '1',   'A-'),
      courseRow(3, 'Marketing Basics',                    'Elective', '0.5', 'A'),
      courseRow(4, 'Ethics & Critical Thinking',          'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'English IV - Writing & Communication', 'Core',    '1',   'A'),
      courseRow(1, 'Economics Seminar',                   'Core',     '1',   'A'),
      courseRow(2, 'Statistics for Social Sciences',      'Core',     '1',   'A-'),
      courseRow(3, 'Communication Studies',               'Elective', '0.5', 'A'),
      courseRow(4, 'College Research & Writing',          'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'English IV - Advanced Composition / Media Writing', 'Core', '1', ''),
      courseRow(1, 'Sociology',                           'Core',     '1',   ''),
      courseRow(2, 'Personal Finance / Applied Economics', 'Elective', '1',  ''),
      courseRow(3, 'Digital Media & Society',             'Elective', '1',   ''),
    ],
  },
]);

// ── Yunfan Yang (Class of 2026, #004) ─────────────────────────────────────────
const yunfanYangSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English I',                           'Core',     '1',   'A'),
      courseRow(1, 'Algebra I',                           'Core',     '1',   'A'),
      courseRow(2, 'Biology',                             'Core',     '1',   'B+'),
      courseRow(3, 'World History',                       'Core',     '0.5', 'A'),
      courseRow(4, 'Physical Education',                  'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English I - Writing Focus',           'Core',     '1',   'A'),
      courseRow(1, 'Geometry',                            'Core',     '1',   'B+'),
      courseRow(2, 'Environmental Science',               'Core',     '1',   'A'),
      courseRow(3, 'Geography',                           'Core',     '0.5', 'A-'),
      courseRow(4, 'Health and Nutrition',                'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English II',                          'Core',     '1',   'A'),
      courseRow(1, 'Algebra II',                          'Core',     '1',   'A'),
      courseRow(2, 'Chemistry',                           'Core',     '1',   'A-'),
      courseRow(3, 'U.S. History',                        'Core',     '0.5', 'A'),
      courseRow(4, 'Sports Psychology',                   'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English II - Literature',             'Core',     '1',   'A'),
      courseRow(1, 'Physics Fundamentals',                'Core',     '1',   'A-'),
      courseRow(2, 'Pre-Calculus',                        'Core',     '1',   'A'),
      courseRow(3, 'World Politics',                      'Core',     '0.5', 'A'),
      courseRow(4, 'Sports Management Basics',            'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'English III',                         'Core',     '1',   'A'),
      courseRow(1, 'Statistics',                          'Core',     '1',   'B+'),
      courseRow(2, 'Biology Advanced',                    'Core',     '1',   'A-'),
      courseRow(3, 'Government',                          'Core',     '0.5', 'A'),
      courseRow(4, 'Fitness Leadership',                  'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'English III - Literature',            'Core',     '1',   'A'),
      courseRow(1, 'Physics - Mechanics',                 'Core',     '1',   'A'),
      courseRow(2, 'Economics',                           'Core',     '0.5', 'A-'),
      courseRow(3, 'Trigonometry',                        'Core',     '1',   'B+'),
      courseRow(4, 'Psychology',                          'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'English IV - Writing & Communication', 'Core',    '1',   'A'),
      courseRow(1, 'Calculus',                            'Core',     '1',   'A'),
      courseRow(2, 'Economics Advanced',                  'Core',     '1',   'A-'),
      courseRow(3, 'Business Management or Entrepreneurship', 'Elective', '0.5', 'A'),
      courseRow(4, 'Athletic Training',                   'Elective', '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'English IV - Media & Analytical Writing', 'Core', '1',  ''),
      courseRow(1, 'Media Psychology',                    'Elective', '1',   ''),
      courseRow(2, 'Sports Management & Leadership',      'Elective', '1',   ''),
    ],
  },
]);

async function upsertStudentWithAccount({ email, password, studentCode, student, semestersCreate }) {
  const existing = await prisma.studentAccount.findUnique({
    where: { email: email.toLowerCase() },
    include: { student: true },
  });

  if (existing) {
    await prisma.$transaction(async (tx) => {
      await tx.studentAccount.delete({ where: { email: email.toLowerCase() } });
      await tx.student.delete({ where: { id: existing.studentId } });
    });
    console.log(`Deleted existing student: ${email}`);
  }

  // Also remove any orphaned student with the same studentCode
  if (studentCode) {
    const orphan = await prisma.student.findUnique({ where: { studentCode } });
    if (orphan) {
      await prisma.student.delete({ where: { studentCode } });
      console.log(`Deleted orphaned student with code: ${studentCode}`);
    }
  }

  const passwordHash = await bcrypt.hash(password, 12);

  await prisma.$transaction(async (tx) => {
    const st = await tx.student.create({
      data: {
        ...student,
        studentCode,
        semesters: { create: semestersCreate },
      },
    });
    await tx.studentAccount.create({
      data: {
        email: email.toLowerCase(),
        passwordHash,
        studentId: st.id,
      },
    });
  });
  console.log(`Seeded: ${email} / ${password}`);
}

async function main() {
  const email = (process.env.ADMIN_EMAIL || 'admin@genesisideas.school').toLowerCase();
  const password = process.env.ADMIN_SEED_PASSWORD || 'admin';
  const passwordHash = await bcrypt.hash(password, 12);

  await prisma.adminUser.upsert({
    where: { email },
    update: { passwordHash },
    create: { email, passwordHash },
  });

  console.log('');
  console.log('=== Admin ===');
  console.log(`  Email:    ${email}`);
  console.log(`  Password: ${password}`);
  console.log('');
  console.log('=== Seeding students ===');

  await upsertStudentWithAccount({
    email: 'ruwen.li@genesisideas.school',
    password: 'Student2024!!',
    studentCode: '26-001',
    student: {
      name: 'Ruwen Li',
      gender: 'Female',
      birthDate: new Date('2006-11-27T00:00:00.000Z'),
      parentGuardian: 'Xiaojun Wu',
      address: 'Unit 1802, Building 12, Baopo Apartment, Jing\'an District',
      city: 'Shanghai',
      province: 'Shanghai',
      zipCode: '200000',
      entryDate: new Date('2022-08-15T00:00:00.000Z'),
      graduationDate: new Date('2026-06-30T00:00:00.000Z'),
      transcriptDate: new Date('2026-03-02T00:00:00.000Z'),
    },
    semestersCreate: ruwenLiSemesters,
  });

  await upsertStudentWithAccount({
    email: 'tao.zhang@genesisideas.school',
    password: 'Student2024!!',
    studentCode: '26-002',
    student: {
      name: 'Tao Zhang',
      gender: 'Male',
      birthDate: new Date('2007-02-18T00:00:00.000Z'),
      parentGuardian: 'Xiaoying Zhang',
      address: 'Room 601, No. 72, Lane 99, Jinhe Road',
      city: 'Shanghai',
      province: 'Shanghai',
      zipCode: '200120',
      entryDate: new Date('2022-08-15T00:00:00.000Z'),
      graduationDate: new Date('2026-06-30T00:00:00.000Z'),
      transcriptDate: new Date('2026-04-23T00:00:00.000Z'),
    },
    semestersCreate: taoZhangSemesters,
  });

  await upsertStudentWithAccount({
    email: 'baoyi.lu@genesisideas.school',
    password: 'Student2024!!',
    studentCode: '26-003',
    student: {
      name: 'Baoyi Lu',
      gender: 'Male',
      birthDate: new Date('2007-12-25T00:00:00.000Z'),
      parentGuardian: 'Kaiming Lu',
      address: 'No. 88 Huasheng Road',
      city: 'Cixi',
      province: 'Zhejiang',
      zipCode: '315300',
      entryDate: new Date('2022-08-15T00:00:00.000Z'),
      graduationDate: new Date('2026-06-30T00:00:00.000Z'),
      transcriptDate: new Date('2026-02-06T00:00:00.000Z'),
    },
    semestersCreate: baoyiLuSemesters,
  });

  await upsertStudentWithAccount({
    email: 'yunfan.yang@genesisideas.school',
    password: 'Student2024!!',
    studentCode: '26-004',
    student: {
      name: 'Yunfan Yang',
      gender: 'Female',
      birthDate: new Date('2007-11-01T00:00:00.000Z'),
      parentGuardian: 'Chunxiao Lu',
      address: 'Room 702, Building 9, Poly City Light, Liangxi District',
      city: 'Wuxi',
      province: 'Jiangsu',
      zipCode: '214000',
      entryDate: new Date('2022-08-23T00:00:00.000Z'),
      graduationDate: new Date('2026-06-30T00:00:00.000Z'),
      transcriptDate: new Date('2026-02-06T00:00:00.000Z'),
    },
    semestersCreate: yunfanYangSemesters,
  });

  console.log('');
  console.log('=== Student accounts (password: Student2024!!) ===');
  console.log('  26-001  ruwen.li@genesisideas.school');
  console.log('  26-002  tao.zhang@genesisideas.school');
  console.log('  26-003  baoyi.lu@genesisideas.school');
  console.log('  26-004  yunfan.yang@genesisideas.school');
  console.log('');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => prisma.$disconnect());
