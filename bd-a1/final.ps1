mkdir "./service-result"

# Copy files from container to local machine
docker cp container_name:/home/doc-bd-a1/res_dpre.csv service-result/
docker cp container_name:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp container_name:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp container_name:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp container_name:/home/doc-bd-a1/vis.png service-result/
docker cp container_name:/home/doc-bd-a1/k.txt service-result/

# Stop the container
docker stop container_name
