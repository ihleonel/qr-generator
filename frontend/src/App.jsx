import { useState } from 'react'
import useGenerate from './Hooks/useGenerate'
import './App.css'

function App() {
  const [payload, setPayload] = useState('')
  const { data, isLoading, error, generate } = useGenerate()

  const submit = () => {
    generate('http://localhost:8000/generate', payload)
  }
  return (
    <>
      <h1 className='title'>Generate QR</h1>
      <input
        className='input'
        type="text"
        value={payload}
        onChange={e => setPayload(e.target.value)}
      />
      <small>{error?.payload}</small>
      <button
        className='submit'
        onClick={submit}
      >
        Generate
      </button>
      {isLoading &&
        <span>Loading ...</span>
      }
      {data !== null &&
        <img
          className='result'
          src={`data:image/svg+xml;base64,${data.qrcode}`}
          alt="QRCode"
          width="200"
          height="200"
        />
      }

    </>
  )
}

export default App
