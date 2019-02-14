# djangoToAWS

We can upload video from url:
http://127.0.0.1:8000/upload/


uploaded video at s3 bucket : media-file-upload-2



 Policies can be retrieved from
 http://127.0.0.1:8000/api/files/policy/
 
 
 with 
 Media type: application/json
 Json :  { "filename": "9.mp4" }
 
 
 I have removed the credentials so this will fail,
 but for the correct credentials and permissions
 this should work.
 

