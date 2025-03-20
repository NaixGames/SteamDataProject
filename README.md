# SteamDataProject - Summary

This is a project to try to do some statistical analysis on Steam to try to predict which factors affect Steam sales. 

Some particular questions that motivated me to do this

- Which factors readily available help predict a game's sales?

- Does Mac support matter for Steam sales?

- Does the number of genres matter for a Steam sale? Do the number of tags?

- Does supporting more languages cause any significant difference in sales?

# Disclaimer

As a disclaimer, do not take everything you see here at face value or as a factual truth. 

This is mostly done for my entertainment, and so I implemented almost everything from scratch. I do not plan to change that.


# SteamDataProject - Summary

In what follows you can see the process in which I arrive at those answers.


# Data and data cleaning

Raw data was obtained from https://www.kaggle.com/datasets/joebeachcapital/top-1000-steam-games/discussion/534302. This provided
a bunch of interesting data, for which we focus on:

- AppID (the game's internal Steam ID)
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

Other data fields were left out at this stage to simplify this analysis, or due to them being unreliable (looking at you Metacritic reviews score).

I did some things to clean the data, like only considered games for whom all these fields are filled correctly, avoiding free games (the free game market is a whole different beast!),
and avoid games that will release past the scrap data of 24 of September of 2024 (note games in testing are still in steam backend! And those are also a whole different thing).

Once that was done I added some fields to facilitate the analysis. 
- An average number of owners based on SteamSpy estimations
- The number of categories the game page provides
- Games main category, which we will use for classifying the game and clustering the analysis. (TODO: Analysis if it is better if we set the cluster tags, and see which one the game belongs to a posteriori)
- The number of genres the game says it belongs to
- The number of tags the game provides
- A field for knowing if the game has the indie genre
- A field for knowing if the game has the indie tag

Now I added some fields for normalizing with respect to time since release. As we said, we want to estimate the number of sales given other factors, but this is skewed to be bigger
for games that have been on sale for more time. To account for this I added;

- The number of days since the game was released
- The average owners per day. That is, we divide the number of estimated owners by the number of days since the game was released. This is akin to a "custom acquisition rate"
- An estimated total lifetime owners. For this, we assume that sales during lifetime follow a Pareto distribution (which is true for the majority of games) and we
use the rule of thumb that a game will have total sales in a year of 3 times what it did in its first week ( https://newsletter.gamediscover.co/p/data-deep-dive-whats-the-long-tail ).
With this can write the Pareto explicitly, and use that to predict the game's total owners.

The last two fields are what we will consider the "output" of our prediction models.

# Data normalization

First, we make some changes of variable so training is less sensible to scale. This is all pretty standard.

First note that both our predicted outputs have a pretty obvious power law. Hence, we will change them to a log scale before making predictions. The same applies to Prices, Positive and negative reviews.
The number of categories follows a power law distribution (ignoring values with only 1 category). I will adjust them to log scale. The number of languages follows a power-law distribution, with some outliers at 29 and 103 (most likely automatic filling of some languages / obvious limit set by translation companies). Again, we take the log of these numbers. 

The number of genres follows a Gaussian-ish distribution, so we normalize them by replacing them with their Z-score.

The number of tags, funny enough, follows a distribution bounded between 1 and 20, with a pretty heavyweight to 20. I will re-adjust them to 0 to 1.

The genre is remapped to a one-shot vector.

# Linear regression

We perform two linear regression by doing simple machine-learning algorithms.


# Hypothesis testing

# The future?

To improve this analysis in the future I plan to do the following:

- Use a neural network for the estimation. I think this should help capture better the self-interaction between
different data fields (for example, differences between different genre play-base).


- Use my own data scrapper. While the data we used contained a bunch of information, it also contains a large number
of data not filled correctly (in particular, estimated owners for a big number of games are just missing).

- Test if having the indie label as a category or tag gives any significant improvement in sales.

- Get a better genre classification. Steam one is barebones at best.


- Include other fields for my analysis. Does the number of screenshots and movies affect the sales? I would say they do,
but companies that can include more screenshots and trailers tend to have a bigger marketing team, hence more budget for marketing,
and I feel afraid to let that into the analysis without looking at possible correlations with other factors.


# TO-DO

- Do linear regression for a first model

- Investigate how the linear regression model can be improved

- Check if we can do some neural networks to improve the estimation

- Test if having the "indie" label cause any statistical significance.

- Test if having Mac support cause any statistical significance lmao.

- Write my own data scrapper.
