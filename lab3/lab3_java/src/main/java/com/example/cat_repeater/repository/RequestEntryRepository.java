package com.example.cat_repeater.repository;

import com.example.cat_repeater.model.RequestEntry;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RequestEntryRepository extends JpaRepository<RequestEntry, Long> {

    List<RequestEntry> findTop10ByOrderByTimestampDesc();

}