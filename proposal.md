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

Example:

> Understanding how the variety of barley and the site on which they grow impact the annual yield is very important. It can be very useful for farmers who want to have the highest yields as possible, but is can also help agronomists to do their job. 

> Missed medical appointments cost the healthcare system a lot of money and affects the quality of care. If we could understand what factors lead to missed appointments it may be possible to reduce their frequency. To address this challenge, I propose building a data visualization app that allows health care administrators to visually explore a dataset of missed appointments. My app will use show the distribution of factors contributing to appointment show/no show and allow users to explore different aspects of this data by filtering and re-ordering on different variables in order to compare factors that contribute to absence.

### Section 2: Description of the data

As mentioned in lecture, in your group of 3 or 4, you are expected to select one of your group members DSCI 531 Lab 4 assignments as a template for your dashboard. 
This is to make sure we do not spend a lot of time looking for a new dataset and understanding it in detail.

If you prefer, you can also choose to visualize your own data **IF ALL MEMBERS OF YOUR GROUP AGREE TO THIS**. Note that the purpose of this first dashboard is to get you familiar with the mechanics of building a dashboard. _If you do choose to use your own data, make sure you clear it with a TA first, and state who approved it in your writeup._ If a TA or instructor has already approved your dataset for DSCI 531 Lab 4, you do not need to get it approved again.

In your proposal, briefly describe the dataset and the variables that you will visualize. Note, all data has to be publicly available since you are required to create a public repo.

Please note, if your dataset has _a lot_ of columns and you plan to visualize them all, provide a high level descriptor of the variable types. For example, indicate that the dataset contains a variety of _demographic variables_ and provide a brief list rather than stating and describing every single variable. You may also want to consider visualizing a smaller set of variables given the short duration of this project.

Example:

> I will be visualizing a dataset of approximately 300,000 missed patient appointments. Each appointment has 15 associated variables that describe the patient who made the appointment (`patient_id`, `gender`, `age`), the health status (`health_status`)of the patient (Hypertension, Diabetes, Alcohol intake, physical disabilities), information about the appointment itself (`appointment_id`, `appointment_date`), whether the patient showed up (`status`), and if a text message was sent to the patient about the appointment (`sms_sent`). Using this data I will also derive a new variable, which is the predicted probability that a patient will show up for their appointment (`prob_show`).

In the above example, column names are specified using backticks. Remember if your dataset has _a lot_ of columns, stick to summaries and avoid listing out every single column. The example also differentiates columns that come with the dataset (i.e. `Age`) from new variables that you might derive for your visualizations (i.e `ProbShow`) - you should make a similar distinction in your write-up.

Another example of a good description of a dataset can be found [here](https://www.kaggle.com/unsdsn/world-happiness) for the World Happiness Report dataset on Kaggle.

### Section 3: Research questions and usage scenarios

The purpose of this section is to get you to think about how someone else might use the app you're going to design, and to think about those needs before you start coding. 
In Block 2, you learned about several versions of research questions - we will again focus on descriptive and exploratory research questions. 
Revise your research question(s) based on the feedback of your peers, and state them in this section.
Then, consider how the dashboard can be used to answer your research question(s) by a fictional person - these are usage scenarios.

Usage scenarios are typically written in a narrative style and include the specific context of usage, tasks associated with that usage context, and a hypothetical walkthrough of how the user would accomplish those tasks with your app. 
If you are using a Kaggle dataset, you may use their "Overview (inspiration)" to create your usage scenario, or you may come up with your own inspiration.

An example usage scenario with tasks (tasks are indicated in brackets, i.e. [task])

> Mary is a policy maker with the Canadian Ministry of Health and she wants to understand what factors lead to missed appointments in order to devise an intervention that improves attendance numbers. 
She wants to be able to [explore] a dataset in order to [compare] the effect of different variables on absenteeism and [identify] the most relevant variables around which to frame her intervention policy. 
When Mary logs on to the "Missed Appointments app", she will see an overview of all the available variables in her dataset, according to the number of people that did or did not show up to their medical appointment. 
She can filter out variables for head-to-head comparisons, and/or rank order patients according to their predicted probability of missing an appointment. 
When she does so, Mary may notice that "physical disability" appears to be a strong predictor missing appointments, and in fact patients with a physical disability also have the largest number of missed appointments. 
She hypothesizes that patients with a physical disability could be having a hard time finding transportation to their appointments, and decides she needs to conduct a follow-on study since transportation information is not captured in her current dataset.

Note that in the above example, "physical disability" being an important variable is fictional - you don't need to conduct an analysis of your data to figure out what is important or not, you just need to imagine what someone could find, and how they may use this information.