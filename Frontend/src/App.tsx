import './App.css'
import { Route, Routes } from 'react-router-dom'
import AiForecastML from './pages/ai-forecast-ml'
import AiForecastNaive from './pages/ai-forecast-naive'

function App() {
  return (
    <div className="container mt-5">
      <Routes>
        <Route path="/" element={<AiForecastNaive />} />
        <Route path="/ai-forecast-naive" element={<AiForecastNaive />} />
        <Route path="/ai-forecast-ml" element={<AiForecastML />} />
      </Routes>
    </div>
  )
}

export default App
