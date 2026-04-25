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

const demoStudentSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English 9',           'Core',       '1',   'A'),
      courseRow(1, 'Algebra I',           'Core',       '1',   'B+'),
      courseRow(2, 'Biology',             'Core',       '1',   'A-'),
      courseRow(3, 'World History',       'Core',       '1',   'B'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English 9',           'Core',       '1',   'A-'),
      courseRow(1, 'Algebra I',           'Core',       '1',   'B'),
      courseRow(2, 'Biology',             'Core',       '1',   'B+'),
      courseRow(3, 'Physical Education',  'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English 10',          'Core',       '1',   'A'),
      courseRow(1, 'Geometry',            'Core',       '1',   'A-'),
      courseRow(2, 'Chemistry',           'Core',       '1',   'B+'),
      courseRow(3, 'World History II',    'Core',       '1',   'A'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English 10',          'Core',       '1',   'B+'),
      courseRow(1, 'Geometry',            'Core',       '1',   'A'),
      courseRow(2, 'Chemistry',           'Core',       '1',   'A-'),
      courseRow(3, 'Art Foundations',     'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'AP English Language', 'Core (AP)',  '1',   'B+'),
      courseRow(1, 'Pre-Calculus',        'Core',       '1',   'A'),
      courseRow(2, 'AP Environmental Science', 'Core (AP)', '1', 'A-'),
      courseRow(3, 'US History',          'Core',       '1',   'B+'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'AP English Language', 'Core (AP)',  '1',   'A'),
      courseRow(1, 'Pre-Calculus',        'Core',       '1',   'A-'),
      courseRow(2, 'AP Environmental Science', 'Core (AP)', '1', 'B+'),
      courseRow(3, 'Computer Science',    'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'AP English Literature', 'Core (AP)', '1',  'A'),
      courseRow(1, 'AP Calculus AB',      'Core (AP)',  '1',   'A-'),
      courseRow(2, 'Physics',             'Core',       '1',   'B+'),
      courseRow(3, 'Economics',           'Core',       '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'AP English Literature', 'Core (AP)', '1',  'A-'),
      courseRow(1, 'AP Calculus AB',      'Core (AP)',  '1',   'A'),
      courseRow(2, 'Physics',             'Core',       '1',   'A-'),
      courseRow(3, 'Senior Capstone',     'Elective',   '0.5', 'A'),
    ],
  },
]);

const alexChenSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English 9',           'Core',       '1',   'B+'),
      courseRow(1, 'Algebra I',           'Core',       '1',   'A'),
      courseRow(2, 'Earth Science',       'Core',       '1',   'A-'),
      courseRow(3, 'World Geography',     'Core',       '1',   'B'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English 9',           'Core',       '1',   'A'),
      courseRow(1, 'Algebra I',           'Core',       '1',   'A-'),
      courseRow(2, 'Earth Science',       'Core',       '1',   'B+'),
      courseRow(3, 'Art Foundations',     'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English 10',          'Core',       '1',   'A-'),
      courseRow(1, 'Algebra II',          'Core',       '1',   'A'),
      courseRow(2, 'Biology',             'Core',       '1',   'A'),
      courseRow(3, 'US History',          'Core',       '1',   'B+'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English 10',          'Core',       '1',   'A'),
      courseRow(1, 'Algebra II',          'Core',       '1',   'A-'),
      courseRow(2, 'Biology',             'Core',       '1',   'A'),
      courseRow(3, 'Drama',               'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'AP English Language', 'Core (AP)',  '1',   'A'),
      courseRow(1, 'AP Calculus BC',      'Core (AP)',  '1',   'A'),
      courseRow(2, 'Chemistry',           'Core',       '1',   'A-'),
      courseRow(3, 'Government',          'Core',       '0.5', 'B+'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'AP English Language', 'Core (AP)',  '1',   'A'),
      courseRow(1, 'AP Calculus BC',      'Core (AP)',  '1',   'A'),
      courseRow(2, 'Chemistry',           'Core',       '1',   'A'),
      courseRow(3, 'Computer Science',    'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'AP English Literature', 'Core (AP)', '1',  'A'),
      courseRow(1, 'AP Statistics',       'Core (AP)',  '1',   'A'),
      courseRow(2, 'AP Physics C',        'Core (AP)',  '1',   'A-'),
      courseRow(3, 'Economics',           'Core',       '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'AP English Literature', 'Core (AP)', '1',  'A'),
      courseRow(1, 'AP Statistics',       'Core (AP)',  '1',   'A'),
      courseRow(2, 'AP Physics C',        'Core (AP)',  '1',   'A'),
      courseRow(3, 'Senior Capstone',     'Elective',   '0.5', 'A'),
    ],
  },
]);

const taoZhangSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English I',                    'Core',       '1',   'A-'),
      courseRow(1, 'Algebra I',                    'Core',       '1',   'A-'),
      courseRow(2, 'Biology',                      'Core',       '1',   'B+'),
      courseRow(3, 'World History',                'Core',       '0.5', 'A-'),
      courseRow(4, 'Introduction to Psychology',   'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English I - Writing',          'Core',       '1',   'A-'),
      courseRow(1, 'Geometry',                     'Core',       '1',   'A-'),
      courseRow(2, 'Environmental Science',        'Core',       '1',   'A-'),
      courseRow(3, 'Geography',                    'Core',       '0.5', 'A-'),
      courseRow(4, 'Human Development',            'Elective',   '0.5', 'A'),
      courseRow(5, 'Health & Wellness',            'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English II',                   'Core',       '1',   'A'),
      courseRow(1, 'Algebra II',                   'Core',       '1',   'A-'),
      courseRow(2, 'Chemistry',                    'Core',       '1',   'A-'),
      courseRow(3, 'U.S. History',                 'Core',       '0.5', 'A'),
      courseRow(4, 'Psychology Foundations',       'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English II - Literature',      'Core',       '1',   'A'),
      courseRow(1, 'Pre-Calculus',                 'Core',       '1',   'A-'),
      courseRow(2, 'Physics Fundamentals',         'Core',       '1',   'A-'),
      courseRow(3, 'World Politics',               'Core',       '0.5', 'A'),
      courseRow(4, 'Social Psychology',            'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'English III',                  'Core',       '1',   'A-'),
      courseRow(1, 'Statistics',                   'Core',       '1',   'A-'),
      courseRow(2, 'AP Psychology',                'Core (AP)',  '1',   'A'),
      courseRow(3, 'Biology Advanced',             'Core',       '1',   'A-'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'English III - Literature',     'Core',       '1',   'A-'),
      courseRow(1, 'AP Statistics',                'Core (AP)',  '1',   'A-'),
      courseRow(2, 'Government',                   'Core',       '1',   'B+'),
      courseRow(3, 'Cognitive Psychology',         'Elective',   '0.5', 'A'),
      courseRow(4, 'Experimental Psychology',      'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'English IV - Analytical Writing', 'Core',    '1',   'A'),
      courseRow(1, 'AP Biology',                   'Core (AP)',  '1',   'A-'),
      courseRow(2, 'Psychology Seminar / Capstone','Core',       '1',   'A'),
      courseRow(3, 'Behavioral Science',           'Elective',   '0.5', 'A'),
      courseRow(4, 'College Research & Writing',   'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'English IV - Advanced Composition', 'Core', '1',   ''),
      courseRow(1, 'AP Human Geography',           'Core (AP)',  '1',   ''),
      courseRow(2, 'Abnormal Psychology',          'Elective',   '1',   ''),
      courseRow(3, 'Counseling & Mental Health Studies', 'Elective', '1', ''),
    ],
  },
]);

const benWangSemesters = makeSemesters([
  {
    key: 'Grade 9 - Fall Semester', sortOrder: 0, courses: [
      courseRow(0, 'English 9',           'Core',       '1',   'B'),
      courseRow(1, 'Algebra I',           'Core',       '1',   'B+'),
      courseRow(2, 'Biology',             'Core',       '1',   'C+'),
      courseRow(3, 'World History',       'Core',       '1',   'B'),
    ],
  },
  {
    key: 'Grade 9 - Spring Semester', sortOrder: 1, courses: [
      courseRow(0, 'English 9',           'Core',       '1',   'B+'),
      courseRow(1, 'Algebra I',           'Core',       '1',   'B'),
      courseRow(2, 'Biology',             'Core',       '1',   'B-'),
      courseRow(3, 'Physical Education',  'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 10 - Fall Semester', sortOrder: 2, courses: [
      courseRow(0, 'English 10',          'Core',       '1',   'B+'),
      courseRow(1, 'Geometry',            'Core',       '1',   'B'),
      courseRow(2, 'Chemistry',           'Core',       '1',   'C+'),
      courseRow(3, 'World History II',    'Core',       '1',   'B+'),
    ],
  },
  {
    key: 'Grade 10 - Spring Semester', sortOrder: 3, courses: [
      courseRow(0, 'English 10',          'Core',       '1',   'A-'),
      courseRow(1, 'Geometry',            'Core',       '1',   'B+'),
      courseRow(2, 'Chemistry',           'Core',       '1',   'B'),
      courseRow(3, 'Music Theory',        'Elective',   '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 11 - Fall Semester', sortOrder: 4, courses: [
      courseRow(0, 'English 11',          'Core',       '1',   'A-'),
      courseRow(1, 'Algebra II',          'Core',       '1',   'B+'),
      courseRow(2, 'Physics',             'Core',       '1',   'B'),
      courseRow(3, 'US History',          'Core',       '1',   'B+'),
    ],
  },
  {
    key: 'Grade 11 - Spring Semester', sortOrder: 5, courses: [
      courseRow(0, 'English 11',          'Core',       '1',   'A'),
      courseRow(1, 'Algebra II',          'Core',       '1',   'B+'),
      courseRow(2, 'Physics',             'Core',       '1',   'B+'),
      courseRow(3, 'Spanish II',          'Elective',   '0.5', 'B'),
    ],
  },
  {
    key: 'Grade 12 - Fall Semester', sortOrder: 6, courses: [
      courseRow(0, 'AP English Literature', 'Core (AP)', '1',  'B+'),
      courseRow(1, 'Pre-Calculus',        'Core',       '1',   'A-'),
      courseRow(2, 'AP Environmental Science', 'Core (AP)', '1', 'B+'),
      courseRow(3, 'Economics',           'Core',       '0.5', 'A'),
    ],
  },
  {
    key: 'Grade 12 - Spring Semester', sortOrder: 7, courses: [
      courseRow(0, 'AP English Literature', 'Core (AP)', '1',  'A-'),
      courseRow(1, 'Pre-Calculus',        'Core',       '1',   'A'),
      courseRow(2, 'AP Environmental Science', 'Core (AP)', '1', 'A-'),
      courseRow(3, 'Senior Capstone',     'Elective',   '0.5', 'A'),
    ],
  },
]);

async function upsertStudentWithAccount({ email, password, student, semestersCreate }) {
  const existing = await prisma.studentAccount.findUnique({
    where: { email: email.toLowerCase() },
    include: { student: true },
  });

  if (existing) {
    // Delete and recreate to get fresh semester data
    await prisma.$transaction(async (tx) => {
      await tx.studentAccount.delete({ where: { email: email.toLowerCase() } });
      await tx.student.delete({ where: { id: existing.studentId } });
    });
    console.log(`Deleted existing student: ${email}`);
  }

  const passwordHash = await bcrypt.hash(password, 12);

  await prisma.$transaction(async (tx) => {
    const st = await tx.student.create({
      data: {
        ...student,
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

  await upsertStudentWithAccount({
    email: 'demo.student@genesisideas.school',
    password: 'Student2024!!',
    student: {
      name: 'Demo Student',
      gender: 'Female',
      birthDate: new Date('2008-01-15T00:00:00.000Z'),
      parentGuardian: 'Sample Parent',
      address: '123 Example Rd',
      city: 'Austin',
      province: 'TX',
      zipCode: '78701',
      entryDate: new Date('2023-09-01T00:00:00.000Z'),
      transcriptDate: new Date('2026-06-01T00:00:00.000Z'),
    },
    semestersCreate: demoStudentSemesters,
  });

  await upsertStudentWithAccount({
    email: 'alex.chen@genesisideas.school',
    password: 'Student2024!!',
    student: {
      name: 'Alex Chen',
      gender: 'Male',
      birthDate: new Date('2007-05-20T00:00:00.000Z'),
      parentGuardian: 'Wei Chen',
      address: '4500 Maple Ave',
      city: 'Dallas',
      province: 'TX',
      zipCode: '75201',
      entryDate: new Date('2022-08-15T00:00:00.000Z'),
      transcriptDate: new Date('2026-06-01T00:00:00.000Z'),
    },
    semestersCreate: alexChenSemesters,
  });

  await upsertStudentWithAccount({
    email: 'tao.zhang@genesisideas.school',
    password: 'Student2024!!',
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
      transcriptDate: new Date('2026-04-23T00:00:00.000Z'),
      graduationDate: new Date('2026-06-30T00:00:00.000Z'),
    },
    semestersCreate: taoZhangSemesters,
  });

  await upsertStudentWithAccount({
    email: 'ben.wang@genesisideas.school',
    password: 'Student2024!!',
    student: {
      name: 'Ben Wang',
      gender: 'Male',
      birthDate: new Date('2006-11-08T00:00:00.000Z'),
      parentGuardian: 'Lisa Wang',
      address: '88 Oak Lane',
      city: 'Houston',
      province: 'TX',
      zipCode: '77002',
      entryDate: new Date('2021-08-20T00:00:00.000Z'),
      transcriptDate: new Date('2025-06-01T00:00:00.000Z'),
    },
    semestersCreate: benWangSemesters,
  });

  console.log('');
  console.log('=== Student accounts ===');
  console.log('  demo.student@genesisideas.school');
  console.log('  alex.chen@genesisideas.school');
  console.log('  tao.zhang@genesisideas.school');
  console.log('  ben.wang@genesisideas.school');
  console.log('  Password: Student2024!!');
  console.log('');
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(() => prisma.$disconnect());
