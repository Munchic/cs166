## CS166 Final Project Proposal

#### Modeling problem

Acute myeloid leukemia (AML) is a type of blood cancer that can occur in children and adults. It triggers one of the most aggressive types in terms of growth speed and resistance to apoptosis (cell death) with only about 27% survival rate (Cancer.net, 2020). It is called myeloid leukemia because the myeloid lineage (see Fig. 1) is affected lead to malfunctional neutrophil and macrophages. This weakens the patient’s innate immune system and prevents from fighting off infections.

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Hematopoiesis_simple.svg/2880px-Hematopoiesis_simple.svg.png)

*Figure 1*. Cell lineage for hematopoietic stem cells divinding into various white blood cells. Figure adapted from Wikipedia.

A contemporary treatment for AML is chemotherapy followed by hematopoietic stem cell (HSC) transplantation. Chemotherapy is meant to wipe out old white blood cells (cancerous and healthy) to make place for HSCs transplantation from a donor. The latter includes a fully-functional collection immune cells from a donor to help fight off leukemia.

A problem arises in selecting a donor due to variability in disease progression that depends on genetic compatibility of donor and recipient (host), specifically in terms of match of antigens presented on major histocompatibility complex (MHC) I and II. A mismatch in MHCs (usually in unrelated donor and host) means that **graft-versus-leukemia** (GvL) behavior is strengthened because the donor killer T cells would recognize the “foreign” cells and destroy them (Sweeney et al., 2019). On the other hand, a large mismatch in MHCs can lead to **graft-versus-host disease **(GvHD), a condition in which host cells are considered foreign and thus are destroyed (Fig. 2).

<img src="/Users/Munchic/Library/Application Support/typora-user-images/Screen Shot 2020-04-05 at 13.02.41.png" alt="Screen Shot 2020-04-05 at 13.02.41" style="zoom:50%;" />Agents

*Figure 2*. Antigen presentation by healthy cell versus leukemia cell to a donor killer T cell.

Since minimizing this overlap might be a great challenge of selecting the perfect donor, often methods like T cell depletion (reduction of donor T cells) helps with the situation. The modelling problem this final project wants to address is that if we have donors of varying genetic similarity (in terms of MHC), how will levels of T cell depletion affect the progression of GvL and GvHD.

#### Agents

This will be a **network simulation** of a simplified immune system and human cells. Each node will represent a cell, and interaction could lead to cell destruction (node deletion/marking red) or cause more copies of the cell to reproduce. The interaction will be between two cells at a time and asynchronously updated — this will resemble the random (not really coordinated) interactions that happen within the blood stream. Genetic overlap of AML cells with donor T cells and healthy cells with donor T cells will be available to set as parameters to the model.

1. **Host cancerous myeloid cells**: chemotherapy will not wipe out old white blood cells (including myeloid) completely, so some will remain and try to proliferate. Upon interaction with donor T cells, depending on genetic mismatch, it will be destroyed. Again, higher mismatch means higher chance of getting destroyed;
2. **Host normal immune cells**: chemotherapy will not wipe out old white blood cells completely, so some will remain and try to proliferate (e.g., host T cells). These can help fight off cancerous myeloid cells but they can also fight foreign donor T cells;
3. **Donor T cells**: these will be the main area of interest, how much of them in the system will lead to GvL or GvHD, how much do we need given a genetic mismatch to stay in healthy equilibrium the longest;
4. **Normal non-immune human cells**: these will be the majority of the system, they can get destroyed by donor T cells depending on conditions;
5. (Optionally) **other immune cells**: there are other immune cells such as B cells that can produce antibodies that help “tag” targets for destruction and increase the chance of cancerous cells being found and destroyed by T cells.

#### References

Cancer.net (2020). Leukemia - Acute Myeloid - AML: Statistics. Retrieved from https://www.cancer.net/cancer-types/leukemia-acute-myeloid-aml/statistics

Sweeney, C., & Vyas, P. (2019). *The Graft-Versus-Leukemia Effect in AML. Frontiers in* Oncology, 9.* doi:10.3389/fonc.2019.01217