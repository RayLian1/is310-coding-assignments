# NBA Players Performance vs Instagram Popularity
## Topic
This project explores the relationship between NBA players’ on-court performance and their popularity on social media, specifically Instagram.

## Research Question
Is there a relationship between an NBA player’s average points per game (PPG) and their number of Instagram followers?

## Unit of Analysis
Each data item represents one NBA player. The dataset includes 50 player, with each row containing information about their performance and popularity.

## Approach
I created this dataset from scratch by manually collecting data on NBA players. I selected 50 well-known current NBA players who have publicly available statistics and Instagram accounts. This approach allowed me to directly decide what data to include and how to structure it.

## Data Collection Process
I gathered player performance data (points per game) by searching for recent NBA statistics for the 2024–2025 season. I collected Instagram follower counts by visiting each player’s official Instagram profile and recording their follower numbers.

## Tools Used
I used Google to find player statistics and Instagram accounts. I organized and structured the dataset using Excel, which allowed me to keep the data consistent and easy to edit.

## Data Decisions
I chose points per game (PPG) as the main performance metric because it is one of the most commonly used and easily understandable statistics in basketball. I also included Instagram followers as a measure of popularity. I decided to include additional columns such as team, position, All-Star status, and years in the NBA to provide more background information, context, and allow for deeper analysis. I rounded follower counts to approximate values to simplify the dataset.

## Challenges
One challenge was ensuring consistency across all data points, especially since different sources may report slightly different statistics. Another challenge was deciding how to handle approximate follower counts and whether to round them. It was also sometimes unclear how to categorize certain players (for example, players who play multiple positions), so I selected the most commonly listed position.

## Patterns and Observations
From collecting the data, I noticed that players with higher scoring averages often tend to have more Instagram followers, but this is not always the case. Some players with lower scoring averages still have high popularity due to factors like personality, marketability, or past achievements. This suggests that performance is important, but not the only factor influencing popularity.

## Later Steps
To expand this dataset, I would scale it to include 500–1000 players using computational methods. For example, I could use web scraping or APIs to automatically collect more player statistics and social media data. I would also consider adding more variables, such as team success, endorsements, or media presence, to better understand what drives popularity. Additionally, I would explore using Python to analyze correlations between performance and followers, and visualize the results using graphs such as histograms.