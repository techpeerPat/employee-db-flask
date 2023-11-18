#  Introduction
This is an example of a completed assignment for Unit 5 of the SDS course for Tech Exchange. 

The application is a simple employee database. It is not connected to a database. The app uses the Faker library to mock employee data. 

The app uses builds a docker container and deploys that container using Cloud Run. 

You can see the live app here: [Employee DB](https://employee-db2-in5i5wkqaa-uc.a.run.app/). 

The app also has a Cloud Build Trigger configured that deploys the app each time code is pushed to a 'staging' branch in a Github repo. 

## Assignment Details and Ideas

1. Supply the studetns with the wroking code and Dockerfile. The main focus should be on building the cloudbuild.yaml file. 

2. Students should create the cloudbuild file that builds a container, saving it to artifact registry and then deploys to Cloud Run. Students can submit the link to the working application

### Stretch Goal Ideas

1. Students can create a trigger in Cloud Build that deploys the app when code is pushed to a repo. 

2. Students can implement testing and use Github Actions to run tests when code is pushed to a repo. 

# Assignment Configuration

You will need to do a few things in order to complete this assignment. 

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


