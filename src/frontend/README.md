This folder contains a static webpage that can be hosted in order to capture images for downstream processing.

During the original project, these files were put into an s3 bucket, and hosted via Cloudfront.

Of note, since the javascript uses secured APIs to capture location and camera data, the page has to be hosted in a secure way (such as https).

For the file to function, a backend lambda needs to be available in this part of the javascript to accept the data payload:
```javascript
    fetch('https://different-url-goes-here.lambda-url.us-east-1.on.aws/', {
        method:"PUT",
        body:payload
    })
```