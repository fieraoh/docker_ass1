mkdir "./service-result" -Force

$containerName = "bd-container"

docker cp "${containerName}:/home/doc-bd-a1/res_dpre.csv" 'service-result/'
docker cp "${containerName}:/home/doc-bd-a1/eda-in-1.txt" 'service-result/'
docker cp "${containerName}:/home/doc-bd-a1/eda-in-2.txt" 'service-result/'
docker cp "${containerName}:/home/doc-bd-a1/eda-in-3.txt" 'service-result/'
docker cp "${containerName}:/home/doc-bd-a1/vis.png" 'service-result/'
docker cp "${containerName}:/home/doc-bd-a1/k.txt" 'service-result/'

# Stop and remove the docker container
docker stop $containerName
docker rm $containerName

Write-Host "Files copied and container removed successfully."
