// Вказуємо, що цей клас належить до пакету model
package com.university.lab4.formcraft.model;

// Імпортуємо необхідні анотації з бібліотек
import jakarta.persistence.*; // Для JPA анотацій (@Entity, @Id, etc.)
import lombok.Getter;       // Lombok для автоматичної генерації геттерів
import lombok.Setter;       // Lombok для автоматичної генерації сеттерів
import java.util.ArrayList;
import java.util.List;

@Getter   // Анотація Lombok: автоматично створює всі гетери (getTitle(), getDescription() і т.д.)
@Setter   // Анотація Lombok: автоматично створює всі сеттери (setTitle(), setDescription() і т.д.)
@Entity   // Головна анотація. Говорить Hibernate: "Цей клас відповідає таблиці в базі даних"
@Table(name = "surveys") // Вказує точну назву таблиці. Якщо це не вказати, назва буде "survey"
public class Survey {

    // --- Поля класу (відповідають стовпцям у таблиці) ---

    @Id // Позначає, що це поле є первинним ключем (primary key) - унікальним ідентифікатором для кожного запису
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    // Вказує, як цей ID має генеруватися. 
    // GenerationType.IDENTITY означає, що база даних (PostgreSQL) сама відповідає за генерацію ID.
    // Кожен новий запис автоматично отримає ID на 1 більший за попередній (1, 2, 3, ...).
    private Long id;

    @Column(nullable = false, length = 255) // @Column дозволяє налаштувати стовпець
    // nullable = false означає, що цей стовпець в базі даних не може бути порожнім (NOT NULL).
    // length = 255 обмежує максимальну довжину рядка.
    private String title;

    @Column(columnDefinition = "TEXT") // columnDefinition = "TEXT" дозволяє зберігати довгі тексти без обмеження в 255 символів.
    private String description;

    @Column(unique = true, nullable = false)
    // unique = true гарантує, що значення в цьому стовпці будуть унікальними для всієї таблиці.
    // Це важливо для посилань, щоб два опитування не мали однакове посилання.
    private String uniqueLink;

    @OneToMany(mappedBy = "survey", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.EAGER)
     private List<Question> questions = new ArrayList<>();
    // Ми не пишемо конструктори, гетери, сеттери, toString(), equals() і hashCode() вручну.
    // Lombok зробить це за нас завдяки анотаціям @Getter та @Setter (та @Data, якщо потрібно).
}