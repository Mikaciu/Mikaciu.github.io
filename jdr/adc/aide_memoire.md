# Appel de cthulhu - aide mémoire

## Système de jeu

1D100 ; la plupart des actions se résolvent à l’aide d’un `D100` (un `D10` + un `D10aines`).

> 00 = 100

Exemple : pour une compétence à 45 %, un `D100` faisant 45 ou moins est réussi.

En combat, l’avantage est à la défense : si l’assaillant et le défenseur font la même qualité de réussite, le défenseur réussit sa défense.

## Qualités de réussite

| D100             | Qualité de réussite                                                 |
| ---------------- | ------------------------------------------------------------------- |
| 01               | Réussite critique. Un jet d'expérience immédiat dans la compétence. |
| ≤ compétence ÷ 5 | Réussite extrême                                                    |
| ≤ compétence ÷ 2 | Réussite majeure                                                    |
| ≤ compétence     | Réussite standard                                                   |
| > compétence     | Échec                                                               |
| 96-100           | Échec critique « fumble »                                           |

### Exemple, pour une compétence à 70 %

| D100   | Qualité de réussite |
| ------ | ------------------- |
| 01     | Réussite critique   |
| 02-14  | Réussite extrême    |
| 15-35  | Réussite majeure    |
| 36-70  | Réussite standard   |
| 71-95  | Échec               |
| 96-100 | Échec critique      |

## Redoublement

Il est possible de redoubler un jet (i.e. relancer le D100), mais avec une justification _roleplay_ (sauf pour le combat et la SAN, qu’il n’est pas possible de redoubler)

### Exemples de justifications

| Compétence     | Justification                                                      |
| -------------- | ------------------------------------------------------------------ |
| Arts & métiers | Recommencer l'œuvre depuis le début                                |
| Baratin        | Se rapprocher pour établir une connection physique                 |
| Conduite       | Faire demi-tour, prendre une autre route                           |
| Discrétion     | Retirer ses chaussures, faire diversion                            |
| Intimidation   | Se lever, se rapprocher, parler plus fort                          |
| Persuasion     | Se rapprocher, poser une question personnelle, toucher la personne |

## Dés de bonus et de malus

Lorsqu’une action est particulièrement facile à accomplir, le gardien pourra donner des dés de bonus.

Fonctionnement : pour chaque dé de bonus, lancer un dé de dizaines supplémentaires.

Avec 1 dé de bonus pour un test de compétence, le joueur lance un D10 et deux D10aines. Il sélectionne le jet le plus favorable pour la réussite de l’action.

Les dés de malus s’utilisent de la même manière, mais cette fois le joueur sélectionnera le jet le plus défavorable pour la réussite de l’action.

### Exemples d'usage

| D10aines 1 | D10aines 2 | D10 | Si dé bonus | Si dé malus |
| ---------- | ---------- | --- | ----------- | ----------- |
| 40         | 80         | 4   | 44          | 84          |
| 00         | 20         | 5   | 05          | 25          |
| 60         | 00         | 0   | 60          | 100         |
| 20         | 00         | 0   | 20          | 100         |

## Expérience

Un jet d’expérience est un jet raté de compétence. Exemple : pour une compétence à 45 %, un D100 faisant plus de 46 est un jet d’expérience réussi.

> Plus l'investigateur progresse dans une compétence, plus il lui est difficile de progresser.

Un jet d'expérience réussi confère `1d8 + 2` points dans cette compétence. S'il est raté, il confère `1d3` points.

### Dépense des points d’expérience

Cette table décrit combien investir de points d'expérience dans une compétence pour pouvoir faire un jet d'expérience.

| Score de compétence | Coût |
| ------------------- | ---- |
| 0-24                | 1 XP |
| 25-49               | 2 XP |
| 50-74               | 3 XP |
| 75-99               | 4 XP |

## Récompenses

## Blessures et soins

```mermaid
flowchart TD;

perso("**Le personnage subit des dégâts d'une seule blessure**") --> subit{ }

subit -->|Inférieurs à la moitié des points de vie max| inferieur
subit -->|Égaux ou supérieurs à la moitié des points de vie max| sup_egal
subit -->|Strictement supérieurs aux points de vie max| sup_strict["fa:fa-skull **Mort**"]

inferieur("`**Dégâts ordinaires**<br>Premiers soins: soignent 1 point ; médecine : soigne 1D3 points`")
sup_egal("`**Blessure grave**<br>1. Tombe à terre<br>2. Test de CON: si échec, tombe inconscient`")
```

### Guérison des blessures graves

**Test de récupération à la fin de chaque semaine.**

- Échec: pas de guérison
- Succès: récupère 1D3 points.
- Succès extrême: récupère 2D3 points et efface la blessure grave.

---

- Dé bonus si soigné correctement (test de Médecine)
- Dé bonus si le patient se repose ou est dans un environnement adéquat
- Dé malus si mauvaises conditions

## Le combat

```mermaid
flowchart TD;
ordre_attaque-->surprise;
ordre_attaque-->ordre_dex;

ordre_attaque ~~~ si_manoeuvre;

ordre_dex ---> action_combat;
ordre_dex ~~~ si_manoeuvre;

subgraph action_combat[*Les tests de combat ne peuvent être redoublés*]
    direction LR
    eviter_coups ~~~ rendre_coups ~~~ manoeuvre;
end

subgraph surprise[" "]
    direction TB
    attaque_surprise-->surprise_oui;
    attaque_surprise-->surprise_non;
end

surprise ~~~ reussite_extreme
surprise ~~~ sous_nombre

sous_nombre("`<h3>En sous-nombre</h3>Si le personnage a déjà esquivé ou rendu les coups durant ce round, les attaques supplémentaires contre lui reçoivent un dé bonus.<br>Ne s'applique pas à ceux qui ont plusieurs attaques (peuvent esquiver/rendre les coups autant de fois qu'ils ont d'attaques avant que la règle ne s'applique)`");
reussite_extreme("`<h3>Réussite extrême</h3><em>Ne s'applique pas à un défenseur qui rend les coups.</em><br><strong>Empalement</strong> = dégâts maximum de l'arme + bonus maximum + dé de l'arme<br><strong>Contondant</strong> = dégâts maximum de l'arme + bonus maximum`");

ordre_attaque("`<h3>Ordre d'attaque</h3>Par ordre de DEX croissante: la valeur la plus élevée joue en premier. *Une arme à feu prêt à tirer agit à DEX + 50.*`")
ordre_dex("`<h3>Résoudre par ordre de DEX</h3>a) Choix entre attaque, fuite ou manœuvre<br>b) Le défenseur esquive, rend les coups ou effectue une mnœuvre<br>c) Attaquant et défenseur font des tests en opposition.`")
attaque_surprise("`<h3>Attaque par surprise</h3>Autoriser un test: la cible anticipe-t-elle l'attaque ? (TOC, Écouter, Psychologie)`")
surprise_oui("`<h3>Oui</h3>Utilisez l'ordre normal de DEX pour le combat`")
surprise_non("`<h3>Non</h3>L'attaque porte automatiquement ou reçoit un dé bonus`")

eviter_coups("`<h3>Éviter les coups</h3>L'attaquant l'emporte ave une niveau de réussite supérieur.<br><strong>Égalité</strong> = le défenseur gagne.<br><strong>Échec mutuel</strong> = aucun dégât n'est infligé.`")
rendre_coups("`<h3>Rendre les coups</h3>Le plus haut de réussite l'emporte.<br><strong>Égalité</strong> = l'attaquant gagne.<br><strong>Échec mutuel</strong> = aucun dégât n'est infligé.`")
manoeuvre("`<h3>Manœuvre</h3>Résoudre comme pour rendre les coups, mais au lieu d'infliger des dégâts, appliquer les effets de la manœuvre.`")

si_manoeuvre("`<h3>Si manœuvre</h3>Comparer les carrures<br><strong>Si l'initiateur est plus petit</strong>: un dé de malus par point de différence.<br><strong>Si différence de 3 ou plus</strong>: la manœuvre est impossible.`")
```
