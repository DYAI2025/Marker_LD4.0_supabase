# CLAUDE.md - AI Assistant Guide for Marker_LD4.0_supabase

## Project Overview

**Marker_LD4.0_supabase** is a comprehensive linguistic and psychological pattern detection framework called "LeanDeep" (version 3.4/4.0). This repository contains **919 YAML marker definitions** designed to identify and analyze communication patterns, relationship dynamics, emotional states, and psychological indicators in human conversation.

### Purpose

The framework enables systematic detection of:
- Communication patterns and dynamics
- Emotional and psychological states
- Relationship quality indicators
- Conflict patterns and repair attempts
- Cognitive biases and defense mechanisms
- Personality and developmental frameworks (e.g., Spiral Dynamics)
- Therapeutic conversation markers (Gottman, attachment theory, etc.)

### Key Frameworks Referenced

This system integrates concepts from:
- **Spiral Dynamics**: Developmental psychology framework (Beige/Purple/Red/Blue/Orange/Green/Yellow/Turquoise)
- **Gottman Method**: Four Horsemen of conflict (criticism, contempt, defensiveness, stonewalling)
- **Attachment Theory**: Secure, anxious, avoidant patterns
- **Love Languages**: Words of affirmation, quality time, receiving gifts, acts of service, physical touch
- **Cognitive Biases**: Attribution errors, anchoring, confirmation bias
- **Defense Mechanisms**: Projection, rationalization, denial
- **Psychopathology Indicators**: BPD, ADHD, OCD, depression, substance use patterns

---

## Repository Structure

### File Organization

```
Marker_LD4.0_supabase/
├── ATO_*.yaml          # Atomic markers (406 files)
├── SEM_*.yaml          # Semantic markers (299 files)
├── CLU_*.yaml          # Cluster markers (143 files)
├── MEMA_*.yaml         # Meta markers (60 files)
├── CFG_*.yaml          # Configuration files
├── EVAL_*.yaml         # Evaluation markers
├── SCN_*.yaml          # Scenario markers
├── metadata.yaml       # System configuration
└── MARKER_WIRKSAMKEITS_KATALOG.md  # Complete catalog (German)
```

### Marker Types by Prefix

| Prefix | Type | Count | Purpose |
|--------|------|-------|---------|
| `ATO_` | Atomic | 406 | Short-term word/phrase patterns that trigger reflexively |
| `SEM_` | Semantic | 299 | Meaning-level patterns requiring context |
| `CLU_` | Cluster | 143 | Combinations of multiple atomic markers |
| `MEMA_` | Meta | 60 | High-level behavioral patterns |
| `CFG_` | Config | 1 | System configuration |
| `EVAL_` | Evaluation | 1 | Evaluation frameworks |
| `SCN_` | Scenario | 2 | Scenario-specific patterns |

---

## YAML Schema Structures

### ATO (Atomic) Marker Schema

**Example: ATO_ACKNOWLEDGE.yaml**

```yaml
schema: "LeanDeep"
version: "3.4"
id: ATO_ACKNOWLEDGE
frame:
  signal: ["acknowledge"]
  concept: "Kenntnisnahme / Quittung"
  pragmatics: "Koordination / Rückmeldung"
  narrative: "interaction"
tags: [ack, coordination]
pattern:
  regex: "\\b(verstanden|zur Kenntnis|notiert|gesehen|angekommen|ok)\\b"
  flags: ["IGNORECASE"]
examples:
  - "Verstanden."
  - "Zur Kenntnis."
  - "Notiert."
```

**Key Fields:**
- `schema`: Framework name (always "LeanDeep")
- `version`: LeanDeep version
- `id`: Unique marker identifier
- `frame`: Conceptual framing (signal, concept, pragmatics, narrative)
- `tags`: Searchable metadata tags
- `pattern`: Regex pattern with flags
- `examples`: Sample matching text

### CLU/SEM (Cluster/Semantic) Marker Schema

**Example: CLU_ACTIVE_REPAIR.yaml**

```yaml
name: CLU_ACTIVE_REPAIR
label: "Aktive Reparatur"
class: cluster
version: 1.0
languages: [de]
intent: "Aktive Versuche, Konflikte zu reparieren durch Entschuldigungen, Empathie oder Zugeständnisse"
temperature_semantics:
  external: RUHE
  latent: REPARIEREND
window:
  size_messages: 20
gates:
  min_msgs: 5
  require_bilateral: false
score:
  method: weighted_k_of_n
  threshold: 0.7
ingredients:
  require:
    - ATO_APOLOGY
    - ATO_EMPATHY_MARKERS
  k_of_n: {k: 2, of: [ATO_COMPROMISE_OFFER, ATO_REPAIR_REQUEST, ATO_POSITIVE_REGARD]}
negative_evidence:
  any_of: [ATO_DEFENSIVENESS, ATO_BLAME_SHIFT]
emits:
  indices:
    trust: +0.2
    deesc: +0.3
    conflict: -0.2
conflicts_with:
  - CLU_HEATED_CONFLICT
semiotic:
  mode: symbolic
  level: pragmatic
  object: "repair_action"
  connotation: ["reparatur", "aktiv"]
  interpretant: "effect_on_state: {trust: +0.2, conflict: -0.2}"
examples:
  positive_de:
    - "Tut mir leid, ich war unfair."
    - "Ich verstehe, wie dich das trifft."
  negative_de:
    - "Das nervt mich."
    - "Du bist schuld."
```

**Key Fields:**
- `name`: Marker identifier
- `class`: cluster or semantic
- `intent`: Human-readable purpose
- `temperature_semantics`: Emotional temperature indicators
- `window`: Context window size
- `gates`: Activation requirements
- `score`: Scoring method and threshold
- `ingredients`: Required and optional component markers
- `negative_evidence`: Markers that block activation
- `emits`: Impact on relationship indices (trust, conflict, etc.)
- `conflicts_with`: Mutually exclusive markers
- `semiotic`: Semiotic analysis metadata
- `examples`: Positive and negative examples

---

## Key Conventions for AI Assistants

### 1. Marker Naming Conventions

**Pattern**: `{PREFIX}_{DESCRIPTIVE_NAME}.yaml`

- **Always UPPERCASE** for prefix and name
- **Use underscores** to separate words
- **Be descriptive**: Name should clearly indicate what pattern is detected
- **Language neutral names** (English preferred) even if patterns are language-specific

**Examples:**
- ✅ `ATO_GUILT_TRIP.yaml`
- ✅ `CLU_ACTIVE_REPAIR.yaml`
- ✅ `SEM_VALIDATION_OF_FEELING.yaml`
- ❌ `guilt_trip.yaml` (missing prefix)
- ❌ `ATO-GUILT-TRIP.yaml` (hyphens instead of underscores)

### 2. File Duplication Handling

**Current State**: Some files have duplicates with " 2" suffix (e.g., `ATO_BETWEENNESS_TERM.yaml` and `ATO_BETWEENNESS_TERM 2.yaml`)

**Convention:**
- Duplicates likely indicate versioning or iteration
- When editing, check for duplicates and clarify which is canonical
- Consider consolidating or removing duplicates unless intentional versioning

### 3. Language Handling

- Markers support multiple languages (primarily German: `de`, English: `en`)
- `languages: [de]` field specifies supported languages
- Pattern regexes should match the target language
- Examples should be provided in each supported language (`positive_de`, `positive_en`)

### 4. Schema Versioning

- Two schema formats exist:
  - **ATO markers**: Use `schema: "LeanDeep"` + `version: "3.4"`
  - **CLU/SEM markers**: Use `version: 1.0` (semantic versioning)
- Maintain version consistency when creating new markers

### 5. Regex Pattern Best Practices

```yaml
pattern:
  regex: "\\b(pattern1|pattern2|pattern3)\\b"
  flags: ["IGNORECASE"]
```

- Use **word boundaries** (`\\b`) to avoid partial matches
- Use **IGNORECASE** flag for case-insensitive matching
- **Escape special characters** properly (`\\s`, `\\b`, `\\.`)
- Test patterns against examples to ensure accuracy
- For multiline patterns in SEM markers, use YAML list format

### 6. Relationship Indices

Markers emit changes to relationship quality indices:

- `trust`: Trust level (+/-)
- `conflict`: Conflict intensity (+/-)
- `deesc`: De-escalation (+/-)
- `coherence`: Conversational coherence (+/-)
- `intimacy`: Emotional intimacy (+/-)
- `safety`: Psychological safety (+/-)

**Convention**: Use increments of 0.1 to 0.3 for moderate effects, up to 0.5 for strong effects.

### 7. Ingredient Composition

Cluster markers compose atomic markers using:

```yaml
ingredients:
  require:                    # ALL must be present
    - ATO_MARKER_1
    - ATO_MARKER_2
  k_of_n:                    # K out of N must be present
    k: 2
    of: [ATO_A, ATO_B, ATO_C]
  any_of:                    # At least ONE must be present
    - ATO_X
    - ATO_Y
```

### 8. Negative Evidence

Use `negative_evidence` to prevent false positives:

```yaml
negative_evidence:
  any_of: [ATO_SARCASM, ATO_IRONY]  # Block if sarcasm/irony detected
```

---

## Development Workflows

### Creating a New Atomic (ATO) Marker

1. **Identify the pattern**: What specific linguistic pattern are you detecting?
2. **Choose a clear name**: `ATO_{DESCRIPTIVE_NAME}.yaml`
3. **Write the regex**: Test it against positive and negative examples
4. **Fill in the schema**:

```yaml
schema: "LeanDeep"
version: "3.4"
id: ATO_YOUR_MARKER_NAME
frame:
  signal: ["brief description"]
  concept: "Human-readable concept"
  pragmatics: "Pragmatic function"
  narrative: "interaction|emotion|cognition"
tags: [tag1, tag2]
pattern:
  regex: "\\b(pattern)\\b"
  flags: ["IGNORECASE"]
examples:
  - "Example 1"
  - "Example 2"
```

5. **Add examples**: At least 3-5 positive examples
6. **Test**: Verify regex matches examples

### Creating a New Cluster (CLU) Marker

1. **Identify component markers**: Which ATO markers compose this cluster?
2. **Define activation logic**: What combination triggers detection?
3. **Determine impact**: How does this affect relationship indices?
4. **Fill in the schema**: Use CLU_ACTIVE_REPAIR.yaml as template
5. **Provide examples**: Both positive and negative cases
6. **Test composition**: Ensure ingredients are valid marker IDs

### Editing Existing Markers

1. **Read the file first**: Understand current pattern and intent
2. **Preserve version info**: Don't change version unless substantive change
3. **Test pattern changes**: Ensure new regex still matches intended cases
4. **Update examples**: If pattern changes, update examples accordingly
5. **Check dependencies**: Search for markers that reference this marker in `ingredients`

```bash
# Find markers that reference a specific marker
grep -r "ATO_YOUR_MARKER" *.yaml
```

### Quality Checks Before Committing

- [ ] **Valid YAML syntax**: Use a YAML validator
- [ ] **Regex is escaped properly**: Double backslashes in YAML strings
- [ ] **ID matches filename**: `id: ATO_EXAMPLE` → `ATO_EXAMPLE.yaml`
- [ ] **Examples match pattern**: Test regex against all examples
- [ ] **No duplicates**: Check for existing similar markers
- [ ] **Consistent formatting**: Follow existing file formatting
- [ ] **Language tags correct**: `languages: [de]` or `[en]` or both

---

## Working with the Catalog

### MARKER_WIRKSAMKEITS_KATALOG.md

This comprehensive German-language catalog documents all markers organized by category. It follows the principle **"What fires together wires together"** - markers with similar activation patterns are grouped together.

**Structure:**
- **Atomare Resonanz-Trigger (ATO)**: Reflexive word/phrase patterns
- **Cluster-Muster (CLU)**: Multi-marker combinations
- **Semantische Felder (SEM)**: Context-dependent patterns
- **Meta-Muster (MEMA)**: High-level behavioral patterns

**When to update:**
- After creating new markers
- After deleting markers
- When marker descriptions change significantly

**Update process:**
1. Read current catalog structure
2. Find appropriate category for new marker
3. Add entry: `| Marker Name | Description | Filename |`
4. Maintain alphabetical or logical ordering within category

---

## Integration with Supabase

The repository name suggests integration with **Supabase** (open-source Firebase alternative).

**Expected architecture** (if not yet implemented):

1. **Marker Storage**: YAML files as source of truth
2. **Database Schema**: Markers stored in Supabase tables
3. **Pattern Matching**: Real-time or batch processing of conversations
4. **Scoring Engine**: Calculates relationship indices based on detected markers
5. **API Layer**: Serves marker detections and relationship metrics

**If implementing Supabase integration:**
- Create database schema matching YAML structure
- Implement YAML → database sync script
- Store conversation messages and detected markers
- Calculate rolling indices (trust, conflict, etc.)
- Provide API endpoints for marker queries

---

## System Configuration (metadata.yaml)

The `metadata.yaml` file contains system-wide configuration:

```yaml
metadata:
  version: "LeanDeep3.4"
  marker_families:
    SURVIVAL: ["SEM_BEIGE_SURVIVAL_MODE", "CLU_SPIRAL_PERSONA_BEIGE"]
    TRIBAL: ["SEM_PURPUR_TRIBAL_MAGIC", "CLU_SPIRAL_PERSONA_PURPUR"]
    # ... (Spiral Dynamics stages)

  intuition_config:
    provisional_window: 3
    confirm_window: 5
    decay_window: 12
    multiplier_base: 1.3
    ewma_alpha: 0.2

  decision_rules:
    flag_high: "SEM_SEEDED_ACTIVATION + ..."
    flag_medium: "..."
    auto_deescalate: "..."

  telemetry:
    tracking_enabled: true
    metrics: ["coherence_stability", "persona_transitions", ...]
```

**Purpose:**
- Organizes markers into conceptual families
- Configures detection windows and thresholds
- Defines decision rules for automated responses
- Enables telemetry and metrics tracking

**Convention**: Only edit metadata.yaml for system-wide changes affecting all markers.

---

## Common Tasks for AI Assistants

### Task 1: Add a New Emotional State Marker

**Example: Adding "ATO_EXCITEMENT.yaml"**

```yaml
schema: "LeanDeep"
version: "3.4"
id: ATO_EXCITEMENT
frame:
  signal: ["excitement"]
  concept: "Aufregung / Begeisterung"
  pragmatics: "Emotionsausdruck"
  narrative: "emotion"
tags: [emotion, positive, energy]
pattern:
  regex: "\\b(excited|can't wait|pumped|thrilled|stoked|woo|yay|omg)\\b"
  flags: ["IGNORECASE"]
examples:
  - "I'm so excited!"
  - "Can't wait for this!"
  - "OMG this is amazing!"
  - "Woo! Let's go!"
```

### Task 2: Create a Cluster from Existing Markers

**Example: Detecting "Healthy Conflict Resolution"**

```yaml
name: CLU_HEALTHY_CONFLICT_RESOLUTION
label: "Gesunde Konfliktlösung"
class: cluster
version: 1.0
languages: [de, en]
intent: "Konstruktive Konfliktbearbeitung mit Empathie und Lösungsorientierung"
window:
  size_messages: 15
score:
  method: weighted_k_of_n
  threshold: 0.6
ingredients:
  require:
    - ATO_EMPATHY_MARKERS
  k_of_n:
    k: 2
    of: [ATO_APOLOGY, ATO_COMPROMISE_OFFER, ATO_VALIDATION_THERAPIST, ATO_PROBLEM_SOLVING]
negative_evidence:
  any_of: [ATO_GOTTMAN_CONTEMPT, ATO_GOTTMAN_CRITICISM, ATO_DEFENSIVENESS]
emits:
  indices:
    trust: +0.3
    conflict: -0.3
    safety: +0.2
```

### Task 3: Search for Related Markers

```bash
# Find all empathy-related markers
grep -l "empathy\|empathie" *.yaml

# Find all Gottman-related markers
ls ATO_GOTTMAN_*.yaml CLU_GOTTMAN_*.yaml

# Find markers that emit trust changes
grep -l "trust:" *.yaml

# Find all German-only markers
grep -l "languages: \[de\]" *.yaml
```

### Task 4: Validate Marker Dependencies

```bash
# Check if ingredient markers exist
# Example: CLU_ACTIVE_REPAIR requires ATO_APOLOGY
if [ -f "ATO_APOLOGY.yaml" ]; then
  echo "✓ ATO_APOLOGY exists"
else
  echo "✗ ATO_APOLOGY missing!"
fi
```

### Task 5: Generate Marker Statistics

```bash
# Count markers by type
echo "ATO markers: $(ls ATO_*.yaml | wc -l)"
echo "CLU markers: $(ls CLU_*.yaml | wc -l)"
echo "SEM markers: $(ls SEM_*.yaml | wc -l)"
echo "MEMA markers: $(ls MEMA_*.yaml | wc -l)"

# Find most referenced markers
grep -oh "ATO_[A-Z_]*" *.yaml | sort | uniq -c | sort -rn | head -20
```

---

## Important Psychological & Linguistic Concepts

### Gottman's Four Horsemen

Markers for detecting relationship-destructive patterns:

- `ATO_GOTTMAN_CRITICISM`: Attacking character vs. specific behavior
- `ATO_GOTTMAN_CONTEMPT`: Disrespect, mockery, sarcasm
- `ATO_GOTTMAN_DEFENSIVENESS`: Self-protection, counter-attacking
- `ATO_GOTTMAN_STONEWALLING`: Withdrawal, silent treatment

### Spiral Dynamics Levels

Developmental psychology markers organized by stage:

| Level | Color | Marker Examples |
|-------|-------|-----------------|
| Survival | Beige | `ATO_SD_BEIGE_LEX`, `SEM_BEIGE_SURVIVAL_MODE` |
| Tribal | Purple | `ATO_SD_PURPLE_LEX`, `SEM_PURPUR_TRIBAL_MAGIC` |
| Power | Red | `ATO_SD_RED_LEX`, `SEM_ROT_POWER_ERUPTION` |
| Order | Blue | `ATO_SD_BLUE_LEX`, `SEM_BLAU_ORDER_ACTIVATION` |
| Achievement | Orange | `ATO_SD_ORANGE_LEX`, `SEM_ORANGE_STRATEGIC_FLOW` |
| Community | Green | `ATO_SD_GREEN_LEX`, `SEM_GRUEN_EMPATHIC_RESONANCE` |
| Systemic | Yellow | `ATO_SD_YELLOW_LEX`, `SEM_GELB_SYSTEMIC_INTEGRATION` |
| Holistic | Turquoise | `ATO_SD_TURQUOISE_LEX`, `SEM_TUERKIS_COSMIC_FLOW` |

### Love Languages (Chapman)

Five ways people express and receive love:

- `ATO_LL_WORDS_OF_AFFIRMATION`: Verbal encouragement
- `ATO_LL_QUALITY_TIME`: Undivided attention
- `ATO_LL_RECEIVING_GIFTS`: Thoughtful presents
- `ATO_LL_ACTS_OF_SERVICE`: Helpful actions
- `ATO_LL_PHYSICAL_TOUCH`: Physical affection (adapted for text)

### Attachment Styles

- `CLU_ATTACHMENT_STYLE_SECURE`: Comfortable with intimacy and autonomy
- `CLU_ATTACHMENT_STYLE_ANXIOUS`: Fear of abandonment
- `CLU_ATTACHMENT_STYLE_AVOIDANT`: Discomfort with closeness

### Cognitive Biases

- `ATO_ANCHORING_PHRASES`: First information dominates
- `ATO_ATTRIBUTION_ERROR`: Attributing to character vs. situation
- `CLU_CONSISTENCY_BIAS_PATTERN`: Defending previous positions

### Defense Mechanisms

- `ATO_PROJECTION`: Attributing own feelings to others
- `ATO_RATIONALIZATION_LEX`: Justifying behavior post-hoc
- `ATO_DENIAL`: Refusing to acknowledge reality
- `ATO_BLAME_SHIFT`: Deflecting responsibility

---

## Testing and Validation

### Manual Testing

```bash
# Test regex pattern against examples
# Use online regex testers like regex101.com
# Pattern: \b(verstanden|zur Kenntnis|notiert)\b
# Test: "Verstanden." → Match ✓
# Test: "Nicht verstanden" → Match ✓ (be aware of context!)
```

### Automated Validation (Future Enhancement)

Consider creating validation scripts:

```python
# validate_marker.py
import yaml
import re

def validate_marker(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        marker = yaml.safe_load(f)

    # Check required fields
    assert 'id' in marker or 'name' in marker

    # For ATO markers
    if 'pattern' in marker:
        regex = marker['pattern']['regex']
        examples = marker.get('examples', [])

        # Test regex against examples
        pattern = re.compile(regex, re.IGNORECASE)
        for example in examples:
            assert pattern.search(example), f"Pattern doesn't match: {example}"

    print(f"✓ {filename} validated")

# Usage: validate_marker('ATO_ACKNOWLEDGE.yaml')
```

---

## Git Workflow

### Branch Strategy

- **Main branch**: Not specified (repository doesn't show default branch)
- **Development branches**: Named with `claude/` prefix for AI-generated work
- **Current branch**: `claude/claude-md-miatn17pcillkk9j-01VB9pUs3z875zMdkGFm2Fij`

### Commit Message Conventions

Based on git history:

```bash
# Good commit messages (from history):
"Add comprehensive marker effectiveness catalog"
"Add files via upload"

# Recommended format:
"Add {marker_name} marker for {purpose}"
"Update {marker_name} pattern to handle {case}"
"Fix regex in {marker_name}"
"Create cluster {marker_name} from {components}"
"Document {topic} in CLAUDE.md"
```

### Commit Guidelines

1. **One logical change per commit**: Don't mix new markers with documentation updates
2. **Test before committing**: Validate YAML syntax
3. **Update catalog if needed**: Add new markers to MARKER_WIRKSAMKEITS_KATALOG.md
4. **Clear commit messages**: Describe what and why, not how

### Push Guidelines

```bash
# Always push to the claude/ branch with session ID
git push -u origin claude/claude-md-miatn17pcillkk9j-01VB9pUs3z875zMdkGFm2Fij

# Retry with exponential backoff on network errors
# (handled automatically by Claude Code)
```

---

## Troubleshooting

### Issue: Regex Not Matching

**Symptoms**: Pattern should match but doesn't fire

**Solutions**:
1. Check **escaping**: YAML requires double backslashes (`\\b` not `\b`)
2. Test on **regex101.com** with actual examples
3. Check **word boundaries**: `\b` might not work with punctuation
4. Verify **flags**: IGNORECASE, MULTILINE as needed

### Issue: Duplicate Marker IDs

**Symptoms**: Two markers with same ID

**Solutions**:
1. Check for files with " 2" suffix
2. Rename one marker to unique ID
3. Update any references in CLU/SEM markers

### Issue: Missing Ingredient Markers

**Symptoms**: CLU marker references non-existent ATO marker

**Solutions**:
1. Search for marker: `ls {MARKER_NAME}.yaml`
2. If missing, create it or remove from ingredients
3. Check for typos in marker name

### Issue: YAML Syntax Error

**Symptoms**: File won't parse

**Solutions**:
1. Validate with: `python -c "import yaml; yaml.safe_load(open('file.yaml'))"`
2. Check **indentation** (use spaces, not tabs)
3. Check **list syntax**: `- item` not `-item`
4. Check **string escaping**: Use quotes for special characters

---

## Future Development Directions

### Potential Enhancements

1. **Validation Suite**: Automated testing of all markers
2. **Marker Composer**: Tool to help create new markers
3. **Dependency Graph**: Visualize marker relationships
4. **Pattern Optimizer**: Suggest regex improvements
5. **Supabase Integration**: Full database schema and API
6. **Real-time Detection**: Stream processing pipeline
7. **Visualization Dashboard**: Show detected patterns over time
8. **Multi-language Support**: Expand beyond German/English
9. **Machine Learning**: Train models to detect patterns ML can't regex
10. **Clinical Integration**: HIPAA-compliant therapy support tools

### Research Questions

- Which markers are most predictive of relationship outcomes?
- What marker combinations indicate therapeutic progress?
- Can we detect personality disorders with marker patterns?
- How do marker patterns differ across cultures?
- What's the optimal window size for cluster detection?

---

## Resources and References

### Theoretical Frameworks

- **Spiral Dynamics**: Beck & Cowan (1996)
- **Gottman Method**: Gottman & Silver (1999) - The Seven Principles
- **Attachment Theory**: Bowlby (1969), Ainsworth (1978)
- **Love Languages**: Chapman (1992)
- **Cognitive Biases**: Kahneman & Tversky
- **Defense Mechanisms**: Freud, Vaillant

### Technical Documentation

- **YAML Specification**: yaml.org
- **Regex Tutorial**: regular-expressions.info
- **Supabase Docs**: supabase.com/docs
- **LeanDeep Framework**: (Internal documentation)

### Related Projects

- Natural Language Processing (NLP) libraries
- Sentiment analysis tools
- Relationship quality assessment instruments
- Psychotherapy process research

---

## Quick Reference

### Most Common Markers

**Positive Relationship Markers:**
- `ATO_APOLOGY`: Apologizing
- `ATO_GRATITUDE`: Expressing thanks
- `ATO_EMPATHY_MARKERS`: Showing empathy
- `ATO_COMPROMISE_OFFER`: Offering compromise
- `CLU_ACTIVE_REPAIR`: Conflict repair attempts

**Negative Relationship Markers:**
- `ATO_BLAME_SHIFT`: Deflecting blame
- `ATO_GOTTMAN_CONTEMPT`: Contempt/disrespect
- `ATO_DEFENSIVENESS`: Defensive responses
- `ATO_GUILT_TRIP`: Manipulation via guilt
- `CLU_HEATED_CONFLICT`: Escalating conflict

**Emotional State Markers:**
- `ATO_ANGER`: Anger expression
- `ATO_ANXIETY_TERMS`: Anxiety/worry
- `ATO_JOY`: Joy/happiness
- `ATO_SADNESS`: Sadness
- `ATO_SURPRISE`: Surprise

**Communication Quality:**
- `ATO_CLARIFICATION_REQUEST`: Seeking clarity
- `ATO_HEDGE_TERM`: Hedging/uncertainty
- `ATO_CERTAINTY_PHRASE`: Expressing certainty
- `ATO_QUESTION`: Asking questions

### File Naming Quick Reference

```
ATO_{NAME}.yaml  - Atomic pattern (word/phrase level)
CLU_{NAME}.yaml  - Cluster pattern (multi-marker)
SEM_{NAME}.yaml  - Semantic pattern (context-dependent)
MEMA_{NAME}.yaml - Meta pattern (high-level)
```

### Essential Fields by Marker Type

**ATO Minimum:**
- `schema`, `version`, `id`, `pattern`, `examples`

**CLU/SEM Minimum:**
- `name`, `class`, `version`, `intent`, `ingredients`, `score`, `examples`

---

## Contact and Contribution

**Repository**: DYAI2025/Marker_LD4.0_supabase

**Branch for AI work**: `claude/claude-md-miatn17pcillkk9j-01VB9pUs3z875zMdkGFm2Fij`

**When contributing:**
1. Follow naming conventions
2. Validate YAML syntax
3. Test regex patterns
4. Provide clear examples
5. Update catalog if adding markers
6. Write clear commit messages
7. Push to appropriate claude/ branch

---

**Last Updated**: 2025-11-22
**LeanDeep Version**: 3.4/4.0
**Total Markers**: 919
**Primary Languages**: German (de), English (en)
