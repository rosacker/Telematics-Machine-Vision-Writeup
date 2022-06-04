# Road Test

To finish this project, a "road test" was conducted by deploying the solution to an edge-computer (an AWS DeepLens), and driving the camera around Bloomington, IL for approximately 30 minutes.

## Trip Path

WIP

## Trip Analysis

### Time Series of a Trip

<iframe src="../images/timeseries_weather.html" height="500px" width="1300px"></iframe>

This time series shows the models confidence over the duration of a 30 minute drive taken at approximately 7 PM on an early summer night. The model clearly lost confidence when entering a downtown region of the city where the skyline blocked its view of the sun. Additionally, the model's confidence changed materially when the trip faced Southwards on a wide-open stretch of road.
