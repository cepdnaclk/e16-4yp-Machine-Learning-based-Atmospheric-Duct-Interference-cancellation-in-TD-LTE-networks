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

1. [Abstract](#abstract)
2. [Related works](#related-works)
3. [Methodology](#methodology)
4. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
5. [Results and Analysis](#results-and-analysis)
6. [Conclusion](#conclusion)
7. [Publications](#publications)
8. [Links](#links)

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
* Find a suitable data sets for the ML models
* Implement several predictive models and using performance metrics choose the best model.
* Study TD-LTE networks and find a solution how to minimize the ADI based on the results from the predictive model
* Implement that solution via machine learning

> **MATLAB - LTE Toolbox**  
> 1. Simulate, analyze, and test the physical layer of LTE wireless communications systems
> 2. Provides standard-compliant functions and apps for the design, simulation, and verification of LTE communications systems
> 3. Build test models and reference measurement channels (RMC) for LTE waveforms.



## Experiment Setup and Implementation

## Results and Analysis

## Conclusion

## Publications
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
