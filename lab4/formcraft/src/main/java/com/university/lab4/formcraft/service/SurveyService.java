package com.university.lab4.formcraft.service;

import com.university.lab4.formcraft.model.Survey;
import com.university.lab4.formcraft.repository.SurveyRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional; // Імпортуй Transactional

import java.util.Optional;
import java.util.UUID;

@Service
public class SurveyService {

    private final SurveyRepository surveyRepository;

    @Autowired
    public SurveyService(SurveyRepository surveyRepository) {
        this.surveyRepository = surveyRepository;
    }

       @Transactional
    public Survey createSurvey(Survey survey) {
        survey.setUniqueLink(UUID.randomUUID().toString().substring(0, 8));

        // Проходимо по кожному питанню, яке прийшло в запиті
        if (survey.getQuestions() != null) {
            survey.getQuestions().forEach(question -> {
                // Встановлюємо "батька" для питання
                question.setSurvey(survey);

                // --- НОВИЙ КОД ---
                // Тепер для кожного питання проходимо по його варіантах відповідей
                if (question.getOptions() != null) {
                    question.getOptions().forEach(option -> {
                        // Встановлюємо "батька" для варіанту відповіді
                        option.setQuestion(question);
                    });
                }
                // --- КІНЕЦЬ НОВОГО КОДУ ---
            });
        }

        return surveyRepository.save(survey);
    }
    
    public Optional<Survey> getSurveyByLink(String uniqueLink) {
    return surveyRepository.findByUniqueLink(uniqueLink);
    }
}
 
