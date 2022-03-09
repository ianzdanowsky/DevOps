Steps to setup Celery and Redis

# pip install Celery redis




# wget http://download.redis.io/redis-stable.tar.gz
# tar xvzf redis-stable.tar.gz
# cd redis-stable
# make




$ celery -A tasks worker --loglevel=info


Para usar o Memorystore do GCP, a VM precisa estar no iprange