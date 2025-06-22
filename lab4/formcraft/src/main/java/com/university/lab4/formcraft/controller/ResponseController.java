package com.university.lab4.formcraft.controller;

import com.university.lab4.formcraft.model.ResponseSession;
import com.university.lab4.formcraft.service.ResponseService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/surveys/{surveyLink}/responses")
public class ResponseController {

    private final ResponseService responseService;

    public ResponseController(ResponseService responseService) {
        this.responseService = responseService;
    }

    @PostMapping
    public ResponseEntity<ResponseSession> submitResponse(@PathVariable String surveyLink, @RequestBody ResponseSession response) {
        ResponseSession savedResponse = responseService.saveResponse(surveyLink, response);
        return new ResponseEntity<>(savedResponse, HttpStatus.CREATED);
    }
}