---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e16-4yp-Machine-Learning-based-Atmospheric-Duct-Interference-cancellation-in-TD-LTE-networkseYY-4yp-project-template
title: Machine Learning based Atmospheric Duct Interference cancellation in TD-LTE networks
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Machine Learning based Atmospheric Duct Interference cancellation in TD-LTE networks

#### Team

- E/16/054, Sathira Shamuditha, [email](mailto:e16054@eng.pdn.ac.lk)
- E/16/351, Madusha Shanaka, [email](mailto:e16351@eng.pdn.ac.lk)
- E/16/389, Nadun Welikanda, [email](mailto:e16389@eng.pdn.ac.lk)

#### Supervisors

- Dr. Upul Jayasinghe, [email](mailto:upuljm@eng.pdn.ac.lk)
- Dr. Suneth Namal Karunarathna, [email](mailto:namal@eng.pdn.ac.lk)

#### Table of content

- [Machine Learning based Atmospheric Duct Interference cancellation in TD-LTE networks](#machine-learning-based-atmospheric-duct-interference-cancellation-in-td-lte-networks)
      - [Team](#team)
      - [Supervisors](#supervisors)
      - [Table of content](#table-of-content)
  - [Abstract](#abstract)
  - [Related works](#related-works)
  - [Methodology](#methodology)
  - [Experiment Setup and Implementation](#experiment-setup-and-implementation)
  - [Results and Analysis](#results-and-analysis)
  - [Conclusion](#conclusion)
  - [Publications](#publications)
  - [Links](#links)

---

## Abstract

Atmospheric ducts are horizontal layers that happen under certain weather conditions in the lower atmosphere. Radio signals guided in the atmospheric duct tend to experience less attenuation and spread further, i.e.hundreds of kilometers [1]. In a large-scale deployed TD-LTE network, atmospheric ducts make faraway downlink (DL) wireless signals propagate beyond the designed protection distance and interfere with local uplink (UL) signals, thus causing severe outage probability. TDD mobile networks are impacted by two types of ducting interference.  

> 1. **External Interference:** This type of interference is caused by the long-distance transmission from nearby country DL signals which will interfere with UL slots of the local TDD network.
> 2. **Internal interference:** This type of interference is caused by long-distance transmission DL signals which will interfere with UL slots within the operators’ network.  

In TD-LTE, there exist three kinds of subframes: uplink, downlink, and special sub-frames. The special sub-frame consists of three parts: DwPTS (Downlink Pilot Time Slot), GP (Guard Period), and UpPTS (Uplink Pilot Time Slot). Moreover, the GP is located at the moment when downlink converts to uplink to prevent interference from downlink signals to uplink signals. Under normal circumstances, any downlink signals from distant BSs beyond the maximum protection distance would experience enough attenuation and hardly interfere with the local uplink signals. But with ADI (Atmospheric Duct Interference)  present, this protection does not work. So as a solution we need to build a model which can predict the ADI and as the next step a method to minimize it like dynamically adjusting the GP.  

## Related works
1. Analysis and prediction of 100 km-scale atmospheric duct interference in TD-LTE net by Ting Zhou, Tianyu Sun, Honglin Hu, Hui Xu, Yang Yang , Ilkka Harjula , Yevgeni Koucheryavy
   1. This paper analyses characteristics of ADI using real network-side big data from the current operated TD-LTE network owned by China Mobile
   2. They also proparse ML model to predict the ADI. That is  SVM (Support Vector Machine)-classifier based spacial prediction method of ADI.
2. A Random Forest-based Prediction Method of Atmospheric Duct Interference in TD-LTE Networks by Tianyu Sun, Ting Zhou, Hui Xu and Yang Yang
   1. This paper also analyses characteristics of ADI using real network-side big data from the current operated TD-LTE network owned by China Mobile.
   2. This paper shows that using machine learning can get a good prediction performance for ADI
   3. This paper also compares the performance of different machine learning algorithms and finds  that Random Forest has a short training time while maintaining the similar accuracy.
3. Recognition and Optimization of Atmospheric Duct in TD-LTE System Based on Convolutional Neural Network by Jin-Hu Shen, Ji-Xiang Liu Jing-Lei Zuo Wen-Bo Ding Ao Shen
   1. This paper is focused on analysing and detection of of atmospheric duct based on network configuration and image recognition using a convolutional neural network
4. Liu F, Pan J, Zhou X, Li G discussed about challenges and opportunities of Atmospheric Ducting Effect in Wireless Communications
   1. They states that this phenomenon can use for duct-Assisted Air-Ground-Sea Integrated Networks.
   2. And this also affect badly on TD-LTE networks and it may cause to interfere the waves. They stated many non ML based solutions to reduce the duct interference.

## Methodology

Describe the steps taken to carry out the project or study. Include the following:

- **Research Design:** Briefly explain the research design, such as case study, survey, or experiment.
- **Data Collection:** Detail the data collection methods, such as surveys, interviews, or observation.
- **Data Analysis:** Explain how the data was analyzed, such as statistical analysis, content analysis, or thematic analysis.
- **Validity and Reliability:** Describe measures taken to ensure the validity and reliability of the data, such as pilot testing, inter-rater reliability, or triangulation.
- **Ethical Considerations:** Discuss ethical considerations, such as informed consent, confidentiality, or risk assessment.

Provide enough information so that the reader can understand and evaluate the methods used in the project or study.


> **MATLAB - LTE Toolbox**  

The LTE Toolbox is a powerful MATLAB-based simulation tool that allows for the simulation and analysis of wireless communication systems. In the proposed system, the LTE Toolbox was used extensively in the experimental setup to simulate, analyze, and test the physical layer of the wireless communication system.

To evaluate the proposed system, experiments were conducted using the LTE Toolbox to generate simulated data. The necessary data was gathered and samples were prepared according to the specifications of the proposed system. The LTE Toolbox was used to simulate the wireless communication system, and Python was used to process the simulation results and develop machine learning algorithms.

Several precautions were taken to ensure the accuracy of the results by controlling the experimental conditions and conducting multiple test runs. The LTE Toolbox was used to generate simulated data under different scenarios to ensure the robustness of the proposed system.

During the implementation of the proposed system, some issues related to the complexity of the LTE Toolbox and the lack of documentation were encountered. However, these issues were overcome by referring to the LTE Toolbox documentation and seeking help from the LTE Toolbox support team.

In conclusion, the LTE Toolbox provides a comprehensive set of simulation and analysis tools required for the proposed system. The results obtained from the experiments showed the effectiveness of the proposed system in wireless communication systems, highlighting the importance of the LTE Toolbox in the development of such systems. 

## Experiment Setup and Implementation

### Overview

In order to conduct experiments, it's important to have a well-defined setup and implementation plan. This helps to ensure that the results are reliable, reproducible, and accurate. In this section, we'll cover some key considerations for setting up and implementing experiments.

### Experimental Design

Before we can begin setting up an experiment, we need to have a clear understanding of the research question we're trying to answer. This involves designing an experimental protocol that will allow us to test our hypothesis. Some key considerations when designing our experiment include:

- **Sample size:** Determining how many subjects or samples we'll need to achieve statistically significant results.
- **Control groups:** Ensuring that we have a control group that is not exposed to the treatment or intervention being tested.
- **Randomization:** Randomly assigning subjects or samples to treatment and control groups to minimize bias.
- **Blinding:** Concealing the treatment or intervention from the subjects or researchers to minimize bias.
- **Replication:** Conducting the experiment multiple times to ensure that the results are consistent.

### Data Collection

Once we have a clear experimental design, we can begin collecting data. This involves selecting appropriate measurement tools and instruments, as well as determining the timing and frequency of data collection. Some key considerations when collecting data include:

- **Validity:** Ensuring that the measurement tools and instruments are valid and accurately measure what they're intended to measure.
- **Reliability:** Ensuring that the measurement tools and instruments are reliable and produce consistent results.
- **Standardization:** Standardizing the measurement tools and instruments across all subjects or samples to minimize variability.
- **Data management:** Developing a system for managing and storing data to ensure accuracy and accessibility.

### Data Analysis

Once we have collected our data, we can begin analyzing it. This involves using statistical tools and methods to test our hypothesis and determine whether the results are statistically significant. Some key considerations when analyzing data include:

- **Descriptive statistics:** Calculating basic statistics, such as means and standard deviations, to describe the data.
- **Inferential statistics:** Using statistical tests, such as t-tests and ANOVA, to determine whether the results are statistically significant.
- **Data visualization:** Creating visual representations of the data, such as graphs and charts, to help communicate the results.
- **Interpretation:** Interpreting the results in the context of the research question and drawing conclusions based on the data.

## Results and Analysis

### Results

In our research, we compared the performance of two predictive models for atmospheric duct interference (ADI) prediction, the ARIMA model and the LSTM model. Our results showed that the LSTM model outperformed the ARIMA model in terms of all the evaluated metrics, including mean absolute error (MAE), mean squared error (MSE), and root mean squared error (RMSE). This suggests that the LSTM model is better suited for ADI prediction than the ARIMA model.

We conducted three runs of each model and calculated the average MSE, RMSE, and MAE across the runs to provide a more accurate estimate of the model's performance. The LSTM model has a lower average MSE, RMSE, and MAE compared to the ARIMA model, indicating that it performs better in terms of prediction accuracy.

### Analysis

After conducting a thorough analysis of various time series models, we have determined that the LSTM model is the best option for predicting atmospheric duct interference (ADI) in 4G LTE networks.

The LSTM model has several advantages over other time series models, including its ability to capture long-term dependencies and its capability to learn from previous predictions, making it a powerful tool for forecasting ADI. By accurately forecasting ADI, we can dynamically adjust the guard period in the network, which can effectively mitigate the negative impact of ADI on the network's performance.

With this solution, we can provide a more efficient and reliable network for users, ultimately leading to improved customer satisfaction and retention. By reducing the impact of ADI on the network, we can ensure that users have a more consistent and reliable experience, which is crucial for maintaining their loyalty and trust in the network.

The implementation of the LSTM time series model and its integration into the network's operations represents a significant step forward in addressing the ADI problem in 4G LTE networks. With this solution, we can proactively identify and address ADI before it negatively affects the network's performance, ultimately leading to a more reliable and efficient network for all users.

## Conclusion

In this project, we explored the problem of atmospheric duct interference (ADI) in 4G LTE networks and proposed a solution to mitigate its negative impact on network performance. We compared the performance of two time series models, the ARIMA model and the LSTM model, and found that the LSTM model outperformed the ARIMA model in predicting ADI.

We then used the LSTM model to develop a methodology for dynamically adjusting the guard period in the network, which effectively mitigates the negative impact of ADI on network performance. Our results showed that this methodology can improve network reliability and provide a more consistent user experience.

Overall, our project provides a solution to a significant problem in 4G LTE networks and demonstrates the power of machine learning in addressing complex network problems. We hope that our work will inspire further research in this area and lead to even more innovative solutions for improving network performance and user experience.

<!-- ## Publications -->
[//]: # "Note: Uncomment each once you uploaded the files to the repository"

<!-- 1. [Semester 7 report](./) -->
<!-- 2. [Semester 7 slides](./) -->
<!-- 3. [Semester 8 report](./) -->
<!-- 4. [Semester 8 slides](./) -->
<!-- 5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./). -->


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/e16-4yp-Machine-Learning-based-Atmospheric-Duct-Interference-cancellation-in-TD-LTE-networks)
- [Project Page](https://cepdnaclk.github.io/e16-4yp-Machine-Learning-based-Atmospheric-Duct-Interference-cancellation-in-TD-LTE-networks/)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)
