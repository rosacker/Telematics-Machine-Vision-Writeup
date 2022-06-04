# Weather Classifier

WIP - Update Image
![](images/weather_demo.gif)

## Purpose  

WIP - Rewrite Purpose
The purpose of this model is to detect the light level (a.k.a. time of day) that the driver has vision of. The motivation here being that dawn/dusk is known to be the most risky time of day to drive. [^1] Potentially time of day could be approximated by just using a clock, but the relationship is not that simple.

[^1]: WIP - Citation Needed

> Light Level ~ Clock Time + Timezone + Geographic Position + Vehicle Heading + etc...

Using machine vision to visually assess "is the sun rising/setting in front of me right now?" is seemingly simpler than trying to think through all of that complexity.

The proposed model takes a single 3 x 224 x 224 image as input, and outputs probability of 4 classes:  
  
1) Day  
2) Dawn/Dust  
3) Night  
4) Undefined  
  
In practice, the Undefined class is almost never used in the training data. It is mostly reserved for totally artificial environments such as a tunnel where no daylight is visible in the photo.

## Data Considerations

WIP - Rewrite Data Considerations
WIP - Add considerations around classes that were binned

The model was trained using the BDD100k dataset [as described previously](../Dataset.md). This dataset has approximately 70,000 training images and 10,000 validation images.

Images were resized down to 224 x 224 pixels in order to align with the Sagemaker Image Classification container.

The dataset was highly imbalanced initially. As shown below, data was down-sampled for training. Validation statistics reported further down are based upon the original validation dataset.

|     Level     | Original Count | Down Sample Rate | Final Count |
| :-----------: | :------------: | :--------------: | ----------- |
|     Clear     |     37,344     |       15%        | 5,518       |
| Partly Cloudy |     4,881      |       100%       | 4,881       |
|   Overcast    |     8,770      |       75%        | 6,554       |
|     Rainy     |     5,070      |       100%       | 5,070       |
|     Snowy     |     5,549      |       100%       | 5,549       |
|   Undefined   |     8,249      |       75%        | 6,202       |
|     Total     |     69,863     |      48.3%       | 33,774      |

## Model Architecture

The model was trained using the [AWS Sagemaker Image Classification](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification.html) container. The model is trained using MXNet, it is a convolutional neural network. Beyond that, the AWS user documentation unfortunately does not give a ton of details on the architecture built behind the scenes. A raw visualization of the architecture exported from Sagemaker [can be found here](images/model_arch-weather.svg). It appears to match the ResNet architecture[^2] terminating with a 6-node classification head.

[^2]: [ResNet Architecture Paper](https://arxiv.org/abs/1512.03385)

Below are the key hyperparameters that were selected:

| Hyperparameter     | Value         | Notes                                                                                                             |
| ------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------- |
| Epochs             | 6             |                                                                                                                   |
| Pretrained Weights | 1             | AWS provides weights pretrained on the ImageNet with 11,000 categories                                            |
| Image Size         | 3 x 224 x 224 | Pretrained weights are only supported at this image size                                                          |
| Layers             | 18            | The minimum supported layer count. The model did show elements of overfitting even at this restricted layer count |
| Optimizer          | Adam          |                                                                                                                   |
| Learning Rate      | 0.001         |                                                                                                                   |
| Mini Batch Size    | 16            |                                                                                                                   |

## Performance

Overall the performance of the model appears to be middle of the road with a 67% accuracy on validation. In general, the model's accuracy seems to be impacted by the fuzzy line between classes: at what point does a cloudy sky become "rainy"? In reviewing mis-classification examples, commonly the ground-truth label was unclear. For example, an image of clear weather sky, but a small amount of snow on the side of the road was labeled "snowy". While that label is not objectively wrong, I think reasonable minds would agree with the models label of "clear" as well.

### F1 Score

|               | precision | recall | f1-score | support |
| :-----------: | :-------: | :----: | -------- | ------- |
|     Clear     |   0.92    |  0.79  | 0.85     | 5346    |
| Partly Cloudy |   0.46    |  0.74  | 0.57     | 738     |
|   Overcast    |   0.58    |  0.64  | 0.61     | 1239    |
|     Rainy     |   0.66    |  0.66  | 0.66     | 738     |
|     Snowy     |   0.78    |  0.59  | 0.67     | 769     |
|   Undefined   |   0.58    |  0.75  | 0.65     | 1170    |
|               |           |        |          |         |
|   accuracy    |   0.74    | 10000  | 0.67     | 10000   |
|   macro avg   |   0.66    |  0.70  | 0.67     | 10000   |
| weighted avg  |   0.77    |  0.74  | 0.75     | 10000   |

### Confusion Matrix

![](images/weather-confusion-matrix.PNG)

## Future Enhancements

WIP rewrite performance

The model trained on the BDD100k dataset does not exactly meet the intended use of that data. Teaching autonomous vehicles to drive isn't directly in line with my intended use (identifying risks to a *human* driver). While it was good enough for a school project, future research should look to collect a different dataset more in line with this use case. A big gap applicable to this "time of day" model was the definitions of daytime/dusk/night were inconsistent between photos. A better dataset for this purpose would likely have a numeric target like "hours till sunset" which is more objective.

Additionally, looking to rebuild the model in a different tool stack would likely be good. The AWS Sagemaker Image Classification container was used as a learning opportunity, but the lack of control I had over the model was limiting. The model was prone to overfitting, and that sagemaker container does not give many options for a data scientist to mitigate those issues.

## Appendix

### Model Interpretation

Below is an example image from each class where the model was highly confident in the correct label. When reading these images, a blue region means that it contributed to the confidence, and a red region means it detracted from the confidence.  

+ [Clear Day](images/weather-clear-shap.jpeg)
+ [Partly Cloudy](images/weather-partlycloudy-shap.jpeg)
+ [Overcast](images/weather-overcast-shap.jpeg)
+ [Rainy](images/weather-rainy-shap.jpeg)
+ [Snowy](images/weather-snowy-shap.jpeg)
+ [Undefined](images/weather-undefined-shap.jpeg)
