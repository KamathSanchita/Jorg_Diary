
---

# Patescibacteria Study

This folder contains the main biological case study of the project, focused on **Patescibacteria MAGs** from marine and terrestrial habitats.

## Purpose

Patescibacteria were used as the central test case for evaluating whether genome circularization improves the interpretation of uncultured microbial genomes. This folder brings together all downstream analyses used to compare **raw** and **circularized/elongated** MAGs.

## Why Patescibacteria?

Patescibacteria are a strong case study for circularization because they are:

- largely **uncultivated**
- often represented by **small, reduced genomes**
- difficult to interpret when assemblies are fragmented
- ecologically important but still poorly resolved
- especially sensitive to missing structural and functional context

For this reason, even modest improvements in assembly continuity can substantially change how their genomes are interpreted.

## Study overview

Using benchmarking-informed thresholds, eligible Patescibacteria MAGs from **marine and terrestrial habitats** were selected for Jorg-based circularization. Circularized and/or elongated genomes were then compared against their original MAGs to evaluate how circularization changed taxonomic assignment, genome quality, structural organization, and functional annotation.

## Main analysis categories

This folder includes four major analysis components:

### 1. Taxonomy
Taxonomic comparison was used to determine whether circularization altered or refined classification.

This may include:
- raw vs circular taxonomic assignments
- lineage consistency checks
- habitat-associated taxonomic patterns
- classification summaries and plots

### 2. CheckM / genome quality
Genome quality assessment was used to compare MAG completeness and contamination before and after circularization.

This may include:
- CheckM completeness values
- contamination estimates
- paired raw vs circular comparisons
- summary tables and plots

### 3. Structural variation
Structural comparisons were used to identify changes such as:

- insertions
- deletions
- inversions
- altered genomic neighborhoods
- locus-level differences between raw and circularized genomes

These analyses help determine whether annotation changes are linked to structural refinement.

### 4. Functional annotation
Functional analyses were used to test whether circularization changed genome interpretation at the annotation level.

This may include:
- KEGG module comparisons
- COG category comparisons
- PFAM family changes
- CAZyme annotation differences
- ortholog gain/loss analysis
- gene-neighborhood examples showing recovered loci

## Why these analyses are combined here

The goal of the Patescibacteria case study is not just to report circularization success, but to determine whether circularization improves downstream biological interpretation.

By integrating:
- **taxonomy**
- **CheckM quality metrics**
- **structural variation**
- **functional annotation**

this folder captures how circularization changes both genome structure and ecological meaning.

## What is included here

This folder may contain:

- candidate MAG lists
- raw and circular genome comparisons
- taxonomy summaries
- CheckM result tables and plots
- structural comparison files
- annotation comparison tables
- locus-level case studies
- summary figures used in the manuscript and poster

## Suggested contents

```text
patescibacteria_study/
├── taxonomy/
├── checkm/
├── structural_variation/
├── functional_annotation/
├── marine_vs_terrestrial/
├── representative_genome_examples/
└── README.md
