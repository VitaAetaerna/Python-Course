# 11. Was ist ein Sortieralgorithmus?
# Ein Sortieralgoritmus sortiert anhand an Mathematischr funktion eine Liste oder einen Array an Zahlen und
# gibt sie dann geordnet und sortiert aus 
# (Kommt darauf an wie es programmiert ist wird es alphabetisch, nach reihenfolge, rückwärts oä. ausgegeben)

# 12. Welchen Unterschied macht es, wenn man Sortieralgorithmen parallelisiert?
# Bei der Paralellisierung wird eine Aufgabe auf mehrere Threads (Arbeiter) aufgeteillt
# Das KANN mehr Leistung und SChnelligkeit als Ergebnis ziehen ABER 
# nie die Theoretische Leistung und Schnelligkeit
# Siehe Amdahls Gesetz

# 13. Was ist ein Suchalgorithmus?
# Ein Suchalgorithmus ist eine Art einen Wert aus einer liste oder einem Array zu suchen
# die Art zu suchen ist immer gleich (Es gibt verschiedene Algorithmen)
# Verschiedene Arten = Verschiedene Dauer + Schnelligkeit

# 14. Welchen Unterschied macht es, wenn man Suchalgorithmen parallelisiert?
# Mehrere Arbeiter können gleichzeitig bestimmte Areale darstellen und absuchen, können sich 
# aber auch behinderden bzw. ausbremsen. Mehr Resourcen werden verwendet

# 15. Wie implementiert man einen Server in Python? Wie implementiert man einen Client fur diesen Server?
# Einen Server (LAN only) würde man ganz einfach mit einem Socket aufstellen der bestimmt viele 
# Verbindungen akzeptiert und alle nicht bekannten Addressen einfach verweigert (Sicherheit). 
# Was man dann mit dem Server machen will ist keine Frage ob man kann sondern wie man kann ,möglich ist so ziemlich alles 
# Dem Client öffnet man einen Socket mit dem er sich auf den Host Socket (Server) verbindet und dann 
# muss man eben festlegen was der Client noch tun soll 