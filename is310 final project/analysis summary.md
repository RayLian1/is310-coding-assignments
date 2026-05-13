# IS310 Final Project Dataset Analysis Summary

## Dataset
Rows: 50
Unit of analysis: one NBA player per row
Original variables: player name, years, position, PPG, Instagram followers, All-Star status
Computational augmentation added: follower counts in millions, log10 followers, PPG rank, follower rank, PPG tier, popularity quartile, above-average flags.

## Main findings
Mean PPG: 21.53
Median PPG: 22.20
Mean Instagram followers: 74.04 million
Median Instagram followers: 75.04 million
Correlation between PPG and raw follower count: -0.002
Correlation between PPG and log10 follower count: -0.047

The correlation is very close to zero, so this dataset does not show a strong linear relationship between scoring average and Instagram popularity. This suggests that follower count is shaped by more than current scoring performance, including career reputation, visibility, market, medias, endorsements, and personality.

## All-Star comparison
|  All-Star  |  Players  |   Mean_PPG |   Median_PPG |   Mean_Followers_M |   Median_Followers_M |
| No         |        21 |      22.6  |         23.9 |              69.52 |                62.27 |
| Yes        |        29 |      20.76 |         21.3 |              77.32 |                82.7  |

## Position comparison
| Position   |   Players |   Mean_PPG |   Mean_Followers_M |
| C          |         9 |      22.51 |              80.69 |
| PF         |         9 |      20.89 |              72.11 |
| PG         |         9 |      19.38 |              96.83 |
| SF         |        13 |      22.83 |              63.51 |
| SG         |        10 |      21.49 |              62.99 |

## Top 5 by followers
| Player Name     |   PPG |   Followers_Millions |
| Jamal Murray    |  19.5 |               149.96 |
| Stephen Curry   |  27.3 |               149.44 |
| Kawhi Leonard   |  26.3 |               147.69 |
| Cade Cunningham |  21.7 |               136.94 |
| Jayson Tatum    |  23.8 |               135.86 |

## Top 5 by PPG
| Player Name      |   PPG |   Followers_Millions |
| Donovan Mitchell |  30   |                14.55 |
| CJ McCollum      |  29.8 |                85.71 |
| Luka Dončić      |  29.7 |                36.4  |
| Franz Wagner     |  29.7 |                62.27 |
| Darius Garland   |  28.3 |                79.91 |
