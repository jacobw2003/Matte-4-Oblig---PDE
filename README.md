# PDE: Poisson likning - Elektrostatiske kondensatormodell

## Hvorfor jeg valgte oppgaven
Jeg valgte denne oppgaven fordi kondensatoren er et grunnleggende komponent i mange elektriske kretser og systemer. Å forstå det elektrostatiske potensialet i en kondensator gir verdifull innsikt i grunnleggende elektromagnetisme, som er essensielt for alle som studerer eller arbeider med elektriske og elektroniske systemer.

## Hva koden gjør
Denne koden løser problemet med å beregne det elektrostatiske potensialet i en kondensator, som består av to parallelle ledende plater med motsatt ladning, separert av en luftgap eller annen isolator. I en kondensator samles elektriske ladninger på platene, noe som skaper et elektrostatisk felt mellom dem. Ved å løse Poisson-ligningen numerisk, kan vi finne potensialfordelingen i og rundt kondensatoren. Dette gir innsikt i hvordan elektriske felt oppfører seg i nærheten av ladde objekter, noe som er grunnleggende i mange områder av fysikk og ingeniørfag.

## Resultat av kjøring
![image](https://github.com/jacobw2003/Matte-4-Oblig---PDE/assets/136694092/9a0ec777-8181-4356-99e8-f807f9baa8b4)

Resultatet viser et 2D-plott av det elektrostatiske potensialet i en kondensator. I plottet kan man se to distinkte områder med høyere intensitet, som representerer de to platene i kondensatoren: den ene er positivt ladet (vist med mørkere farge) og den andre er negativt ladet (vist med lysere farge). Områdene rundt disse høyintensitetspunktene viser en gradvis endring i potensialet, som tilsvarer det elektrostatiske feltet som går fra den positive til den negative platen.

Fargene i plottet indikerer forskjellige nivåer av potensial, med en fargebar til høyre som angir potensialets størrelse. 
Nullpotensialet er satt mellom de to platene, noe som er vanlig praksis for å visualisere potensialforskjellen i en kondensator. 
Potensialfordelingen viser at det er høyest ved platene og avtar med avstanden fra dem, noe som er konsistent med hvordan elektrostatiske felt fungerer i virkeligheten.

Plottet gir en visuell representasjon av løsningen på Poisson-ligningen for en spesifikk ladningsfordeling og er et nyttig verktøy for å forstå elektrostatiske felter og potensialer. 
