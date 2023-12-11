#  Introduction


# Assignment Configuration

Students will need to do a few things in order to complete this assignment succesfully. 

1. Enable Cloud Build, Cloud Run and Artifact Registry services in Google Cloud Console. 

2. Open your cloud console and run the following commands:

```
PROJECT_ID=$(gcloud config list --format='value(core.project)')
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')
```

3. Grant the Cloud Run Admin role to the Cloud Build service account:

```
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
    --role=roles/run.admin
```


4. Grant the IAM Service Account User role to the Cloud Build service account for the Cloud Run runtime service account:

```
gcloud iam service-accounts add-iam-policy-binding \
    $PROJECT_NUMBER-compute@developer.gserviceaccount.com \
    --member=serviceAccount:$PROJECT_NUMBER@cloudbuild.gserviceaccount.com \
    --role=roles/iam.serviceAccountUser
```
# Building Your Containers

Step 1: Create a Repository in your Artifact Registry. <br>
**Note: You will need to use your project ID and specific region for this command. This is an example. We are creting a repo in us-west2 and calling the Repository "quickstart-docker-repo"**

```
gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker \
    --location=us-west2 --description="Docker repository"
```

Step 2: Verify that the Repository was created in Artifact Registry

```
gcloud artifacts repositories list
```

Step 3: Build your container using your config file: 

Once you createt your cloudbuild.yaml file, you can test that it is configured correctly by using the following commmand or similar: 

```
gcloud builds submit --region=us-west2 --config cloudbuild.yaml
```

### Hints

Use the following command in your terminal to find your proejct ID:

```
gcloud config get-value project
```

