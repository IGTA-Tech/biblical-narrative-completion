#!/usr/bin/env python3
"""
Quality Checker for Biblical Narrative Sections

This script analyzes completed sections and assigns quality grades based on:
- Word counts for each component
- Presence of specific archaeological citations
- Number of ancient sources referenced
- Theological depth indicators
- Overall completeness

Usage:
    python quality_checker.py                    # Check entire document
    python quality_checker.py --section "Proverbs 1-5"  # Check specific section
    python quality_checker.py --recent 5         # Check last 5 sections added
"""

import re
import sys
from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class QualityScore:
    section_name: str
    narrative_words: int
    historical_words: int
    cultural_words: int
    political_words: int
    theological_words: int
    connection_words: int
    archaeological_citations: int
    ancient_sources: int
    scholarly_perspectives: int
    total_score: int
    grade: str
    feedback: List[str]

class QualityChecker:
    """Analyzes Biblical narrative sections for quality."""

    # Archaeological evidence patterns to look for
    ARCHAEOLOGICAL_PATTERNS = [
        r'stele|stela',
        r'inscription',
        r'tablet',
        r'ostraca|ostracon',
        r'excavation',
        r'tell\s+\w+',
        r'archaeological',
        r'cuneiform',
        r'papyri|papyrus',
        r'scroll',
        r'artifact'
    ]

    # Ancient source patterns
    ANCIENT_SOURCE_PATTERNS = [
        r'Epic of',
        r'Code of',
        r'Annals of',
        r'Chronicles? of',
        r'Book of the Dead',
        r'Enuma Elish',
        r'Gilgamesh',
        r'Mari tablets',
        r'Amarna Letters',
        r'Dead Sea Scrolls',
        r'Septuagint',
        r'Targum',
        r'Mishnah',
        r'Talmud'
    ]

    # Scholarly perspective indicators
    SCHOLARLY_PATTERNS = [
        r'traditional\s+(?:dating|view|scholarship)',
        r'critical\s+scholarship',
        r'scholars?\s+debate',
        r'consensus',
        r'disputed',
        r'argued|argues',
        r'proposed|proposes',
        r'early\s+dating.*late\s+dating',
        r'conservative.*liberal',
        r'maximalist.*minimalist'
    ]

    def __init__(self, filepath: str = 'jewish_biblical_narrative_enhanced.md'):
        self.filepath = filepath
        with open(filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def extract_sections(self) -> List[Dict[str, str]]:
        """Extract all contextual analysis sections from the document."""
        sections = []

        # Pattern to match section headers like "### Genesis Chapters 1-5: Contextual Analysis"
        section_pattern = r'### (.+?):\s*Contextual Analysis\s*\n(.*?)(?=\n###|\Z)'

        matches = re.finditer(section_pattern, self.content, re.DOTALL)

        for match in matches:
            section_name = match.group(1).strip()
            section_content = match.group(2).strip()

            # Extract components
            components = self._extract_components(section_content)

            sections.append({
                'name': section_name,
                'content': section_content,
                **components
            })

        return sections

    def _extract_components(self, content: str) -> Dict[str, str]:
        """Extract the 6 required components from a section."""
        components = {}

        component_patterns = {
            'narrative': r'\*\*Narrative Summary:\*\*\s*(.*?)(?=\*\*Historical|\Z)',
            'historical': r'\*\*Historical and Archaeological Context:\*\*\s*(.*?)(?=\*\*Cultural|\Z)',
            'cultural': r'\*\*Cultural Practices Reflected:\*\*\s*(.*?)(?=\*\*Political|\Z)',
            'political': r'\*\*Political Situation:\*\*\s*(.*?)(?=\*\*Theological|\Z)',
            'theological': r'\*\*Theological Themes:\*\*\s*(.*?)(?=\*\*Connection|\Z)',
            'connection': r'\*\*Connection to Broader Narrative:\*\*\s*(.*?)(?=\n---|\n###|\Z)'
        }

        for key, pattern in component_patterns.items():
            match = re.search(pattern, content, re.DOTALL)
            components[key] = match.group(1).strip() if match else ''

        return components

    def count_words(self, text: str) -> int:
        """Count words in text."""
        return len(re.findall(r'\b\w+\b', text))

    def count_patterns(self, text: str, patterns: List[str]) -> int:
        """Count occurrences of patterns in text."""
        count = 0
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            count += len(matches)
        return count

    def grade_section(self, section: Dict[str, str]) -> QualityScore:
        """Grade a single section and return quality score."""

        # Count words in each component
        narrative_words = self.count_words(section.get('narrative', ''))
        historical_words = self.count_words(section.get('historical', ''))
        cultural_words = self.count_words(section.get('cultural', ''))
        political_words = self.count_words(section.get('political', ''))
        theological_words = self.count_words(section.get('theological', ''))
        connection_words = self.count_words(section.get('connection', ''))

        # Count quality indicators
        historical_text = section.get('historical', '')
        archaeological_citations = self.count_patterns(historical_text, self.ARCHAEOLOGICAL_PATTERNS)
        ancient_sources = self.count_patterns(historical_text, self.ANCIENT_SOURCE_PATTERNS)
        scholarly_perspectives = self.count_patterns(historical_text, self.SCHOLARLY_PATTERNS)

        # Calculate score
        score = 0
        feedback = []

        # Archaeological citations (20 points)
        if archaeological_citations >= 5:
            score += 20
        elif archaeological_citations >= 3:
            score += 15
            feedback.append(f"Good archaeological citations ({archaeological_citations}), but aim for 5+ for full points")
        elif archaeological_citations >= 1:
            score += 10
            feedback.append(f"Needs more archaeological citations (found {archaeological_citations}, need 5+)")
        else:
            feedback.append("CRITICAL: No archaeological citations found!")

        # Scholarly balance (15 points)
        if scholarly_perspectives >= 3:
            score += 15
        elif scholarly_perspectives >= 2:
            score += 12
            feedback.append("Good scholarly perspectives, could add more")
        elif scholarly_perspectives >= 1:
            score += 8
            feedback.append("Needs more scholarly perspectives (found 1, need 3+)")
        else:
            score += 5
            feedback.append("CRITICAL: No scholarly perspectives/debates mentioned")

        # Cultural depth (15 points)
        if cultural_words >= 200:
            score += 15
        elif cultural_words >= 150:
            score += 12
            feedback.append(f"Cultural section a bit short ({cultural_words} words, aim for 200+)")
        else:
            score += 8
            feedback.append(f"Cultural section too short ({cultural_words} words, need 200+)")

        # Theological richness (20 points)
        if theological_words >= 250:
            score += 20
        elif theological_words >= 200:
            score += 17
            feedback.append(f"Theological section good but could expand ({theological_words} words)")
        else:
            score += 12
            feedback.append(f"Theological section too short ({theological_words} words, need 250+)")

        # Word counts met (10 points)
        word_count_score = 0
        if narrative_words >= 150: word_count_score += 2
        else: feedback.append(f"Narrative too short ({narrative_words}/150)")

        if historical_words >= 250: word_count_score += 2
        else: feedback.append(f"Historical too short ({historical_words}/250)")

        if cultural_words >= 200: word_count_score += 2

        if political_words >= 200: word_count_score += 2
        else: feedback.append(f"Political too short ({political_words}/200)")

        if theological_words >= 250: word_count_score += 1

        if connection_words >= 250: word_count_score += 1
        else: feedback.append(f"Connection too short ({connection_words}/250)")

        score += word_count_score

        # Narrative connection (10 points)
        if connection_words >= 300:
            score += 10
        elif connection_words >= 250:
            score += 8
        else:
            score += 5

        # Writing quality (10 points) - basic check
        total_words = (narrative_words + historical_words + cultural_words +
                      political_words + theological_words + connection_words)

        if total_words >= 1400:
            score += 10
        elif total_words >= 1200:
            score += 8
            feedback.append(f"Total word count a bit low ({total_words}, aim for 1400+)")
        else:
            score += 5
            feedback.append(f"Total word count too low ({total_words}, need 1400+)")

        # Determine grade
        if score >= 97:
            grade = "A+"
        elif score >= 93:
            grade = "A"
        elif score >= 90:
            grade = "A-"
        elif score >= 87:
            grade = "B+"
        elif score >= 83:
            grade = "B"
        else:
            grade = "B- or lower"

        # Add positive feedback for excellent work
        if score >= 97:
            feedback.insert(0, "🏆 EXCELLENT WORK! A+ quality maintained!")
        elif score >= 93:
            feedback.insert(0, "✅ Great work! Just a few tweaks to reach A+")

        return QualityScore(
            section_name=section['name'],
            narrative_words=narrative_words,
            historical_words=historical_words,
            cultural_words=cultural_words,
            political_words=political_words,
            theological_words=theological_words,
            connection_words=connection_words,
            archaeological_citations=archaeological_citations,
            ancient_sources=ancient_sources,
            scholarly_perspectives=scholarly_perspectives,
            total_score=score,
            grade=grade,
            feedback=feedback
        )

    def check_all_sections(self) -> List[QualityScore]:
        """Check all sections in the document."""
        sections = self.extract_sections()
        scores = []

        for section in sections:
            score = self.grade_section(section)
            scores.append(score)

        return scores

    def print_report(self, scores: List[QualityScore]):
        """Print a formatted quality report."""
        print("\n" + "="*80)
        print("📊 BIBLICAL NARRATIVE QUALITY REPORT")
        print("="*80 + "\n")

        # Summary statistics
        total_sections = len(scores)
        avg_score = sum(s.total_score for s in scores) / total_sections if total_sections > 0 else 0
        a_plus_count = sum(1 for s in scores if s.total_score >= 97)
        a_count = sum(1 for s in scores if 93 <= s.total_score < 97)
        needs_work = sum(1 for s in scores if s.total_score < 90)

        print(f"Total Sections Analyzed: {total_sections}")
        print(f"Average Score: {avg_score:.1f}/100")
        print(f"A+ Sections (97+): {a_plus_count} ({a_plus_count/total_sections*100:.1f}%)")
        print(f"A Sections (93-96): {a_count} ({a_count/total_sections*100:.1f}%)")
        print(f"Needs Work (<90): {needs_work}")
        print("\n" + "-"*80 + "\n")

        # Individual section scores
        for score in scores:
            print(f"📖 {score.section_name}")
            print(f"   Grade: {score.grade} ({score.total_score}/100)")
            print(f"   Words: N:{score.narrative_words} H:{score.historical_words} " +
                  f"C:{score.cultural_words} P:{score.political_words} " +
                  f"T:{score.theological_words} Con:{score.connection_words}")
            print(f"   Citations: Arch:{score.archaeological_citations} " +
                  f"Sources:{score.ancient_sources} Scholarly:{score.scholarly_perspectives}")

            if score.feedback:
                print(f"   Feedback:")
                for fb in score.feedback:
                    print(f"      • {fb}")
            print()

        print("="*80)
        print(f"📈 OVERALL PROJECT GRADE: {avg_score:.1f}/100")

        if avg_score >= 97:
            print("🏆 STATUS: A+ QUALITY - EXCELLENT! Keep it up!")
        elif avg_score >= 93:
            print("✅ STATUS: A QUALITY - Very good, small improvements for A+")
        elif avg_score >= 90:
            print("⚠️  STATUS: A- QUALITY - Good, but needs enhancement")
        else:
            print("❌ STATUS: Below A- - Significant work needed")

        print("="*80 + "\n")

        return avg_score

def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='Check quality of Biblical narrative sections')
    parser.add_argument('--section', help='Check specific section by name')
    parser.add_argument('--recent', type=int, help='Check last N sections')
    parser.add_argument('--file', default='jewish_biblical_narrative_enhanced.md',
                       help='Path to narrative file')

    args = parser.parse_args()

    checker = QualityChecker(args.file)
    scores = checker.check_all_sections()

    if args.section:
        # Filter to specific section
        scores = [s for s in scores if args.section.lower() in s.section_name.lower()]
        if not scores:
            print(f"❌ Section '{args.section}' not found!")
            return 1
    elif args.recent:
        # Get last N sections
        scores = scores[-args.recent:]

    avg_score = checker.print_report(scores)

    # Return exit code based on quality
    if avg_score >= 97:
        return 0  # Success - A+ quality
    elif avg_score >= 90:
        return 1  # Warning - Below A+ but acceptable
    else:
        return 2  # Error - Below A-

if __name__ == '__main__':
    sys.exit(main())
