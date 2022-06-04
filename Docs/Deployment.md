# Architecture

The majority of this solution was deployed using AWS Sagemaker and AWS Rekognition along with standard AWS services such as Lambda, Step Functions, DynamoDB.

<object data="../images/AWS-Architecture.pdf" type="application/pdf" style="height:650px;width:100%"></object>

## Synchronous Trip Data Capture

The first half of this system focuses on the capture of driver data. A small website was developed ([source code](https://github.com/rosacker/Telematics-Machine-Vision-Writeup/tree/master/src/frontend)) that a user can access with their Smartphone. When the user starts a "trip", images and GPS data are automatically captured every 5 seconds. This data is sent to an API which saves the photo and associated metadata for future processing.

Visualized below are a series of photos captured through this system at 5 second intervals and 480p resolution.

![](images/data_capture_demo.gif)

## Asynchronous Trip Summary Pipeline

As a batch process, trip data is processed through a machine vision pipeline. When triggered, the batch process hosts the 3 sagemaker models discussed in the "Models" section of this book on Sagemaker Endpoints. The pipeline then loops through each unique trip id, and grabs all of the associated image URLs from a DynamoDB database. Each image is then processed through a Lambda which invokes the Sagemaker Endpoints as well as the Rekognition `detect_labels` API. The model detections are then stored in another DynamoDB database for downstream use. Finally, the sagemaker endpoints are shut down once all trips have been processed.

The backend source code can be [found here](https://github.com/rosacker/Telematics-Machine-Vision-Writeup/tree/master/src/backend)

## Future Enhancements

### Scale

The system build for this project works well for small-medium scale. However, for a major insurance company to use it, there would likely need to be some hardening done on the batch pipeline. One service to look into would be AWS Kinesis which may provide better scalability when processing potentially millions of images daily.

### Security

The initial system does not have user identify or user authentication implemented. Implementing a service such as AWS Cognito would be needed in order to make this production grade.

### User Data Limits

This system sends one 480p image every 5 seconds from a user's smartphone. That equates to approximately. Given that the average American spends ~50 minutes driving per day[^1], that would equate to about 18 GB captured per person, per month. This could cause significant issues for user data caps and battery life. Additional tuning would be needed to determine if a lower resolution, lower frequency option for data capture would be acceptable. Alternatively, looking for ways to run the models on the user device (such as Tensorflow.js) would likely reduce data use (though increase battery use).

[^1]: Source - [Link](https://aaafoundation.org/wp-content/uploads/2018/02/18-0019_AAAFTS-ADS-Research-Brief.pdf)
