package com.example.cat_repeater; // Або com.example.cat_repeater.config

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
// Якщо потрібні інші налаштування, їх можна додати тут
// import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;

@Configuration
@EnableWebMvc // <--- Спробуй додати цю анотацію
public class WebConfig implements WebMvcConfigurer {

    // Ти можеш залишити цей клас порожнім, або додати сюди специфічні веб-налаштування, якщо потрібно.
    // Наприклад, для простого перенаправлення:
    // @Override
    // public void addViewControllers(ViewControllerRegistry registry) {
    //     registry.addViewController("/").setViewName("index"); // Це вже робить твій контролер, але для прикладу
    // }

    // Нам важливо, щоб Spring "побачив" цей конфігураційний клас і застосував @EnableWebMvc
}