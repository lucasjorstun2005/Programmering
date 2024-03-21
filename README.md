# Loggbok
===========
## Vecka 12
> På fredagen började jag definera klasserna Game, Player, Humanplayer, Computerplayer, Board, och Move. Jag tänkte att jag börjar med att göra funktionen för spelbrädet och med lite tips från Rikard förstod jag ungefär hur jag skulle göra för att då fram rutorna och raderna i brädet. Det ända jag behövde lösa var hur jag skulle få allt att skrivas ut för spelaren, och jag hittade denna artikeln/"dokumentation" om funktionen sys.stdout.write. Här är länken till den artikeln: https://www.geeksforgeeks.org/sys-stdout-write-in-python/
> På måndagen satte igång katalogen och fil för tre-i-rad och planering med mål inför projektet:
### Mål
> 1. Definera klasserna. Dessa klasser är en klass för spelets gång, klasser för spelare, både för mänskliga spelare samt datorspelare om något sådant skulle vilja implementeras någon annan gång eller kanske av någon annan. Jag kommer själv inte göra det då det blir för komplicerat. Förutom de klasserna ska det också vara en klass för spelbrädet där jag definerar hur brädet ska se ut. Jag ska också ha en klass "move" för vad som händer när en spelare gör ett drag
> 2. Logik för spelets gång, alltså sätta igång spelet, vems tur det är, spelaren gör sitt drag, kollar efter en vinst, om det är en vinst välj ut en vinnare, annars gör det till den andra spelarens tur. (Bara kalla funktioner, inte funktionerna själva än)
> 3. Regler, alltså win conditions för vertikala, horisontella och diagonella vinster
> 4. Alla funktionerna för mål 2
## Vecka 11
> Satt mest och funderade på vad jag skulle göra för projekt, tänkte att jag kanske skulle göra något som är objektorienterat och det slutade upp med att jag tänkte göra ett tre-i-rad spel.
## Vecka 10
> Jag gjorde klart hänga gubbe. Det var inte ett jättesvårt projekt och det ända riktiga problemet jag hade var att jag hade använt i som variabel i en nested loop när "main" loopen också använde i som variabel. Utöver det så var det några småfix jag gjorde samt en lite bättre interface för det. Till exempel så lade jag till att ordet var gömt med understreck så att man kan följa hur långt man har kommit. Jag tog ingen direkt hjälp av youtube, stack overflow eller liknande då det inte behövdes. 
## Vecka 9
> Jag började med ett lite mindre projekt på hänga gubbe. Jag ville inte göra något som skulle ta jättelång tid så jag tog något lite mindre. Jag gjorde en lista med ord och började lite grann med implementation av programmet i sig
## Vecka 8
> Jag fixade en del errors som jag hade i koden, de flesta var bara lite småfel jag hade i koden men jag hade en där jag hade en circular import så jag fick fixa lite med mina imports och använda funktionsargument istället så fixade det sig. På torsdagen gjorde jag klart projektet, jag fixade några errors, framförallt så var det att jag inte kunde få summan från min dictionary med resultaten. Detta var för att den blandade ihop str och int när jag använde sum. Så jag fick göra sum(list(matchar.values())) För att få det jag ville ha, jag skulle kunna göra lite finjusteringar men jag var ganska trött på projektet så jag tror att jag rör mig vidare ifrån det.
## Vecka 51 - 4
> Under dessa veckor har jag lagt mitt projekt åt sidan lite grann och övat på andra områden inom Python. Jag har gjort en hel del på sidan Leetcode där jag löst olika problem. Exempel på saker jag lärt mig mer om är Binary träd, depth-first search och Breadth-first search. Har också lärt mig mer om listor och hur man kan använda dom. Har också lärt mig mer om andra grundläggande koncept som loopar, datatyper. Det finns andra saker jag lärt mig mer om men jag anser att det är det jag nämnde som jag lärt mig mest om.
## Vecka 50
> Jag förbättrade "funktionen" för ettpar, tvåpar, tretal och fyrtal då den inte var optimal som sagt i loggboken för vecka 49. Det jag gjorde var att jag först försökte komma på någon lösning men kom inte direkt på någon optimal lösning först. Så det jag började göra var att leta efter lite bibliotek som kanske har något i stilen till vad jag ville göra. Jag hittade ett som hette Counter från biblioteket collections som finns med när man installerar python. Jag läste lite om det här https://realpython.com/python-counter/ Sedan så lekte jag runt med lite olika potentiella lösningar tills jag hittade en som jag är ganska säker på kommer att fungera.

## Vecka 49
> Jag implementerade funktionaliteten för tvåpar, tretal, fyrtal, och chans. Chans var väldigt simpelt men resten var lite svårare, jag tyckte att tvåpar var det svåraste att göra då jag behövde komma på ett sätt att kunna separera på de två olika paren. Tretal och fyrtal var inte "svårt" men jag kan göra en bättre implementation av det.
## Vecka 48
> Jag började med att implementera "matcharna" för svaren till tärningarna. Jag gjorde för ettor, tvåor, treor, fyror, femmor, sexor, och ett par. Det var inga större problem då det var ganska simpelt men jag behövde lära mig hur jag hanterar dictionaries. Det jag inte visste hur man gjorde var att öka värdet på ett value, jag hittade denna artikeln https://phoenixnap.com/kb/python-add-to-dictionary vilket var där jag lärde mig hur man gjorde det. Paret var lite svårare då jag fick göra en nested loop men det var inte direkt några större problem

## Vecka 47
> Jag började med Yatzy. Jag fick lära mig mer om att definera funktioner men framförallt att använda dom. Alltså att använde de olika funktionerna jag har i andra funktioner för att få programmet att "gå runt".
## Vecka 46
> Jag började och blev klar med blackjack. Jag tyckte att det lättaste var att deala medans det svåraste var att få essets funktionalitet att fungera. Det var också lite svårt med olika conditionals för att vinna. Jag behövde sätta de i vissa ordningar så att det blev rätt, till exempel så ville jag ha att det skulle stå "Blackjack!" när man fick blackjack. I början så satte jag den elifen i win conditionals vilket blev fel då man först behövde standa och efter det så kom det fram blackjack. Sedan hade jag också satt den elifen efter min "vinst" elif så den kom aldrig fram. Så där fick jag ändra så att den istället hamnade i loopen när man dealar och att om man får blackjack så avslutas spelet direkt och man behöver inte säga stand först. Jag använde ingen annan hjälp utan jag lyckades lösa det själv.

## Vecka 45
> Jag gjorde 5B vilken jag tyckte var hyfsat enkel men lite svår att debugga, så jag gjorde en infinite loop medvetet som bröts när det blev Yatzy. Alltså gjorde jag en while True på hela programmet och när det blev yatzy bröts det.

## Vecka 43
> Jag gjorde 4B som jag tyckte gick ganska bra att göra men den var lite svår tyckte jag. Jag gjorde också uppgift 4C och fixade några problem som jag hade med 4B. Tyckte att 4C var ganska svår och tyckte att det var den svåraste jag hade gjort än så länge. Jag gjorde också 4D och 5A. 5A var lätt men 4D var mycket svårare än 4C

## Vekca 42
> Jag fortsatte med listorna och blev klar med 4A. Jag fick problem med Git, det går inte för dig att se uppgifterna för 7100 men tror bara att det får vara så då jag inte riktigt vet hur jag ska lösa det.

## Vecka 41
> Jag gjorde for-each och for listor med range, samt att jag började med att göra uppgifterna för listor.
> Jag lärde mig hur jag kan använda for loopar samt att jag lärde mig om hur man kan använda listor.
> Jag använde mig av stackoverflow för att ta reda på hur jag kunde göra en ekvation för att ta reda på om ett tal är ett primtal.
> Tyckte inte att det var jättesvårt, framförallt for looparna var inte särskilt svårt mend det var lite svårare att med listor, framförallt tyckte jag att det var svårt att få fram hur jag skulle ta reda på om ett tal var ett primtal, så därför sökte jag upp det.

## Vecka 40
> Jag fortsatte med uppgifter om flödesscheman.
> Jag känner att jag kan bra om flödescheman och att jag har lärt mig hur man använder det och vad det är bra för.

## Vecka 39
> Jag gjorde uppgifter 1, 2, 3 i 7073. Alla gick bra och jag hade inga direkta problem med de. Det jag lärde mig var hur man gjorde flödesscheman.


## Vecka 38
> Jag gjorde tärningsspelet i uppgift 7070, det gick bra och jag tyckte att pengasystemet var lite utmanande men det var ingenting som var jättesvårt direkt. Det var inte jättesvårt att lösa pengasystemet men det var lättare att lösa när man var nogrann att man har med det som ska vara med i.
> Använde mig inte av youtube, stackoverflow eller liknande.
> Jag vet inte om jag lärde mig så mycket nytt, men jag blev bättre på att använda if-satser.
