
## Canais de Notificação

- [[PUSH]]
- [[HISTORY]]
- [[Email]]
- [[Profissional/Hotmart/Foundation Components/WhatsApp]]


## Cache : 

Usa o [[Redis]]

# Staging 

redis-cli -c -h notification-center-redis.gdlda0.ng.0001.use1.cache.amazonaws.com -p 6379

Limpar o cache especifico : 

redis-cli -c -h notification-center-redis.gdlda0.ng.0001.use1.cache.amazonaws.com -p 6379 --scan --pattern "*8fd815fb-3a33-4c51-b792-b60cd106d27d*" | xargs -L 100 redis-cli -c -h notification-center-redis.gdlda0.ng.0001.use1.cache.amazonaws.com -p 6379 DEL