package com.university.lab4.formcraft.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        // Ця конфігурація дозволяє нашому фронтенду на localhost:3000
        // надсилати запити до нашого бекенду на localhost:8080
        registry.addMapping("/api/**") // Дозволити CORS для всіх шляхів, що починаються з /api/
                .allowedOrigins("http://localhost:3000") // Дозволити запити ТІЛЬКИ з цієї адреси
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS") // Які HTTP методи дозволено
                .allowedHeaders("*") // Які HTTP заголовки дозволено
                .allowCredentials(true);
    }
}