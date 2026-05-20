# Short-read MAG Circularization with Jorg
## Benchmarking, workflow refinement, and application to Patescibacteria

This project evaluates the potential of short-read Illumina data for metagenome-assembled genome (MAG) circularization using **Jorg**, improves workflow automation, and tests how circularization changes the structural and functional interpretation of **Patescibacteria** genomes from marine and terrestrial habitats. This repository is meant to track all the necessary steps to successfully make and improve the tool Jorg runs. The git page of the Jorg tool is [Here](https://github.com/lmlui/Jorg/tree/master).


---

## Project summary

Most metagenome-assembled genomes generated from short-read data remain fragmented, which limits robust structural, functional, and ecological interpretation. This is especially problematic for **Patescibacteria**, an abundant but largely uncultured bacterial lineage characterized by reduced genomes, limited metabolic capacity, and poorly resolved genome architecture. Although long-read and hybrid sequencing approaches are promising, they are still not always feasible for large collections of MAGs.

Together, these gaps motivated the present study, which evaluates the potential of short-read Illumina data for MAG circularization using **Jorg**. We first applied Jorg to systematically assess its advantages, limitations, and performance against key dependent variables influencing computational resource consumption. Building on these results, we further improved the workflow to make it more automated than the current implementation. Using the knowledge gained from this benchmarking, we then tested the approach on **Patescibacteria MAGs from marine and terrestrial habitats**. Of **171 eligible MAGs**, **60 were circularized and/or elongated**, after which we compared MAGs before and after circularization in terms of **taxonomy, completeness, structural variation, and functional annotation**. This study therefore provides both a practical assessment of Jorg for short-read MAG circularization and a test case for understanding how circularization can improve downstream interpretation of microbial data.

---

## Why this project matters

Genome circularization is a vital refinement step for MAG analysis because it can:

- improve structural accuracy
- restore genomic context
- strengthen interpretation of gene neighborhoods and synteny
- improve pathway and module recovery
- clarify replication-associated context
- enhance ecological inference from uncultured genomes

This is particularly important for **Patescibacteria**, because they are:

- largely **uncultivated**
- often represented by **small and reduced genomes**
- frequently recovered as **fragmented MAGs**
- difficult to interpret using standard short-read assemblies alone
- ecologically relevant but functionally under-resolved

For such organisms, even a small improvement in genome continuity can substantially alter how we interpret metabolic potential, structural organization, and evolutionary patterns.

---

## Study aims

This project was designed around three central questions:

1. **How does genome circularization improve the resolution and interpretation of uncultured bacterial genomes?**
2. **Can circularized Patescibacteria genomes reveal habitat-associated evolutionary patterns across marine and terrestrial environments?**
3. **Does circularization improve recovery of functional potential relative to fragmented MAGs?**

---

## Why Patescibacteria?

Patescibacteria were selected as a focal lineage because they provide a strong biological test case for genome circularization.

### Why they fit this project
- They are **abundant but poorly characterized**
- Many members remain **uncultured**
- They often have **ultra-small, streamlined genomes**
- Their ecological roles are difficult to infer from fragmented assemblies
- Their reduced genomic content makes them especially sensitive to assembly fragmentation

### Why circularization matters for them
Circularization can improve:
- detection of compact functional loci
- interpretation of structural rearrangements
- reconstruction of replication-associated features
- gene-neighborhood and operon-like context
- confidence in ecological and evolutionary inference

In short, Patescibacteria are a powerful case study for testing whether circularization improves biological interpretation beyond what standard MAG assemblies can provide.

---

## Workflow overview

The overall workflow of this project is:

**Input MAGs**  
→ **filter by contig number and coverage**  
→ **benchmark Jorg performance**  
→ **refine workflow automation**  
→ **run circularization/elongation**  
→ **compare raw vs circularized MAGs**  
→ **analyze taxonomy, completeness, structural variation, and functional annotation**

Adding workflow figure here:

```markdown
![Workflow overview](figures/workflow_overview.png)
```

## Key results

- **171 MAGs** met the filtering criteria for circularization analysis.
- **60 MAGs** were successfully **circularized and/or elongated**.
- Benchmarking identified **contig number** and **coverage** as major variables influencing Jorg performance, runtime, and memory usage.
- Circularization refined genome interpretation across **taxonomy**, **completeness**, **structural variation**, and **functional annotation**.
- Comparative analyses showed post-circularization changes in **KEGG modules**, **COG categories**, **PFAM families**, **CAZyme profiles**, and **ortholog content**.
- Locus-level examples demonstrated that circularization can recover **structurally distinct genomic regions** and **functionally informative genes** that remain fragmented or obscured in raw MAGs.
- The **Patescibacteria case study** showed that even relatively well-assembled short-read MAGs can gain additional biological resolution after circularization.

## Conclusion

This work shows that even relatively well-assembled short-read MAGs can benefit from circularization, and that genome refinement can alter downstream interpretation of microbial function and structure in meaningful ways.
   





