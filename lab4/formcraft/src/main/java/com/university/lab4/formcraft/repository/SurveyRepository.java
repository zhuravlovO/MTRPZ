package com.university.lab4.formcraft.repository;

import com.university.lab4.formcraft.model.Survey;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional; // Важливо імпортувати Optional

@Repository
public interface SurveyRepository extends JpaRepository<Survey, Long> {
    
    // Просто оголоси метод з такою назвою, і Spring сам напише реалізацію!
    // "find" + "By" + "UniqueLink" -> Spring зрозуміє, що треба шукати по полю uniqueLink.
    // Optional<Survey> - це кращий спосіб повернути результат, який може бути відсутнім.
    Optional<Survey> findByUniqueLink(String uniqueLink);
}