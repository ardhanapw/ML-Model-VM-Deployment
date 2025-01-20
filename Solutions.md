
# Solutions

1.	Brief explanations for question 1-6:
-	I utilized the YOLOv11n model
-	The python code that I wrote accepts an input image, then returns that image with bounding boxes, each with their classes and prediction confidence
-	I created the Dockerfile that install dependencies of the code and ran it. The Docker Image is built on Google Cloud Build.
-	The Docker Image can be ran either on CPU or GPU. I imported ‘Ultralytics’ module on my python code, the library automatically adjusts the model inference settings based on available device.
-	I chose GCP to deploy the Docker image. To automate the deployment of the Docker image, open Cloud Build, then connect a source code repository. Create a Cloud Build trigger that’s invoked by an event (i.e. new pushed commit), and select the connected repository and one of its branch as event source. On the repository, create a cloudbuild.yaml file containing all the build steps needed to create the Compute Engine VM and deploy the Docker Image on it.
2.	I use python 3.11 slim base image on building the Docker Image. Other base images are supported as long as they’re meeting the system requirements of the  ‘Ultralytics’ module.

3.	Here are the steps to test whether the solution works correctly and efficiently:
-	Access the Compute Engine VM within a browser
-	The main.py saves the annotated .jpg at the /output directory. Run the Docker Image within the VM, with writable directory on the VM mounted into the container. 
```
docker run -v /path/to/writable/dir:/app/output IMAGE_NAME
```
-	See if the output .jpg is generated at the mounted directory
-	Download and inspect the output .jpg

4.	If GPU utilization for PyTorch inference is not needed yet, we can reduce the Docker Image size by installing CPU-only PyTorch. 
