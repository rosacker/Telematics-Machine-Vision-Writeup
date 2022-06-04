This lambda function is used to look through the sagemaker models and rekognition api to get all of the machine vision detections we're interested in.

The `rekog_label_targets.json` is used to filter all of the detections rekognition gives down to the ones we care about. In practice, many of these labels don't seem to trigger often.
