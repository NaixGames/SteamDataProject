# SteamDataProject - Summary

This is a project to try to do some statistical analysis on steam to try to predict which factors affect Steam sales, at least from a statistical point of view.

As a disclaimer, do not take everything you see here as face values or as a factual truth. If YOU think a particular feature would make your game sell better, then go and do it.

Some particular questions that motivated me to do this

- Which factors easily available can help predict a game steam sales?

- Do Mac support actually matter for steam sales?

- Do number of genres actually matter for a steam sale? Do number of tags?

- Does having the "indie" label cause any significant difference in sales? 

- Does supporting more languages cause any significant difference in sales?



In what follows you can see the process in which I arrive to those answers.


# Data and data cleaning

Raw data was obtained from https://www.kaggle.com/datasets/joebeachcapital/top-1000-steam-games/discussion/534302. This provided
a bunch of interesting data, for which we focus on:

- AppID (the game internal steam ID)
- Name
- Release date
- Estimated owners (estimated by SteamSpy)
- Peak CCU (the biggest amount of players playing the game at the same time)
- age (the age rating of the game)
- Price (in dollars)
- DLC count
- Supported languages (the supported languages in written text for the game)
- Windows (if Windows if supported)
- Mac (if Mac if supported)
- Linux (if Linux if supported)
- Positive (number of positive reviews)
- Negative (number of negative reviews)
- Categories (the categories the game provides as information for it, like Single-Player, achievements, etc)
- Genres (the genres for the game, like Adventure, Action, Indie, Simulation)
- Tags (the tags for the game)

Other data fields where left out at this stage to simplify this analysis, or due to them being unreliable (looking at you Metacritic reviews score).

I did some things to clean the data, like only considered games for whom all this fields are filled correctly, avoiding free games (the free game market is a whole different beast!),
and avoid games that will release past the scrap data of 24 of September of 2024 (note games in testing are still in steam backend! And those are also a whole different thing).

Once that was done I added some fields to facilitate the analysis. 
- An average number of owners based on SteamSpy estimations
- The number of categories the game page provides
- Games main category, which we will use for classifying the game and clustering the analysis. (TODO: Analysis if it is better if we set the cluster tags, and see which one the game belongs too a posteriori)
- The number of genres the game says it belongs to
- The number of tags the game provides
- A field for knowing if the game has the indie genre
- A field for knowing if the game has the indie tag

Now I added some fields for normalizing with respect to time since release. As we said, we want to estimate the number of sales given other factors, but this is skewed to be bigger
for games that have been on sale for more time. To account for this I added

- The number of days since the game was released
- The average owners per day. That is, we divide the number of estimated owners by the number of days since the game released. This is akin to a "custom acquisition rate"
- A estimated total lifetime owners. For this we assume that sales during lifetime follows a pareto distribution (which is true for the majority of games) and we
use the rule of thumb that a game will have total sales in a year of 3 times of what it did in its first week ( https://newsletter.gamediscover.co/p/data-deep-dive-whats-the-long-tail ).
With this can actually write the Paretto explicitly, and use that to predict the game total owners.

The last two fields are what we will consider the "output" of our prediction models, and we will compare both in time.

# Data normalization

# Linear regression

# Hypothesis testing

# The future?

To improve this analysis in the future I plan to do the following:

- Use my own data scrapper. While the data we used contained a bunch of information, it also contains a big number
of data not filled correctly (in particular, estimated owners for a big number for games is just missing).

- Include other fields for my analysis. Do number of screenshots and movies affect the sales? I would say they do,
but companies that can include more screenshots and trailer tend to have a bigger marketing team, hence more budget for marketing,
and I feel afraid to let that into the analysis without looking at possible correlations with other factors.

- Use a neural network for regression. I think this should help capture better the self-interaction between
different data fields.



# TO-DO

- Clean the data to avoid games that have demo / Playtest in the name. Clean games with too little players.

- Explain the process I used to clean the data (DO THIS FIRST!)

- Explain the things I did for data normalization

- Do linear regression for a first model

- Investigate how the linear regression model can be improved

- Check if we can do some neural network to improve the estimation

- Test if having the "indie" label cause any statistical significance.

- Test if having MAc support cause any statistical significance lmao.

- Write my own data scrapper.
