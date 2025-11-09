mkdir -p docs

# 1) Company Profile
cat > docs/01_company_profile.yaml <<'YAML'
name: "Sumeet’s Intelligence Lab (SIL)"
industry: "Artificial Intelligence, Consulting, and Education Technology"
founder: "Sumeet Mahadev Jogdanker"
location: "Melbourne, Australia"
mission: "To build secure, intelligent, and personalized AI systems that enhance human performance, creativity, and decision-making."
vision: "Empower every student, creator, and business to have their own private AI that understands their world."
core_values:
  - "Innovation through simplicity"
  - "Privacy-first intelligence"
  - "AI that feels personal"
  - "Balance of logic, empathy, and creativity"
current_projects:
  - "Private LLM for internal AI knowledge retrieval"
  - "HustleMate AI – Productivity and Mental Resilience App"
  - "NFT Certificate Verification Platform for RMIT University"
  - "Digital Strategy Consulting Projects (Toll Group, Zepto, etc.)"
  - "AI Governance Framework using COBIT 2019"
  - "FuzzDocs: IoT Security Evaluation System"
  - "Myself2.0 – Personal AI Clone"
target_audience:
  - "University teams and startups"
  - "Consultants and project managers"
  - "Content creators and entrepreneurs"
  - "Researchers building ethical AI"
YAML

# 2) Business & Consulting Projects Summary
cat > docs/02_business_projects.txt <<'TXT'
== Business & Consulting Projects ==
1. Practera Industry Experience (RMIT)
   - Role: Business Analyst, Project Manager
   - Duration: Nov 2025 cohort
   - Key Outcomes: Stakeholder mapping, digital strategy design, AI integration plans.

2. Toll Group Sustainability Project
   - Focus: Capacity constraints & research-skill gaps in university–industry collaboration.
   - Deliverable: Digital collaboration platform with empathy mapping and SDG alignment.

3. Sagami Brand Expansion (Trade Anywhere)
   - Focus: Business development, event coordination, customer perception analytics.
   - Region: Australia (Melbourne, Sydney, Brisbane)
   - Outcome: Market entry strategy and performance tracking dashboard.

4. Zepto Digital Strategy Report
   - Analyzed Zepto’s operational strengths, conducted SWOT and TOWS analysis.
   - Delivered a digital growth roadmap and innovation strategy.

5. Digital Risk Management for WindWave Enterprises
   - Focus: Cybersecurity, business continuity, and digital resilience framework.

6. Governance and Change (Queensland ICT Projects)
   - Implemented COBIT 2019-based change management intervention.
   - Addressed governance shortfalls in public ICT programs.
TXT

# 3) AI & Technical Projects
cat > docs/03_ai_technical_projects.txt <<'TXT'
== AI & Technical Projects ==
1. NFT Certificate Verification System (RMIT)
   - Blockchain-based digital credentialing solution.
   - Tech Stack: Solidity, Polygon, IPFS, Web3.js, VS Code, MetaMask.
   - Purpose: Enable universities to issue tamper-proof certificates as NFTs.

2. HustleMate AI
   - AI-powered productivity app designed to help students plan, reflect, and stay disciplined.
   - Features: AI voice companion, weekly progress tracker, motivational feedback, habit analysis.
   - Tools: Relevance AI, Make.com, FlutterFlow, Gemini API.

3. Private LLM for AI & Consulting Teams
   - Uses LangChain + Ollama for on-device reasoning over internal datasets.
   - Purpose: Secure, domain-specific LLM that stores internal documents privately.
   - Features: Embedding search, RAG pipeline, and API access.

4. FuzzDocs: IoT Security Evaluation Framework
   - Automated vulnerability testing for IoT ecosystems.
   - Stack: Python, Scapy, and OWASP framework integration.

5. Myself2.0 (AI Clone)
   - A personalized AI model replicating Sumeet’s tone, empathy, and motivational style.
   - Functions: Emotional reasoning, scheduling, and motivational responses.

6. AI Governance and Ethics Framework
   - Explores risk management, accountability, and fairness in AI adoption.
TXT

# 4) Data Science & Analytics Projects
cat > docs/04_data_analytics_projects.txt <<'TXT'
== Data Science & Analytics Projects ==
1. Hotel Management Data Problem Project
   - Identified data cleaning issues, missing values, and bias in hotel booking dataset.
   - Tools: Orange, Excel, Python (Pandas, Matplotlib).

2. FXCS Bond Analysis (BAFI1065)
   - Created Excel bond portfolio simulation with formula transparency.
   - Calculated yields, spreads, and portfolio duration metrics.

3. Business Analytics using Orange
   - Conducted regression and scatter plot analysis using multiple axes and categorical/numeric data.

4. Microsoft News Recommendation System (Machine Learning)
   - Implemented XGBoost model for click-through rate (CTR) and AUC evaluation.
TXT

# 5) Personal Brand, Fitness & Motivation
cat > docs/05_personal_fitness_brand.txt <<'TXT'
== Personal Fitness & Motivation ==
Sumeet’s fitness journey focuses on strength, balance, and longevity.
- Workout Style: Calisthenics & Heavy Lifting hybrid
- Goals: 8-10% body fat, strength with aesthetics
- Supplements: Whey, Creatine, Zinc, Magnesium
- Content: Gym vlogs, motivational storytelling, AI-enhanced edits
- Philosophy: “Comfort is the enemy of growth.”

== Vlogging & Creativity ==
YouTube Channel: “Sumeething Special”
Themes: Melbourne nightlife, fitness transformation, AI lifestyle integration.
AI Tools Used: Runway ML, CapCut AI, Pika Labs, ElevenLabs, Relevance AI.
Tone: Confident, reflective, cinematic.
TXT

# 6) Resume & Industry Experience
cat > docs/06_resume_experience.txt <<'TXT'
== Professional Experience ==
1. Infosys Ltd — Software Engineer (Apple Account)
   - Duration: 3 years
   - Focus: Frontend development, client delivery, agile collaboration.

2. Trade Anywhere Ltd — Business Development Intern (Sagami Brand)
   - Duration: 6 months
   - Skills: Business analysis, partnership strategy, campaign analytics.

3. EzyMart — Retail Manager & Customer Experience Specialist
   - Duration: 6 months (Melbourne)
   - Skills: Team management, sales optimization, customer care.

4. RMIT University — Postgraduate Student (Master of Business IT)
   - Focus: Digital Strategy, AI Governance, and Business Analytics.
TXT

# 7) Knowledge Policy & Tone Guide
cat > docs/07_tone_policy.txt <<'TXT'
== SIL Knowledge Policy ==
Purpose: Ensure the LLM reflects Sumeet’s communication style — clear, grounded, motivational.
Tone: Confident, intelligent, approachable.
Rules:
- Prefer action steps over theory.
- Always provide reasoning or evidence.
- Avoid robotic or overly formal tone.
- Reference sources (e.g., [02_business_projects.txt]).
TXT
