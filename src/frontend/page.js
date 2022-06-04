let camera_button = document.querySelector("#start-trip-sensors");
let video = document.querySelector("#video");
let click_button = document.querySelector("#start-trip");
let canvas = document.querySelector("#canvas");
let dataurl = document.querySelector("#dataurl");
let dataurl_container = document.querySelector("#dataurl-container");
let my_location = null;
let trip_uuid = crypto.randomUUID();

let counter = document.querySelector("#sent-images")
let count = 0;

function showPosition(position) {
    my_location = position;
  }

function error(err) {
    console.warn(`ERROR(${err.code}): ${err.message}`);
  }

camera_button.addEventListener('click', async function() {
   	let stream = null;

    try {
        my_location = navigator.geolocation.watchPosition(showPosition, error, {enableHighAccuracy: true, maximumAge: 0});
    	stream = await navigator.mediaDevices.getUserMedia({ video: {facingMode: "environment" }, audio: false });
        
    }
    catch(error) {
    	alert(error.message);
    	return;
    }

    video.srcObject = stream;
    video.play();
    video.style.display = 'block';
    camera_button.style.display = 'none';

    cycle_Picture();
    setInterval(cycle_Picture, 5000);   
});

function cycle_Picture() {
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    let image_data_url = canvas.toDataURL('image/jpeg');
    const data = image_data_url.replace(/^data:image\/\w+;base64,/, "");

    const payload = JSON.stringify(
        {trip_id: trip_uuid,
         lat: my_location.coords.latitude,
         long: my_location.coords.longitude,
         accuracy: my_location.coords.accuracy,
         speed: my_location.coords.speed,
         timestamp: my_location.timestamp,
         image: data
        });

    fetch('https://different-url-goes-here.lambda-url.us-east-1.on.aws/', {
        method:"PUT",
        body:payload
    })
    
    count++;
    counter.innerHTML = "Images Uploaded: " + count;
   }

