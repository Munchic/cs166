# Final project: network simulation

#### Simulation of graft-host-leukemia interactions after hematopoietic stem cell transplantation for acute myeloid leukemia

Source code: https://github.com/Munchic/cs166/blob/master/gvhd-gvl-simulation.ipynb

- Parameter quantification
- Ratio of T cell to cancer cells
- Rewrite the part about ATP and stuff

## I. Background

#### 1. About acute myeloid leukemia

Leukemia (blood cancer) develops from mutations that disrupt the normal development pathway of blood cells, often causing the overproduction of non-functional blood cells. American Cancer Society (2018) describes that acute myeloid leukemia (AML) is the most common type of leukemia and can occur in both children and adults. It is called myeloid leukemia because this disease affects the **myeloid progenitor cell** lineage (Fig. 1), which develops into erythrocytes (red blood cells) and essential cells of the innate immune system, responsible for immediate defense against pathogens. An example of innate immune cells affected under AML is neutrophils which make up about 60% of all white blood cells. In a bacterial infection, neutrophils are the first-responders that react to inflammatory signals and perform phagocytosis — engulfment and destruction of a pathogen. If the myeloid cells cannot mature (in AML), the patient can suffer from anemia (low red blood cells count and thus low oxygen delivery to organs) as well severely weakened immune system (e.g., from netropenia).

<img src="/Users/Munchic/Desktop/CS166/FP Fig 1.png" alt="As2 Fig 1" style="zoom:50%;" />

*Figure 1*. Hematopoietic stem cell lineage with focus on the myeloid progenitor cell specialization. Lymphoid progenitor cell lineage is hidden in this diagram. Original diagram by Rad and Häggström (2009).

Although it is a rare cancer (1% of all cancers), AML starts in the bone marrow, quickly moves to the blood, triggers one of the most aggressive cancers in terms of growth speed and resistance to apoptosis. The breadth of the white blood cells AML affects leads to the weakening of the patient’s innate immune system and prevents from ﬁghting oﬀ infections. Statistically, only 28.3% of patients survive after five years, according to the National Cancer Institute (2019).

#### 2. Modern treatment

A contemporary treatment for AML is chemotherapy followed by hematopoietic stem cell (HSC) transplantation. Chemotherapy is meant to wipe out old white blood cells (cancerous and healthy) to make place for HSCs transplantation from a donor. HSC transplant, often called a *graft* in a clinical setting, includes a fully-functional collection immune cells from a donor to help ﬁght oﬀ leukemia.

The most effective transplantation for AML is allogeneic (from other individuals) stem cell transplant from donors whose major histocompatibility complex (MHC) allele closely matches to the that of the receiver, such as from siblings or matched unrelated donor (Battipaglia et al., 2018). MHC (also called human leukocyte **antigen**) is a cell surface protein that present a peptide, a piece of protein manufactured within a cell, for effector immune cells to distinguish between infected (or non-self) and healthy cells. For example, killer CD8+ T cells can detect this antigen presentation and inject granzymes to explode to explode the infected cell (Fig. 2).

<img src="/Users/Munchic/Desktop/CS166/FP Fig 2.png" alt="img" style="zoom:50%;" />

*Figure 2*. Illustration CD8+ T-cell mediated cytotoxicity against an infected cell (cell with a foreign antigen). Original diagram by Dananguyen.

#### 3. Problem definition

A problem arises in selecting a donor due to variability in disease progression that depends on genetic compatibility of donor and recipient (host), speciﬁcally in terms of match of antigens presented on major histocompatibility complex (MHC) I and II. A mismatch in MHCs (usually in unrelated donor and host) means that graft-versus-leukemia (GvL) behavior is strengthened because the donor killer T cells would recognize the “foreign” cells and destroy them (Sweeney et al., 2019). On the other hand, a large mismatch in MHCs can lead to graft-versus-host disease (GvHD), a condition in which host cells are considered foreign and thus are destroyed (Fig. 2).

#### 4. Motivation for simulation

Since minimizing this overlap might be a great challenge of selecting the perfect donor, often methods like T cell depletion (reduction of donor T cells) helps with the situation. The modeling problem this ﬁnal project wants to address is that if we have donors of varying genetic similarity (in terms of MHC), how will levels of T cell depletion aﬀect the progression of GvL and GvHD.

#### 5. Glossary

- **GvHD** — graft-versus-host disease, tranplant attacking normal host cells
- **GvL** — graft-versus-leukemia, transplant attacking blood cancer cells
- **IS** — immune system
- [**H**]**SC**[**T**] — [hematopoietic] stem cell [transplant], healthy bone marrow transplant
- **MHC** — major histocompatibility complex, cell surface proteins to show cell identity
- **RBC** — red blood cell

## II. T cell depletion

#### 1. Mechanism overview

#### 2. Clinical studies

#### 3. Data gathering

## III. Network architecture

#### 1. Overview and assumptions

This project aims to create a network simulation of a simpliﬁed immune system and human cells. Each node will represent a cell, and interaction could lead to cell destruction (node deletion/marking red) or cause more copies of the cell to reproduce ("self-interaction” of stem cells that can divide).

Cancer cells undergo fermentation in which they burn glucose rapidly (to convert to usable ATP energy) without using oxygen; thus, they can proliferate as long as there is energy source. Normal cells require oxygen for this same process, and they use up glucose at a lower pace; the oxygen is carried via red blood cells, a derivative of healthy myeloid cells.

When cancer myeloid cells progress, they will use up resources needed for healthy (donor) myeloid cells to develop. As a reminder, myeloid cells can develop to RBCs that carry oxygen to non-blood cells; therefore impeding development of normal myeloid cells will cause cell death in human host’s other non-blood cells. Additionally, myeloid cells can develop into parts of the innate immune system like neutrophils to protect the host from infections; again, impeding this development can cause cell death due to external pathogen.

In this simulation, there are various dynamics being modelled:

1. Interpopulation interactions upon introduction of different levels of graft CD8+ T cells
2. Intrapopulation interactions with cancer myeloid cells competing for resources (e.g., glucose) with healthy donor myeloid cells which carry oxygen to all healthy cells

There are several assumptions that distinguish this simplified immune system from the complex human immune system:

- **Enclosed system**: only initialized (after chemotherapy and transplantation) immune and host cells can participate (destroy or multiply) in this system; there is no outflux or influx of cells;
- **Immune system abstraction**: because CD8+ T cells play the most important role in GvHD and GvL, we will represent as if they are the only component of the immune system and count other cells as “normal cells” without a particular functionality;
- **Linear genetic overlap**: MHC compatibility is qualified with a large number of genetic markers, each carrying a different contribution towards GvHD/GvL; to simplify, we will use percentages (e.g., $100\%$ = twin, $50\%$ = sibling or parent, $<0.01\%$ = completely unrelated donor);
- **One-on-one interaction**: in this system, only two cells can interact with each other at a time to simplify the update rule and approximations;
- **No signalling pathways**: in a real IS, there are many cytokines (secreted substances that orchestrate immune cells), in this case we just assume that those pathways happen in the background, and relevant cells directly interact;
- **Self-replication only in multipotent stem cells**: this simulation will allow for indefinite self-replication of multipotent hematopoietic stem cells (like in real life) but no replication for myeloid progenitor cells (in real life, they have a limited number of replication cycles);
- **Homogeneity in a cell type population**: this simulation will assume that all cells of the same type will have the same quantitative abilities (e.g., need for oxygen/chance of destroying another cell). In reality, CD8+ T cells will have different T cell receptors (TCR) that determine their potency and affinity towards different kinds of antigens;
- **Constancy of HSCs in production and existence**: this simulation will assume that transplanted HSCs are just there (in the background) and don’t interact with any cell, they will just summon new donor CD8+ T cells and donor myeloid cells; in reality, HSCs divide indefinitely and some of them mature into specialized cells;

#### 2. Cellular agents

1. **Host cancerous myeloid cells**: chemotherapy will not wipe out old myeloid cells completely, so some will remain and try to proliferate; 
   1. 
2. **Host normal T cells**: chemotherapy will not wipe out old white blood cells completely, so some will remain and try to proliferate (e.g., host T cells). These can help ﬁght oﬀ cancerous myeloid cells but they can also ﬁght foreign donor T cells;
3. **Donor T cells**: these will be the main area of interest, how much of them in the system will lead to GvL or GvHD, how much do we need given a genetic mismatch to stay in healthy equilibrium the longest;
4. Host normal hematopoietic stem cells 
5. **Normal non-immune human cells**: these will be the majority of the system (including red blood count), they can get destroyed by donor T cells depending on conditions;

#### 3. Interactions

The interaction will be between two cells at a time and asynchronously updated — this will resemble the random (not really coordinated) interactions that happen within the blood stream. The type of interaction and outcomes will differ depending on what type of agents interact. Apart from interaction of cellular agents, there are global resources (Fig. 3) that the cells compete for to proliferate. 

ASSUME THAT DONOR MYELOID WILL TRANSFORM INTO HEALTHY ONEs

<img src="/Users/Munchic/Desktop/CS166/FP Fig 3.1.png" alt="Screen Shot 2020-04-20 at 17.55.34" style="zoom:50%;" />

*Figure 3*. Interaction diagram of cellular agents in the network simulation. This figure abstracts different types of myeloid cells (e.g., red blood cell/neutrophil) to one type meant to support non-blood cells in a human host.

Let us describe in detail the types of interaction for agents of this system:

1. **Immune and immune**
   1. **Cancer myeloid cells and donor T cells**: upon interaction with donor T cells, depending on genetic mismatch, it will be destroyed. Again, higher mismatch means higher chance of getting destroyed;
   2. **Cancer myeloid cells and host T cells**: upon interaction with host T cells, with a small chance (due to high MHC similarity), the cancer myeloid cells will be destroyed;
   3. **Donor T cells and host T cells**: upon interaction, depending on genetic mismatch, either one of the two can be destroyed or can be left untouched;
2. **Immune and non-immune**
   1. **Cancer myeloid cells and normal cells**: an interaction between these cells will be ignored since they are not directly affecting each other
   2. **Cancer myeloid cells and normal cells**: an interaction between these cells will be ignored since they are not directly affecting each other

#### 4. Parameters

Genetic overlap of AML cells with donor T cells and healthy cells with donor T cells will be available to set as parameters to the model.

1. **Fixed conditioning variables for a baseline simulation**
   1. **Post-chemo AML cells count** ($N_{AML} \in \mathbb{N}$ or `cell_aml_count`):
   2. **Normal non-blood cells count** ($N_{norm} \in \mathbb{N}$ or `cell_norm_count`):
   3. **Relapse chance** ($p_{relapse} \in [0, 1]$ or `p_relapse`): chance of re-appearance of cancer myeloid cells even after the whole cancer population has been wiped out
   4. **Maximal myeloid capacity** ($N_{myeloid\_cap}$ or `cap_myeloid`): myeloid cells are produced from the hematopoietic stem cells located in the bone marrow; due to limit of resources (e.g., glucose), higher growth of myeloid leukemia cells will impede normal myeloid cell maturation;
   5. WQHDUIWQDJHIUWDQ **T cell to cancer myeloid cell ratio** ($k_{transplant}=\dfrac{N_{Tcell}}{N_{AML}}$ or `ratio_t_myeloid`): ratio of counts of T cell in a **non-depleted** transplant to the number of myeloid leukemia cells present in the host after chemotherapy;
   6. **Host cell death threshold** ($\mu_{cell\_death} < 1- \dfrac{N_{AML}}{N_{myeloid\_cap}}\in [0, 1] $ or `thres_cell_death`): threshold of percentage of heatlhy myeloid cells as a total of myeloid capacity, below which the innate immune system and oxygen will be compromised, leading to cell death;
   7. **Cell death chance** ($p_{cell\_death}$ or `p_cell_death`): probability of cell death in an asynchronous update when the host has reached the cell death threshold

2. **Independent “toggle” variables**
   1. **T cell depletion** ($N_{deplete} \in [0, 1]$ or `t_deplete_perc`):
   2. **MHC compatibility** ($MHC_{overlap} \in [0, 1]$ or `mhc_overlap_perc`):

#### 5. Metrics

1. **Overall survival** ($T_{survival}$ or `time_survival`):
2. **Survival without GvHD** ($T_{-GvHD}$ or `time_no_gvhd`):
3. **Survival without GvL** ($T_{-GvL}$ or `time_no_gvl`):
4. **Remission time **($T_{remission}$ or `time_remission`):
5. **Relapse time** ($T_{relapse}$ or `time_relapse`):

## IV. Evaluation scenarios

#### 1. No HSCT intervention



#### 2. Non-depleted HSCT 



#### 3. Low T cell depletion in HSCT



#### 4. Moderate T cell depletion in HSCT



#### 5. High T cell depletion in HSCT



## V. Results

#### 1. No HSCT intervention



#### 2. Non-depleted HSCT

1. **Low MHC compatibility**
2. **High MHC compatibility**



#### 3. Low T cell depletion in HSCT

1. **Low MHC compatibility**
2. **High MHC compatibility**



#### 4. Moderate T cell depletion in HSCT

1. **Low MHC compatibility**
2. **High MHC compatibility**



#### 5. High T cell depletion in HSCT

1. **Low MHC compatibility**
2. **High MHC compatibility**



## VI. Discussion



## VII. Appendix

#### References

American Cancer Society (2018). What Is Acute Myeloid Leukemia (AML)? Retrieved from https://www.cancer.org/cancer/acute-myeloid-leukemia/about/what-is-aml.html

Battipaglia, G., Ruggeri, A., Labopin, M., Volin, L., Blaise, D., Socié, G., … Nagler, A. (2018). Refined graft-versus-host disease/relapse-free survival in transplant from HLA-identical related or unrelated donors in acute myeloid leukemia. Bone Marrow Transplantation. doi:10.1038/s41409-018-0169-6

Cancer.net (2020). Leukemia - Acute Myeloid - AML: Statistics. Retrieved from https://www.cancer.net /cancer-types/leukemia-acute-myeloid-aml/statistics

National Cancer Institute (2019). Cancer Stat Facts: Leukemia - Acute Myeloid Leukemia (AML). Retrieved from https://seer.cancer.gov/statfacts/html/amyl.html

Sweeney, C., & Vyas, P. (2019). The Graft-Versus-Leukemia Eﬀect in AML. Frontiers in Oncology, 9.* doi:10.3389/fonc.2019.01217

Rad, A., & Häggström, M. (2009). Simplified hematopoiesis. Retrieved from https://commons.wikimedia.org/wiki/File:Hematopoiesis_simple.svg

#### Learning outcomes

- #cs166