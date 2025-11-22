#!/usr/bin/env python3
"""
Marker Neutralization Script v2.0
LD-3.5 Canon: Bias-safe refactor of marker definition files

Replaces interpretive, diagnostic, or moralizing terminology with neutral,
form-based linguistic descriptions.
"""

import json
import re
import pathlib
import yaml
from datetime import datetime
from typing import Dict, List, Any, Tuple
import copy


# ============================================================================
# JSON SERIALIZATION HELPERS
# ============================================================================

def make_serializable(obj):
    """Convert an object to a JSON-serializable format."""
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, dict):
        return {k: make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [make_serializable(item) for item in obj]
    else:
        return str(obj)

# ============================================================================
# FORBIDDEN STEMS - Terms to eliminate from all marker metadata
# ============================================================================
FORBIDDEN_STEMS = [
    # German psychological/therapeutic terms
    "Resonanz", "resonanz",
    "Trigger", "trigger",
    "Stabilisierung", "stabilisierung",
    "Bindung", "bindung",
    "Widerstand", "widerstand",
    "Integration", "integration",

    # Gottman framework
    "Gottman", "gottman",
    "Stonewall", "stonewall", "stonewalling",
    "Verachtung", "verachtung", "contempt",  # Gottman contempt

    # Toxicity/negativity
    "toxicity", "toxic", "toxisch",
    "neediness", "needy", "bedürftig",
    "manipulativ", "manipulation",

    # Emotional/diagnostic labels
    "Schuld", "schuld",
    "guilt", "guilt_bind",
    "Overwhelm", "overwhelm", "overwhelmed", "überwältigung",
    "shame", "Scham", "scham",
    "attachment",
    "avoidance", "avoidant", "Vermeidung",
    "validation", "Validierung",
    "trauma",

    # Clinical diagnoses
    "borderlin", "Borderline",
    "narziss", "narcis",
    "codependent", "coabhängig",
]

# ============================================================================
# SEED MAPPING - Known transformations from biased to neutral
# ============================================================================
SEED_MAP = {
    # German mappings
    "Emotional Overwhelm": "High-Affect Self-Report",
    "Emotionale Überwältigung": "High-Affect Self-Report",
    "Stonewalling / Rückzug": "Conversation-Exit Move",
    "Stonewalling": "Conversation-Exit Move",
    "Rückzug": "Conversation-Exit Move",
    "Offensives Flirten": "Flirtation with Boundary Tension",
    "Verantwortungsabwälzung": "Responsibility-Attribution-Shift",
    "Leichte, witzige Kritik": "Humorous Critique Form",
    "Subtil-manipulative Bedürftigkeitskommunikation": "Need-Expression with Obligation-Pressure (Cluster)",
    "Resonanz/Joining": "Turn-Alignment",
    "Resonanz": "Turn-Alignment",
    "Affekt-Trigger": "Lexical-Salience",
    "Integration/Reframing": "Discourse-Mode",
    "Integration": "Discourse-Mode",
    "Stabilisierung": "Fluency/Complexity",
    "Grenzen/Rollen": "Role-Labels/Deixis",
    "Theorie/Metawechsel": "Meta-Lexis",

    # Gottman concepts
    "Verachtung / Überlegenheit": "Derision-Display",
    "Verachtung": "Derision-Lexis",
    "Contempt": "Derision-Display",
    "Criticism": "Critique-Pattern",
    "Defensiveness": "Counter-Justification",
    "Abwehr": "Counter-Justification",

    # Manipulation/guilt
    "Schuldappell / Guilt Trip": "Obligation-Pressure Speech-Act",
    "Schuldappell": "Obligation-Pressure Lexis",
    "Guilt Trip": "Obligation-Pressure Speech-Act",
    "Emotionale Manipulation": "Obligation-Pressure Pragmatics",
    "Manipulation signal": "Coercion-Pattern",

    # Shame/affect
    "Scham ausdrücken": "Self-Conscious Affect Expression",
    "Scham": "Self-Conscious Affect",
    "shame": "Self-Conscious Affect",

    # Attachment
    "Bindungsstil: ängstlich": "Proximity-Seeking Pattern",
    "Bindungsstil": "Relational-Pattern",
    "ängstliche Bindungshinweise": "Proximity-Seeking Signals",
    "Attachment": "Relational-Pattern",
    "attachment": "Relational-Pattern",

    # Conflict patterns
    "Gesprächsverweigerung, emotionale Abschottung": "Conversation-Exit, Engagement-Withdrawal",
    "Gesprächsverweigerung": "Conversation-Exit",
    "Demütigung, Statusabwertung": "Status-Lowering Display",
    "Demütigung": "Status-Lowering",

    # Validation/support
    "Selbstoffenbarung von sozialer Normverletzung": "Norm-Violation Self-Report",
    "Nähe-Suche bei gleichzeitiger Alarmierung": "Proximity-Seeking with Distress-Signal",
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def contains_forbidden(text: str) -> bool:
    """Check if text contains any forbidden stem."""
    if not text or not isinstance(text, str):
        return False
    text_lower = text.lower()
    return any(stem.lower() in text_lower for stem in FORBIDDEN_STEMS)


def map_from_seed(text: str) -> str:
    """Try to map text using seed mapping (exact or partial match)."""
    if not text or not isinstance(text, str):
        return None

    # Try exact match first
    if text in SEED_MAP:
        return SEED_MAP[text]

    # Try case-insensitive match
    for key, value in SEED_MAP.items():
        if key.lower() == text.lower():
            return value

    return next(
        (
            value
            for key, value in SEED_MAP.items()
            if key.lower() in text.lower()
        ),
        None,
    )


def neutralize_string(text: str) -> str:
    """
    Neutralize a string by:
    1. Checking seed map
    2. Extracting non-forbidden tokens
    3. Creating generic neutral label
    """
    if not text or not isinstance(text, str):
        return text

    # Try seed mapping first
    mapped = map_from_seed(text)
    if mapped:
        return mapped

    # If contains forbidden terms, extract valid tokens
    if contains_forbidden(text):
        # Extract alphanumeric tokens
        tokens = re.findall(r'[A-Za-zÄÖÜäöüß]+', text)
        # Filter out forbidden stems
        clean_tokens = [
            t for t in tokens
            if t and not any(stem.lower() in t.lower() for stem in FORBIDDEN_STEMS)
        ]

        if not clean_tokens:
            return "Conversation-Feature"

        # Use first clean token as base
        return f"{clean_tokens[0].capitalize()}-Feature"

    # No forbidden terms, return as-is
    return text


def clean_tags(tags: List[str]) -> List[str]:
    """Remove tags containing forbidden stems."""
    if not tags or not isinstance(tags, list):
        return tags

    return [
        tag
        for tag in tags
        if isinstance(tag, str) and not contains_forbidden(tag)
    ]


# ============================================================================
# MARKER PROCESSING
# ============================================================================

def clean_marker(marker: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]:
    """
    Clean a single marker definition.
    Returns: (cleaned_marker, was_changed)
    """
    original = copy.deepcopy(marker)
    changed = False

    # Fields to check at top level
    TOP_FIELDS = ["label", "name", "description"]

    for field in TOP_FIELDS:
        if field in marker and isinstance(marker[field], str):
            if contains_forbidden(marker[field]):
                new_value = neutralize_string(marker[field])
                marker[field] = new_value
                changed = True

    # Frame fields
    if "frame" in marker and isinstance(marker["frame"], dict):
        frame = marker["frame"]
        FRAME_FIELDS = ["concept", "pragmatics", "narrative"]

        for field in FRAME_FIELDS:
            if field in frame and isinstance(frame[field], str):
                if contains_forbidden(frame[field]):
                    new_value = neutralize_string(frame[field])
                    frame[field] = new_value
                    changed = True

            # Handle lists in frame (e.g., frame.signal)
            if field in frame and isinstance(frame[field], list):
                for i, item in enumerate(frame[field]):
                    if isinstance(item, str) and contains_forbidden(item):
                        frame[field][i] = neutralize_string(item)
                        changed = True

    # Tags
    if "tags" in marker and isinstance(marker["tags"], list):
        original_tags = marker["tags"][:]
        marker["tags"] = clean_tags(marker["tags"])
        if original_tags != marker["tags"]:
            changed = True

    return marker, changed


def process_yaml_file(file_path: pathlib.Path) -> Dict[str, Any]:
    """
    Process a single YAML marker file.
    Returns change record.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not data:
            return None

        original = copy.deepcopy(data)
        cleaned, was_changed = clean_marker(data)

        if was_changed:
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                yaml.dump(cleaned, f,
                         allow_unicode=True,
                         default_flow_style=False,
                         sort_keys=False)

            # Determine if needs manual review
            needs_review = (
                "Conversation-Feature" in str(cleaned) or
                "-Feature" in str(cleaned)
            )

            return {
                "file": str(file_path.name),
                "id": data.get("id", "UNKNOWN"),
                "old": make_serializable(original),
                "new": make_serializable(cleaned),
                "needs_manual_review": needs_review
            }

        return None

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution function."""
    print("=" * 80)
    print("Marker Neutralization Script v2.0")
    print("LD-3.5 Canon: Deterministic Bias-Safe Refactor")
    print("=" * 80)
    print()

    # Find all YAML files
    root = pathlib.Path("/home/user/Marker_LD4.0_supabase")
    yaml_files = list(root.glob("*.yaml")) + list(root.glob("*.yml"))

    print(f"Found {len(yaml_files)} YAML marker files")
    print()

    all_changes = []
    processed = 0
    modified = 0

    for yaml_file in sorted(yaml_files):
        change = process_yaml_file(yaml_file)
        if change:
            all_changes.append(change)
            modified += 1
            print(f"✓ Modified: {yaml_file.name}")
        processed += 1

    print()
    print("=" * 80)
    print(f"Processing complete:")
    print(f"  - Total files processed: {processed}")
    print(f"  - Files modified: {modified}")
    print(f"  - Files unchanged: {processed - modified}")
    print("=" * 80)
    print()

    # Save migration map
    migrations_dir = root / "migrations"
    migrations_dir.mkdir(exist_ok=True)

    map_file = migrations_dir / "marker_label_map.json"
    with open(map_file, 'w', encoding='utf-8') as f:
        json.dump(all_changes, f, indent=2, ensure_ascii=False)

    print(f"Migration map saved to: {map_file}")
    print(f"Total changes recorded: {len(all_changes)}")

    # Count files needing review
    needs_review = [c for c in all_changes if c.get("needs_manual_review", False)]
    if needs_review:
        print(f"⚠ Files needing manual review: {len(needs_review)}")
        for change in needs_review[:10]:  # Show first 10
            print(f"  - {change['file']} ({change['id']})")
        if len(needs_review) > 10:
            print(f"  ... and {len(needs_review) - 10} more")

    return all_changes


if __name__ == "__main__":
    changes = main()
