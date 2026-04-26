/** Shared UI copy: English UI uses English only; Chinese UI uses Chinese only. */

export function getNavStrings(language) {
  const en = language === 'en';
  return {
    discovery: en ? 'DISCOVERY' : '发现我们',
    academics: en ? 'ACADEMICS' : '学术',
    admission: en ? 'ADMISSION' : '入学',
    support: en ? 'STUDENT SUPPORT' : '学生支持',
    langToggleAria: en ? 'Switch to Chinese' : 'Switch to English',
    /** Single entry: student portal (admin uses same page with admin credentials) */
    signIn: en ? 'Login' : '登入',
    dropdownDiscovery: en
      ? [
          { label: 'Meet Our School', to: '/discovery' },
          { label: 'Our Mission',     to: '/discovery' },
          { label: 'About Our Faculty', to: '/discovery' },
        ]
      : [
          { label: '认识学校', to: '/discovery' },
          { label: '办学使命', to: '/discovery' },
          { label: '师资介绍', to: '/discovery' },
        ],
    dropdownAcademics: en
      ? [
          { label: 'Learning Style',      to: '/academics' },
          { label: 'Subjects',            to: '/academics' },
          { label: 'Curriculum Options',  to: '/academics' },
        ]
      : [
          { label: '学习方式', to: '/academics' },
          { label: '学科科目', to: '/academics' },
          { label: '课程选择', to: '/academics' },
        ],
    dropdownAdmission: en
      ? [
          { label: 'Apply Now',      to: '/admission' },
          { label: 'Tuition & Fees', to: '/admission' },
          { label: 'FAQ',            to: '/admission' },
        ]
      : [
          { label: '立即申请',   to: '/admission' },
          { label: '学费与费用', to: '/admission' },
          { label: '常见问题',   to: '/admission' },
        ],
    dropdownSupport: en
      ? [
          { label: 'Academic Advising', to: '/support' },
          { label: 'Life Counseling',   to: '/support' },
        ]
      : [
          { label: '学业辅导', to: '/support' },
          { label: '生活辅导', to: '/support' },
        ],
  };
}

export function getAuthPageStrings(language) {
  const en = language === 'en';
  return {
    portalTitle: en ? 'Student portal' : '學生專區',
    portalSubtitle: en
      ? 'Sign in or create an account to access your transcript.'
      : '登入或註冊帳號以使用線上成績單。',
    tabSignIn: en ? 'Sign in' : '登入',
    tabRegister: en ? 'Register' : '註冊',
    tablistAria: en ? 'Sign in or register' : '登入或註冊',
    signInBlurb: en
      ? 'Sign in with the email and password you used when you registered.'
      : '請使用註冊時的電子郵件與密碼登入。',
    signInCta: en ? 'Sign in' : '登入',
    registerBlurb: en
      ? 'Enter the same information that appears on your official transcript header (name, birth date, guardian, address).'
      : '請填寫與正式成績單抬頭一致的資料（姓名、生日、監護人、住址等）。',
    registerRequiredNote: en
      ? 'Fields marked * are required.'
      : '標示 * 為必填。',
    birthDate: en ? 'Birth date' : '生日',
    gender: en ? 'Gender' : '性別',
    genderFemale: en ? 'Female' : '女',
    genderMale: en ? 'Male' : '男',
    parentGuardian: en ? 'Parent / guardian' : '家長／監護人',
    address: en ? 'Street address' : '地址',
    city: en ? 'City' : '城市',
    province: en ? 'State / province' : '州／省',
    zipCode: en ? 'ZIP / postal code' : '郵遞區號',
    email: en ? 'Email' : '電子郵件',
    password: en ? 'Password' : '密碼',
    displayName: en ? 'Name on transcript' : '成績單姓名',
    passwordHint: en ? 'At least 8 characters.' : '至少 8 個字元。',
    signingIn: en ? 'Signing in…' : '登入中…',
    signIn: en ? 'Sign in' : '登入',
    creating: en ? 'Creating…' : '建立中…',
    createAccount: en ? 'Create account' : '建立帳號',
    loginFailed: en ? 'Login failed' : '登入失敗',
    registerFailed: en ? 'Registration failed' : '註冊失敗',
    unexpectedLogin: en ? 'Unexpected response from server.' : '伺服器回應異常。',
    missingApiUrl: en
      ? 'API address is not configured. Set REACT_APP_API_URL, or run npm start (defaults to http://localhost:4000).'
      : '未設定 API 位址。請設定 REACT_APP_API_URL，或使用 npm start（預設 http://localhost:4000）。',
    backHome: en ? 'Back to site' : '返回網站首頁',
  };
}

export function getHomeSlogan(language) {
  const en = language === 'en';
  return {
    line: en
      ? 'Empowering the next generation of innovators and thinkers'
      : '培育下一代创新者与思想者',
    cta: en ? 'Learn more' : '了解更多',
  };
}

export function getTestimonialCopy(language) {
  const en = language === 'en';
  return {
    title: en ? 'Testimonials' : '学生感言',
    mobileHint: en ? 'Tap a photo to read their story.' : '点击照片查看感言全文。',
    close: en ? 'Close' : '关闭',
  };
}

export const SEO_DEFAULTS = {
  siteName: 'Genesis of Ideas International School',
  siteUrl: 'https://genesisideas.school/',
  // Use absolute URL for og:image when deployed; logo works as fallback
  ogImage: 'https://genesisideas.school/logo512.png',
  twitterCard: 'summary_large_image',
};
