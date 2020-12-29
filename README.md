# legal-decisions-recommender

# Untertitel

*Code-Dokumentation zur Abschlussarbeit "Ähnlichkeiten von Rechtsprechungstexten - Entwurf einer netzwerkbasierten Empfehlungsfunktion für Gerichtsentscheidungen" im Studiengang Angewandte Informatik an der [HTW Berlin](www.htw-berlin.de). Realisiert mit Unterstützung des [Data Analytics Center](https://www.fokus.fraunhofer.de/de/viscom/dana) des Fraunhofer FOKUS (Berlin).*

## Notebooks:
1. [DataAnalysis](https://github.com/rosaba/legal-decisions-recommender/blob/master/DataAnalysis.ipynb) :

	Exploration und (weitere) Bereinigung der Daten; Zusammenführung von Textfragmenten.

2. [CitationExtraction](https://github.com/rosaba/legal-decisions-recommender/blob/master/CitationExtraction.ipynb) :

	Extraktion von Rechtsprechungszitaten (auf Basis des zuvor mit [ler.conll](https://github.com/elenanereiss/Legal-Entity-Recognition/blob/master/data/ler.conll) trainierten [CRF-Modells](https://github.com/rosaba/legal-decisions-recommender/tree/master/scripts/models) nach [Legal-Entity-Recognition](https://github.com/elenanereiss/Legal-Entity-Recognition)) aus allen im Datensatz enthaltenen Gründe- sowie Tenor-Texte; Exploration und Analyse der Resulate; Abbildung der Zitate auf Dokumente.

3. [EvaluationCitationExtraction](https://github.com/rosaba/legal-decisions-recommender/blob/master/EvaluationCitationExtraction.ipynb) : 

	Kleine Evaluation der Güte des Extraktionsverfahrens.

4. [CitationNetwork](https://github.com/rosaba/legal-decisions-recommender/blob/master/CitationNetwork.ipynb) : 

	Erzeugung und Analyse eines Zitationsnetzwerks der Rechtsprechungen; Entwicklung eines netzwerkbasierten Empfehlungsalgorithmus für gerichtliche Entscheidungen; anekdotische Evaluation des Verfahrens; Vorbereitung der Gesamtevaluation - Teil I: netzwerkbasierte Empfehlungen.

5. [TextbasedRecommends](https://github.com/rosaba/legal-decisions-recommender/blob/master/TextbasedRecommends.ipynb)  

	Preprocessing des Trainingskorpus für word2vec-Verfahren; Training des word2vec-Modells; stichprobenartige Evaluation der word embeddings; Erzeugung von Dokumentenembeddings; visuelle und stichprobenartige Evaluation der Dokumentenembeddings durch Clustering; Entwicklung der textbasierte Empfehlungsfunktion für Rechtsprechungen; anekdotische Evaluation; Vorbereitung der Gesamtevaluation - Teil II: textbasierte Empfehlungen.

6. [HybridRecommends](https://github.com/rosaba/legal-decisions-recommender/blob/master/HybridRecommends.ipynb) :

	Berechnung der hybriden Leseempfehlungen für Rechtsprechungen; anekdotische Evaluation; Vorbereitung Gesamtevaluation - Teil III: hybride Empfehlungen.
