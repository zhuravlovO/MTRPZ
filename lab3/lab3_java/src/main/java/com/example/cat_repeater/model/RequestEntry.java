package com.example.cat_repeater.model; 

import jakarta.persistence.*; 
import java.time.LocalDateTime;

@Entity
public class RequestEntry {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String phrase;
    private int repetitions;

    @Lob 
    @Column(columnDefinition="TEXT") 
    private String generatedText;

    private LocalDateTime timestamp;

    public RequestEntry() {
    }


    public RequestEntry(String phrase, int repetitions, String generatedText) {
        this.phrase = phrase;
        this.repetitions = repetitions;
        this.generatedText = generatedText;
        this.timestamp = LocalDateTime.now();
    }

   
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getPhrase() {
        return phrase;
    }

    public void setPhrase(String phrase) {
        this.phrase = phrase;
    }

    public int getRepetitions() {
        return repetitions;
    }

    public void setRepetitions(int repetitions) {
        this.repetitions = repetitions;
    }

    public String getGeneratedText() {
        return generatedText;
    }

    public void setGeneratedText(String generatedText) {
        this.generatedText = generatedText;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(LocalDateTime timestamp) {
        this.timestamp = timestamp;
    }
}