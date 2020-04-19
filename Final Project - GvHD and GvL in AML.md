# Final project: network simulation

#### Simulation of graft-host-leukemia interactions after hematopoietic stem cell transplantation for acute myeloid leukemia

Source code: 

## Background

#### About acute myeloid leukemia

Acute myeloid leukemia (AML) is a type of blood cancer that can occur in children and adults. It triggers one of the most aggressive types in terms of growth speed and resistance to apoptosis (cell death) with only about 27% survival rate (Cancer.net, 2020). It is called myeloid leukemia because the myeloid lineage (see Fig. 1) is aﬀected lead to malfunctional neutrophil and macrophages. This weakens the patient’s innate immune system and prevents from ﬁghting oﬀ infections.

#### Modern treatment

A contemporary treatment for AML is chemotherapy followed by hematopoietic stem cell (HSC) transplantation. Chemotherapy is meant to wipe out old white blood cells (cancerous and healthy) to make place for HSCs transplantation from a donor. The latter includes a fully-functional collection immune cells from a donor to help ﬁght oﬀ leukemia.

#### Problem definition

A problem arises in selecting a donor due to variability in disease progression that depends on genetic compatibility of donor and recipient (host), speciﬁcally in terms of match of antigens presented on major histocompatibility complex (MHC) I and II. A mismatch in MHCs (usually in unrelated donor and host) means that graft-versus-leukemia (GvL) behavior is strengthened because the donor killer T cells would recognize the “foreign” cells and destroy them (Sweeney et al., 2019). On the other hand, a large mismatch in MHCs can lead to graft-versus-host disease (GvHD), a condition in which host cells are considered foreign and thus are destroyed (Fig. 2).

#### Motivation for simulation

Since minimizing this overlap might be a great challenge of selecting the perfect donor, often methods like T cell depletion (reduction of donor T cells) helps with the situation. The modelling problem this ﬁnal project wants to address is that if we have donors of varying genetic similarity (in terms of MHC), how will levels of T cell depletion aﬀect the progression of GvL and GvHD.

## Network architecture

#### Cellular agents

#### Interactions

#### Parameters

#### Outcomes

## Evaluation scenarios



## Appendix

#### References

Cancer.net (2020). Leukemia - Acute Myeloid - AML: Statistics. Retrieved from https://www.cancer.net /cancer-types/leukemia-acute-myeloid-aml/statistics

Sweeney, C., & Vyas, P. (2019). The Graft-Versus-Leukemia Eﬀect in AML. Frontiers in Oncology, 9.* doi:10.3389/fonc.2019.01217



#### Learning outcomes

- #cs166