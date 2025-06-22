package com.university.lab4.formcraft.repository;

import com.university.lab4.formcraft.model.ResponseSession;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ResponseSessionRepository extends JpaRepository<ResponseSession, Long> {
}