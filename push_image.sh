docker-compose build
docker tag pixelmixer-nlp_pixelmixer-nlp 031858794960.dkr.ecr.us-west-1.amazonaws.com/pixelmixer-nlp
aws ecr get-login-password | docker login --username AWS --password-stdin  031858794960.dkr.ecr.us-west-1.amazonaws.com 
docker push 031858794960.dkr.ecr.us-west-1.amazonaws.com/pixelmixer-nlp
