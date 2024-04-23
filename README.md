# causal-inference-forest-fire-ignition

Up-to-date documentation: https://www.pywhy.org/dowhy/v0.11.1/user_guide/index.html


Requirements:
-	We need the isolated effect of each factor on fire susceptibility.
    o	From this we can somewhat determine the size of the adjustment value for each factor (factor with smaller influence gets smaller adjustment values)
-	We need to compare the effect strengths of the different factor classes to each other.
-	Is FFMC an effect modifier? --> If yes, then we need to estimate the ACEs for FFMC subgroups.
    

Notes
- Explore if it is possible to calculate the CATE per factor-class given the FFMC class
        - unfortunately not yet possible to do it with gmc - this supports only average causal effects so far (arrow strength)
- Can we use causal graphs which include variables without data in dowhy
        - Yes this is easily possible with traditional dowhy api
        - It causes problems when using gcm
        - Conclusion: We should present graphs with variables we have data about & variables we do not have data of
- How to derive adjustment values from causal estimates?
- How to make predictions with causal mechanisms? - Is it possible?
        - If we set the causal mechanisms ourselves with models trained on parent nodes, its easy to make predictions
        - it seems that so far autoset mechanisms can not be accessed to make predictions
- CICD pipeline


Roadmap
- Check if CATE works with categorical data in traditional dowhy API
- Figure out how to derive adjustment values from causal estimates
- Implement full causal pipeline for calculating adjustment values
- Create more complete causal graph and run pipeline

CATE
- Whats the ATE for factors (forest type, forest cover & exposition) for FFMC subgroups
- How to interpret those values

Research Questions:
- Direct causal influence of factors
- Making predictions? Interventional samples, setting parent nodes of fire



Last status 16.04.2024
- Estimated direct causal influence and ATE for three factors based on simple graph
- Based on dowhy tests graph is rejected
- The last things I did was to think about research questions & to create a more complete graph with triggers (see drawio)
- I wanted to write Christian Schmidt for Temperature, Precipitation, ... values
- How to model that FFMC is depending on last FFMC value in the Graph?
- Most important part is to get the research questions right - so that I can write a paper


Research Questions Causal Inference Fire Ignition


- We want to compare the causal impact of the different factors on fire ignition
        Method: Quantification of Arrow Strength

- We want to find the Average Causal Effect (ACE) of the factors on fire ignition. The causal impact mediated over other factors (e.g. forest type --> forest cover --> fire ignition) should be removed.
        Method: We use the GCM to calculate the ACE for each factor given a reference and treatment value. We block the forward paths of other factors by fixing the value of the factor

- We want to use the causal model for prediction of wildfire ignition (danger)
        Method: We draw interventional samples from the GCM for a certain combination of predictor values
                We evaluate using test set and compare to other ML approaches

Methodology:
        - Everything should be doable with GCM


Research Question:
- Quantification of causal importance of arrows (direct effects)
- What is the Controlled Direct Effect (CDE) of forest type, forest cover & exposition on forest fire ignition?
- Can we use the GCM to make comparably good predicitons?

Output:
- Graph with Causal Importance of predictors (& confidence)
- Graph with ACE vs CDE of three factors
- Evaluation graph of predicitve performance


# TODOs
- Decision - only all data / ignore location uncertainty
- Notebook - investigate data (train & test)
- Notebook - causal prediction & evaluation
- Notebook - quantification of arrow strenght






