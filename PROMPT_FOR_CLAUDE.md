# Prompts for Using Claude Code to Complete Sections

**This file contains recommended prompts for using Claude Code (or any AI assistant) to help complete Biblical narrative sections while maintaining A+ quality.**

---

## ⚡ Quick Start Prompt

**Use this to have Claude complete a single section:**

```
I'm working on the biblical-narrative-completion project. Please help me complete a contextual analysis for [BOOK NAME] chapters [X-Y].

Requirements:
- Follow the structure in SECTION_TEMPLATE.md exactly
- Maintain A+ quality (97+/100 score from quality_checker.py)
- Include 5+ specific archaeological citations with names, dates, and scholars
- Present multiple scholarly perspectives (traditional vs critical)
- Cite specific ancient sources (tablets, inscriptions, texts)
- Word count targets: Historical 250-400, Theological 250-400, all others 200-350+

Before we start, please:
1. Read the relevant biblical text ([BOOK] chapters [X-Y])
2. Review completed A+ examples: Joshua 1-5, Psalms 1-5, Genesis 1-5
3. Follow the 6-component structure from SECTION_TEMPLATE.md

Please provide:
1. **Narrative Summary** (150-250 words)
2. **Historical & Archaeological Context** (250-400 words with SPECIFIC citations)
3. **Cultural Practices Reflected** (200-350 words)
4. **Political Situation** (200-350 words)
5. **Theological Themes** (250-400 words)
6. **Connection to Broader Narrative** (250-400 words)

Focus especially on archaeological detail - name specific artifacts, sites, excavations, and scholars.
```

---

## 🔄 Session Continuation Prompt

**Use this when resuming work across multiple sessions:**

```
I'm continuing work on the biblical-narrative-completion project.

Current status:
- [X]/240 sections complete ([Y]%)
- Last completed: [Book/Section]
- Quality average: [Score]/100

Next target: Complete [BOOK NAME] chapters [X-Y] contextual analysis.

Please:
1. Review CURRENT_PROGRESS.md to understand what's been completed
2. Check quality_checker.py output to maintain consistency
3. Review 2-3 recent completed sections to match style and depth
4. Complete the new section following SECTION_TEMPLATE.md

Maintain A+ quality (97+/100):
- 5+ archaeological citations (sites, artifacts, scholars, dates)
- 3+ scholarly perspectives (debates, traditional vs critical)
- 2+ ancient source citations (tablets, texts, inscriptions)
- All word count requirements met
- Strong theological depth
- Clear narrative connections

Start with [BOOK] chapters [X-Y].
```

---

## 📊 Quality Enhancement Prompt

**Use this when a section scored below 97:**

```
I have a Biblical narrative section that scored [SCORE]/100 on quality_checker.py, below the A+ threshold of 97+.

Section: [BOOK] chapters [X-Y]

Quality checker feedback:
[PASTE FEEDBACK FROM quality_checker.py]

Please enhance this section to reach 97+ by:

1. **Adding Archaeological Detail** (if score indicates this):
   - Add 3-5 more specific citations
   - Name actual artifacts (steles, tablets, inscriptions, ostraca)
   - Name excavation sites and archaeologists
   - Include dates (e.g., "c. 1208 BCE", "14th century BCE")
   - Reference ancient texts (e.g., "Merneptah Stele", "Amarna Letters")

2. **Expanding Scholarly Perspectives** (if needed):
   - Add "traditional dating vs. critical scholarship" discussions
   - Include academic debates
   - Present multiple viewpoints fairly

3. **Meeting Word Counts** (if any section is too short):
   - Expand [SPECIFIC SECTION] from [CURRENT] to [TARGET] words
   - Add more detail and depth, not filler

4. **Enriching Theological Themes** (if shallow):
   - Add more biblical cross-references
   - Develop theological concepts more fully
   - Connect to redemptive history

Please provide the enhanced version of the entire section.
```

---

## 🎯 Batch Processing Prompt

**Use this to complete multiple sections efficiently:**

```
I need to complete multiple Biblical narrative sections for the biblical-narrative-completion project.

Target sections:
1. [BOOK] chapters [X-Y]
2. [BOOK] chapters [A-B]
3. [BOOK] chapters [M-N]

For EACH section, provide:
- All 6 required components (Narrative, Historical, Cultural, Political, Theological, Connection)
- A+ quality (97+/100)
- Specific archaeological citations (5+ per section)
- Scholarly perspectives (3+ per section)
- Ancient sources (2+ per section)

Process:
1. Complete section 1 first
2. Wait for my quality check
3. Revise if needed
4. Then proceed to section 2
5. Repeat

Let's start with section 1: [BOOK] chapters [X-Y].

Use SECTION_TEMPLATE.md structure and reference completed examples (Joshua 1-5, Psalms 1-5).
```

---

## 🔍 Research-Heavy Prompt

**Use this for difficult books requiring extensive research:**

```
I need to complete a contextual analysis for [BOOK] chapters [X-Y], which is challenging due to [sparse archaeology / complex theology / disputed authorship / etc.].

Please approach this systematically:

**Phase 1: Research**
1. Identify key archaeological sites related to this book
2. Find relevant ancient Near Eastern texts/parallels
3. Note major scholarly debates about dating, authorship, setting
4. Identify cultural practices reflected in the text
5. Trace major theological themes

**Phase 2: Write**
Complete all 6 components with special attention to:
- [SPECIFIC CHALLENGE - e.g., "Limited archaeological evidence, so focus on literary/historical parallels"]
- [SPECIFIC STRENGTH - e.g., "Rich theological content, develop this deeply"]

**Phase 3: Quality Check**
Before submitting, verify:
- 5+ specific archaeological/historical citations
- 3+ scholarly perspectives presented
- All word counts met
- Theological depth appropriate for an A+ grade

Book: [NAME]
Chapters: [X-Y]
Begin with research phase.
```

---

## 📚 New Testament Specific Prompt

**Use this for NT books (special considerations):**

```
I need to complete a contextual analysis for [NT BOOK] chapters [X-Y].

New Testament specific requirements:
1. **Greco-Roman Context**: Include Roman imperial background, Hellenistic culture
2. **Jewish Context**: Second Temple Judaism, Pharisees/Sadducees, synagogue practice
3. **Archaeological Evidence**: Inscriptions, papyri, NT manuscripts, sites (e.g., Pilate inscription, Caiaphas ossuary)
4. **OT Fulfillment**: Show how this connects to OT promises and types
5. **Early Church Context**: How early Christians used/understood this text

Archaeological sources to consider:
- NT papyri (P45, P46, P52, etc.)
- Inscriptions (Pilate, Gallio, etc.)
- Coins from the period
- Excavations (Capernaum, Jerusalem, Corinth, Ephesus, etc.)
- Roman historical sources (Josephus, Tacitus, Pliny)

Scholarly debates to address:
- Dating of the book
- Authorship questions
- Historical reliability
- Relationship to other NT books

Please complete [BOOK] chapters [X-Y] following SECTION_TEMPLATE.md with NT-specific depth.
```

---

## 🏺 Prophetic Books Prompt

**Use this for major/minor prophets:**

```
I need to complete a contextual analysis for [PROPHET] chapters [X-Y].

Prophetic book specific requirements:
1. **Historical Setting**: Identify the specific period (e.g., "Hezekiah's reign, 701 BCE, during Sennacherib's invasion")
2. **Archaeological Correlation**:
   - Assyrian/Babylonian annals mentioning events
   - Seals, bullae, ostraca from the period
   - Destruction layers matching prophecy timing
3. **Message Context**: Who was the audience? What crisis were they facing?
4. **Theological Themes**: Judgment, restoration, messianic hope, covenant lawsuit
5. **NT Fulfillment**: How does NT cite/apply this prophecy?

Archaeological sources for this prophet:
[LIST RELEVANT - e.g., for Isaiah: "Taylor Prism, Lachish reliefs, Hezekiah's tunnel, etc."]

Scholarly debates to address:
- Unity of the book (e.g., Isaiah 1-39 vs 40-66)
- Dating of composition
- Historical vs. predictive prophecy

Complete [PROPHET] chapters [X-Y] with prophetic-specific depth.
```

---

## ✅ Quality Verification Prompt

**Use this before committing work:**

```
I've completed a contextual analysis for [BOOK] chapters [X-Y]. Before committing, please review it as if you were quality_checker.py.

Evaluate:
1. **Archaeological Citations** (need 5+): Count and list them
2. **Ancient Sources** (need 2+): Count and list them
3. **Scholarly Perspectives** (need 3+): Count and identify them
4. **Word Counts**: Check each component against requirements
5. **Theological Depth**: Is it substantive or superficial?
6. **Narrative Connection**: Does it tie to broader Bible story?

Provide:
- Estimated quality score (/100)
- Grade (A+, A, A-, etc.)
- Specific improvements needed if below 97

If score is 97+, I'll commit. If below, I'll revise based on your feedback.

Here's the section to review:
[PASTE SECTION]
```

---

## 🎓 Learning from Examples Prompt

**Use this to understand what makes A+ quality:**

```
Please analyze one of the completed A+ sections to help me understand what makes it excellent.

Section to analyze: [Joshua 1-5 / Psalms 1-5 / Genesis 1-5]

Please identify:
1. How many archaeological citations? List them with specificity level.
2. How many scholarly perspectives? What debates are presented?
3. How many ancient sources cited? Name them.
4. Word count for each component
5. What makes the theological section rich?
6. How does it connect to broader narrative?
7. Writing style observations (what makes it engaging?)

Then provide a "template" or "formula" I can follow for my next section.

This will help me internalize what A+ looks like.
```

---

## 💡 Tips for Using These Prompts

### 1. **Always Include Context**
Tell Claude about the project, quality standards, and reference files (SECTION_TEMPLATE.md, completed examples).

### 2. **Be Specific About Quality**
Mention the 97+/100 requirement, archaeological citation count, scholarly perspective count.

### 3. **Reference Examples**
Point to Joshua 1-5, Psalms 1-5, or Genesis 1-5 as models.

### 4. **Iterate**
- First draft from Claude
- Run quality_checker.py
- Ask Claude to enhance based on feedback
- Run checker again
- Commit when 97+

### 5. **Customize for Book Type**
- Torah: Focus on ancient Near Eastern parallels
- Historical: Archaeological sites and events
- Wisdom: Cross-cultural wisdom literature
- Prophets: Historical setting and fulfillment
- Gospels: Greco-Roman and Jewish context
- Epistles: Early church and theological development

### 6. **Fact-Check**
Always verify:
- Archaeological claims (dates, sites, scholars)
- Ancient sources (correct names, dates)
- Biblical references (correct citation)
- Scholarly positions (accurately represented)

### 7. **Maintain Voice**
The completed sections have a consistent scholarly but accessible tone. Ask Claude to match the style of existing sections.

---

## ⚠️ Common Pitfalls to Avoid

### Pitfall 1: Generic Archaeological Statements
**Bad:** "Archaeological evidence supports this."
**Good:** "Excavations at Tell es-Sultan (ancient Jericho) by Kathleen Kenyon (1952-1958) revealed..."

### Pitfall 2: No Scholarly Debates
**Bad:** "This happened in the 8th century BCE."
**Good:** "Traditional dating places this in the 8th century BCE during Hezekiah's reign, while critical scholarship proposes..."

### Pitfall 3: Shallow Theology
**Bad:** "This shows God is good."
**Good:** "This passage develops the theology of divine hesed (covenant faithfulness), demonstrating how God maintains covenant commitment despite human failure, anticipating the ultimate expression of hesed in Christ (cf. Romans 5:8)..."

### Pitfall 4: Missing Connections
**Bad:** "This is an important passage."
**Good:** "This passage anticipates the New Covenant promised in Jeremiah 31:31-34, partially fulfilled at Pentecost (Acts 2), and ultimately consummated in Christ's work (Hebrews 8-10)..."

---

## 📖 Example Perfect Prompt (Copy/Paste Ready)

```
I'm working on the biblical-narrative-completion project to complete Biblical narrative sections from 53.8% to 100% at A+ quality.

Please help me complete: Proverbs chapters 1-5 contextual analysis

Requirements for A+ quality (97+/100):
- Follow SECTION_TEMPLATE.md structure (6 components)
- Include 5+ specific archaeological citations (name artifacts, sites, scholars, dates)
- Present 3+ scholarly perspectives (traditional vs. critical, debates)
- Cite 2+ ancient sources (texts, inscriptions, tablets)
- Meet word counts: Historical 250-400, Theological 250-400, others 200-350+
- Rich theological depth with biblical cross-references
- Strong connections to broader biblical narrative

Reference these A+ examples:
- Joshua 1-5 (excellent archaeological detail)
- Psalms 1-5 (outstanding theological depth)
- Genesis 1-5 (superb cultural analysis)

Please provide all 6 components for Proverbs 1-5:
1. Narrative Summary
2. Historical & Archaeological Context (SPECIFIC citations!)
3. Cultural Practices Reflected
4. Political Situation
5. Theological Themes
6. Connection to Broader Narrative

Begin with research, then write the complete section.
```

---

**Use these prompts to maintain consistent A+ quality across all 111 remaining sections!** 📖✨
