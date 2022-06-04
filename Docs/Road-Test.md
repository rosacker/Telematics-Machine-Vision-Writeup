# Road Test

To finish this project, a "road test" was conducted by accessing the front-end website on a smart phone and driving around Bloomington, IL for approximately 30 minutes.

## Trip Path

<iframe src="../images/general_map.html" height="1300px" width="1300px"></iframe>

The trip went through a variety of different portions of Bloomington. This includes single family houses, dense historic residential areas, the downtown area, a few major roads, and a brief trip on the highway. The trip was conducted approximately an hour before sunset on a day with light cloud coverage.

## Trip Analysis

### Intersection Map

<iframe src="../images/intersection_map.html" height="1300px" width="1300px"></iframe>

This map shows the intersections observed during the road test. Generally the system seems to have done well at identifying major intersections with stop lights, but often misses 3-way or uncontrolled intersections. Additionally, there appear to be multiple detections for the same intersection while approaching. A system would need to be created to prevent this in the future.


### Time Series of a Trip

<iframe src="../images/timeseries_weather.html" height="500px" width="1300px"></iframe>

This time series shows the models confidence over the duration of a 30 minute drive taken at approximately 7 PM on an early summer night. The model clearly lost confidence when entering a downtown region of the city where the skyline blocked its view of the sun. Additionally, the model's confidence changed materially when the trip faced Southwards on a wide-open stretch of road.


WIP - Add more trip analysis