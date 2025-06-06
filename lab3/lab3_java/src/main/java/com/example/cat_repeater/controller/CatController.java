package com.example.cat_repeater.controller;

import com.example.cat_repeater.model.RequestEntry;
import com.example.cat_repeater.repository.RequestEntryRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
public class CatController {

    private static final Logger log = LoggerFactory.getLogger(CatController.class);

    private final RequestEntryRepository requestEntryRepository;

    @Autowired
    public CatController(RequestEntryRepository requestEntryRepository) {
        this.requestEntryRepository = requestEntryRepository;
    }

    private void addHistoryToModel(Model model) {
        List<RequestEntry> history = requestEntryRepository.findTop10ByOrderByTimestampDesc();
        model.addAttribute("history", history);
        log.info("Fetched {} history entries.", history.size());
    }

    @GetMapping("/")
    public String showHomePage(Model model) {
        // Додаємо порожні атрибути для форми, щоб уникнути помилок Thymeleaf при першому завантаженні,
        // якщо phraseInput використовується для value у формі (хоча в поточному index.html це не так)
        if (!model.containsAttribute("phraseInput")) {
            model.addAttribute("phraseInput", "");
        }
        addHistoryToModel(model);
        return "index";
    }

    @PostMapping("/testgenerate")
    @ResponseBody // Щоб повернути просто текст, а не шукати шаблон
    public String testGenerateEndpoint() {
    log.info("Test generate endpoint was called!");
    return "Test generate endpoint reached!";
    }
    
    @PostMapping("/generate")
    public String generateRepeatedText(@RequestParam("phrase") String phraseFromForm,
                                       @RequestParam("repetitions") int repetitionsFromForm,
                                       Model model) {

        log.info("Processing POST request to /generate with phrase: [{}] and repetitions: [{}]", phraseFromForm, repetitionsFromForm);

        StringBuilder resultTextBuilder = new StringBuilder();
        for (int i = 0; i < repetitionsFromForm; i++) {
            resultTextBuilder.append(phraseFromForm);
            if (i < repetitionsFromForm - 1) {
                resultTextBuilder.append(System.lineSeparator());
            }
        }
        String finalGeneratedText = resultTextBuilder.toString();

        RequestEntry entry = new RequestEntry(phraseFromForm, repetitionsFromForm, finalGeneratedText);
        RequestEntry savedEntry = requestEntryRepository.save(entry);

        log.info("Saved new request entry with ID: {}", savedEntry.getId());

        model.addAttribute("generatedText", finalGeneratedText);
        model.addAttribute("phraseInput", phraseFromForm); // Передаємо введену фразу назад
        
        addHistoryToModel(model);
        return "index";
    }
}