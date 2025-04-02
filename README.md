# SteamDataProject - Summary

This is a project that uses some statistical analysis on Steam's data to try to predict which factors affect Steam sales. This started motivated by the myth "Mac support does not translate into better sales" in GameDev,
but wanted to see what else I could learn.

TLDR: Mac support does not seem to boost Steam sales. Action and Casual games seem to sell better than any other genre. 

# Disclaimer

As a disclaimer, do not take everything you see here at face value or as a factual truth. 

This is mostly done for my entertainment, and so I implemented almost everything from scratch. This includes some linear regression, hypothesis testing and neural networks libraries. 


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
- Windows (if Windows is supported)
- Mac (if Mac is supported)
- Linux (if Linux is supported)
- Positive (number of positive reviews)
- Negative (number of negative reviews)
- Categories (the categories the game provides as information for it, like Single-Player, achievements, etc)
- Genres (the genres for the game, like Adventure, Action, Indie, Simulation)
- Tags (the tags for the game)

Other data fields were left out at this stage to simplify this analysis, or due to them being unreliable (looking at you Metacritic reviews score).

I did some things to clean the data, like only considered games for whom all these fields are filled correctly, avoiding free games (the free game market is a whole different beast!),
and avoiding games that will release past the scrap data of 24 of September of 2024 (games being testing are still in Steam's backend! ).

Once that was done I added some fields to facilitate the analysis. 
- An average number of owners based on SteamSpy estimations
- The number of categories the game page provides
- Games main category, which we will use for classifying the game and clustering the analysis. (TODO: Analysis if it is better if we set the cluster tags, and see which one the game belongs to a posteriori)
- The number of genres the game says it belongs to
- The number of tags the game provides
- A field for knowing if the game has the indie genre
- A field for knowing if the game has the indie tag

I added some fields for normalizing time since the release date. As we said, we want to estimate the number of sales given other factors, but this is skewed to be bigger
for games that have been on sale for more time. To account for this I added;

- The number of days since the game was released
- The average owners per day. That is, we divide the number of estimated owners by the number of days since the game was released. This is akin to a "customer acquisition rate"
-The expected total lifetime sales. I get this by taking the average customers and then extrapolating what would be the total sales by using the "folklore rule"; sales in a year are three times the sales in your first week.


The last two fields are what I expected to use for "output" for the models and compare them, however, I didn't get a single model to perform well enough on the second one. I plan to return to it eventually, but in what follows, I will only consider the first one.

# Data normalization

First, we make some changes of variables so training is less sensible to scale.

First note that both our predicted outputs have a pretty obvious power law. Hence, we will change them to a log scale before making predictions. The same applies to prices, positive reviews and negative reviews.
The number of categories follows a power law distribution (ignoring values with only 1 category). I will adjust them to log scale. The number of languages follows a power-law distribution, with some outliers at 29 and 103 (most likely automatic filling of some languages / obvious limit set by translation companies). Again, we take the log of these numbers. 

The number of tags, funny enough, follows a distribution bounded between 1 and 20, with a pretty heavyweight to 20. I will re-adjust them to 0 to 1.

The genre is remapped to a one-shot vector.

# Linear regression

I perform a linear regression. From this, I got a model that predicted pretty well the owners of some games, with an average squared loss of 1.67 on the validation set (although your millage may vary).

By looking at the training weights some interesting things can be deduced:

1.- Action and Casual genres are what sell best. I see this as splitting the "hardcore" audience (mostly focused on action games) and the more casual one in the second group. Everything else is more niche when compared to these other groups.

2.- The number of categories and number of tags have a noticeable effect on predicted sales. I expect there is a correlation between games with more budgets (which then tend to perform better) and games with more features, so I expect this is showing this correlation, somehow.

3.- Positive and negative reviews both have a good impact on sales; however, this is just showing that when a game sells better it gets more reviews; both positive and negative ones. What is really interesting here is that positive ones DO have a much higher impact on owners than negative ones (which is much more than I expected). 

4.- Both Mac and Linux support seems to have little to no weight on owners (and this is expanded on next section).

While other conclusions could be obtained from this, I believe they would be tainted by the fact we are doing a linear model (and not a more sophisticated one).

# Hypothesis testing

As mentioned before, what motivated this was the question of whether Mac support reflects on better sales of games. What I managed to get with this analysis, by doing a t-student test, is that there is no evidence giving native Mac support provides a boost in game owners (in fact, the p-value of the test was so low that Python approximated it as plain 0). The same thing happens with Linux. I suppose this is due to the presence of wine and proton compatibility layers.

# Neural Network model

After doing the Linear model I obtained a way to compute approximately the owners of games of steam, which while it performed well didn't perform TOO well. This is not as surprising; it is certainly not capturing correctly many factors that come into play when players decide which games to buy. For example; I do not expect the price to linearly translate to owners, but something more complicated, since price is used as a proxy for "quality" for most customers.

For this, I did a couple of neural network models. At first, I only did backpropagation on the models with different activation functions (mainly linear, leaky ReLU and smooth Relu), which all gave around 1.38 of average squared loss on the validation set after enough training. However, when trying it with some common game data the results were pretty bad. Looking at the weights I noticed it was in general pretty biased to give low results on sales. That makes sense; since most games on Steam sell pretty poorly, and I was testing it with relatively known games, which are over the mean of expected sales. I expected data normalization to address some of this, but it seems it wasn't enough. To try to fix this I included L2 normalization for the weights, and surprisingly, it performed much better. The new models gave me around 1.4 squared loss (ignoring the regularization term) but performed much better with known game data.

I would like to make some deductions of this; but since the neural network models are much more complicated, that is not that easy :). Hopefully in the future.



# The future?

To improve this analysis in the future I plan to do the following:


- Use my own data scrapper. While the data we used contained a bunch of information, it also contained a large number
of data not filled correctly (in particular, estimated owners for a big number of games are just missing).

- Test if having the indie label as a category or tag gives any significant improvement in sales.

- Try to get a better genre classification. Steam one is barebones at best. Maybe clustering could work better.

- Include other fields for my analysis. Does the number of screenshots and movies affect the sales? I would say they do,
but companies that can include more screenshots and trailers tend to have a bigger marketing team, hence more budget for marketing,
and I feel afraid to let that into the analysis without looking at possible correlations with other factors.

- Grab my libraries and produce applications to automate this process and have other people easily test the models. That would be really nice :).