#!/usr/bin/env bash
curl -X POST -is -u "${BITBUCKET_PIPELINE_USERNAME}:${BITBUCKET_PIPELINE_APP_PASSWORD}" \
-H 'Content-Type: application/json' \
"https://api.bitbucket.org/2.0/repositories/${BITBUCKET_PIPELINE_REPO}/pipelines/" \
-d '
{
    "target": {
        "ref_type": "branch",
        "type": "pipeline_ref_target",
        "ref_name": "master",
        "selector": {
            "type": "branches",
            "pattern":"master"
        }
    }
}'