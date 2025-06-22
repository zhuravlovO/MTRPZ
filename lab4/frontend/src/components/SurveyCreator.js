import React, { useState } from 'react';
import axios from 'axios';
import {
  TextField, Button, Container, Paper, Typography, Box, Link, IconButton,
  Select, MenuItem, FormControl, InputLabel
} from '@mui/material';
import AddCircleOutlineIcon from '@mui/icons-material/AddCircleOutline';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

const initialQuestion = {
  text: '',
  type: 'text',
  options: [],
};

function SurveyCreator() {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [questions, setQuestions] = useState([{ ...initialQuestion }]);
  const [createdSurveyLink, setCreatedSurveyLink] = useState(null);

  // --- Функції для керування питаннями ---
  const handleQuestionChange = (index, field, value) => {
    const newQuestions = [...questions];
    newQuestions[index][field] = value;
    // Якщо тип питання змінюється на текстове, очищуємо варіанти відповідей
    if (field === 'type' && value === 'text') {
      newQuestions[index].options = [];
    }
    setQuestions(newQuestions);
  };

  const addQuestion = () => {
    setQuestions([...questions, { ...initialQuestion, options: [] }]);
  };

  const removeQuestion = (index) => {
    const newQuestions = questions.filter((_, qIndex) => qIndex !== index);
    setQuestions(newQuestions);
  };

  // --- Функції для керування варіантами відповідей ---
  const handleOptionChange = (qIndex, oIndex, value) => {
    const newQuestions = [...questions];
    newQuestions[qIndex].options[oIndex].text = value;
    setQuestions(newQuestions);
  };

  const addOption = (qIndex) => {
    const newQuestions = [...questions];
    newQuestions[qIndex].options.push({ text: '' });
    setQuestions(newQuestions);
  };

  const removeOption = (qIndex, oIndex) => {
    const newQuestions = [...questions];
    newQuestions[qIndex].options = newQuestions[qIndex].options.filter((_, optIndex) => optIndex !== oIndex);
    setQuestions(newQuestions);
  };

  // --- Функція відправки форми ---
  const handleSubmit = async (event) => {
    event.preventDefault();
    // Видаляємо порожні варіанти відповідей перед відправкою
    const cleanedQuestions = questions.map(q => ({
      ...q,
      options: q.options.filter(opt => opt.text.trim() !== '')
    }));

    const newSurvey = { title, description, questions: cleanedQuestions };

    try {
      const response = await axios.post('http://localhost:8080/api/surveys', newSurvey);
      setCreatedSurveyLink(response.data.uniqueLink);
    } catch (error) {
      alert('Помилка при створенні опитування!');
    }
  };

  return (
    <Container maxWidth="md">
      <Paper elevation={3} style={{ padding: '32px', marginTop: '32px' }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Конструктор опитування
        </Typography>
        <Box component="form" onSubmit={handleSubmit}>
          <TextField label="Назва опитування" fullWidth margin="normal" value={title} onChange={(e) => setTitle(e.target.value)} required />
          <TextField label="Опис" fullWidth multiline rows={3} margin="normal" value={description} onChange={(e) => setDescription(e.target.value)} />
          
          <Typography variant="h5" sx={{ mt: 4, mb: 2 }}>Питання</Typography>

          {questions.map((q, qIndex) => (
            <Paper key={qIndex} variant="outlined" sx={{ p: 2, mb: 2 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                <TextField 
                  label={`Питання №${qIndex + 1}`} 
                  fullWidth 
                  value={q.text}
                  onChange={(e) => handleQuestionChange(qIndex, 'text', e.target.value)}
                  required
                />
                <FormControl sx={{ minWidth: 180 }}>
                  <InputLabel>Тип питання</InputLabel>
                  <Select
                    value={q.type}
                    label="Тип питання"
                    onChange={(e) => handleQuestionChange(qIndex, 'type', e.target.value)}
                  >
                    <MenuItem value="text">Текстове поле</MenuItem>
                    <MenuItem value="single_choice">Один вибір</MenuItem>
                    <MenuItem value="multiple_choice">Декілька виборів</MenuItem>
                  </Select>
                </FormControl>
                <IconButton onClick={() => removeQuestion(qIndex)} color="error" disabled={questions.length <= 1}>
                  <RemoveCircleOutlineIcon />
                </IconButton>
              </Box>

              { (q.type === 'single_choice' || q.type === 'multiple_choice') && (
                <Box sx={{ mt: 2, ml: 4 }}>
                  <Typography variant="subtitle1">Варіанти відповідей</Typography>
                  {q.options.map((opt, oIndex) => (
                    <Box key={oIndex} sx={{ display: 'flex', alignItems: 'center', gap: 1, mt: 1 }}>
                      <TextField 
                        label={`Варіант ${oIndex + 1}`} 
                        size="small" 
                        fullWidth
                        value={opt.text}
                        onChange={(e) => handleOptionChange(qIndex, oIndex, e.target.value)}
                      />
                       <IconButton onClick={() => removeOption(qIndex, oIndex)} size="small" color="secondary">
                         <RemoveCircleOutlineIcon />
                       </IconButton>
                    </Box>
                  ))}
                  <Button startIcon={<AddCircleOutlineIcon />} onClick={() => addOption(qIndex)} sx={{ mt: 1 }}>
                    Додати варіант
                  </Button>
                </Box>
              )}
            </Paper>
          ))}
          
          <Button startIcon={<AddCircleOutlineIcon />} onClick={addQuestion} variant="outlined" sx={{ mt: 2 }}>
            Додати питання
          </Button>

          <Button type="submit" fullWidth variant="contained" sx={{ mt: 4, mb: 2, fontSize: '1.1rem' }}>
            Створити опитування
          </Button>
        </Box>
      </Paper>
      
       ( {createdSurveyLink && (
  <Paper elevation={3} style={{ padding: '20px', marginTop: '20px' }}>
    <Typography variant="h6">Опитування успішно створено!</Typography>
    <Typography>
      Посилання для проходження: {' '}
      <Link href={`/survey/${createdSurveyLink}`} target="_blank" rel="noopener noreferrer">
        {`/survey/${createdSurveyLink}`}
      </Link>
    </Typography>
  </Paper>
)}  )
    </Container>
  );
}

export default SurveyCreator;