---
layout: card
inline: false
resource: Lesson Plan
domain:
  - Processing Data
subdomain:
  - Analyzing Data

sample_resource: false

title: "Basic Descriptive Statistics: Measures of Central Tendency"

teaser: >
  This lesson plan introduces students to some of the foundational tools and concepts for basic descriptive statistics, emphasizing measures of central tendency.  Students will spend some time defining key terms, and then will see those concepts in action through analyzing a dataset they create.

keywords:
  - "Descriptive Statistics"
  - "Measures Of Central Tendency"
  - "Statistical Analysis"

metadata:
  source: 
  author: 
  date: "2024"
  license: "CC BY-NC-SA"
  citation: 
---

# Instructor Notes

# Measures of Central Tendency
# Lesson Overview

This set of activities introduces some basic assumptions and methods of descriptive statistical analysis.  Descriptive statistics are usually contrasted with inferential statistics.  Inferential statistics strive to derive valid conclusions about some phenomena by analyzing datasets; descriptive statistics focus more on understanding concretely how a given dataset strives to represent some given phenomena.   The activities outlined below cover the concept of distribution and will detail some tools for beginning to understand how observations are distributed within a dataset, focussing primarily on measures of central tendency.

# Learning Goals
- Define and illustrate the concept of data distribution.
- Introduce the concept of descriptive statistics.
- Practice calculating and understanding measures of central tendency.

# Readings
Matthew J.C. Crump, [*Answering Questions with Data*, 2-2.4.6](https://www.crumplab.com/statistics/02-Describing_Data.html#this-is-what-too-many-numbers-looks-like)
Douglas Shafer and Zhiyi Zhang, [*Introductory Statistics*, 2.2: “Measures of Central Location”](https://stats.libretexts.org/Bookshelves/Introductory_Statistics/Introductory_Statistics_(Shafer_and_Zhang)/02%3A_Descriptive_Statistics/2.02%3A_Measures_of_Central_Location_-_Three_Kinds_of_Averages)

# Agenda
- Defining key concepts (10 minutes)
- Exploring Distributions and Central Tendencies (40 minutes)
- Centrality Measures in a Dataset (25 minutes)

# Activities
## Defining key concepts (10 minutes)
Have students work in small groups to generate definitions in their own words of the key concepts covered in the reading or answer the following questions.  After students work together for five minutes, the class could come back together as a whole to share their best definitions.
- Population versus sample (for review)
- What is a histogram and what does this kind of chart allow you to see?
- Central tendency
- Mean, median, and mode
- Symmetrical versus skewed distributions
- Outliers

## Exploring Distributions and Central Tendencies (40 minutes)
This activity invites students to generate a dataset for their class and use it to practice calculating basic descriptive statistics.  Working collectively (or in small groups if necessary) have each student look up (using google maps) the driving distance from their hometown and record that distance in a central document.  Using this basic dataset, perform the following operations:
- It is possible that members of the class are from a non-contiguous continent, in which case Google maps will not calculate a driving distance.  If this happens, you might use this event as an occasion to reflect upon the inherent messiness of data.  Have students discuss how to handle such instances.  Should you exclude these observations?  Should you use an alternative tool or technique for calculating distance?  Should you allow students to guess or to estimate?  What are the pros and cons of each method?
- Have student groups sketch informally on a piece of paper a histogram from the data (as demonstrated in section 2.2.2 of the Crump reading), with distance listed on the x-axis and number of observations on the y-axis.  Ask different groups to generate histograms with different sized “bins.”  So, one group would create a histogram with bins of 500 miles each, another with bins of 250 miles, another with 100 miles, and so forth as practical. Once these histograms have been generated, ask students to discuss the shape of the data and why the histogram is shaped like it is.  Do students think the histogram would be representative of your institution as a whole?  Why or why not?
- Have students calculate the mean, median, and mode for their dataset.  How do these differ?  Ask them to describe what each measure tells them about the dataset as a whole.  What is the relation between the mean and the median?  Is the data “skewed” in one way or another?  Why might this be?  What kinds of factors impact the distribution of your observations?  For example, how might cost impact who attends or does not attend your institution?  How about community ties?  Or immigration policies, making it harder or facilitating foreign student attendance?  How about financial aid policies?  In general, what kinds of policies, economic realities, or cultural factors might bias your data?

## Centrality Measures in a Dataset (25 minutes)
This exercise utilizes the Gapminder dataset that reports the per capita consumption of CO2 for each country in the world and for each year between 1990 and 2017 ([link](https://drive.google.com/file/d/1DyaSngM0u6ePh_D8RVduL6y92v015x4S/view)).  (Gapminder is a nonprofit organization that utilizes data to address problems of global concern; you can read about the organization [here](https://www.gapminder.org/about/about-gapminder/)).

Before asking students to analyze the data, have them view [Gapminder’s data documentation page](https://www.gapminder.org/data/documentation/), which describes their overall methodology for gathering data.  What kinds of limitations might there be to their approach to data collection?  For example, what is the effect of taking countries as the basic unit of measure?  In what ways might such an approach make sense?  What might the decision to focus on specific countries make it difficult or impossible to see?

Using a software platform of your choice, invite students to pick a year from the dataset and calculate the mean, median, and mode for that year and to create a histogram of the data.  If feasible, you can divide students into small groups and have them work together to generate the various measures of central tendency for select years equally spaced through the dataset.  (Working in groups has the added advantage of allowing students to help each other learning to use the software platform).  
- After they’ve calculated their results, have a representative from each group write their means, medians, and modes in order on a board or in a shared document.
Once these calculations are completed and available for everyone to review, ask groups to develop answers to the following questions:
- What does each measure tell us about the dataset as a whole?
- What trends do the calculated measures display, if any?  
- What kinds of questions do your observations prompt?  What would you like to know more about?  What forces or global disparities might account for the trends you observe?

If time remains, have students repeat the exercise for a specific country of their choice.
