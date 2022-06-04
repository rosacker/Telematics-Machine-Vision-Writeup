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

The model was trained using the BDD100k dataset [as described previously](../Dataset.md). This dataset has approximetly 70,000 training images and 10,000 validation images.

Images were resized down to 224 x 224 pixels in order to align with the Sagemaker Image Classification container.

The dataset was highly imbalanced initially. As shown below, data was down-sampled for training. Validation statistics reported further down are based upon the original validation dataset.

|    Level    | Original Count | Down Sample Rate | Final Count |
| :---------: | :------------: | :--------------: | ----------- |
| city street |     43,516     |       25%        | 10,820      |
|   highway   |     17,379     |       50%        | 8,620       |
| residential |      8074      |       100%       | 8,074       |
|  undefined  |      894       |       100%       | 894         |
|    Total    |     69,863     |      40.7%       | 28,408      |

## Model Architecture

WIP - Rewrite architecture

The model was trained using the [AWS Sagemaker Image Classification](https://docs.aws.amazon.com/sagemaker/latest/dg/image-classification.html) container. The model is trained using MXNet, it is a convolutional neural network. Beyond that, the AWS user documentation unfortunately does not give a ton of details on the architecture built behind the scenes. Below are the key hyperparameters that were selected:

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

WIP - rewrite performance

Overall the performance of the model appears to be fairly good with a 92% accuracy on validation. However, the model appears to struggle with the "Dawn/Dusk" class (often labeling it as "daytime" instead). In part, I assume this is due to the ambiguity of how "Dawn/Dusk" was defined during labeling.

### F1 Score

WIP rewrite F-scores

|              | precision | recall | f1-score | support |
| :----------: | :-------: | :----: | -------- | ------- |
|  dawn/dusk   |   0.57    |  0.53  | 0.55     | 778     |
|   daytime    |   0.93    |  0.94  | 0.94     | 5258    |
|    night     |   0.98    |  0.98  | 0.98     | 3929    |
|  undefined   |   0.74    |  0.57  | 0.65     | 35      |
|              |           |        |          |         |
|   accuracy   |           |        | 0.92     | 10000   |
|  macro avg   |   0.80    |  0.75  | 0.78     | 10000   |
| weighted avg |   0.92    |  0.92  | 0.92     | 10000   |

### Confusion Matrix

![](images/weather-confusion-matrix.PNG)

## Future Enhancements

WIP rewrite performance

The model trained on the BDD100k dataset does not exactly meet the intended use of that data. Teaching autonomous vehicles to drive isn't directly in line with my intended use (identifying risks to a *human* driver). While it was good enough for a school project, future research should look to collect a different dataset more in line with this use case. A big gap applicable to this "time of day" model was the definitions of daytime/dusk/night were inconsistent between photos. A better dataset for this purpose would likely have a numeric target like "hours till sunset" which is more objective.

Additionally, looking to rebuild the model in a different tool stack would likely be good. The AWS Sagemaker Image Classification container was used as a learning opportunity, but the lack of control I had over the model was limiting. The model was prone to overfitting, and that sagemaker container does not give many options for a data scientist to mitigate those issues.

## Appendix

### Model Interpretation

WIP - rewrite shapley

Below is an example image from each class where the model was highly confident in the correct label. When reading these images, a blue region means that it contributed to the confidence, and a red region means it detracted from the confidence.  

+ [Day](images/timeofday-daytime-shap.jpeg)
+ [Dawn/Dusk](images/timeofday-dusk-shap.jpeg)
+ [Night](images/timeofday-night-shap.jpeg)
+ [Undefined](images/timeofday-undefined-shap.jpeg)
