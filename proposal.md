## Milestone 1: Projet set-up and dashboard proposal

In this milestone, you will set-up your project for development and submit a dashboard proposal. In the second milestone, you will submit the final version of your first dashboard created in python and Altair.

## Proposal

Your proposal should be no more than 1,000 words.

When submitting your proposal as a (separate) markdown document (named `proposal.md` which lives on GitHub.com), please include the following sections in this order:

1. Motivation and purpose
2. Description of the data
3. Research questions you are exploring

The proposal will be marked as whole, and you will be assessed on the quality and clarity of your writing, the feasability of what you propose using the writing and reasoning rubrics.

Each of the proposal sections are described below and include an example of what is expected. You don't have to write your own proposal _exactly_ the same as the examples; the examples just serve as a guide. When writing your proposal consider whether what you are proposing is realistic to implement in a two week time frame.

### Section 1: Motivation and Purpose

In a few sentences, provide some motivation for why you are creating a dashboard. What problem is could it solve? What is the "purpose" of the dashboard? Be brief and clear.


> Barley is part of the major cereal grains used worldwide. Understanding how the annual yield of barley is impacted by the variety or site on which it grows is very important. It can help farmers to have the highest yield as possible and increase their productivity, but it can also help agronomists to have a better understanding of how the environment impacts each variety of barley. To help those farmers increase their productivity, we decided to create an app that could allow them to explore a dataset containing information on annual yields for different sites and barley varieties. This app will allow the users to see the annual yield for selected varieties and particular sites, for the years 1931, 1932, or both. It should help them understand what variety or what site is the most suitable to their situation.

### Section 2: Description of the data

As mentioned in lecture, in your group of 3 or 4, you are expected to select one of your group members DSCI 531 Lab 4 assignments as a template for your dashboard. 
This is to make sure we do not spend a lot of time looking for a new dataset and understanding it in detail.


In your proposal, briefly describe the dataset and the variables that you will visualize. Note, all data has to be publicly available since you are required to create a public repo.

> We chose the barley dataset from the vega-datasets python package. This dataset shows the yields of 10 different varieties of barley at 6 different sites in Minnesota during the years 1931 and 1932. It first appeared in the 1934 paper  "Statistical Determination of Barley Varietal Adaption" by the three agronomists who led this experiment: F.R. Immer, H.K. Hayes, and L. Powers.

> This dataset contains 4 columns : `yield`, `variety`, `year` and `site`.

> The 10 varieties studied are : Velvet, Trebi, No. 457, No. 462, Peatland, No. 475, Manchuria, Glabron, Svansota, and Wisconsin No 38.

> The 6 sites studied are : University Farm, Waseca, Morris, Crookston, Grand Rapids, and Duluth.

> There are no missing data in this dataset, and all the possible combinations of variety and sites are present for the years 1931 and 1932.

> We speculate here that the yield is in kilograms per hectare.



### Section 3: Research questions and usage scenarios

The purpose of this section is to get you to think about how someone else might use the app you're going to design, and to think about those needs before you start coding. 
In Block 2, you learned about several versions of research questions - we will again focus on descriptive and exploratory research questions. 
Revise your research question(s) based on the feedback of your peers, and state them in this section.
Then, consider how the dashboard can be used to answer your research question(s) by a fictional person - these are usage scenarios.

Usage scenarios are typically written in a narrative style and include the specific context of usage, tasks associated with that usage context, and a hypothetical walkthrough of how the user would accomplish those tasks with your app. 
If you are using a Kaggle dataset, you may use their "Overview (inspiration)" to create your usage scenario, or you may come up with your own inspiration.


> Our research questions are : <br>
Given some sites and some varieties, what variety of barley had the highest yield during a specific year? <br>
Given some sites and some varieties, what site had the highest yield during a specific year? <br>
Given some sites and some varieties, what is the variety of barley with the highest yield for each of the sites?

> George is a farmer who just bought land in Waseca to add to the land he already owns in Crookston. He would like to grow barley on his two lands, but he doesn't know which variety he should use to have the highest yield. 

> He needs to have the ability to [explore] the dataset so that he can [compare] the annual yield of each variety on both of his lands and [identify] which variety is the best one for him. Moreover, George knows that the way of growing each variety of barley is different. 
> Therefore, he needs to be able to [compare] if the difference of yield between 
> - choosing two different varieties for each of his sites 
> - choosing only one variety for both lands 

> is worth it. Finally, George is wondering if he should buy a third land. However, he does not want to spend time learning how to grow another type of barley, so he needs to [compare] the yields of the varieties he already has at hand, for every site. Thanks to our app, he could [identify] the site of the land that he wants to buy. 

> When George uses the "BaRley app", he will see three graphs and a map. The two first graphs will show the annual yield according to the site, and the annual yield according to the variety. The third graph will show different plots of the yield per variety for each site. Finally, a map will show where the selected sites are in Minnesota.

> George will have the ability to filter which year, which varieties and which sites will be represented on the graphs.
Once George has selected the two sites where his lands are (Waseca and Crookston), he realizes that Velvet is the variety that has the highest yield in both sites for the years 1931 and 1932. After that, he selects the Velvet variety and notices that the site that has the highest yield for this variety is Morris. Thus, he decides to buy a new land in Morris.
