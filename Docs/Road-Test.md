# Road Test

To finish this project, a "road test" was conducted by accessing the front-end website on a smart phone and driving around Bloomington, IL for approximately 30 minutes.

## Trip Path

<iframe src="../images/general_map.html" height="1300px" width="1300px"></iframe>

The trip went through a variety of different portions of Bloomington. This includes single family houses, dense historic residential areas, the downtown area, a few major roads, and a brief trip on the highway. The trip was conducted approximately an hour before sunset on a day with light cloud coverage.

## Trip Analysis

### Weather Model Performance

![](Models/images/weather_demo.gif)

The model appeared to do a fairly good job at detecting the clear/partially cloudy weather throughout the trip. Notably, it seems to fail in very sunny photos where the color of the sky gets washed out.

#### Time Series

Below shows a time series of the weather model's output throughout the trip. The model clearly lost confidence when entering a downtown region of the city where the skyline blocked its view of the sun. Additionally, the model's confidence changed materially when the trip faced Southwards on a wide-open stretch of road.

<iframe src="../images/timeseries_weather.html" height="500px" width="1300px"></iframe>

### Street Category Performance

![](Models/images/scene_demo.gif)

The model seems to have a large number of false positives for the "highway" class. As called out on the [Dataset](Dataset.md) page, the training dataset appears to have a bias towards major city driving. A theory for this overuse of the "highway" class would be that the model is picking up on the open space in a smaller town, and it associates open space with highways.

### Time of Day Performance

![](Models/images/timeofday_demo.gif)

#### Time Series

Below shows a time series of the time of day model's output throughout the trip. The model clearly changed its prediction when entering the downtown area. This appears to be related to the tall buildings blockings it's view of the setting sun.

<iframe src="../images/timeseries_daytime.html" height="500px" width="1300px"></iframe>

### Rekognition Performance

![](images/number_of_cars_demo.gif)

The Rekognition portion of the system appears to do well at identifying cars, stop lights and intersections. The only pitfall noticed was the system does not identify objects far in the distance. While this may be what is desired (a car 500 feet in front of you likely doesn’t affect your driving), the inability to control this falloff was a disappointment.  

#### Intersection Map

This map shows the intersections observed during the road test. Generally the system seems to have done well at identifying major intersections with stop lights, but often misses 3-way or uncontrolled intersections. Additionally, there appear to be multiple detections for the same intersection while approaching. A system would need to be created to prevent this in the future.

<iframe src="../images/intersection_map.html" height="1300px" width="1300px"></iframe>
