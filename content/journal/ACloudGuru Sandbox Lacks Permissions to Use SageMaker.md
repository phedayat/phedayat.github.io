---
title: ACloudGuru Sandbox Lacks Permissions To Use AWS SageMaker
date: "2023-11-27"
---

If you've ever tried to use AWS SageMaker in the AWS sandbox environment provided by [ACloudGuru](https://www.pluralsight.com/cloud-guru), then you've probably run into these errors:
```
user/cloud_user is not authorized to perform: sagemaker:ListEndpoints because no identity-based policy allows the sagemaker:ListEndpoints action
```

```
user/cloud_user is not authorized to perform: sagemaker:ListModels because no identity-based policy allows the sagemaker:ListModels action
```

```
user/cloud_user is not authorized to perform: sagemaker:ListNotebookInstances because no identity-based policy allows the sagemaker:ListNotebookInstances action
```

```
user/cloud_user is not authorized to perform: sagemaker:ListTrainingJobs because no identity-based policy allows the sagemaker:ListTrainingJobs action
```

Or this one when ignoring the earlier errors and still attempting to create a notebook instance:
```
user/cloud_user is not authorized to perform: sagemaker:CreateNotebookInstance
```

These errors are telling us that we lack permissions to do pretty much everything in SageMaker; makes sense to head into IAM and add the policies.

Navigating to IAM then Users reveals our user, `cloud_user`. Here we can check the policies that we're allotted in a sandbox environment. In particular, we're assigned two policies: `allow_all` and `Playground_AWS_Sandbox`. The latter is for denying access to particular EC2 AMIs; the former is what governs our access in AWS.

A quick look at the JSON reveals the issue:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAllPermissions",
            "Effect": "Allow",
            "NotAction": [
                "lightsail:*",
                "sagemaker:*"
            ],
            "Resource": "*"
        }
    ]
}
```

The key `NotAction` is an IAM JSON policy element [that's equivalent to saying "all resources *except* these"](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_notaction.html). In particular, the policy assigned to us excludes exactly the AWS service we need to complete the demos in the AWS ML Specialty.

Attempting to edit the policy proves fruitless, as we're faced with this error:
```
user/cloud_user is not authorized to perform: iam:CreatePolicyVersion
```

Through the forums, I've found our answer: [SageMaker *was never supported*, due to the cost](https://acloud.guru/forums/aws-certified-machine-learning-specialty/discussion/-Mg7pL4c7KK4V5ufifVX/how-to-get-around-explicit-deny-for-sagemakercreatetrainingjob?answer=-MjAFPqn0gxj4ZosMzTz). Luckily, we can still use SageMaker via the labs; to follow along with the demos, you have to run the risk of incurring possible charges on your AWS account. Proceed with caution.