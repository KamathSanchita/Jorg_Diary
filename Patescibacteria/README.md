# Benchmarking

This folder contains the benchmarking analyses used to evaluate the performance and practical limits of **Jorg** for short-read MAG circularization.

## Purpose

The benchmarking workflow was designed to assess:

- how **contig number** influences circularization success
- how **coverage** affects performance and output quality
- how Jorg behaves across different MAG characteristics
- how input variables shape **runtime** and **memory usage**
- which thresholds are most appropriate for selecting candidate MAGs for circularization

## What is included here

This folder may contain:

- runtime benchmarking results
- memory usage summaries
- contig-number vs performance analyses
- coverage-based filtering analyses
- candidate-threshold evaluation
- summary tables and plots used in the manuscript and poster

## Why this matters

Benchmarking was a critical first step in this project because it helped define the practical strengths and limitations of Jorg before applying it to **Patescibacteria MAGs** from marine and terrestrial habitats. These analyses also informed workflow refinement and helped improve automation of the original pipeline.

## Suggested contents

```text
benchmarking/
├── runtime_memory/
├── coverage_contigs/
├── summary_tables/
├── plots/
└── README.md
