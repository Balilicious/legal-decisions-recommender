# legal-decisions-recommender
## Conception of a Recommender Function for German Court Decisions based on Citation Networks

*Code-Dokumentation zur Abschlussarbeit "Ähnlichkeiten von Rechtsprechungstexten - Entwurf einer netzwerkbasierten Empfehlungsfunktion für Gerichtsentscheidungen" im Studiengang Angewandte Informatik an der [HTW Berlin](https://www.htw-berlin.de/). Realisiert mit Unterstützung des [Data Analytics Center](https://www.fokus.fraunhofer.de/de/viscom/dana) des Fraunhofer FOKUS (Berlin).*



## Vorgehen:

I. <u>Daten</u>: Akquise → Vorbereitung (filtern, restruktutieren, säubern) → Analyse (s.  [scripts](https://github.com/rosaba/legal-decisions-recommender/tree/master/scripts) & 1. Notebook)

II. <u>Zitate</u>: Extraktion (& deren Evaluation) → Analyse → Abbildung auf Dokumente (s. 2. & 3. Notebook)

III. <u>Empfehlungsfunktion/en</u> für Gerichtsentscheidungen:

> a) netzwerkbasierte Empfehlungsfunktion: Aufbau und Analyse des Zitationsnetzwerks → Entwicklung des Empfehlungsalgorithmus → experimentelle Evaluation (s. 4. Notebook)

> *vergleichend zu a):*

> b) textbasierte Empfehlungsfunktion: Vorbereitung Trainingskorpus → Training word2vec-Modell → Erzeugung von Dokumentenvektoren → Entwicklung textbasierte Empfehlungsfunktion → experimentelle Evaluation (s. 5. Notebook)

> c) hybride Empfehlungsfunktion: Kombination der Verfahren aus a) und b) → experimentelle Evaluation (s. 6. Notebook)

IV. <u>Gesamtevaluation</u> durch Expertengruppe



## Notebooks:

1. [DataAnalysis](https://github.com/rosaba/legal-decisions-recommender/blob/master/DataAnalysis.ipynb) :

	> Exploration und (weitere) Bereinigung der Daten; Zusammenführung von Textfragmenten.

2. [CitationExtraction](https://github.com/rosaba/legal-decisions-recommender/blob/master/CitationExtraction.ipynb) :

	> Extraktion von Rechtsprechungszitaten (auf Basis des zuvor mit [ler.conll](https://github.com/elenanereiss/Legal-Entity-Recognition/blob/master/data/ler.conll) trainierten [CRF-Modells](https://github.com/rosaba/legal-decisions-recommender/tree/master/scripts/models) nach [Legal-Entity-Recognition](https://github.com/elenanereiss/Legal-Entity-Recognition)) aus allen im Datensatz enthaltenen Gründe- sowie Tenor-Texte; Exploration und Analyse der Resulate; Abbildung der Zitate auf Dokumente.

3. [EvaluationCitationExtraction](https://github.com/rosaba/legal-decisions-recommender/blob/master/EvaluationCitationExtraction.ipynb) : 

	> Kleine Evaluation der Güte des Extraktionsverfahrens aus 2.

4. [CitationNetwork](https://github.com/rosaba/legal-decisions-recommender/blob/master/CitationNetwork.ipynb) : 

	> Erzeugung und Analyse eines Zitationsnetzwerks der Rechtsprechungen; Entwicklung eines netzwerkbasierten Empfehlungsalgorithmus für gerichtliche Entscheidungen; anekdotische Evaluation des Verfahrens; Vorbereitung der Gesamtevaluation - Teil I: netzwerkbasierte Empfehlungen.

5. [TextbasedRecommends](https://github.com/rosaba/legal-decisions-recommender/blob/master/TextbasedRecommends.ipynb) : 

	> Preprocessing des Trainingskorpus für word2vec-Verfahren; Training des word2vec-Modells; stichprobenartige Evaluation der word embeddings; Erzeugung von Dokumentenembeddings; visuelle und stichprobenartige Evaluation der Dokumentenembeddings durch Clustering; Entwicklung der textbasierte Empfehlungsfunktion für Rechtsprechungen; anekdotische Evaluation; Vorbereitung der Gesamtevaluation - Teil II: textbasierte Empfehlungen.

6. [HybridRecommends](https://github.com/rosaba/legal-decisions-recommender/blob/master/HybridRecommends.ipynb) :

	> Berechnung der hybriden Leseempfehlungen für Rechtsprechungen; anekdotische Evaluation; Vorbereitung Gesamtevaluation - Teil III: hybride Empfehlungen.

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]


[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

