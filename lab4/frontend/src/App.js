import './App.css';
import { BrowserRouter as Router, Routes, Route, Link as RouterLink } from 'react-router-dom';
import SurveyCreator from './components/SurveyCreator';
import SurveyTaker from './components/SurveyTaker';
import { Container, Typography, AppBar, Toolbar } from '@mui/material';

function App() {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            <RouterLink to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
              FormCraft
            </RouterLink>
          </Typography>
        </Toolbar>
      </AppBar>
      <Container component="main" sx={{ mt: 4, mb: 4 }}>
        <Routes>
          <Route path="/" element={<SurveyCreator />} />
          <Route path="/survey/:link" element={<SurveyTaker />} />
        </Routes>
      </Container>
    </Router>
  );
}

export default App;