- down_rechtsprechung_internet_bgh_strafsachen.py :

  > alle verfügbaren Rechtsprechungsdokumente des BGH herunterladen, die Strafsachen betreffen → Ergebnis: [data_rechtsprechung_bgh_strafsachen.zip](https://github.com/rosaba/legal-decisions-recommender/blob/master/scripts/orig_data/data_rechtsprechung_bgh_strafsachen.zip)
- convert_bgh_xml.py :

  > Im Original liegen die Daten als XML-Dateien vor. BGH-Daten werden nach JSON konvertiert → Ergebnis: [converted_bgh_straf_decisions_nocomma.json](https://github.com/rosaba/legal-decisions-recommender/blob/master/scripts/orig_data/converted_bgh_straf_decisions_nocomma.json)

- restructure_bgh_json.py

  > filtert, säubert und strukturiert die Datenmenge im Sinne der später folgenden Weiterverarbeitung um → Ergebnis: [restructured_bgh_decisions_nocomma.json](https://github.com/rosaba/legal-decisions-recommender/blob/master/scripts/orig_data/restructured_bgh_decisions_nocomma.json) – hiernach wird restructured_bgh_decisions_nocomma.json mit dem Befehl `sed '1s/^/[/;$!s/$/,/;$s/$/]/' scripts/orig_data/restructured_bgh_decisions_nocomma.json > data/dataframes/restructured_bgh_decisions.json`in ein gültiges json [restructured_bgh_decisions.json](https://github.com/rosaba/legal-decisions-recommender/blob/master/data/dataframes/restructured_bgh_decisions.json) gewandelt

- extract_rs_citations.py

  > extrahiert basierend auf Modell [crf-f.pkl](https://github.com/rosaba/legal-decisions-recommender/blob/master/scripts/models/crf-f.pkl) die in den Textkategorien Gründe und Tenor enthaltenen Rechtsprechungszitate - Ergebnis ist eine Liste von Tupeln, die das Zitat im Wortlaut und dessen jeweilige Start- und Endindizes im Text beinhalten

- extract_entities.py

  > identifiziert unterschiedliche Entitäten juristischer Texte auf Basis von [crf-f.pkl](https://github.com/rosaba/legal-decisions-recommender/blob/master/scripts/models/crf-f.pkl)