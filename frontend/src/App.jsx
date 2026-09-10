import { useState } from 'react'
import './App.css'

function App() {
  const [destination, setDestination] = useState('')
  const [totalBudget, setTotalBudget] = useState('')
  const [numDays, setNumDays] = useState('')
  const [numPeople, setNumPeople] = useState('')
  const [interests, setInterests] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch('http://127.0.0.1:8000/plan-trip', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          destination,
          total_budget: Number(totalBudget),
          num_days: Number(numDays),
          num_people: Number(numPeople),
          interests: interests.split(',').map(i => i.trim()).filter(i => i.length > 0)
        })
      })

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <h1>Plan Your Trip with Viharam</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Destination (e.g. Goa)" value={destination} onChange={(e) => setDestination(e.target.value)} />
        <input type="number" placeholder="Total Budget (₹)" value={totalBudget} onChange={(e) => setTotalBudget(e.target.value)} />
        <input type="number" placeholder="Number of Days" value={numDays} onChange={(e) => setNumDays(e.target.value)} />
        <input type="number" placeholder="Number of People" value={numPeople} onChange={(e) => setNumPeople(e.target.value)} />
        <input type="text" placeholder="Interests (comma-separated)" value={interests} onChange={(e) => setInterests(e.target.value)} />
        <button type="submit" disabled={loading}>
          {loading ? 'Planning...' : 'Plan My Trip'}
        </button>
      </form>

      {error && <p style={{ color: 'red' }}>Error: {error}</p>}

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  )
}

export default App