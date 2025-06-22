package com.university.lab4.formcraft.repository;

import com.university.lab4.formcraft.model.SubmittedAnswer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface SubmittedAnswerRepository extends JpaRepository<SubmittedAnswer, Long> {
}