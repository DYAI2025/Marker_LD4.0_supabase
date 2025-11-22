# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Changed - 2025-11-22

#### feat: neutralized marker labels and frames (bias-safe refactor, no logic change)

**Scope**: LD-3.5 Canon marker definition files  
**Impact**: Metadata only (labels, descriptions, frame concepts) - no detection logic changes

Performed deterministic, non-destructive refactor of all marker definition files (*.yaml) to replace interpretive, diagnostic, or moralizing terminology with neutral, form-based linguistic descriptions.

**Key Changes**:
- Eliminated all Gottman framework terminology (Gottman, Stonewalling, Contempt, etc.)
- Replaced psychological/therapeutic labels with linguistic pattern descriptions
- Neutralized emotional/diagnostic terminology (shame, guilt, attachment, trauma, etc.)
- Removed all clinical diagnosis references (borderline, narcissistic, codependent, etc.)

**Unchanged**:
- All marker IDs (`id` fields)
- All detection patterns (`pattern` fields)
- All algorithmic weights and scoring logic
- All activation rules and thresholds

**Statistics**:
- Files processed: 922
- Files modified: 27 (in final pass)
- Files with parse errors: 9 (malformed YAML, skipped)
- Validation: ✅ Clean - no forbidden terms in metadata

**Example Transformations**:
- "Stonewalling / Rückzug" → "Conversation-Exit Move"
- "Verachtung / Überlegenheit" → "Derision-Display"
- "Scham ausdrücken" → "Self-Conscious Affect Expression"
- "Schuldappell / Guilt Trip" → "Obligation-Pressure Speech-Act"

**Artifacts**:
- Full migration report: `reports/MIGRATION_REPORT.md`
- Change mapping: `migrations/marker_label_map.json`
- Original backups: `backups/*.yaml`
- Neutralization script: `scripts/neutralize_markers_v2.py`

**Idempotency**: Re-running the neutralization script produces no additional changes, confirming stable output.

**Rationale**: Ensure marker definitions use neutral, observable linguistic terminology rather than interpretive psychological frameworks, improving scientific rigor and reducing potential bias in conversational analysis.

