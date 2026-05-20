
# Workflow Automation

This folder contains the refined and semi-automated workflow developed around **Jorg** for short-read MAG circularization.

## Purpose

The workflow component of this project was developed to improve the usability, consistency, and scalability of the original Jorg implementation. In addition to running Jorg itself, this workflow introduces two major refinements:

- a **pre-filtering step** to identify MAGs most suitable for circularization
- an **output analysis step** to systematically compare genomes before and after circularization

Together, these additions make the workflow more practical for larger MAG datasets and more informative for downstream biological interpretation.

## Workflow outline

The refined workflow consists of the following stages:

1. **Input MAG collection**
2. **Pre-filtering**
3. **Jorg-based circularization / elongation**
4. **Output analysis**
5. **Downstream interpretation**

## Pre-filtering step

The pre-filtering step was designed to reduce unnecessary computation and prioritize MAGs most likely to benefit from circularization.

### This step includes:
- filtering by **contig number**
- filtering by **coverage**
- identifying candidate MAGs within practical benchmarking thresholds
- excluding MAGs unlikely to circularize successfully or efficiently

### Why this step matters
Benchmarking showed that variables such as **contig count** and **coverage** strongly influence Jorg performance, runtime, and memory usage. Pre-filtering therefore serves as a critical decision step before circularization.

## Circularization step

Eligible MAGs are processed with **Jorg** using short-read Illumina data.

### This stage focuses on:
- iterative baiting and reassembly
- improvement of candidate MAG continuity
- genome circularization and/or elongation
- generation of refined output assemblies for downstream comparison

## Output analysis step

The output analysis step was added to make the workflow more informative than simply producing circularized genomes.

### This step includes:
- comparing **raw vs circularized MAGs**
- recording which genomes were **circularized**, **elongated**, or unchanged
- preparing results for downstream evaluation of:
  - taxonomy
  - completeness
  - structural variation
  - functional annotation

### Why this step matters
This stage transforms the workflow from a purely assembly-oriented procedure into a comparative framework for assessing how circularization changes biological interpretation.

## What is included here

This folder may contain:

- workflow wrapper scripts
- helper scripts for filtering and execution
- candidate selection logic
- run summaries
- automation scripts
- intermediate processing files
- documentation for workflow steps

## Suggested contents

```text
workflow_automation/
├── pre_filtering/
├── jorg_execution/
├── output_analysis/
├── helper_scripts/
├── workflow_diagrams/
└── README.md
