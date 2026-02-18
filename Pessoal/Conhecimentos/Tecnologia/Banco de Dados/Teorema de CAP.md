 O Teorema de CAP(Consistency Availability Partition Tolerance) é um princípio fundamental em sistemas distribuídos e [[Banco de dados]]. 
 
 Ele afirma que em um sistema distribuído, é impossível garantir simultaneamente Consistência, Disponibilidade e Tolerância a Partições.

- Consistência: Todos os nós em um sistema distribuído veem os mesmos dados ao mesmo tempo.
- Disponibilidade: Todos os nós em um sistema distribuído estão sempre disponíveis para processar solicitações.
- Tolerância a Partições: O sistema continua funcionando mesmo que haja falhas de comunicação entre os nós.

![[Teorema de CAP.png]]

De acordo com o Teorema de CAP, é possível garantir no máximo duas das três propriedades mencionadas acima. Por exemplo, se um sistema prioriza consistência e disponibilidade, pode sofrer com problemas de tolerância a partições. Da mesma forma, se prioriza disponibilidade e tolerância a partições, pode comprometer a consistência dos dados.

É importante considerar o Teorema de CAP ao projetar sistemas distribuídos e bancos de dados, pois ajuda a definir as prioridades e trade-offs necessários para atender às necessidades do sistema. 
