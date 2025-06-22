import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import {
 Paper, Typography, Button, Box, CircularProgress, Alert,
  Radio, RadioGroup, FormControlLabel, FormControl, FormLabel, Checkbox, FormGroup, TextField
} from '@mui/material';

function SurveyTaker() {
  const { link } = useParams();
  const [survey, setSurvey] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    // ... (код завантаження даних залишається без змін) ...
    const fetchSurvey = async () => {
      try {
        const response = await axios.get(`http://localhost:8080/api/surveys/${link}`);
        setSurvey(response.data);
      } catch (err) {
        setError('Помилка завантаження опитування або його не знайдено.');
      } finally {
        setLoading(false);
      }
    };
    fetchSurvey();
  }, [link]);

  const handleInputChange = (questionId, value, type) => {
    // ... (логіка обробки відповідей залишається без змін) ...
    if (type === 'multiple_choice') {
        const currentAnswers = answers[questionId] ? answers[questionId].split(',') : [];
        const newAnswers = currentAnswers.includes(value)
          ? currentAnswers.filter(ans => ans !== value)
          : [...currentAnswers, value];
        
        setAnswers({ ...answers, [questionId]: newAnswers.join(',') });
      } else {
        setAnswers({ ...answers, [questionId]: value });
      }
  };

  const handleSubmit = async (event) => {
    // ... (логіка відправки залишається без змін) ...
    event.preventDefault();
    const submittedAnswers = Object.keys(answers).map(questionId => ({
      question: { id: parseInt(questionId) },
      answerText: answers[questionId]
    }));
    const responsePayload = { submittedAnswers };
    try {
      await axios.post(`http://localhost:8080/api/surveys/${link}/responses`, responsePayload);
      setSubmitted(true);
    } catch (err) {
      setError('Сталася помилка при надсиланні відповідей.');
    }
  };
  
  if (loading) return <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}><CircularProgress /></Box>;
  if (error) return <Alert severity="error">{error}</Alert>;
  if (!survey) return <Alert severity="warning">Опитування не знайдено.</Alert>;

  if (submitted) {
    return (
        <Paper elevation={3} style={{ padding: '32px', marginTop: '32px', textAlign: 'center' }}>
            <Typography variant="h4" gutterBottom>Дякуємо!</Typography>
            <Typography>Ваші відповіді було успішно надіслано.</Typography>
        </Paper>
    );
  }

  return (
    <Paper elevation={3} style={{ padding: '32px', marginTop: '32px' }}>
      <Typography variant="h4" component="h1" gutterBottom>{survey.title}</Typography>
      <Typography paragraph>{survey.description}</Typography>
      <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 3 }}>
        {survey.questions.map((question, index) => (
          <FormControl component="fieldset" fullWidth margin="normal" key={question.id}>
            <FormLabel component="legend">{index + 1}. {question.text}</FormLabel>
            
            {question.type === 'text' && (
              <TextField
                variant="outlined"
                fullWidth
                onChange={(e) => handleInputChange(question.id, e.target.value, question.type)}
              />
            )}

            {question.type === 'single_choice' && (
              <RadioGroup name={`question_${question.id}`} onChange={(e) => handleInputChange(question.id, e.target.value, question.type)}>
                {question.options.map(option => (
                  <FormControlLabel key={option.id} value={option.id.toString()} control={<Radio />} label={option.text} />
                ))}
              </RadioGroup>
            )}

            {question.type === 'multiple_choice' && (
              <FormGroup>
                {question.options.map(option => (
                  <FormControlLabel key={option.id} control={<Checkbox value={option.id.toString()} onChange={(e) => handleInputChange(question.id, e.target.value, question.type)} />} label={option.text} />
                ))}
              </FormGroup>
            )}
          </FormControl>
        ))}
        <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>
          Надіслати відповіді
        </Button>
      </Box>
    </Paper>
  );
}

export default SurveyTaker;