# vecka 11
### Vecka 11, 10/3

## 1 Diskutera i grupp
Denna gången är det en fördel att diskutera de flesta uppgifterna.
Planera din tid, så att du hinner arbeta med alla övningarna. Du ska alltså inte göra "färdigt" alla tidigare övningar innan du går vidare på nästa.

### 1a 
Vilka strängar matchas av det reguljära uttrycket: "ab" ? Testa era svar på https://regex101.com/ 
"a b"
"aBBa"
"sabotör"

### 1b 
Betrakta uttrycket "nisse". Vad skriver jag för att matcha både "Nisse", "NISSE" och "nisse"?

### 1c 
Vilka strängar matchas av "a*n" ?
"an"
"amerikan"
"naturlig"
"annandag"

### 1d 
Vilka strängar matchas av "[ae]n" ?
"naiv"
"inconsequential"
"bae"

### 1e 
Vilka strängar matchas av "je.+e"?
"je"
"jee"
"jeppe"
"je je"

### 1f 
Vilka strängar matchas av "\san?\s"
"sansad"
" annan "
"    an   na   an   "
"be a darling"

### 1e 
Skriv ner med egna ord, vad följande uttryck matchar. "Strängar som innehåller…"
"lines?"
"^a*ö$"
"[aeiouyåäö]+"
"[123456789]\d*"
"\d{4}-\d{2}-\d{2}



### 2a 
Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".


### 2b 
Skriv ner ett testscenario för user storyn. Använd en punktlista. Fundera särskilt på vad som ska testas implicit och explicit.
Implicit = underförstått, testas indirekt
Explicit = uttryckligen, testas direkt


### 3 
Titta på kodexemplet från lektionen. Skriv upp allt du är osäker på och diskutera i grupp eller fråga om på nästa lektion.

def test_view_sprint_planning(page: Page):
    """Testa att det går att se Sprint planning"""
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Klicka på button "First"
    locator = page.get_by_role("button")
    first_button = locator.get_by_text("First")
    first_button.click(timeout=100)

    # Hitta button med texten "Sprint planning"
    sp_button = page.get_by_role("button").get_by_text(re.compile("Sprint planning"))
    expect(sp_button).to_be_visible()
    
    # Klicka på den
    sp_button.click(timeout=100)

    # Finns rubriken "Sprint planning"?
    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

----

## 2 Öva på regex
### 1a 
Skriv ett regex som kontrollerar att det finns en längd i strängen, som anges i centimeter:
"Fiskarna som jag fångade var 55 cm långa."

### 1b 
Denna gången vill vi veta om det finns två längder.

### 1c 
Längderna ska vara samma enhet.
"Fiskarna som jag fångade var 55 cm långa, så båda fick plats i min 1,23 m långa låda."


### 2 
Skriv ett regex som matchar ett svenskt postnummer. Postnummer består av fem siffror indelade i två grupper med mellanslag emellan. Exempel: "123 45"
Om du vill övertänka fördjupa dig mera: https://sv.wikipedia.org/wiki/Postnummer_i_Sverige 


### 3 
Skriv ett regex som matchar ett datum skrivet enligt den internationella standarden ISO 8601, alltså 10 tecken med bindestreck mellan avdelningarna. Exempel: 2025-03-10.


### 4 
Skriv ett regex som matchar ett pengavärde i siffror. Exempel på värden som ska matchas:
200 kr
12,50 kr
0,35 kr


### 5a 
Skriv ett regex som matchar en e-postadress (användarnamn@server.domän) enligt följande icke kompletta regler.
användarnamn kan innehålla bokstäver, siffror och specialtecknen som punkt och bindestreck
server kan innehålla samma sorts tecken
domän kan innehålla bokstäver och siffror

### 5b 
Gör ett regex som matchar en komplett e-postadress enligt specifikationen i artikeln här:
What is a valid email address format 


Träna mer på regex: Regex Golf (svår)

----

## 3 
Öva på user stories

Skapa user stories som beskriver funktionaliteten i https://lejonmanen.github.io/agile-helper/ 
För varje user story ska du skriva ett scenario. Målet är att all befintlig funktionalitet ska täckas in av en user story - alla knappar ska bli klickade minst en gång.
Gör gärna den här uppgiften tillsammans med klasskamrater, så ni kan diskutera era scenarion, skillnader och likheter.

Exempel:
[User story 1]
Story: Som en användare, vill jag se mötet "sprint planning" som utspelar sig första dagen på en sprint, så att jag vet vad jag ska göra på mötet.

Scenario:
- Navigera till webbsidan https://lejonmanen.github.io/agile-helper/ 
- Klicka på knappen med texten "First"
- Klicka på knappen vars text innehåller "Sprint planning"
- Kontrollera att ett <dialog> element visas på sidan, som innehåller en rubrik med texten "Sprint planning"

---
## 4 
Öva på E2E test
Utgå från dina user stories och scenarion i föregående uppgift. Skriv kod med Playwright som testar dem. Ta hjälp av kodexemplet i presentationen.


