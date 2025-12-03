#!/usr/bin/env python3
"""
Progress Tracker for Biblical Narrative Completion

Tracks completion of sections and updates CURRENT_PROGRESS.md

Usage:
    python progress_tracker.py                 # Show current progress
    python progress_tracker.py --update        # Update CURRENT_PROGRESS.md
    python progress_tracker.py --session "Completed Proverbs 1-5"  # Log session work
"""

import re
import sys
from datetime import datetime
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class BookInfo:
    """Information about a Biblical book."""
    name: str
    testament: str
    category: str
    total_sections: int
    completed_sections: int = 0

class ProgressTracker:
    """Tracks progress through Biblical narrative completion."""

    # Define all books and their expected sections
    BOOKS = {
        # Old Testament - Torah
        'Genesis': BookInfo('Genesis', 'OT', 'Torah', 10),
        'Exodus': BookInfo('Exodus', 'OT', 'Torah', 8),
        'Leviticus': BookInfo('Leviticus', 'OT', 'Torah', 5),
        'Numbers': BookInfo('Numbers', 'OT', 'Torah', 6),
        'Deuteronomy': BookInfo('Deuteronomy', 'OT', 'Torah', 7),

        # Old Testament - Historical
        'Joshua': BookInfo('Joshua', 'OT', 'Historical', 5),
        'Judges': BookInfo('Judges', 'OT', 'Historical', 4),
        'Ruth': BookInfo('Ruth', 'OT', 'Historical', 1),
        '1 Samuel': BookInfo('1 Samuel', 'OT', 'Historical', 7),
        '2 Samuel': BookInfo('2 Samuel', 'OT', 'Historical', 5),
        '1 Kings': BookInfo('1 Kings', 'OT', 'Historical', 5),
        '2 Kings': BookInfo('2 Kings', 'OT', 'Historical', 5),
        '1 Chronicles': BookInfo('1 Chronicles', 'OT', 'Historical', 6),
        '2 Chronicles': BookInfo('2 Chronicles', 'OT', 'Historical', 8),
        'Ezra': BookInfo('Ezra', 'OT', 'Historical', 2),
        'Nehemiah': BookInfo('Nehemiah', 'OT', 'Historical', 3),
        'Esther': BookInfo('Esther', 'OT', 'Historical', 2),

        # Old Testament - Wisdom
        'Job': BookInfo('Job', 'OT', 'Wisdom', 9),
        'Psalms': BookInfo('Psalms', 'OT', 'Wisdom', 30),
        'Proverbs': BookInfo('Proverbs', 'OT', 'Wisdom', 6),
        'Ecclesiastes': BookInfo('Ecclesiastes', 'OT', 'Wisdom', 3),
        'Song of Solomon': BookInfo('Song of Solomon', 'OT', 'Wisdom', 2),

        # Old Testament - Major Prophets
        'Isaiah': BookInfo('Isaiah', 'OT', 'Major Prophets', 13),
        'Jeremiah': BookInfo('Jeremiah', 'OT', 'Major Prophets', 11),
        'Lamentations': BookInfo('Lamentations', 'OT', 'Major Prophets', 1),
        'Ezekiel': BookInfo('Ezekiel', 'OT', 'Major Prophets', 10),
        'Daniel': BookInfo('Daniel', 'OT', 'Major Prophets', 3),

        # Old Testament - Minor Prophets (1 section each)
        'Hosea': BookInfo('Hosea', 'OT', 'Minor Prophets', 1),
        'Joel': BookInfo('Joel', 'OT', 'Minor Prophets', 1),
        'Amos': BookInfo('Amos', 'OT', 'Minor Prophets', 1),
        'Obadiah': BookInfo('Obadiah', 'OT', 'Minor Prophets', 1),
        'Jonah': BookInfo('Jonah', 'OT', 'Minor Prophets', 1),
        'Micah': BookInfo('Micah', 'OT', 'Minor Prophets', 1),
        'Nahum': BookInfo('Nahum', 'OT', 'Minor Prophets', 1),
        'Habakkuk': BookInfo('Habakkuk', 'OT', 'Minor Prophets', 1),
        'Zephaniah': BookInfo('Zephaniah', 'OT', 'Minor Prophets', 1),
        'Haggai': BookInfo('Haggai', 'OT', 'Minor Prophets', 1),
        'Zechariah': BookInfo('Zechariah', 'OT', 'Minor Prophets', 1),
        'Malachi': BookInfo('Malachi', 'OT', 'Minor Prophets', 1),

        # New Testament - Gospels
        'Matthew': BookInfo('Matthew', 'NT', 'Gospels', 6),
        'Mark': BookInfo('Mark', 'NT', 'Gospels', 4),
        'Luke': BookInfo('Luke', 'NT', 'Gospels', 5),
        'John': BookInfo('John', 'NT', 'Gospels', 4),

        # New Testament - Acts
        'Acts': BookInfo('Acts', 'NT', 'Acts', 6),

        # New Testament - Pauline Epistles
        'Romans': BookInfo('Romans', 'NT', 'Pauline Epistles', 4),
        '1 Corinthians': BookInfo('1 Corinthians', 'NT', 'Pauline Epistles', 4),
        '2 Corinthians': BookInfo('2 Corinthians', 'NT', 'Pauline Epistles', 3),
        'Galatians': BookInfo('Galatians', 'NT', 'Pauline Epistles', 2),
        'Ephesians': BookInfo('Ephesians', 'NT', 'Pauline Epistles', 2),
        'Philippians': BookInfo('Philippians', 'NT', 'Pauline Epistles', 1),
        'Colossians': BookInfo('Colossians', 'NT', 'Pauline Epistles', 1),
        '1 Thessalonians': BookInfo('1 Thessalonians', 'NT', 'Pauline Epistles', 1),
        '2 Thessalonians': BookInfo('2 Thessalonians', 'NT', 'Pauline Epistles', 1),
        '1 Timothy': BookInfo('1 Timothy', 'NT', 'Pauline Epistles', 2),
        '2 Timothy': BookInfo('2 Timothy', 'NT', 'Pauline Epistles', 1),
        'Titus': BookInfo('Titus', 'NT', 'Pauline Epistles', 1),
        'Philemon': BookInfo('Philemon', 'NT', 'Pauline Epistles', 1),

        # New Testament - General Epistles
        'Hebrews': BookInfo('Hebrews', 'NT', 'General Epistles', 3),
        'James': BookInfo('James', 'NT', 'General Epistles', 1),
        '1 Peter': BookInfo('1 Peter', 'NT', 'General Epistles', 2),
        '2 Peter': BookInfo('2 Peter', 'NT', 'General Epistles', 1),
        '1 John': BookInfo('1 John', 'NT', 'General Epistles', 2),
        '2 John': BookInfo('2 John', 'NT', 'General Epistles', 1),
        '3 John': BookInfo('3 John', 'NT', 'General Epistles', 1),
        'Jude': BookInfo('Jude', 'NT', 'General Epistles', 1),

        # New Testament - Apocalyptic
        'Revelation': BookInfo('Revelation', 'NT', 'Apocalyptic', 5),
    }

    def __init__(self, filepath: str = 'jewish_biblical_narrative_enhanced.md'):
        self.filepath = filepath
        self.load_document()
        self.scan_completed_sections()

    def load_document(self):
        """Load the narrative document."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def scan_completed_sections(self):
        """Scan document to find all completed sections."""
        # Pattern to match contextual analysis sections
        pattern = r'### (.+?):\s*Contextual Analysis'
        matches = re.findall(pattern, self.content)

        # Count sections per book
        for match in matches:
            # Extract book name from section title
            # e.g., "Genesis Chapters 1-5" -> "Genesis"
            for book_name in self.BOOKS.keys():
                if book_name in match:
                    self.BOOKS[book_name].completed_sections += 1
                    break

    def get_total_sections(self) -> int:
        """Get total number of sections needed."""
        return sum(book.total_sections for book in self.BOOKS.values())

    def get_completed_sections(self) -> int:
        """Get number of completed sections."""
        return sum(book.completed_sections for book in self.BOOKS.values())

    def get_completion_percentage(self) -> float:
        """Get overall completion percentage."""
        total = self.get_total_sections()
        completed = self.get_completed_sections()
        return (completed / total * 100) if total > 0 else 0.0

    def get_category_progress(self) -> Dict[str, Tuple[int, int]]:
        """Get progress by category."""
        categories = {}
        for book in self.BOOKS.values():
            key = f"{book.testament} - {book.category}"
            if key not in categories:
                categories[key] = [0, 0]  # [completed, total]
            categories[key][0] += book.completed_sections
            categories[key][1] += book.total_sections
        return categories

    def print_progress_report(self):
        """Print a detailed progress report."""
        total = self.get_total_sections()
        completed = self.get_completed_sections()
        percentage = self.get_completion_percentage()
        remaining = total - completed

        print("\n" + "="*80)
        print("📊 BIBLICAL NARRATIVE COMPLETION PROGRESS")
        print("="*80 + "\n")

        print(f"Overall Progress: {completed}/{total} sections ({percentage:.1f}%)")
        print(f"Remaining: {remaining} sections")
        print(f"Status: {'🏆 COMPLETE!' if completed == total else '📝 In Progress'}")
        print("\n" + "-"*80 + "\n")

        # Progress by category
        print("Progress by Category:\n")
        categories = self.get_category_progress()
        for category, (comp, tot) in sorted(categories.items()):
            pct = (comp / tot * 100) if tot > 0 else 0
            status = "✅" if comp == tot else "📝"
            bar_length = 40
            filled = int(bar_length * comp / tot) if tot > 0 else 0
            bar = "█" * filled + "░" * (bar_length - filled)
            print(f"{status} {category:30s} [{bar}] {comp:3d}/{tot:3d} ({pct:5.1f}%)")

        print("\n" + "-"*80 + "\n")

        # Books needing work
        print("Next Books to Complete:\n")
        incomplete_books = [
            (book.name, book.completed_sections, book.total_sections, book.category)
            for book in self.BOOKS.values()
            if book.completed_sections < book.total_sections
        ]

        # Sort by category priority: Wisdom -> Major Prophets -> Minor Prophets -> NT
        priority_order = {
            'Wisdom': 1,
            'Major Prophets': 2,
            'Minor Prophets': 3,
            'Gospels': 4,
            'Acts': 5,
            'Pauline Epistles': 6,
            'General Epistles': 7,
            'Apocalyptic': 8
        }

        incomplete_books.sort(key=lambda x: (priority_order.get(x[3], 99), x[0]))

        for i, (name, comp, tot, category) in enumerate(incomplete_books[:10], 1):
            remaining = tot - comp
            print(f"{i:2d}. {name:20s} - {remaining} section{'s' if remaining != 1 else ''} remaining ({category})")

        if len(incomplete_books) > 10:
            print(f"    ... and {len(incomplete_books) - 10} more books")

        print("\n" + "="*80 + "\n")

    def generate_session_summary(self, session_notes: str) -> str:
        """Generate a session summary to add to CURRENT_PROGRESS.md"""
        completed = self.get_completed_sections()
        total = self.get_total_sections()
        percentage = self.get_completion_percentage()

        today = datetime.now().strftime("%Y-%m-%d")

        summary = f"""
## Session Summary ({today})

**Completed This Session:**
{session_notes}

**Current Status:**
- Total Sections: {completed}/{total} ({percentage:.1f}%)
- Sections Completed This Session: [Count from session notes]

---

"""
        return summary

def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='Track Biblical narrative completion progress')
    parser.add_argument('--file', default='jewish_biblical_narrative_enhanced.md',
                       help='Path to narrative file')
    parser.add_argument('--update', action='store_true',
                       help='Update CURRENT_PROGRESS.md')
    parser.add_argument('--session', help='Session notes for summary')

    args = parser.parse_args()

    tracker = ProgressTracker(args.file)
    tracker.print_progress_report()

    if args.session:
        summary = tracker.generate_session_summary(args.session)
        print("\n📝 Session Summary Generated:")
        print(summary)

        if args.update:
            # Append to CURRENT_PROGRESS.md
            with open('CURRENT_PROGRESS.md', 'a') as f:
                f.write(summary)
            print("✅ CURRENT_PROGRESS.md updated!")

    return 0

if __name__ == '__main__':
    sys.exit(main())
