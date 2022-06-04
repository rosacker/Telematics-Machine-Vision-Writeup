This lambda function was used to resize images to the right resolution for the image classification container.

Be warned that PIL is not bundled in lambda environments by default.

A layer was bundled with the lambda to resolve this: `arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p38-Pillow:3`