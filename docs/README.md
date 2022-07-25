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

## Methodology

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
