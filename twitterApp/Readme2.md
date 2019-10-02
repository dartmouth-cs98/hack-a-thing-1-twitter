## Hack-A-Thing-2

### What I Learned / What I Did:
* The Goal
  * The goal of this Hack-A-Thing was to create a Twitter bot that would read input from twitter and determine whether a tweet was an insult or not. If it was, the bot would respond with an insult of its own. There were four parts to this program:
   * Connecting to and receiving input from Twitter (by using the Twitter API)
   * Creating and training a model to identify insults and other toxic comments
   * Using the model to categorize comments from twitter
   * Creating a generator to respond to the comment

  * I attempted the first two with some success.  

* For this Hack-A-Thing, I explored three main areas to accomplish the goals above:
   * Setting up and using an API (attempted)
   * Gained familiarity with various well known NLP algorithms and packages.
   * Exploring the basic functionality of several python packages.

  * Using the Twitter API:
   1. I registered with twitter to get my consumer and authentication keys. I attempted to connect to my account using tweepy, but was unable to authenticate. I am not sure why I had this problem, and stack overflow was not able to help me.

  * Within NLP, I explored the following topics:
   1. Cleaning and preparing text with nltk: tokenization, stemming, use of stop words, and other preprocessing techniques.
     * For the model, I used their tokenization method to break strings apart by punctuation. If I understood the model better, I would use a better tokenization method. (ex. Bob's -> Bob, s  -> would be broken apart using their method).

   2. I chose to try and implement a Naive Bayes model & Support Vector Machine. I found several interesting readings that explained the Naive Bayes model, and followed a Kaggle tutorial to develop the model to train with the 'Toxic Comments Dataset' from 'Google Jigsaw'.
     * The tutorial: https://www.kaggle.com/jhoward/nb-svm-strong-linear-baseline#Building-the-model
     * I tried to understand the model and how the code worked. As I went through each part, I tried to make small changes / customizations, such as loading a stop words list from nltk instead of leaving the option empty.
     * Additionally, I tried to refactor and comment each section of the code based on my understanding of how the algorithm/code worked.


  * I also gained some experience using the following python packages:
   1. Numpy for working with specialized arrays.
   2. I used Pandas Dataframes to read the Kaggle's csv data. I gained familiarity with several methods for manipulating and representing Pandas dataframes.


### Who participated
* I worked on this project independently.

### How does this hack-a-thing inspire you or relate to your possible project ideas?
* Most of my project ideas involve processing text and machine understanding. While I am not ready to implement an algorithm to do this, I have developed the understanding necessary to start researching how to complete a project using machine understanding.  

### What Didn't Work
* My Tweepy program did not authenticate even though I had the correct credentials. I did not get to try authenticating with other Twitter Api wrappers like python-twitter or Twurl.
* The NBSVM model runs and trains correctly, even with my small modifications. The next challenge would be to use that model to categorize Twitter comments.

### Output
1. The program first outputs the categories and number of entries per category.
  * All categories have the same number of entries because every feature is associated with a category by a boolean (0 or 1).
1. Several statistic s about each category are printed using the display feature of Dataframes. Most importantly, it shows what proportion of entries are in each category with the mean statistic.
1. The program outputs the first 100 documents with their tokens and the token's relative frequency in the dataset.
1. Lastly, the program outputs the first 100 features it uses. 


### Resources
* I used the following resources:
  * https://www.kaggle.com/jhoward/nb-svm-strong-linear-baseline#Building-the-model
  * https://medium.com/predict/we-might-be-nothing-but-a-temporary-fluctuation-e2539bd38823?source=post_recirc---------2----------------
  * http://www.nltk.org/book/
  * https://www.analyticsvidhya.com/blog/2017/06/word-embeddings-count-word2veec/?source=post_page-----1d5a2d638958
