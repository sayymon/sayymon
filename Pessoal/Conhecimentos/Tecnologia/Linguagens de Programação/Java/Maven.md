
Aumentar memoria de execucao do maven 

MAVEN_OPTS="-Xmx2g -Xms512m" mvn clean install 

Rodar ignorando os certificados : 

mvn clean install -Dmaven.wagon.http.ssl.insecure=true -Dmaven.wagon.http.ssl.allowall=true

Na Hotmart tem essa tretinha com o repo : 

https://repo1.maven.org/maven2/

Que precisa ajustar no settings.xml o seguinte : 

De : 

                <repository>
                    <snapshots/>
                    <id>central2</id>
                    <name>maven-central2</name>
                    <url>https://maven.ceon.pl/artifactory/repo/</url>
                </repository>

Para : 

                <repository>
                    <snapshots/>
                    <id>central2</id>
                    <name>maven-central2</name>
                    <url>https://repo1.maven.org/maven2/</url>
                </repository>   

