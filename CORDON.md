# Project CORDON

Computational Observation and Resistance Decoding for Olive Networks

Status: locked program, 15 August 2026
Owner: Owen Wassmer + Connor
Mode: computational only until a named Italian partner agrees to wet-lab or field work
Workspace: ~/Desktop/Connor/olive-xylella/

This is not a survey of options. It is the program.

---

## 0. The decision, in one paragraph

We will not try to invent a field cure for *Xylella fastidiosa*. EFSA already closed that door: existing treatments reduce symptoms and do not eliminate the bacterium from outdoor trees. We will not start a wet lab, import cultures, move plant material, or fly our own hyperspectral plane.

We will do the two things a two-person computational team can actually move, and that the literature says are worth the most money and trees:

1. Make the northern infection front visible before humans can see it.
2. Turn published resistance biology into a usable target map for Italian breeders and, later, for peptide or phage partners.

That is Project CORDON. Ninety days to a partner-ready evidence pack. Then we either attach to CNR-IPSP / BeXyl or we stop.

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

**Artifact A — Front Nowcast v0**
A reproducible pipeline that, for the Bari / northern-Puglia buffer, joins:

- official sample positives/negatives (Puglia CKAN + emergenzaxylella maps),
- Sentinel-2 time series (free Copernicus),
- a drought/water-stress layer so we do not call every thirsty tree infected,

and emits a 10–20 m suspicion map with precision, recall, and a mandatory “drought-only” ablation. Success is not a pretty map. Success is: the model flags trees that later appear in the official positives at a rate better than chance and better than NDVI-only, on a held-out year.

**Artifact B — Resistance Decoder v0**
A cited gene-and-mechanism graph from:

- Giampetruzzi 2016 (Leccino vs Ogliarola transcriptome),
- La Notte / Saponari / Giampetruzzi 2024 (Leccino offspring, including S105),
- Montilon 2022 / Sabella 2019 / Surano 2022 (pit membranes, hydraulics),
- public *Xfp* ST53 genome(s),

outputting: (1) a ranked list of olive genes/pathways that distinguish resistance from susceptibility, (2) a ranked list of ST53 surface/xylem-exposed proteins, (3) at most ten AMP or phage-target hypotheses, each with a citation trail and an explicit “do not synthesize” flag.

**Artifact C — Partner brief**
A 6-page note in English (and a 2-page Italian cover) for CNR-IPSP Bari: what we built, what we need (labeled airborne scenes or a seedling panel), what we will never do (cultures, movement of plants).

### 4.2 What we are explicitly not building

- A consumer app for tourists.
- A drone company.
- A CRISPR olive.
- A backyard phage lab.
- A prize challenge in month 1.
- Another literature review with no pipeline.

### 4.3 Why this wedge, not the others

Slowing the front is the only intervention PNAS priced in the high hundreds of millions of euros. Previsual detection is the only AI capability already shown, in *Nature Plants* and *Nature Communications*, to see this infection before eyes can. The official label set already exists in open data. That is a Vesuvius-shaped problem with the CT scan already on the public internet.

Resistance decoding is the Rosie-shaped problem: public sequence and transcriptome, ranked targets, handoff to people with greenhouses (CNR already inoculated Leccino seedlings). Breeding cycles in olive are measured in years. A better ranking of which seedlings to inoculate first is a real acceleration.

A field therapeutic is a decade and a regulated lab. We do not pretend otherwise.

### 4.4 Technology decisions (locked)

| Decision | Choice | Why |
|---|---|---|
| Compute | Owen’s Mac, local Python, no new paid cloud | Free-tier-safe; Copernicus and Puglia data are free |
| Satellite | Sentinel-2 L2A via Copernicus Dataspace | 10 m, 5-day, enough for a v0 nowcast; hyperspectral comes later via a partner |
| Labels | Puglia CKAN CAMP_2020_2023 + official maps | The only landscape-scale molecular truth |
| Model class, nowcast | Gradient-boosted trees on spectral indices + land-surface temperature proxies first; small CNN only if trees lose | Need an interpretable drought ablation; do not start with a foundation model |
| Oracle | Held-out campaign year of official PCR | Vesuvius rule: external evaluator, not self-score |
| Omics | Reanalysis of published counts / GEO / paper supplements, not new sequencing | We do not generate olive RNA in this apartment |
| AMP / phage | Paper candidates only | Quarantine pest. No synthesis. |
| Literature engine | Connor + Exa search + Firecrawl extract + arXiv | Already configured |
| Partner #1 | CNR-IPSP Bari (Saponari, Boscia, Giampetruzzi, Saldarelli) | They isolated it, they published the resistance progeny, they sit in Bari |
| Partner #2 if #1 is silent | BeXyl consortium / CRSFA Basile Caramia (Locorotondo) | Already on the 2024 paper |
| Do not compete with | Planetek REDoX, Zarco-Tejada group, BIOVEXO biopesticide work | Complement. Offer the open nowcast + decoder. |
| Legal | Computational. No plant or insect movement. No unpublished genome redistribution if licenses forbid it. | Xylella is an EU quarantine pest |
| Language of outreach | English brief + Italian one-pager | Courtesy, and Bari is the audience |
| Budget, 90 days | $0 cash besides time. Optional later: Copernicus commercial extras, still skippable | Matches Owen’s constraint |

### 4.5 Team shape

- Owen: decisions, partner email, any later travel to Bari.
- Connor: literature graph, data pull, pipeline, evaluation, brief drafts.
- Named scientist (not us): inoculation, qPCR, any phage or peptide assay.

If we cannot name that scientist by day 90, the program pauses. We do not freelance biology.

---

## 5. Ninety-day plan

### Days 1–14 — Inventory and honesty

- Download CAMP_2020_2023 and document every column, CRS, and missingness. Do not assume coordinates are tree-precise until we prove it.
- Pull emergenzaxylella map layers if public; if not, note the gap.
- Stand up a Sentinel-2 pull for a box covering Lecce–Brindisi–Taranto–Bari, 2020–2025, summer windows only first.
- Build the citation graph of the 25 core papers (this file’s bibliography).
- Write `data/README.md` with licenses.

Exit gate: we can point to a row in the CSV, a lat/lon or comune, a Sentinel tile, and a PCR result, for at least 100 trees. If the open CSV is comune-level only, we downgrade the nowcast to comune/grid and say so. We do not hallucinate tree-level labels.

### Days 15–45 — Front Nowcast v0

- Features: NDVI, NDRE, NMDI / water indices, red-edge, seasonal amplitude, a coarse land-surface-temperature or water-balance proxy.
- Train on 2020–2022 official labels, test on 2023 (or whichever year is held out).
- Mandatory ablations: (i) NDVI-only, (ii) drought/water-only, (iii) full.
- Report precision-recall, not accuracy. The class is rare on the northern front.
- Write `nowcast/EVAL.md` with maps of errors.

Exit gate: full model beats NDVI-only and drought-only on the held-out year, or we publish a negative result and stop this track.

### Days 46–75 — Resistance Decoder v0

- Retrieve Giampetruzzi 2016 DEGs and the 2024 S105/S215/S234 transcriptomic contrasts.
- Map to olive genome IDs. Cluster into pit-membrane / cell-wall / hydraulics / photosynthesis / secondary metabolism.
- Pull ST53 proteome; rank xylem-exposed and biofilm-associated proteins against published phage and AMP literature.
- Emit at most ten candidates, each with: target, why, closest published analogue, why it might fail, “do not synthesize.”

Exit gate: a table a CNR postdoc could take to a lab meeting without us in the room.

### Days 76–90 — Handoff

- 6-page English brief + 2-page Italian cover.
- Email CNR-IPSP corresponding authors on the 2024 Frontiers paper (Giampetruzzi, Saldarelli) and Boscia/Saponari.
- Ask for one thing only: either a labeled airborne subset, or permission to score our seedling ranking against their unpublished inoculation panel. Not a tour. Not a grant. One dataset or one scoring.

Exit gate: a sent letter and a public repo of A+B. Reply optional. If they bite, Phase 2 is jointly designed. If they do not, we still have two citable artifacts.

---

## 6. Phase 2 (only after a partner)

In order, and only with them:

1. Replace Sentinel-2 with their airborne hyperspectral/thermal over the same labeled trees (Zarco-Tejada physics, our labels and software).
2. Score the resistance ranking on real seedlings.
3. If a peptide or phage look serious, **they** apply to work with a containment lab. We stay computational.
4. Only then consider a Vesuvius-style prize, and only if we can release a labeled cube the way EduceLab released CT scans.

---

## 7. Risks we are not going to be cute about

- Official open data may be too coarse for tree-level learning. Then we nowcast comunes, not trees, and we say so.
- Spectral “Xylella” is entangled with drought and *Verticillium*. If we cannot beat those baselines, we do not ship.
- Replant-with-Leccino is already happening and is the real landscape strategy. We do not talk as if farmers are waiting for us.
- ST1 near grapes can become the bigger European story. We watch it. We do not pivot the 90 days unless Bari’s olive front goes quiet and CNR asks us to.
- A chatbot-designed AMP that we synthesize ourselves would be reckless and, for a quarantine pest, possibly illegal. We will not do it.
- Social conflict around felling is real (Gatti 2026 and a decade of protest). Our product is earlier, more precise suspicion — which can reduce indiscriminate cuts, or can be abused to justify them. The brief will recommend confirmation-by-PCR before any removal, always.

---

## 8. Immediate next actions (this week)

1. Pull the Puglia CSV and write the data inventory.
2. Freeze the 25-paper library under `olive-xylella/papers/`.
3. Draft the Italian one-pager skeleton (unsent).
4. Do not email Bari until Artifact A or B exists. Empty hands waste that introduction.

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
- Puglia open data CAMP_2020_2023; emergenzaxylella.it.
- Agromillora / Agrimeca Nov 2025 — current front, ST1/ST26, 8,000 km².
- BeXyl / Il Post via Boscia, Jan 2026 — Salento recovery, vector decline.
- Vesuvius Challenge Grand Prize writeup, 2024.
- Roberts / The Scientist, Mar 2026 — Rosie / Conyngham case, with the not-a-cure caveat.

---

## 10. One-sentence contract

CORDON exists to put a drought-controlled suspicion map on the Bari front and a cited resistance-and-target table in a CNR inbox within 90 days, without touching a live bacterium.
