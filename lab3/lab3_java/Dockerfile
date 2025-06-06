FROM eclipse-temurin:21-jre-alpine

WORKDIR /app

COPY target/cat-repeater-0.0.1-SNAPSHOT.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-Xmx256m", "-Xss256k", "-jar", "app.jar"]