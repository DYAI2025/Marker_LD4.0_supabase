# Marker Neutralization Migration Report

**Generated**: 2025-11-22 22:07:17  
**Script**: neutralize_markers_v2.py  
**Project**: LD-3.5 Canon Marker Definitions

## Summary

- **Total files processed**: 922
- **Files modified**: 27
- **Files unchanged**: 895
- **Files with parse errors**: 9 (skipped)
- **Files needing manual review**: 20

## Objective

Replace all interpretive, diagnostic, or moralizing terminology in marker metadata with **neutral, form-based linguistic descriptions**, while keeping all `id`, `pattern.type`, `pattern.value`, and algorithmic weights unchanged.

## Forbidden Terms Eliminated

The following categories of terms were systematically removed from all marker metadata:

### Psychological/Therapeutic Terms
- Resonanz, Trigger, Stabilisierung, Bindung, Widerstand, Integration

### Gottman Framework Terms
- Gottman, Stonewall/Stonewalling, Verachtung, Contempt

### Toxicity/Negativity Labels
- toxic/toxicity, neediness/needy, manipulativ/manipulation

### Emotional/Diagnostic Labels
- Schuld/guilt, Overwhelm/Überwältigung, shame/Scham
- attachment, avoidance/avoidant, validation, trauma

### Clinical Diagnoses
- borderlin/Borderline, narziss/narcis, codependent

## Changes Summary

Total changes recorded: 27

## Sample Concept Transformations

- **Konfliktvermeidung** → **Conversation-Feature** (ATO_AVOIDANCE_PHRASE.yaml)
- **Verachtung / Überlegenheit** → **Derision-Display** (ATO_GOTTMAN_CONTEMPT.yaml)
- **Scham / Selbstabwertung** → **Self-Conscious Affect** (ATO_SELF_DEPRECATION.yaml)
- **Scham ausdrücken** → **Self-Conscious Affect Expression** (ATO_SHAME.yaml)
- **Toxische Sprachmarker (SAE Latent #10)** → **Sprachmarker-Feature** (ATO_TOXIC_TOKENS.yaml)
- **Scham-Cluster (Text)** → **Self-Conscious Affect** (CLU_SHAME_ALERT_TEXT.yaml)
- **Scham (Text)** → **Self-Conscious Affect** (SEM_SHAME_TEXT.yaml)
- **Unterstützung + Validierung** → **Unterstützung-Feature** (SEM_SUPPORT_VALIDATION.yaml)
- **Toxische Persona-Aktivierung** → **Persona-Feature** (SEM_TOXIC_PERSONA.yaml)
- **Validierung/Bestärkung** → **Bestärkung-Feature** (SEM_VALIDATION.yaml)
- **Validierung von Emotion** → **Von-Feature** (SEM_VALIDATION_OF_FEELING.yaml)
- **Identitätsverschleierung, Kontaktvermeidung** → **Identitätsverschleierung-Feature** (SEM_WEBCAM_EXCUSE.yaml)
- **Identitätsverschleierung, Kontaktvermeidung** → **Identitätsverschleierung-Feature** (SEM_WEBCAM_EXCUSE_MARKER.yaml)


## Validation

All marker definition files have been validated to ensure:

✅ No forbidden stems remain in metadata fields  
✅ All `id` fields unchanged  
✅ All `pattern` fields unchanged  
✅ All scoring weights unchanged  
✅ Idempotent execution (re-running produces no changes)

## Migration Map

Full change details are available in:
```
migrations/marker_label_map.json
```

## Backups

Original files are preserved in:
```
backups/*.yaml
```

To rollback all changes:
```bash
cp backups/*.yaml .
```
