package com.university.lab4.formcraft.controller;

import com.university.lab4.formcraft.model.Survey;
import com.university.lab4.formcraft.service.SurveyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController // Поєднує @Controller та @ResponseBody. Каже Spring, що методи повертатимуть JSON
@RequestMapping("/api/surveys") // Всі запити до цього контролера будуть починатися з /api/surveys
public class SurveyController {

    private final SurveyService surveyService;

    @Autowired
    public SurveyController(SurveyService surveyService) {
        this.surveyService = surveyService;
    }

    // Цей метод буде обробляти POST-запити на адресу /api/surveys
    @PostMapping
    public ResponseEntity<Survey> createSurvey(@RequestBody Survey survey) {
        // @RequestBody говорить Spring взяти JSON з тіла запиту і перетворити його на об'єкт Survey

        Survey createdSurvey = surveyService.createSurvey(survey);

        // Повертаємо створений об'єкт та HTTP статус 201 (Created)
        return new ResponseEntity<>(createdSurvey, HttpStatus.CREATED);
    }
    @GetMapping("/{uniqueLink}")

    public ResponseEntity<Survey> getSurveyByLink(@PathVariable String uniqueLink) {
    // @PathVariable говорить Spring взяти значення з URL (b3c04806) і передати його в змінну uniqueLink

    return surveyService.getSurveyByLink(uniqueLink)
            .map(survey -> ResponseEntity.ok(survey)) // Якщо опитування знайдено, повернути його і статус 200 OK
            .orElse(ResponseEntity.notFound().build()); // Якщо не знайдено, повернути статус 404 Not Found
    }
}
 