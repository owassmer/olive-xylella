# Project CORDON

Computational Observation and Resistance Decoding for Olive Networks

Status: current program, 15 August 2026
Owner: Owen Wassmer + Connor
Mode: computational only until a named Italian partner agrees to wet-lab or field work
Workspace: ~/Desktop/Connor/olive-xylella/

This is not a survey of options. It is the program.

---

## 0. The decision, in one paragraph

We will not invent a field cure. EFSA closed outdoor clearance. We will not start a wet lab or fly a plane.

We will do two things a computational team can move:

1. Test whether an official diagnostic-positive olive has a remotely detectable signature before or around the sample date, at tree scale, after matching for cultivar, place, drought, and canopy. If that test dies, stop calling this early detection.
2. Turn published resistance biology into a ranked target list for Italian breeders.

That is Project CORDON. No 90-day cap. Attach to CNR-IPSP / BeXyl when there is a number and a table, not a pitch.

---

## 1. What the crisis actually is

### 1.1 The organism

This is not a virus and not a “bug” in the insect sense, though an insect carries it.

- Pathogen: *Xylella fastidiosa* subsp. *pauca*, sequence type ST53 (historically CoDiRO).
- Lifestyle: xylem-limited Gram-negative bacterium. Cells attach to vessel walls, form biofilm (DNA, protein, exopolysaccharide). The plant answers with tyloses and gums. Water transport fails. The tree scorches from the canopy down and dies.
- Vector in Europe: the meadow spittlebug *Philaenus spumarius*, a xylem feeder. Sharpshooters that drive Pierce’s disease in California are not established here.
- Host range of the species: hundreds of plant species (EFSA host database: 696 species / 88 families as of the 2023 update; still growing). The Apulian olive catastrophe is a specific collision: ST53 + highly susceptible local cultivars + abundant *P. spumarius* + a climate that lets the vector live on olive for long periods.

First EU detection: olive in southern Puglia, October 2013. Containment declared May 2015 because eradication was already infeasible.

### 1.2 What has been lost

Independent sources do not agree on a single tree-count, and we should not pretend they do.

- Agromillora / regional synthesis (Nov 2025): infected area ~8,000 km², about 40% of Puglia; more than 10 million olive trees dead.
- Popular and campaign figures often cite ~21 million trees infected. Treat that as an upper popular estimate, not a census.
- FADN-farm study (2025): €132 million economic loss on surveyed Salento farms.
- Schneider et al., PNAS 2020: if ST53 keeps spreading through climatically suitable European olive land, Italy’s 50-year grower impact is €1.9–5.2 billion if production ceases after die-off, or €0.6–1.6 billion if resistant cultivars can be replanted. Slowing radial spread from 5.18 to 1.1 km/year saves €0.5–1.3 billion over 50 years. Almost all Italian, Greek, and Spanish olive land is climatically suitable.

The cultural loss is not in those numbers. Centuries-old *Ogliarola salentina* and *Cellina di Nardò* groves are landscape, identity, and oil chemistry, not just yield.

### 1.3 Where it is now (as of late 2025 / early 2026)

- The *pauca* ST53 front has slowed. Northernmost confirmed olive finds as of late March 2025: seven trees on the southern outskirts of Bari, treated as hitchhiking-vector cases along roads, promptly eradicated.
- In old Salento, some heavily damaged trees have started producing again. Donato Boscia (CNR, the 2013 isolation team) attributes this empirically to fewer spittlebugs and therefore fewer “superinfections” of the same tree — not to a cure.
- New and more dangerous complexity: in 2024 Bari province also yielded *X. fastidiosa* subsp. *fastidiosa* ST1 (Pierce’s disease genotype) next to Europe’s most important table-grape district (Noicattaro / Rutigliano), plus *multiplex* ST26 on the Murge. Tens of thousands of tests; eradication of ST1 including ~30 ha of vineyard is underway. California sharpshooters are absent; *P. spumarius* is considered a secondary vector for Pierce’s. This is still a live risk, not a closed incident.
- The same species, different subspecies, is established or under eradication in Corsica, PACA, Occitanie, Balearics, Alicante, Porto, Tuscany, Lazio.

So the popular story “it is racing unstoppably north and nobody has anything” is half right. The *pauca* olive front slowed. The strategic picture got worse: more subspecies, grape at risk, and the olive problem is now endemic in the south.

### 1.4 What has already been tried

| Approach | Result | Status |
|---|---|---|
| Eradication of all hosts in a radius | Politically explosive; too late once established | Containment only south of the buffer |
| Vector control (soil tillage of nymphs; adult insecticides Apr–Oct) | Slows the front; does not clear the south | Mandatory in demarcated areas |
| 50 m felling around a positive | Standard EU tool | Still in force |
| Zinc / copper / citric acid (Dentamet) and N-acetylcysteine | Symptom reduction, some harvests kept; pathogen remains | EFSA 2016: not a cure. Later work still “promising field-transferable,” not sterilizing |
| Severe pruning + bioactive sprays | Vigorous flush, temporary | Same EFSA caveat |
| Sniffer dogs | Useful for cryptic detection | Operational niche, not landscape scale |
| Airborne hyperspectral + thermal (Zarco-Tejada) | >80% previsual detection vs qPCR (2018); <6% uncertainty after disentangling drought (2021); >92% across Xf vs Verticillium | Proven physics, not an operational public system |
| Resistant cultivars Leccino, FS-17 (Favolosa), later Lecciana and Leccio del Corno | Infected, but lower load, slower internal spread, milder dieback, longer incubation | Only legal replant set in the infected zone |
| Screening the rest of olive diversity | No cultivar beat Leccino / FS-17 | La Notte / Saponari 2024: Leccino offspring are the real seam |
| Phage (Ahern 2014 CA; Clavijo-Coppens 2021 Med; MATE 2 2024) | Lytic in vitro; very short list | Not a field olive product |
| EU projects POnTE, XF-ACTORS, BeXyl, BIOVEXO | The professional backbone | We attach to them. We do not reinvent them. |

Official monitoring: more than one million diagnostic tests in ten years. Open slice: Regione Puglia CKAN dataset `dati-monitoraggio-xylella-fastidiosa` (CAMP_2020_2022.csv, CAMP_2020_2023.csv), last updated 23 Dec 2025. Maps and guidance: emergenzaxylella.it.

### 1.5 What “resistance” actually means

It is not immunity.

A resistant olive still gets infected. Incubation is longer. Canopy dieback is milder and more limited. Bacterial concentration is lower. Internal spread is limited. That last point matters epidemiologically: a spittlebug feeding on Leccino acquires less bacterium, so landscape inoculum falls as resistant groves replace dead susceptible ones.

Mechanisms that have actual evidence, not slogans:

- Pit membranes: ST53 exploits degraded pit membranes to move vessel-to-vessel. Susceptible *Cellina di Nardò* shows severe pit-membrane degradation; Leccino does not to the same degree (Montilon 2022, Giampetruzzi 2021).
- Hydraulics: Leccino is constitutively less prone to xylem cavitation and refills vessels faster (Sabella 2019). Infected physiology looks like drought; resistant trees manage that drought better (Surano 2022).
- Transcriptome: 659 differentially expressed genes in infected Leccino vs 447 in Ogliarola (Giampetruzzi 2016). Cell-wall receptors and immune pathways recur.
- Endophytes: Leccino keeps a more stable xylem/endophytic community under OQDS.
- Heritability: of 171 symptom-poor spontaneous genotypes in the high-inoculum zone, 139 unique SSR profiles; Leccino, Cellina, and Ogliarola were the most common candidate parents. Among 61 Leccino progeny, 67% scored highly resistant, resistant, or tolerant, versus 32% from Cellina and 49% from Ogliarola. Artificial inoculation of four open-pollinated Leccino seedlings confirmed the phenotype. One genotype (S105) was transcriptomically more resilient than S215 and S234 (La Notte, Saponari, Giampetruzzi, Saldarelli et al. 2024).

This is the breeding door. It is also the computational door: the gene lists already exist in public papers.

---

## 2. The two technologies you named, read honestly

### 2.1 The dog (Rosie / Paul Conyngham, 2026)

What actually happened: a mast-cell tumor, failed surgery and chemo, tumor sequenced at UNSW, ChatGPT used to navigate neoantigen design, AlphaFold used for structure, Pall Thordarson’s lab made the mRNA and put it in lipid nanoparticles, a vet administered it with a checkpoint inhibitor. Largest tumors shrank. Mobility came back. It was not a cure. Boosters are being designed against resistance mutations. The checkpoint inhibitor confounds attribution.

Transferable pieces:

- Tissue → data → ranked targets → a real wet-lab partner who already has a manufacturing workflow.
- Speed (about two months from finished design to injectable) came from using an existing mRNA pipeline, not from the chatbot.
- A computationally literate non-biologist can orchestrate specialists if the target definition is crisp.
- Personalization was the point. A one-off for one patient.

What does **not** transfer:

- “AI cured cancer.” It did not.
- We cannot inject an olive with an mRNA cancer vaccine.
- We should not freelance a therapeutic into a quarantine pest system.

What we steal: the Rosie loop. Sequence (or public genome) → model the vulnerability → rank candidates → hand a short list to people who can actually make and test them.

### 2.2 The scrolls (Vesuvius Challenge)

What actually happened: carbon ink is almost invisible on carbonized papyrus in CT. Brent Seales’s virtual unwrapping + an open CT dataset + >$1M in prizes + a public Discord produced, in under a year, readable Greek from inside an unopened scroll. Winning traits: multiple model architectures to block hallucination, label smoothing, held-out folds, independent papyrologists as the real evaluator, open-sourced winning code.

Transferable pieces:

- The scientific object is a **hidden signal in a 3-D noisy volume**. For olives, the hidden signal is previsual physiological change (fluorescence, thermal, pigment) inside a landscape that also has drought, *Verticillium*, salt, and age.
- Open labeled data plus a hard external oracle (here: qPCR / official positives, not papyrologists) beats a closed academic demo.
- Do not launch a prize until you have a dataset the crowd can train on and a scorer that cannot be gamed.

What does **not** transfer on day one:

- We do not have a million-dollar prize budget.
- Puglia already spent a decade and a million PCR tests. We do not get to act as if the data problem is unsolved. We get to **operationalize** what Zarco-Tejada proved and what the Osservatorio already collected.

---

## 3. Cross-domain moves that are actually useful

These are not metaphors for the slide deck. Each one maps onto a CORDON workstream.

| Foreign domain | Hidden-signal trick | Olive use |
|---|---|---|
| Vesuvius ink detection | Multi-architecture ensemble + human oracle | Previsual front model: spectral/thermal features, official PCR as labels, never a single net |
| Drought-vs-disease spectroscopy (Zarco-Tejada 2021) | Divergent abiotic vs biotic spectral pathways | Mandatory: every detection model must beat a drought-only baseline |
| Rosie neoantigen ranking | Mutation list → MHC-style filter → structure | ST53 proteome → xylem-exposed proteins → AMP/phage targets |
| Cancer circulating-tumor-DNA | Detect the pathogen before the lesion | Vector PCR in the buffer (Puglia already trialing this) + our nowcast as the spatial prior |
| Genomic selection in livestock | Predict breeding value from relatives + markers | Leccino-offspring SSR/transcriptome → a ranking of untested seedlings |
| Pierce’s disease / PdR1 in grape | One locus, decades of breeding | Do not assume a single olive locus. Rank pathways (pit membrane, hydraulics, cell wall) first |
| Citrus HLB / Huanglongbing | Another xylem/phloem uncured epidemic; remote sensing + resistant rootstocks | Steal operational playbooks, not molecules |
| Antimicrobial-peptide generators (2025–26 AMPGAN, MAC-AMP, ProDCARL) | De novo sequence design against a proteome | Phase-2 paper candidates only, never synthesis by us |
| Epidemic nowcasting (COVID wastewater, influenza ILI) | Noisy spatially biased tests → front | Puglia’s million tests are a biased but gold surveillance system. Model the bias. |

---

## 4. Locked program design

### 4.1 What we are building

Two artifacts, one partner brief.

**Artifact A — Pre-diagnostic test (then a nowcast only if it lives)**
Tree-level official diagnostic labels (campaign workbooks 2013–2025). Crown geometry from Puglia 0.15–0.20 m orthophotos and Crecco WV2-derived rasters. Sentinel-2 time series as the repeatable VNIR/red-edge/SWIR measurement, unmixed with VHR fractions. Sentinel-1 and Landsat LST (100 m native) as structure and drought controls.

Artifact A is a ledger of measurement hypotheses, not one test. Branches close; the artifact closes only when every accessible, biologically plausible measurement branch is tested or proven inaccessible. See `nowcast/ARTIFACT_A.md`. Branch A0 (raw absolute Sentinel-2 NDMI at 10/20 m) is a closed negative on 1,679 matched pairs. That null bounds the cheapest sensor; it does not answer whether the precursor is absent or diluted by the 400 m² SWIR pixel. Open branches: temporal anomaly (A1), crown-fraction dilution (A2), released crown-scale WV2/CIR optical (A3), WV-3 SWIR (A4), airborne physiology (A5).

**Artifact B — Resistance Decoder v0**
Unchanged object: ranked olive pathways and ST53-exposed targets from papers we hold. S105/S215 beat parental Leccino on canopy. Computational only. Do not synthesize.

**Artifact C — Partner brief**
Written only after Artifact A has a lag number and Artifact B has a table. The ask is then a named missing measurement (WV-3 SWIR, airborne HS+thermal, IRIDE), not a general introduction.

### 4.2 What we are explicitly not building

- A consumer app for tourists.
- A drone company.
- A CRISPR olive.
- A backyard phage lab.
- A prize challenge in month 1.
- Another literature review with no pipeline.

### 4.3 Why this wedge, not the others

Slowing the front is the intervention PNAS priced in the high hundreds of millions of euros. Official diagnostic points already exist at tree coordinates. Sub-meter geometry is on public ImageServers. The question is whether a physiological signal exists *before* the diagnostic date after drought matching. That is the Vesuvius-shaped problem. The oracle is the official result, not a self-score.

Resistance decoding is the Rosie-shaped problem: public transcriptome, ranked targets, handoff to people with greenhouses. Unchanged.

A field therapeutic is a decade and a regulated lab. We do not pretend otherwise.

### 4.4 Technology decisions (locked)

| Decision | Choice | Why |
|---|---|---|
| Compute | Owen’s Mac, local Python, no new paid cloud | Free-tier-safe; Copernicus and Puglia data are free |
| Satellite | S2 time series + VHR crowns + S1 + Landsat LST | S2 is the cadence/SWIR baseline, not the spatial unit |
| Labels | Campaign xlsx 2013–2025; call them diagnostic until assay is read | Tree-level official result, symptom, cultivar |
| Model class, nowcast | Matched case-control first; GBT only if a lag survives | No Transformer until matching holds |
| Oracle | Held-out comuni and a later campaign | No random neighbor split |
| Omics | Reanalysis of published counts / GEO / paper supplements, not new sequencing | We do not generate olive RNA in this apartment |
| AMP / phage | Paper candidates only | Quarantine pest. No synthesis. |
| Literature engine | Connor + Exa search + Firecrawl extract + arXiv | Already configured |
| Partner #1 | CNR-IPSP Bari (Saponari, Boscia, Giampetruzzi, Saldarelli) | They isolated it, they published the resistance progeny, they sit in Bari |
| Partner #2 if #1 is silent | BeXyl consortium / CRSFA Basile Caramia (Locorotondo) | Already on the 2024 paper |
| Do not compete with | Planetek REDoX, Zarco-Tejada group, BIOVEXO biopesticide work | Complement. Offer the open nowcast + decoder. |
| Legal | Computational. No plant or insect movement. No unpublished genome redistribution if licenses forbid it. | Xylella is an EU quarantine pest |
| Language of outreach | English brief + Italian one-pager | Courtesy, and Bari is the audience |
| Budget | $0 cash. ESA TPM / PRISMA / SAOCOM are free applications | Paid imagery only after Experiment 1 |

### 4.5 Team shape

- Owen: decisions, partner email, any later travel to Bari.
- Connor: literature graph, data pull, pipeline, evaluation, brief drafts.
- Named scientist (not us): inoculation, qPCR, any phage or peptide assay.

If we cannot name that scientist by day 90, the program pauses. We do not freelance biology.

---

## 5. Current work order

1. Orthophoto note + Crecco v5 download + CAMP ∩ Crecco count.
2. Experiment 1 matching protocol frozen, then F7 as the first table (symptom-absent 2021).
3. Longitudinal S2/S1 extract at −365…+90 days. Out-of-area metric.
4. PRISMA register (catalog is public). 2015_IR used as CIR context, not NDMI.
5. Decoder table to olive loci / Suppl. S4 when PDFs arrive.
6. Partner brief only after a lag number exists. Ask is WV-3 SWIR or airborne HS, named.

No 90-day stop. If Experiment 1 dies after matching, Artifact A is closed as a negative. Decoder continues.

---

## 6. After a partner

1. Add their airborne HS+thermal on the same diagnostic trees.
2. Score the decoder on real seedlings.
3. Peptide or phage stays in their containment lab.
4. ESA TPM WorldView-3 SWIR if Experiment 1 says mixed pixels are the limit.

---

## 7. Risks

- Diagnostic points may not sit on the crown. VHR attach can fail. Report the miss rate.
- Spectral Xylella is entangled with drought and *Verticillium*. Matching is the control. If it dies, stop.
- `SINTOMO` and `RISULTATO` are official fields, not a named assay until we read each campaign.
- Replant-with-Leccino is already the landscape strategy.
- ST1 on grape is a separate product. Filter olive + pauca for Artifact A.
- No synthesis. Quarantine pest.
- Earlier suspicion can reduce indiscriminate cuts or justify them. Confirm with a lab test before removal.

---

## 8. This week

1. Write `data/ORTOFOTO.md`. Download Crecco v5. Count CAMP ∩ Crecco.
2. Freeze `nowcast/EXPERIMENT1.md`. Run the 2021 symptom-absent table if n ≥ 40.
3. Do not email Bari.

---

## 9. Core sources (primary, not press)

- Saponari et al. 2013 / 2019 — first detection; Apulia review.
- EFSA 2016 statement — treatments do not eliminate the pathogen.
- EFSA 2017 — Leccino / FS-17 susceptibility review.
- Giampetruzzi et al. 2016 BMC Genomics — Leccino vs Ogliarola transcriptome.
- Zarco-Tejada et al. 2018 Nature Plants — previsual spectral traits, >80% vs qPCR.
- Zarco-Tejada et al. 2021 Nature Communications — biotic vs abiotic pathways, <6% uncertainty.
- Schneider et al. 2020 PNAS — €1.9–5.2bn / €0.6–1.6bn; value of slowing spread.
- Montilon et al. 2022 Plant Pathology — pit membranes.
- Surano et al. 2022 Frontiers — hydraulics of resistant vs susceptible.
- La Notte, Saponari, Giampetruzzi, Saldarelli et al. 2024 Frontiers — Leccino offspring, 67% R/T.
- Ahern et al. 2014; Clavijo-Coppens et al. 2021; Sabri et al. 2024 — Xylella phages.
- Commission IR (EU) 2020/1201 and 2024/2507 — legal regime.
- Puglia campaign workbooks 2013–2025 (`raw/data/camp_xlsx/`); CKAN extract is a subset.
- Crecco et al. 2025 Data in Brief; figshare 28191245 v5.
- Agromillora / Agrimeca Nov 2025 — current front, ST1/ST26, 8,000 km².
- BeXyl / Il Post via Boscia, Jan 2026 — Salento recovery, vector decline.

---

## 10. One-sentence contract

CORDON exists to test, at individual-tree scale, whether official diagnostic positivity has a remotely detectable precursor after drought and cultivar matching, and to put a cited resistance-target table in a CNR inbox, without touching a live bacterium.
