package com.university.lab4.formcraft.service;

import com.university.lab4.formcraft.model.ResponseSession;
import com.university.lab4.formcraft.repository.ResponseSessionRepository;
import com.university.lab4.formcraft.repository.SurveyRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;

@Service
public class ResponseService {

    private final ResponseSessionRepository responseSessionRepository;
    private final SurveyRepository surveyRepository;

    public ResponseService(ResponseSessionRepository responseSessionRepository, SurveyRepository surveyRepository) {
        this.responseSessionRepository = responseSessionRepository;
        this.surveyRepository = surveyRepository;
    }

    @Transactional
    public ResponseSession saveResponse(String surveyLink, ResponseSession responseSession) {
        // Знаходимо опитування, на яке відповідають
        var survey = surveyRepository.findByUniqueLink(surveyLink)
                .orElseThrow(() -> new RuntimeException("Survey not found"));

        responseSession.setSurvey(survey);
        responseSession.setSubmissionDate(LocalDateTime.now());
        responseSession.getSubmittedAnswers().forEach(answer -> answer.setResponseSession(responseSession));

        return responseSessionRepository.save(responseSession);
    }
}