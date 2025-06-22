package com.university.lab4.formcraft.model;

import com.fasterxml.jackson.annotation.JsonIgnore;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
@Table(name = "submitted_answers")
public class SubmittedAnswer {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "response_session_id", nullable = false)
    @JsonIgnore
    private ResponseSession responseSession; // До якої сесії належить ця відповідь

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "question_id", nullable = false)
    private Question question; // На яке питання ця відповідь

    @Column(columnDefinition = "TEXT")
    private String answerText; // Текст відповіді (для типу 'text') або ID обраних варіантів
}