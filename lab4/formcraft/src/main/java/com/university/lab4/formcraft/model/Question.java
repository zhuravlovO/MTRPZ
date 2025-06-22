package com.university.lab4.formcraft.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;
import java.util.ArrayList;
import java.util.List;

@Getter
@Setter
@Entity
@Table(name = "questions")
public class Question {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String text; // Текст питання

    @Column(nullable = false)
    private String type; // Тип питання: 'single_choice', 'multiple_choice', 'text'

    // --- Зв'язок "Багато-до-Одного" ---
    @ManyToOne(fetch = FetchType.LAZY) // Багато питань (@ManyToOne) можуть належати одному опитуванню.
    @JoinColumn(name = "survey_id", nullable = false) // Створює стовпець "survey_id" в таблиці "questions"
    @JsonIgnore // Дуже важлива анотація!
    private Survey survey;

    @OneToMany(mappedBy = "question", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<AnswerOption> options = new ArrayList<>();
}