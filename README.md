# SteamDataProject - Summary

This is a project to try to do some statistical analysis on Steam to try to predict which factors affect Steam sales. This actually started motivated by the myth "Mac support does not translate into better sales" in GameDev,
but wanted to see what else I could learn.

TLDR: Mac support does indeed does not support Steam sales, Action and Casual games sell better than any other genre.

# Disclaimer

As a disclaimer, do not take everything you see here at face value or as a factual truth. 

This is mostly done for my entertainment, and so I implemented almost everything from scratch. I do not plan to change that.


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


The two field is what we will consider the "output" of our prediction models.

# Data normalization

First, we make some changes of variable so training is less sensible to scale. This is all pretty standard.

First note that both our predicted outputs have a pretty obvious power law. Hence, we will change them to a log scale before making predictions. The same applies to Prices, Positive and negative reviews.
The number of categories follows a power law distribution (ignoring values with only 1 category). I will adjust them to log scale. The number of languages follows a power-law distribution, with some outliers at 29 and 103 (most likely automatic filling of some languages / obvious limit set by translation companies). Again, we take the log of these numbers. 

The number of tags, funny enough, follows a distribution bounded between 1 and 20, with a pretty heavyweight to 20. I will re-adjust them to 0 to 1.

The genre is remapped to a one-shot vector.

# Linear regression

We perform a linear regression by doing simple machine-learning algorithms. From this I got a model that predicted pretty well the owners of some games (although your millage may vary).

By looking at the training weights some interesting things can be deduced:

1.- Action and Casual genres are what sell best. I see this as splitting the "hardcore" audience (mostly focussed on action games) and the more casual one in the second group. Everything else is more niche when compared to this other groups.

2.- Number of categories and number of tags have a noticeable effect of predicted sales. I expect there is a correlation with games with more budgets (which then tend to perform better) and game with more features, so I expect this is showing this correlation, somehow.

3.- Positive and negative reviews both have a good impact in sales; however this is just showing that when a game sells better it gets more reviews; both positive and negative ones. What is really interesting here is that positive ones DO have a much higher impact in owners than negative ones (which is much more expected). 

4.- Both Mac and Linux support seems to have little to no weight on owners (and this is expanded on next section).

While other conclusion could be obtained from this, I believe they would be tainted by the fact we are doing a linear model (and not a more sophisticated one).

# Hypothesis testing

As mentioned before, what really motivated this was the question of whatever Mac support reflects on better sell of games. What I managed to get with this analysis, by doing a t-student test, is that there is absolutely no evidence giving native Mac support provides a boost in game owners (in fact, the p-value of test was so low that python approximated it as plain 0). Same thing happens with Linux.

# Neural Network model

After doing the Linear model I obtained an way to compute approximately the owners of games of steam, which while it performed well it didn't perform TOO well. This is not as surprising; it is certainly not capturing correctly many factors that came into play when players decide which games to buy. For example; I do not expect owners
translate linearly to price, but rather like a parabola (in which price is used a proxy for "quality" from a certain point).




# The future?

To improve this analysis in the future I plan to do the following:


- Use my own data scrapper. While the data we used contained a bunch of information, it also contains a large number
of data not filled correctly (in particular, estimated owners for a big number of games are just missing).

- Test if having the indie label as a category or tag gives any significant improvement in sales.

- Get a better genre classification. Steam one is barebones at best.

- Include other fields for my analysis. Does the number of screenshots and movies affect the sales? I would say they do,
but companies that can include more screenshots and trailers tend to have a bigger marketing team, hence more budget for marketing,
and I feel afraid to let that into the analysis without looking at possible correlations with other factors.

