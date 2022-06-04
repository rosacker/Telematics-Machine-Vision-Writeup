# Telematics Context

Vehicle Telematics and the concept of "Usage Based Insurance" have become commonplace in the US Auto Insurance Industry over the past decade[^1][^2][^3]. The general idea with these programs is that policyholders agree to put a device in their car that monitors their operation of the vehicle, and in return they *generally*[^4] receive a reduction in premium. This is thought to be mutually beneficial because the insured has more agency in controlling the premium they are charged, and the insurer has more certainty around the risk they are assuming for an individual policy.

[^1]: https://www.statefarm.com/insurance/auto/discounts/drive-safe-save
[^2]: https://www.progressive.com/auto/discounts/snapshot/
[^3]: https://www.geico.com/driveeasy/getting-started/
[^4]: Some programs such as Progressive's Snapshot Program do not insure a discount.

The key part of these systems is the device which captures driver behavior. Traditionally, a freestanding/autonomous device was placed in the vehicle with sensors such as a GPS, an accelerometer and ways to communicate the data back to a central server. Over time, insurers have looked to reduce the cost of these devices. This generally comes in the form of smaller bluetooth enabled devices which connect to the policyholder's smartphone, or some insurers simply just use a smartphone app with no additional technology required.[^5]

[^5]: https://www.casact.org/sites/default/files/2021-03/6U_NAIC_Telematics.pdf

These systems generally focus on data which can be captured using devices traditionally found on a smartphone (GPS, Accelerometer, Compass, etc...). With these sensors, it is possible to track events such as "hard braking", "fast acceleration", "hard turning", "over the speed limit". This data has a much more direct relationship to a policyholder's risk than some traditional rating variables such as location and credit report data which has a great appeal for public opinion. Some insurers have even promised to discontinue use of data such as credit reports[^6] because they feel that telematics data is more appropriate.

[^6]: https://www.caranddriver.com/news/a33555840/root-auto-insurance-credit-scores-racism/

There is one additional device on smartphones which till now has not been broadly used for vehicle telematics: the camera. While much of the data captured through telematics has a meaningful causal relationship with insurance risk (i.e. It makes sense that hard braking events would relate to crashes), they are still somewhat of a proxy. There are totally valid reasons to have hard braking events in a car, and simply treating all of them as equal does not seem optimal. Where a camera could expand vehicle telematics is giving additional context around these more traditional events. If the accelerometer detects a hard braking event, can that be correlated with the driver waiting till the last minute to avoid rear ending someone, or was it because someone else ran a red light? Those two stories both had the potential to end in a crash, but "fault" is something that can only really be assessed when machine vision is incorporated into the solution.
