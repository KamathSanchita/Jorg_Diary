# Circularization Results

This folder contains the primary output genomes generated through the circularization workflow, including MAGs that were successfully **circularized** and genomes that were **elongated or structurally improved** after Jorg-based refinement.

## Purpose

The purpose of this folder is to organize the direct outputs of the circularization pipeline and provide the core genome set used for downstream comparison with the original MAGs.

These results represent the transition point between workflow execution and biological interpretation.

## What is included here

This folder may contain:

- successfully **circularized genomes**
- **elongated genomes** that improved in continuity but did not fully circularize
- candidate output assemblies from iterative Jorg runs
- summary tables listing outcome categories
- metadata describing circularization status
- per-genome output files used in downstream analyses

## Output categories

The genomes in this folder may be grouped into categories such as:

### 1. Circularized genomes
These genomes reached a circular or near-complete form after refinement and represent the strongest outputs of the workflow.

### 2. Elongated genomes
These genomes did not fully circularize but showed measurable improvement in continuity, extension, or local assembly structure.

### 3. Non-improved / unresolved candidates
Where relevant, this folder may also contain records of genomes that did not circularize successfully, to help document workflow limits and candidate outcomes.

## Why this folder matters

This folder is central to the project because it contains the genomes that were compared against their raw MAG counterparts for:

- taxonomy
- completeness
- structural variation
- functional annotation
- locus-level interpretation

It therefore serves as the main bridge between the computational workflow and the downstream biological analyses.

## Suggested contents

```text
circularization_results/
├── circularized_genomes/
├── elongated_genomes/
├── unresolved_candidates/
├── summary_tables/
├── metadata/
└── README.md
