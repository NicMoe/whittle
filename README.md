# whittle
Used to better understand de-identified and aggregated data sets. Purposes:
- Is a data set aggregated sufficiently for effective de-identification?
- For aggregations from the same original data, what are the relationships between the various variables?
- For multiple aggregation tables, is it possible for them to come from the same source data?

## whittle function
When provided with proportional breakdowns from a data set, what might the original disaggregated data set look like? This function takes multiple linked proportion groups, and using multiple stages of Monte Carlo simulation narrows down plausible original set values. For example, let's say we are provided two tables of data about housing stock in a city:

| n = 1,000 units       | near transit | not near transit |
|-----------------------|--------------|------------------|
| single family *(64%)* | 22%          | 78%              |
| row house *(14%)*     | 32%          | 68%              |
| multi-family *(22%)*  | 65%          | 35%              | 

| n = 1,000 units       | owner-occupied | renter-occupied | unoccupied |
|-----------------------|----------------|-----------------|------------|
| single family *(64%)* | 71%            | 25%             | 4%         |
| row house *(14%)*     | 32%            | 61%             | 7%         |
| multi-family *(22%)*  | 14%            | 80%             | 6%         |

With this information, perhaps we're interested in estimating the relationship between transit-adjacency and occupancy status.

1. Given proportions from a data table and a total *n*, estimate the initial range of possible values for each proportion. For example, if we know there are 1,000 housing units in a city and (the provided aggregate value) 14% of them are rowhouses, then we can assume this percentage represents between 135 and 144 units within the original data set. This range, for each individual proportion, becomes our set of initial priors.
2. For each simulation run, define which aggregates to match on / or how many aggregates to match on. Initially this requirement should be loose as your parameter sets (possible combinations) could be astronomical.
3. Create a bunch of possible combinations randomly generated given the priors until there is a sufficient number that hit the aggregate match target (100 successes should suffice).
4. Based on the values represented by the subset of successes, narrow the working range for each proportion to generate a new set of priors. If the number of combinations to get a sufficient set of matches is small, make the aggregates target more restrictive for the next round.
5. Repeat step 3. Repeat this process until a solution (or large enough group of solutions) is found that satisfies all the aggregate values. This could be a single solution, or there could be a range of solutions.
