___
# <div align="center">Machine Learning based Atmospheric Duct Interference cancellation in TD-LTE networks</div>
___

## **Aim**
$\qquad$ The aim of the project is to find a method to overcome the problem which is caused by the atmospheric duct to TD-LTE networks. In order to do that we are aiming to build two ML-based models which can predict the duct interference and the other one to minimize such interference.


## **Introduction**

$\qquad$ Atmospheric ducts are horizontal layers that happen under certain weather conditions in the lower atmosphere. Radio signals guided in the atmospheric duct tend to experience less attenuation and spread further, i.e.hundreds of kilometers. In a large-scale deployed TD-LTE network, atmospheric ducts make faraway downlink (DL) wireless signals propagate beyond the designed protection distance and interfere with local uplink (UL) signals, thus causing severe outage probability. TDD mobile networks are impacted by two types of ducting interference.  

> 1. **External Interference:** This type of interference is caused by the long-distance transmission from nearby country DL signals which will interfere with UL slots of the local TDD network.
> 2. **Internal interference:** This type of interference is caused by long-distance transmission DL signals which will interfere with UL slots within the operators’ network.  

$\qquad$ In TD-LTE, there exist three kinds of subframes: uplink, downlink, and special sub-frames. The special sub-frame consists of three parts: DwPTS (Downlink Pilot Time Slot), GP (Guard Period), and UpPTS (Uplink Pilot Time Slot). Moreover, the GP is located at the moment when downlink converts to uplink to prevent interference from downlink signals to uplink signals. Under normal circumstances, any downlink signals from distant BSs beyond the maximum protection distance would experience enough attenuation and hardly interfere with the local uplink signals. But with ADI (Atmospheric Duct Interference)  present, this protection does not work. So as a solution we need to build a model which can predict the ADI and as the next step a method to minimize it like dynamically adjusting the GP.  

## **Expected Outcomes**

The outcome of the project is to achieve the following,  
> 1. Predict atmospheric duct interference via machine learning  
> 2. Provide a machine learning-based solution to minimize such interference
