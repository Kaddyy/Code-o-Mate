from wahlanwendung import models, db
import re



#ProgrSpr
java = models.progrSpr(sprache='Java', beschreibung='Java ist eine Programmiersprache und eine Laufzeitumgebung, die zuerst im Jahre 1995 von Sun Microsystems veröffentlicht wurde. Es gibt eine täglich wachsende Anzahl von Anwendungen und Websites, die nur funktionieren, wenn auf dem Endgerät Java installiert ist. Java ist schnell, sicher und zuverlässig.', absolutes_erg=0, relatives_erg=0, link1='https://java.com/de/', link2='https://de.wikipedia.org/wiki/Java_(Programmiersprache)', helloWorld="System.out.println(\\\"Hello World\\\");")
python = models.progrSpr(sprache='Python', beschreibung='Python ist eine Multiparadigmensprache. ... Objektorientierte und strukturierte Programmierung werden vollständig unterstützt, funktionale und aspektorientierte Programmierung werden durch einzelne Elemente der Sprache unterstützt.', absolutes_erg=0, relatives_erg=0, link1='https://www.python.org/', link2='https://de.wikipedia.org/wiki/Python_(Programmiersprache)', helloWorld="print(\\\"Hello World\\\")")
swift = models.progrSpr(sprache='Swift', beschreibung='Swift ist eine schnelle und effiziente Programmiersprache, die Feedback in Echtzeit gibt und sich nahtlos in bestehenden Objective‑C Code einbinden lässt. So können Entwickler sichereren und zuverlässigeren Code schreiben, Zeit sparen und ihre Apps noch besser machen. Eine bildschöne App, entwickelt mit Swift.', absolutes_erg=0, relatives_erg=0, link1='https://www.apple.com/de/swift/', link2='https://de.wikipedia.org/wiki/Swift_(Programmiersprache)', helloWorld="println(\\\"Hello World\\\")")
cplusplus = models.progrSpr(sprache='C++', beschreibung='C++ ist eine von der ISO genormte Programmiersprache. Sie wurde ab 1979 von Bjarne Stroustrup bei AT&T als Erweiterung der Programmiersprache C entwickelt. C++ ermöglicht sowohl die effiziente und maschinennahe Programmierung als auch eine Programmierung auf hohem Abstraktionsniveau.', absolutes_erg=0, relatives_erg=0, link1='https://www.cplusplus.com/', link2='https://de.wikipedia.org/wiki/C%2B%2B', helloWorld="cout << \\\"Hello World\\\" << endl;")
csharp = models.progrSpr(sprache='C#', beschreibung='C# greift Konzepte der Programmiersprachen Java, C++, Haskell, C sowie von Delphi auf. C# zählt zu den objektorientierten Programmiersprachen und unterstützt sowohl die Entwicklung von sprachunabhängigen . NET-Komponenten als auch COM-Komponenten für den Gebrauch mit Win32-Anwendungsprogrammen.', absolutes_erg=0, relatives_erg=0, link1='https://docs.microsoft.com/de-de/dotnet/csharp/tour-of-csharp/', link2='https://de.wikipedia.org/wiki/C-Sharp', helloWorld="System.Console.WriteLine(\\\"Hello World\\\");")
javascript = models.progrSpr(sprache='JavaScript', beschreibung='JavaScript ist eine Programmiersprache, die als Zusatztechnik in Webseiten eingebunden wird. Die JavaScript-Programme, auch Scripte genannt, werden vom Web-Browser interpretiert. Das heißt, sie werden in Prozessoranweisungen übersetzt und ausgeführt.', absolutes_erg=0, relatives_erg=0, link1='https://developer.mozilla.org/de/docs/Web/JavaScript', link2='https://de.wikipedia.org/wiki/JavaScript', helloWorld="console.log(\\\"Hello World\\\");")
matlab = models.progrSpr(sprache='Matlab', beschreibung='Matlab dient im Gegensatz zu Computeralgebrasystemen nicht der symbolischen, sondern vorrangig der numerischen (zahlenmäßigen) Lösung von Problemen. Die Software wird in der Industrie und an Hochschulen vor allem für numerische Simulation sowie Datenerfassung, Datenanalyse und -auswertung eingesetzt.', absolutes_erg=0, relatives_erg=0, link1='https://de.mathworks.com/products/matlab.html', link2='https://de.wikipedia.org/wiki/Matlab', helloWorld="disp('Hello World');")
go = models.progrSpr(sprache='Go', beschreibung='Go ist eine kompilierte Sprache, bei der Wert auf eine hohe Übersetzungsgeschwindigkeit gelegt wurde. Go orientiert sich syntaktisch an der Programmiersprache C mit einigem Einfluss aus der Wirthschen Sprachfamilie (Pascal, Modula und insbesondere Oberon).', absolutes_erg=0, relatives_erg=0, link1='https://golang.org/', link2='https://de.wikipedia.org/wiki/Go_(Programmiersprache)', helloWorld="fmt.Printf(\\\"Hello World\\\")")
htmlcss = models.progrSpr(sprache='HTML/CSS', beschreibung='HTML steht als Abkürzung für „Hypertext Markup Language“. Sie macht Browsern eine Interpretation und Anzeige sowie das Verknüpfen von Webseiten möglich. Im aktuellen Standard nutzt man XHTML und HTML 5 um insbesondere Suchmaschinen-optimierte und User-orientierte Webseiten mit allen nötigen Elementen zu erstellen. CSS steht für Cascading Style Sheets, was übersetzt „gestufte Stilvorlagen“ bedeutet. Es handelt sich dabei um eine Gestaltungs- und Formatierungssprache, mit der das Aussehen von HTML-Dokumenten bestimmt wird. Es geht also um Design oder Stil, nicht um den Inhalt einer Webseite.', absolutes_erg=0, relatives_erg=0, link1='https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web/HTML_basics', link2='https://developer.mozilla.org/de/docs/Learn/Getting_started_with_the_web/CSS_basics', helloWorld="HTML: &lt;p&gt;Hello World&lt;/p&gt; | CSS: content: \\\"Hello World\\\";" )
sql = models.progrSpr(sprache='SQL', beschreibung='Die Abkürzung SQL steht für den Begriff Structured Query Language und bezeichnet eine Sprache für die Kommunikation mit relationalen Datenbanken. Mit SQL-Befehlen lassen sich Daten relativ einfach einfügen, verändern oder löschen.', absolutes_erg=0, relatives_erg=0, link1='https://www.w3schools.com/sql/', link2='https://de.wikipedia.org/wiki/SQL', helloWorld="SELECT 'Hello World';")
php = models.progrSpr(sprache='PHP', beschreibung='PHP (rekursive Abkürzung von PHP: Hypertext Preprocessor) ist eine serverseitige Open-Source-Skriptsprache, die vorwiegend zur Erstellung dynamischer Webseiten verwendet wird.', absolutes_erg=0, relatives_erg=0, link1='https://www.php.net/manual/de/intro-whatis.php', link2='https://wiki.selfhtml.org/wiki/PHP', helloWorld="echo 'Hello World';")
r = models.progrSpr(sprache='R', beschreibung='Die Statistik-Software R ist eine objekt-orientierte, interaktive Programmiersprache, mit der einfach statistische Auswertungen vorgenommen, vielfältige Grafiken erstellt und Simulationen durchgeführt werden können. Sie kann umsonst vom Internet heruntergeladen werden. Es gibt viele Ergänzungspakete.', absolutes_erg=0, relatives_erg=0, link1='https://www.r-project.org/', link2='https://de.wikipedia.org/wiki/R_(Programmiersprache)', helloWorld="cat(\\\"Hello World\\\")")
typescript = models.progrSpr(sprache='TypeScript', beschreibung='TypeScript ist eine von Microsoft entwickelte Programmiersprache, die auf den Vorschlägen zum ECMAScript-6-Standard basiert. Sprachkonstrukte von TypeScript, wie Klassen, Vererbung, Module und anonyme Funktionen, wurden auch in ECMAScript 6 übernommen.', absolutes_erg=0, relatives_erg=0, link1='https://www.typescriptlang.org/', link2='https://de.wikipedia.org/wiki/TypeScript', helloWorld="alert('Hello World');")
kotlin = models.progrSpr(sprache='Kotlin', beschreibung='Kotlin wurde von dem in St. Petersburg ansässigen IntelliJ-Entwicklungsteam konzipiert. Die neue Programmiersprache wurde nach der vor der Stadt gelegenen Insel Kotlin benannt. Die Namensgebung ist also ein dezenter Hinweis auf Java: Dieser Name bezeichnet ja auch gleichermaßen eine Programmiersprache und eine Insel.', absolutes_erg=0, relatives_erg=0, link1='https://kotlinlang.org/', link2='https://de.wikipedia.org/wiki/Kotlin_(Programmiersprache)', helloWorld="println(\\\"Hello World\\\")")
abap = models.progrSpr(sprache='ABAP', beschreibung='ABAP ist eine proprietäre Programmiersprache der Softwarefirma SAP, die für die Programmierung kommerzieller Anwendungen im SAP-Umfeld entwickelt wurde . Die Abkürzung steht für „Advanced Business Application Programming“.', absolutes_erg=0, relatives_erg=0, link1='https://help.sap.com/doc/abapdocu_751_index_htm/7.51/de-DE/abenabap_overview.htm', link2='https://de.wikipedia.org/wiki/ABAP', helloWorld="WRITE: 'Hello World'.")

db.session.add(java)
db.session.add(python)
db.session.add(swift)
db.session.add(cplusplus)
db.session.add(csharp)
db.session.add(javascript)
db.session.add(matlab)
db.session.add(go)
db.session.add(htmlcss)
db.session.add(sql)
db.session.add(php)
db.session.add(r)
db.session.add(typescript)
db.session.add(kotlin)
db.session.add(abap)

#fragenkatalog
frage1 = models.fragenkat(fragennr=1, frage='Ist es deine erste Programmiersprache, welche du lernen möchtest?', antwort1='Ja', antwort2='Nein', nachfolger=1)
frage2 = models.fragenkat(fragennr=2, frage='Ist es dir wichtig im Anschluss auch weitere Sprachen zu lernen?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage3 = models.fragenkat(fragennr=3, frage='Willst du mit dieser Programmiersprache in den Arbeitsmarkt einsteigen?', antwort1='Ja', antwort2='Nein', nachfolger=1)
frage4 = models.fragenkat(fragennr=4, frage='Wie wichtig ist dir dein späteres Gehalt?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage5 = models.fragenkat(fragennr=5, frage='Willst du in Trend-Themen wie Big Data, KI-Entwicklung und Machine Learning einsteigen?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage6 = models.fragenkat(fragennr=6, frage='Interessierst du dich für das IoT?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage7 = models.fragenkat(fragennr=7, frage='Interessierst du dich für IT-Sicherheit?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage8 = models.fragenkat(fragennr=8, frage='Möchtest du DB aufsetzen und verwalten?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage9 = models.fragenkat(fragennr=9, frage='Willst du Betriebssysteme programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=1)
frage10 = models.fragenkat(fragennr=10, frage='Möchtest du Linux / Mac / Windows programmieren?', antwort1='Linux', antwort2='macOS', antwort3='Windows', antwort4='Ich finde alle Betriebssysteme interessant', nachfolger=0)
frage11 = models.fragenkat(fragennr=11, frage='Möchtest du Softwareanwendungen programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage12 = models.fragenkat(fragennr=12, frage='Interessierst du dich an Mikrocontroller und Maschinen?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage13 = models.fragenkat(fragennr=13, frage='Hast du Interesse an Wirtschaftsfelder?', antwort1='Ja', antwort2='Nein', nachfolger=2)
frage14 = models.fragenkat(fragennr=14, frage='Hast du Interesse daran Zahlen und Statistiken auszuwerten?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage15 = models.fragenkat(fragennr=15, frage='Möchtest du SAP programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=0)
frage16 = models.fragenkat(fragennr=16, frage='Hast du Interesse daran Videospiele zu programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=1)
frage17 = models.fragenkat(fragennr=17, frage='In welcher Engine möchtest du entwickeln?', antwort1='Unity 3D', antwort2='Unreal', antwort3='Beide Engines interessieren mich', nachfolger=0)
frage18 = models.fragenkat(fragennr=18, frage='Hast du Interesse daran Webseiten zu programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=1)
frage19 = models.fragenkat(fragennr=19, frage='Möchtest du im Frontend oder im Backend programmieren', antwort1='Frontend', antwort2='Backend', antwort3='Ich möchte beides lernen', nachfolger=0)
frage20 = models.fragenkat(fragennr=20, frage='Hast du Interesse daran Apps zu programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=1)
frage21 = models.fragenkat(fragennr=21, frage='Möchtest du für Android oder IOS programmieren?', antwort1='Android', antwort2='IOS', antwort3='Mich interessieren beide Betriebssysteme', nachfolger=0)
frage22 = models.fragenkat(fragennr=22, frage='Hast du Interesse daran Roboter zu programmieren?', antwort1='Ja', antwort2='Nein', nachfolger=0)

db.session.add(frage1)
db.session.add(frage2)
db.session.add(frage3)
db.session.add(frage4)
db.session.add(frage5)
db.session.add(frage6)
db.session.add(frage7)
db.session.add(frage8)
db.session.add(frage9)
db.session.add(frage10)
db.session.add(frage11)
db.session.add(frage12)
db.session.add(frage13)
db.session.add(frage14)
db.session.add(frage15)
db.session.add(frage16)
db.session.add(frage17)
db.session.add(frage18)
db.session.add(frage19)
db.session.add(frage20)
db.session.add(frage21)
db.session.add(frage22)


#antwortkatalog
#erste Sprache
antwort1 = models.antwortkat(fragennummer=1, antwort='a01_01', java=3, python=1, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort2 = models.antwortkat(fragennummer=1, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#andere Sprachen
antwort3 = models.antwortkat(fragennummer=2, antwort='a01_01', java=3, python=0, swift=0, cplusplus=3, csharp=3, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort4 = models.antwortkat(fragennummer=2, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Arbeitsmarkt
antwort5 = models.antwortkat(fragennummer=3, antwort='a01_01', java=5, python=3, swift=0, cplusplus=3, csharp=3, javascript=4, matlab=0, go=0, htmlcss=0, sql=4, php=2, r=1, typescript=0, kotlin=0, abap=2)
antwort6 = models.antwortkat(fragennummer=3, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Gehalt
antwort7 = models.antwortkat(fragennummer=4, antwort='a01_01', java=0, python=4, swift=3, cplusplus=1, csharp=3, javascript=1, matlab=0, go=5, htmlcss=0, sql=2, php=0, r=4, typescript=3, kotlin=2, abap=4)
antwort8 = models.antwortkat(fragennummer=4, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Trend-Themen
antwort9 = models.antwortkat(fragennummer=5, antwort='a01_01', java=1, python=2, swift=0, cplusplus=2, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=3, typescript=0, kotlin=0, abap=0)
antwort10 = models.antwortkat(fragennummer=5, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#IoT
antwort11 = models.antwortkat(fragennummer=6, antwort='a01_01', java=2, python=0, swift=0, cplusplus=2, csharp=0, javascript=0, matlab=0, go=5, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort12 = models.antwortkat(fragennummer=6, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#It-Sicherheit
antwort13 = models.antwortkat(fragennummer=7, antwort='a01_01', java=0, python=3, swift=0, cplusplus=2, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort14 = models.antwortkat(fragennummer=7, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#DB
antwort15 = models.antwortkat(fragennummer=8, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=5, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort16 = models.antwortkat(fragennummer=8, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Betriebssysteme
antwort17 = models.antwortkat(fragennummer=9, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort18 = models.antwortkat(fragennummer=9, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Linux/macOS/Windows
antwort19 = models.antwortkat(fragennummer=10, antwort='a01_01', java=3, python=0, swift=0, cplusplus=3, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort20 = models.antwortkat(fragennummer=10, antwort='a01_02', java=3, python=0, swift=0, cplusplus=3, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort21 = models.antwortkat(fragennummer=10, antwort='a01_03', java=2, python=0, swift=0, cplusplus=2, csharp=3, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort22 = models.antwortkat(fragennummer=10, antwort='a01_04', java=1, python=0, swift=0, cplusplus=1, csharp=1, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#SW
antwort23 = models.antwortkat(fragennummer=11, antwort='a01_01', java=2, python=0, swift=0, cplusplus=2, csharp=2, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort24 = models.antwortkat(fragennummer=11, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Mikrocontroller/Maschinen
antwort25 = models.antwortkat(fragennummer=12, antwort='a01_01', java=0, python=0, swift=0, cplusplus=5, csharp=0, javascript=0, matlab=5, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort26 = models.antwortkat(fragennummer=12, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Wirtschaft
antwort27 = models.antwortkat(fragennummer=13, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort28 = models.antwortkat(fragennummer=13, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Zahlen/Statistik
antwort29 = models.antwortkat(fragennummer=14, antwort='a01_01', java=0, python=3, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=5, typescript=0, kotlin=0, abap=0)
antwort30 = models.antwortkat(fragennummer=14, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#SAP
antwort31 = models.antwortkat(fragennummer=15, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=10)
antwort32 = models.antwortkat(fragennummer=15, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Videospiele
antwort33 = models.antwortkat(fragennummer=16, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort34 = models.antwortkat(fragennummer=16, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Engine
antwort35 = models.antwortkat(fragennummer=17, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=3, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort36 = models.antwortkat(fragennummer=17, antwort='a01_02', java=0, python=0, swift=0, cplusplus=3, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort37 = models.antwortkat(fragennummer=17, antwort='a01_03', java=0, python=0, swift=0, cplusplus=3, csharp=3, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Webseiten
antwort38 = models.antwortkat(fragennummer=18, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=2, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort39 = models.antwortkat(fragennummer=18, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Front-/Backend
antwort40 = models.antwortkat(fragennummer=19, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=5, matlab=0, go=0, htmlcss=10, sql=0, php=0, r=0, typescript=5, kotlin=0, abap=0)
antwort41 = models.antwortkat(fragennummer=19, antwort='a01_02', java=0, python=2, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=5, php=10, r=0, typescript=0, kotlin=0, abap=0)
antwort42 = models.antwortkat(fragennummer=19, antwort='a01_03', java=0, python=2, swift=0, cplusplus=0, csharp=0, javascript=5, matlab=0, go=0, htmlcss=10, sql=5, php=10, r=0, typescript=5, kotlin=0, abap=0)

#Apps
antwort43 = models.antwortkat(fragennummer=20, antwort='a01_01', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=10, abap=0)
antwort44 = models.antwortkat(fragennummer=20, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Android/IOS
antwort45 = models.antwortkat(fragennummer=21, antwort='a01_01', java=3, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort46 = models.antwortkat(fragennummer=21, antwort='a01_02', java=0, python=0, swift=10, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort47 = models.antwortkat(fragennummer=21, antwort='a01_03', java=3, python=0, swift=10, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)

#Roboter
antwort48 = models.antwortkat(fragennummer=22, antwort='a01_01', java=0, python=0, swift=0, cplusplus=4, csharp=0, javascript=0, matlab=5, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)
antwort49 = models.antwortkat(fragennummer=22, antwort='a01_02', java=0, python=0, swift=0, cplusplus=0, csharp=0, javascript=0, matlab=0, go=0, htmlcss=0, sql=0, php=0, r=0, typescript=0, kotlin=0, abap=0)


db.session.add(antwort1)
db.session.add(antwort2)
db.session.add(antwort3)
db.session.add(antwort4)
db.session.add(antwort5)
db.session.add(antwort6)
db.session.add(antwort7)
db.session.add(antwort8)
db.session.add(antwort9)
db.session.add(antwort10)
db.session.add(antwort11)
db.session.add(antwort12)
db.session.add(antwort13)
db.session.add(antwort14)
db.session.add(antwort15)
db.session.add(antwort16)
db.session.add(antwort17)
db.session.add(antwort18)
db.session.add(antwort19)
db.session.add(antwort20)
db.session.add(antwort21)
db.session.add(antwort22)
db.session.add(antwort23)
db.session.add(antwort24)
db.session.add(antwort25)
db.session.add(antwort26)
db.session.add(antwort27)
db.session.add(antwort28)
db.session.add(antwort29)
db.session.add(antwort30)
db.session.add(antwort31)
db.session.add(antwort32)
db.session.add(antwort33)
db.session.add(antwort34)
db.session.add(antwort35)
db.session.add(antwort36)
db.session.add(antwort37)
db.session.add(antwort38)
db.session.add(antwort39)
db.session.add(antwort40)
db.session.add(antwort41)
db.session.add(antwort42)
db.session.add(antwort43)
db.session.add(antwort44)
db.session.add(antwort45)
db.session.add(antwort46)
db.session.add(antwort47)
db.session.add(antwort48)
db.session.add(antwort49)


db.session.commit()