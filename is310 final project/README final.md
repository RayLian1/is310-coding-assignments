# NBA Players Performance vs Instagram Popularity

## Topic
This project explores the relationship between NBA players’ on-court performance and their popularity on social media, specifically Instagram.

## Research Question
Is there a relationship between an NBA player’s average points per game (PPG) and their number of Instagram followers?

## Unit of Analysis
Each data item represents one NBA player. The dataset includes 50 player, with each row containing information about their performance and popularity.

## Dataset Files
`nba_instagram_dataset_final_augmented.csv`: final dataset with original and computationally augmented columns
`analysis_summary.md`: short summary of the main computational findings
`final_data_essay.docx`: final individual data essay

## Original Variables
Player Name, Years, Position, PPG, Instagram Followers, All-Star
PPG means points per game

## Computationally Added Variables
Followers_Millions (Instagram followers converted into millions)
Log10_Followers (Log-transformed follower count to make very large numbers easier to compare)
PPG_Rank (Ranking by PPG, with 1 as the highest)
Follower_Rank (Ranking by follower count, with 1 as the highest)
PPG_Tier (Player scoring category based on PPG)
Popularity_Tier (Instagram popularity quartile)
Above_Average_PPG (Whether the player is above the dataset mean for PPG)
Above_Average_Followers (Whether the player is above the dataset mean for Instagram followers)

## Methods
The initial dataset was made manually by collecting public information about current NBA players, including PPG and Instagram follower counts. For the final project, I used computational methods to augment the dataset. These methods included creating rankings, converting follower counts into millions, applying a log transformation, and grouping players into scoring and popularity categories.

## Main Findings
In this dataset, PPG and Instagram followers do not have a strong linear relationship. The correlation between PPG and Instagram followers is about -0.002, which is very close to zero. This means that scoring more points per game does not automatically predict having more Instagram followers in this dataset. Popularity appears to be influenced by other cultural factors such as career reputation, media attention, market, personality, and public image.

## Limitations
This dataset is limited because it includes only 50 players and focuses mainly on one performance statistic. Instagram follower counts also change over time, and the dataset uses approximate counts rather than exact historical snapshots. Some categories, such as position and All-Star status, simplify players who may have more complex careers. Because of these limits, the dataset should be interpreted as an exploratory cultural dataset rather than a complete measurement of NBA popularity.

## Ethical Considerations

The dataset uses public-facing information about public figures, but it still raises questions about how people are represented as data. Reducing a player to PPG and follower count can hide important context, including injuries, team role, personality, race, nationality, media coverage, and commercial branding. The dataset should not be used to make unfair judgments about individual players.

## Conclusion
This project shows that sports popularity is not only about performance. While scoring is important in basketball, Instagram popularity is also shaped by culture, media, visibility, and reputation. Treating NBA players as data makes patterns easier to see, but it also shows how much context information can be lost when it is simplified into only numbers.
