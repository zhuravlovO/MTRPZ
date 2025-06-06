package com.example.cat_repeater;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@ComponentScan(basePackages = {"com.example.cat_repeater"}) 
public class CatRepeaterApplication {

    public static void main(String[] args) {
        SpringApplication.run(CatRepeaterApplication.class, args);
    }

}