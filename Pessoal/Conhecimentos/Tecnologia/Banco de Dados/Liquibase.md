
Desbloquear tabela quando o Liquibase por algum motivo não executou corretamente :
```sql
UPDATE DATABASECHANGELOGLOCK SET LOCKED = FALSE, LOCKGRANTED = NULL, LOCKEDBY = NULL WHERE ID = 1;
```