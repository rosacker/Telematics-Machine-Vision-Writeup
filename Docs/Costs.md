# Project Costs

## Model Training Costs

The training dataset for each model was approximately 70,000 images with an additional 10,000 held out for validation.

Using AWS Rekognition, the costs to train these models was as follows:

|         Model         | Training Images | Training Cost |
|:---------------------:|:---------------:|---------------|
|  Stop Light Detection |       WIP       | WIP           |
|    Street Category    |       WIP       | WIP           |
| Time of Day Detection |       WIP       | WIP           |
|   Weather Detection   |       WIP       | WIP           |
| Road Object Detection |       WIP       | WIP           |

While this cost might be material for a hobbyist project, for a corporation, this cost is significantly cheaper than the Data Scientist cost to train a similar performance set of models.

## Live Runtime Costs

The majority of this architecture is serverless which means costs were fairly low while setting up the process. At scale, each image costs approximately $X (WIP) to process.

That breaks down as follows:  

|        Service       | Cost |
|:--------------------:|:----:|
|      API Gateway     |  WIP |
|      AWS Lambda      |  WIP |
|  Sagemaker Endpoint  |  WIP |
| Rekognition Endpoint |  WIP |
|    DynamoDB Table    |  WIP |
