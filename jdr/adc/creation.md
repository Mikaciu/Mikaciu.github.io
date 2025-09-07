# Création de personnage et règles additionnelles

## Choix du concept

Plutôt que répartir les points de caractéristiques, le joueur va sélectionner deux occupations: l'occupation principale pour laquelle il va disposer de l'intégralité des points, et l'occupation secondaire, pour laquelle il disposera de la moitié des points d'occupation. Une des deux occupations doit avoir une origine martiale.

> En termes de jeu, cela signifie que l'investigateur doit savoir manier une arme à feu.

Les occupations sont décrites dans le livre du joueur entre les pages 55 et 79.

> L'intérêt de choisir l'occupation avant de répartir les points est de connaître les caractéristiques qui donneront des points d'occupation.

## Génération des caractéristiques

Répartir `520` points entre `FOR`, `CON`, `TAI`, `DEX`, `APP`, `INT`, `POU`, `EDU`. Les caractéristiques doivent être comprises entre `15%` et `90%`. Un accord du gardien est nécessaire si `INT < 40` ou `TAI < 40`.
Moyennes: `FOR 50`, `CON 50`, `TAI 60`, `DEX 50`, `APP 50`, `INT 50`, `POU 50` (_cf_ p37).

### Âge

| Âge   | Modificateurs                                                                                                | Mouvement |
| ----- | ------------------------------------------------------------------------------------------------------------ | --------- |
| 15-19 | -5% entre `FOR` et `TAI`. -5% `EDU`. Lancez deux fois les dés pour la chance et gardez le meilleur résultat. |           |
| 20-39 | Un test d'expérience en `EDU`                                                                                |           |
| 40-49 | Deux jets d'expérience en `EDU`. -5% entre `FOR`, `CON` et `DEX`. -5% `APP`                                  | -1        |
| 50-59 | Trois jets d'expérience en `EDU`. -10% entre `FOR`, `CON` et `DEX`. -10% `APP`                               | -2        |
| 60-69 | Quatre jets d'expérience en `EDU`. -20% entre `FOR`, `CON` et `DEX`. -15% `APP`                              | -3        |
| 70-79 | Quatre jets d'expérience en `EDU`. -40% entre `FOR`, `CON` et `DEX`. -20% `APP`                              | -4        |
| 80-89 | Quatre jets d'expérience en `EDU`. -80% entre `FOR`, `CON` et `DEX`. -25% `APP`                              | -5        |

### Impact (`IMP`) et carrure (`CAR`)

| `FOR` + `TAI` | `IMP` (modificateur aux dégâts) | `CAR` (sert aux manœuvres de combat) |
| ------------- | ------------------------------- | ------------------------------------ |
| 2-64          | -2                              | -2                                   |
| 65-84         | -1                              | -1                                   |
| 85-124        | 0                               | 0                                    |
| 125-164       | +1d4                            | +1                                   |
| 165-204       | +1d6                            | +2                                   |

### Mouvement (`MVT`)

En un round de combat, un investigateur peut se déplacer de son score de mouvement en mètres, et à 5 fois cette valeur s'il court.

| `FOR` et `DEX`                  | `MVT` |
| ------------------------------- | ----- |
| strictement inférieures à `TAI` | 7     |
| égales ou supérieures à `TAI`   | 8     |
| strictement supérieures à `TAI` | 9     |

### Autres valeurs

- Valeur de `SAN` initiale = la valeur de `POU`
- Points de magie (`PM`) = `POU` / 5
- Points de vie (`PV`) = (`CON` + `TAI`) / 10, arrondi à l'inférieur
- Chance :`3d6 * 5`

## Distribution des points de compétences

Les compétences doivent avoir un score inférieur à `75%`.

Répartir les compétences en fonction des occupations (l'intégralité des points de la première occupation, la moitié de la seconde), en dépensant tout d'abord une partie pour le crédit (les points peuvent provenir de l'une, l'autre ou les deux occupations).

Répartir `INT x 2` points dans n'importe quelle compétence hormis `Mythe de Cthulhu`.

### Bagage d'expérience de la division

- Retirer `1d10 SAN`
- ajouter une phobie ou une manie (3 cartes tirées, une choisie)
- 60 points de compétence à répartir parmi:
  - `Conduite`
  - `Écouter`
  - `Premiers soins`
  - `Sciences`
  - `Trouver Objet Caché`
  - une compétence sociale (`Baratin`, `Charme`, `Intimidation`, `Persuasion`)
  - une compétence de combat (`Combat rapproché`, `Combat à distance`)
  - une compétence manuelle (`Électricité`, `Électronique`, `Mécanique`)

### Historiques (optionnel)

Maximum 3 tirages + 1 par dizaine à partir de 30 ans (4 à 30 ans, 5 à 40, etc). Un historique ne peut être pris qu'une seule fois.

_Cf_. [Historiques](historiques.md)

### Passions et hobbies (optionnel)

Lancer `1d3+1` fois sur la table suivante. Un seul jet possible par catégorie.

| 1d100 | Passion / hobby | Type     | Table   |
| ----- | --------------- | -------- | ------- |
| 01-17 | Art             | pratique | Table A |
| 18-34 | Technologie     | intérêt  | Table B |
| 35-50 | Gastronomie     | pratique | Table C |
| 51-66 | Jeux            | pratique | Table D |
| 67-83 | Spectacle       | intérêt  | Table E |
| 84-00 | Sport           | pratique | Table F |

#### Table A - Intérêt pour un art

L'intérêt pour un art confère `10%` de bonus pour calculer les plages de réussite majeure et extrême, dans le domaine en question (une spécialisation de la compétence `Arts et Métiers`).

| 1d100 | Art          |
| ----- | ------------ |
| 01-10 | Chant        |
| 11-20 | Littérature  |
| 21-30 | Musique      |
| 31-40 | Peinture     |
| 41-50 | Sculpture    |
| 51-60 | Calligraphie |
| 61-70 | Danse        |
| 71-80 | Opéra        |
| 81-90 | Photographie |
| 91-00 | Cinéma       |

#### Table B - Intérêt pour la technologie

| 1d100 | Hobby technologique                                   | Compétence associée           |
| ----- | ----------------------------------------------------- | ----------------------------- |
| 6–10  |  Radioamateur et chasseur de signaux                  | Science: physique             |
| 11–15 |  Photographe expérimentateur                          | Arts et Métiers: photographie |
| 16–20 |  Mécanicien automobile du dimanche                    | Mécanique                     |
| 26–35 |  Électricien autodidacte                              | Électricité                   |
| 36–45 |  Astronome amateur                                    | Science : astronomie          |
| 46–55 |  Horloger                                             | Arts & métiers: horlogerie    |
| 86–90 |  Chimiste amateur (développe ses propres photos)      | Science: chimie               |
| 31–40 |  Bidouilleur de drones et de robots `DIY`             | Électronique                  |
| 61–70 |  Spécialiste en cybersécurité et chiffrement          | Science: cryptographie        |
| 81–90 |  Passionné d’intelligence artificielle et de chatbots | Informatique                  |

#### Table C - Pratique de la gastronomie

La pratique de la gastronomie confère `3d6%` dans Arts et Métiers: cuisine

| 1d100 | Spécialité                    |
| ----- | ----------------------------- |
| 01-08 | Chocolat                      |
| 09-16 | Pâtisserie                    |
| 17-24 | Fruits                        |
| 25-32 | Digestifs                     |
| 33-39 | Épices                        |
| 40-46 | Végétarien                    |
| 47-53 | Vin                           |
| 54-60 | Fromages                      |
| 61-68 | Fruits de mer                 |
| 69-76 | Grillades                     |
| 77-84 | Cuisine régionale (spécifiez) |
| 85-92 | Street food                   |
| 93-00 | Plats traditionnels familiaux |

#### Table D - Pratique d'un jeu

La pratique d'un jeu confère `3d6%` dans sa compétence associée.

| 1d100 | Jeu               | Compétence associée      |
| ----- | ----------------- | ------------------------ |
| 01-08 | Bridge            | Jeu                      |
| 09-16 | Tarot             | Jeu                      |
| 17-24 | Échecs            | Psychologie              |
| 25-32 | Dames             | Jeu                      |
| 33-40 | Backgammon        | Jeu                      |
| 41-48 | Courses hippiques | Naturalisme              |
| 49-56 | Loterie           | Jeu                      |
| 57-64 | Machines à sous   | Jeu                      |
| 65-72 | Poker             | Psychologie              |
| 73-80 | Jeux de rôle      | Arts & Métiers : comédie |
| 81-90 | Jeux de société   | Jeu                      |
| 91-00 | Blackjack         | Jeu                      |

#### Table E - Divertissement et spectacle

| 1d100 | Divertissement / spectacle   |
| ----- | ---------------------------- |
| 01-05 | Boxe (anglaise ou française) |
| 06-10 | Cabaret                      |
| 11-15 | Cinéma                       |
| 16-25 | Concerts (chant ou musique)  |
| 26-30 | Conférences intellectuelles  |
| 31-35 | Courses automobiles          |
| 36-40 | Courses cyclistes            |
| 41-45 | Courses hippiques            |
| 46-50 | Débats                       |
| 51-55 | Lectures                     |
| 56-60 | Meeting aériens              |
| 61-65 | Musées                       |
| 66-75 | Opéra                        |
| 76-80 | Poésie                       |
| 81-85 | Récits                       |
| 86-90 | Tennis                       |
| 91-00 | Théâtre                      |

#### Table F - Pratique d'un sport

Hormis l'haltérophilie, la pratique d'un sport confère `3d6%` dans sa compétence associée.
L'haltérophilie autorise un jet d'expérience en `FOR` toutes les 5 séances d'entraînement (une séance par session de jeu). Préciser au gardien que le joueur fait une séance d'entraînement. Il ne sera pas possible d'utiliser le temps pour une autre activité.

| 1d100 | Sport                | Compétence associée             |
| ----- | -------------------- | ------------------------------- |
| 01-06 | Football             | athlétisme                      |
| 07-12 | Rugby                | athlétisme                      |
| 13-18 | Tennis               | athlétisme                      |
| 19-24 | Natation             | nager                           |
| 25-30 | Cyclisme             | athlétisme                      |
| 31-36 | Boxe                 | Combat rapproché: corps à corps |
| 37-42 | Escrime              | Combat rapproché: épée          |
| 43-48 | Ski                  | athlétisme                      |
| 49-54 | Voile                | navigation                      |
| 55-60 | Equitation           | équitation                      |
| 61-66 | Tir à l’arc          | combat à distance: arc          |
| 67-72 | Arts martiaux        | combat rapproché: art martiaux  |
| 73-78 | Plongée sous-marine  | plongée sous-marine             |
| 79-84 | Haltérophilie        | `FOR`                           |
| 85-88 | Tir sportif          | combat à distance: au choix     |
| 89-92 | Course d’orientation | orientation                     |
| 93-94 | Base-ball            | athlétisme                      |
| 95-96 | Cricket              | athlétisme                      |
| 97-98 | Polo                 | équitation                      |

#### Table G - Investissements / paris

Si le joueur décide qu'il a investi ou parié, demander la somme investie.

> Attention: cela peut mener à une altération du crédit du personnage.

| 1d100 | Résultat                                    |
| ----- | ------------------------------------------- |
| 01-05 | Banqueroute ! Vous avez tout perdu !        |
| 06-15 | Perte ! Divisez la mise par 1d10 + 1        |
| 16-45 | Perte ! Divisez la mise par 1d3 + 1         |
| 46-55 | Neutre ! Vous récupérez votre mise          |
| 56-85 | Gain ! Multipliez votre mise par 1d3 + 1    |
| 86-95 | Gain ! Multipliez votre mise par 1d10 + 1   |
| 96-00 | Jackpot ! Multipliez votre mise par 2d8 + 1 |

### Table H - collections

| 1d100 | Collection      | Quantité / année |
| ----- | --------------- | ---------------- |
| 01-10 | Antiquités      | 1d6 pièces / an  |
| 11-15 | Armes à feu     | 1d6 pièces / an  |
| 16-20 | Art religieux   | 1d10 pièces / an |
| 21-25 | Bijoux          | 3d10 pièces / an |
| 26-30 | Objets occultes | 1d4 pièces /an   |
| 31-35 | Figurines       | 2d10 pièces / an |
| 36-40 | Montres         | 1d6 pièces / an  |
| 41-45 | Armes blanches  | 1d6 pièces / an  |
| 46-50 | Herbier         | 3d20 pièces / an |
| 51-60 | Livres rares    | 2d6 pièces / an  |
| 61-65 | Médailles       | 4d4 pièces / an  |
| 66-70 | Monnaies        | 4d20 pièces / an |
| 71-75 | Sculptures      | 1d4 pièces / an  |
| 76-85 | Tableaux        | 1d6 pièces / an  |
| 86-90 | Timbres         | 3d20 pièces / an |
| 91-97 | Vins            | 4d20 pièces / an |
| 98-00 | Voitures        | 1d2 pièces / an  |

## Tables additionnelles

### Lieu de résidence

| 1d100 | Lieu de résidence                                                                      |
| ----- | -------------------------------------------------------------------------------------- |
| 1-48  | Appartement (dans la ville, étage sur 1d10)                                            |
| 49-58 | Duplex (deux étages avec terrasse, étage sur 1d10+10)                                  |
| 59-68 | Hébergé par un ami (car sa demeure est trop grande pour lui)                           |
| 69-78 | Hôtel (toute l’année)                                                                  |
| 79-83 | Maison dans un parc de la ville                                                        |
| 84-88 | Maison particulière (pavillon, résidence, manoir, château)                             |
| 89-98 | Vue exceptionnelle sur un site particulier (central park, la tour Eiffel, …) (retirer) |
| 99-00 | Dans un lieu appartenant au Patrimoine national (Empire state building, Campus, …)     |

### Situation maritale

Définir succinctement le conjoint : nom, apparence physique, `APP`, âge (à la liberté du joueur).

| 1d100 | Situation maritale                                                         |
| ----- | -------------------------------------------------------------------------- |
| 01-35 | Depuis l’âge de (`1d8 + 24` ans) / `30%` pour avoir une maîtresse/un amant |
| 36-70 | Non / `30%` pour être divorcé                                              |
| 71-00 | Fiancé (depuis `1d10` mois)                                                |

### Famille descendante

Définir les noms et âges des enfants (à la liberté du joueur).

| 1d100 | Famille descendante |
| ----- | ------------------- |
| 01-59 | Non                 |
| 60-79 | 1                   |
| 80-92 | 2                   |
| 93-00 | 3                   |

### Survie des parents

| Âge du PJ       | Mère   | Père   |
| --------------- | ------ | ------ |
| la vingtaine    | `99 %` | `90 %` |
| la trentaine    | `90 %` | `80 %` |
| la quarantaine  | `70 %` | `60 %` |
| la cinquantaine | `40 %` | `30 %` |

### Mort d'un parent

| 1d100 | Situation maritale                                                                                |
| ----- | ------------------------------------------------------------------------------------------------- |
| 01-10 | Assassiné (d’une agression, d’un cambriolage, d’une bombe)                                        |
| 11-20 | D’une maladie (10 % qu’elle soit honteuse)                                                        |
| 21-60 | De sa belle mort (dans un lit, chez soi avec ses proches)                                         |
| 61-70 | Pendant la guerre (Vietnam,Irak) (sur le front ou d’un obus à l’arrière des lignes)               |
| 71-90 | Un tragique accident (de voiture, de moto, de train, d’avion, de dirigeable, en bateau)           |
| 91-00 | Il ou elle a disparu (ça fait 1dX années avec un X. égal à l’âge du PJ, jeter 1d12 pour les mois) |

### Lieu de l'enfance

| 1d100 | Lieu de l'enfance                                    |
| ----- | ---------------------------------------------------- |
| 01-20 | Petite ville (moins de 10 000 habitants)             |
| 21-40 | Ville de taille moyenne (10 000 à 100 000 habitants) |
| 41-70 | Grande ville (plus de 100 000 habitants)             |
| 71-85 | Banlieue résidentielle (pavillons, appartements)     |
| 86-95 | Ferme (élevage, culture, exploitation forestière)    |
| 96-00 | Milieu aisé (résidence, manoir, château)             |

### Frères et sœurs

| 1d100 | Frères et sœurs                                                                                                                                                                       |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 01-50 | Vous êtes un exemplaire unique. (`30%` pour être le dernier descendant, pas de cousins)                                                                                               |
| 51-80 | Vous avez partagé vos jouets avec...                                                                                                                                                  |
| 81-00 | Vous fûtes un de plus ! tirez deux fois sur la table des genres (retirez sur cette table, oubliez le résultat « enfant unique » mais donnez un bonus de `+50%` à la deuxième option). |

### Genre des frères et sœurs

| 1d100 | Genre  |
| ----- | ------ |
| 01-50 | Garçon |
| 51-00 | Fille  |

### Âge des frères et sœurs

| 1d100 | Âge par rapport au PJ                              |
| ----- | -------------------------------------------------- |
| 01-45 | Plus jeune. Tirez `1d10` années en moins que vous. |
| 46-55 | Vous êtes jumeaux !                                |
| 56-00 | Plus âgé. Tirez 1d10 années en plus de votre âge.  |

### Milieu social

| 1d100 | Milieu social          |
| ----- | ---------------------- |
| 01-05 | indigent (`5%`)        |
| 06-20 | Pauvre (`25%`)         |
| 21-80 | classe moyenne (`50%`) |
| 81-95 | Aisé (`75%`)           |
| 96-00 | Riche (`95%`)          |

### Professions

| 1d100 | Profession / Occupation                                                             |
| ----- | ----------------------------------------------------------------------------------- |
| 01-04 | Artiste (acteur, sculpteur, photographe, peintre, musicien, danseur, illustrateur)  |
| 05-08 | Écrivain (romancier, poète, journaliste, scénariste, critique littéraire)           |
| 09-12 | Cadre commercial (directeur des ventes, agent immobilier, responsable marketing)    |
| 13-15 | Clergé (prêtre, pasteur, nonne, rabbin, imam, missionnaire)                         |
| 16-19 | Employé (secrétaire, réceptionniste, opérateur de saisie, agent d’entretien)        |
| 20-23 | Fonctionnaire (inspecteur, greffier, agent municipal, préfet, douanier)             |
| 24-27 | Intellectuel (professeur, chercheur, historien, philosophe, linguiste)              |
| 28-31 | Profession libérale (architecte, avocat, médecin spécialiste, notaire, vétérinaire) |
| 32-35 | Artisan/Manuel (charpentier, plombier, électricien, agriculteur, mineur, forgeron)  |
| 36-39 | Marchand (antiquaire, libraire, commerçant ambulant, restaurateur, négociant)       |
| 40-43 | Médecin (chirurgien, pédiatre, psychiatre, médecin légiste, urgentiste)             |
| 44-47 | Militaire (officier, sous-officier, pilote, ingénieur militaire, instructeur)       |
| 48-51 | Sportif (boxeur, nageur, alpiniste, footballeur, escrimeur, jockey, skieur)         |
| 52-54 | Détective privé / Enquêteur                                                         |
| 55-57 | Journaliste d’investigation / Reporter                                              |
| 58-60 | Explorateur / Guide touristique                                                     |
| 61-63 | Diplomate / Ambassadeur / Traducteur                                                |
| 64-66 | Espion / Agent secret                                                               |
| 67-69 | Dresseur d’animaux / Soigneur                                                       |
| 70-72 | Conservateur de musée / Bibliothécaire spécialisé                                   |
| 73-75 | Inventeur / Ingénieur / Technicien                                                  |
| 76-78 | Marin / Navigateur / Pêcheur                                                        |
| 79-81 | Chauffeur de maître / Conducteur professionnel                                      |
| 82-84 | Restaurateur d’art / Collectionneur d’objets étranges                               |
| 85-87 | Spécialiste en folklore / Ethnologue / Cryptozoologue                               |
| 88-89 | Agent du gouvernement (FBI, MI6, police scientifique, analyste)                     |
| 90-91 | Occultiste / Médium / Théosophe                                                     |
| 92-93 | Antiquaire / Spécialiste en langues anciennes                                       |
| 94    | Archéologue / Egyptologue / Historien de l’art                                      |
| 95    | Hacker / Informaticien / Analyste en sécurité                                       |
| 96    | Gardien de musée / Veilleur de nuit                                                 |
| 97    | Guide de secte / Prêtre d’un culte oublié (très rare, lié au Mythe)                 |
| 98    | Collectionneur d’artefacts interdits (très rare, lié au Mythe)                      |
| 99    | Bibliothécaire du savoir interdit (très rare, lié au Mythe)                         |
| 00    | Explorateur des contrées du rêve (exceptionnel, lié au Mythe de Cthulhu)            |

### Degré de réussite

| 1d100 | Degré de réussite                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------- |
| 01-04 | Ruiné, en disgrâce ou poursuivi par la justice                                                    |
| 05-10 | Licencié, limogé ou en vacances forcées pour raisons de santé ou de scandale                      |
| 11-18 | Sans emploi, vit de petits boulots ou d’aides                                                     |
| 19-25 | Travaille occasionnellement, peine à joindre les deux bouts                                       |
| 26-40 | Débute dans le métier, manque d’expérience, doit faire ses preuves                                |
| 41-60 | Fait son travail, reconnu pour sa compétence ordinaire                                            |
| 61-75 | Est apprécié par ses collègues, a une bonne réputation locale                                     |
| 76-85 | Est reconnu par ses pairs, sollicité pour des projets ou des conseils                             |
| 86-92 | Est un spécialiste régional ou national, son nom circule dans les cercles professionnels          |
| 93-97 | Est une référence dans son domaine, invité à des conférences ou à des événements prestigieux      |
| 98-99 | Est le spécialiste mondial, son expertise est recherchée internationalement                       |
| 00    | Génie ou prodige, son nom est associé à des découvertes majeures ou à des œuvres révolutionnaires |

### Origines ethniques

| 1d100 | Origine ethnique                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------ |
| 01-90 | Souche européenne                                                                                |
| 91-93 | Souche asiatique                                                                                 |
| 94-96 | Souche africaine                                                                                 |
| 97-00 | Souche indigène (tribus amérindienne, choisir la tribu : Sioux, Apaches, Comanches, Iowas, etc.) |

#### Origines ethniques européennes

| 1d100 | Origine ethnique |
| ----- | ---------------- |
| 01-05 | Allemande        |
| 06-30 | Anglaise         |
| 31-40 | Espagnole        |
| 41-50 | Française        |
| 51-55 | Hollandaise      |
| 56-65 | Irlandaise       |
| 66-85 | Italienne        |
| 86-95 | Polonaise        |
| 96-00 | Russe            |

## Regain de points de `SAN`

### Psychanalyse

Il est possible de regagner des points de `SAN` en suivant une psychanalyse.
Le maximum de `SAN` atteignable par ce biais est la `SAN` maximum du psychanalyste.
Il est possible de suivre `Psychanalyse / 10` séances espacées d'une semaine. Après quoi il faudra faire une pause de `Psychanalyse / 20` semaines.
Chaque séance donne lieu à un jet de Psychanalyse. Par tranche de `25%` de marge de réussite (cumulable entre les séances), le patient reçoit 1 `SAN`.
Réussite spéciale : `10` points de marge supplémentaire
Réussite critique : un point de `SAN` supplémentaire pour le patient
Echec critique : -2 `SAN` pour le patient.

### Pratique artistique

Après une expérience traumatisante, les PJ peuvent tenter de modéliser ce qu'ils ont vu. Cela nécessite un jet de pratique artistique (sculpture, peinture, croquis, …), qui permet de regagner 1 `SAN` par tranche de `25%` de marge de réussite.
Attention : si le joueur choisit cette option en fin de séance, il ne lui sera pas possible de faire autre chose avant la séance suivante (comme de l’entraînement).

### Confiance

Dès qu'une caractéristique d'un investigateur passe au dessus de `90%`, il a un regain de confiance en lui qui lui fait regagner `2d3` `SAN`.

## Expérience

À la fin de chaque mission accomplie, des points d'expérience sont accordés. Les points d'expérience se dépensent pour faire des jets d'expérience dans les compétences.

| Compétence | XP nécessaires |
| ---------- | -------------- |
| 0-24%      | 1              |
| 25-49%     | 2              |
| 50-74%     | 3              |
| 75-99%     | 4              |

Une fois le seuil atteint, un D100 est lancé. S'il fait plus que le niveau actuel de la caractéristique ("jet d'expérience"), celle-ci est augmentée de `1d8+2` points. Sinon, elle gagne `1d3` points.

## Apprentissage

Il est possible de communiquer son savoir à autrui.

Le jet à faire est un jet d'`EDU`, si la compétence fait partie de ses compétences d'occupations. Il fait un jet d'`INT` sinon.

Difficulté : la difficulté du jet est égale au score de la compétence à améliorer.

Le jet est ensuite bonifié de la différence qu'il existe entre la compétence du professeur et celle de l'élève. Enfin, il est augmenté selon la compétence psychologie du professeur:

- `+5%` si le professeur a moins de `24%`
- `+10%` si le professeur a entre `25` et `49%`
- `+15%` si le professeur a entre `50` et `74%`
- `+20%` si le professeur a entre `75` et `99%`

| Résultat du jet    | Effet                                                                               |
| ------------------ | ----------------------------------------------------------------------------------- |
| Test réussi        | une barre                                                                           |
| Test échoué        | rien n'arrive                                                                       |
| Réussite spéciale  | moins de temps est nécessaire (possibilité de faire un second jet)                  |
| Réussite critique  | 2 barres et moins de temps nécessaire (possibilité de faire un second jet)          |
| Echec critique     | `-1d3` dans la compétence en question (l'élève se remet en question sur son savoir) |
