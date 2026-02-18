hotctl eks context --profile integration  
  
kubectl run -i --tty --rm redis-cli --image=redis --restart=Never -- bash  

redis-cli -c -h notification-center-redis.50fvzs.clustercfg.use1.cache.amazonaws.com -p 6379